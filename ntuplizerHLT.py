#!/usr/bin/python
import ROOT
import itertools
import resource
from array import array
from math import sqrt, pi, log10, log, exp
# load FWlite python libraries
from DataFormats.FWLite import Handle, Events
from utils import deltaR,SetVariable,DummyClass,productWithCheck,checkTriggerIndex
from VBFutils import Sort,GetVariablesToFill

Handle.productWithCheck = productWithCheck

pt_min          = 20
eta_max         = 2.4
NHFmax          = 0.9
NEMFmax         = 0.99
CHFmin          = 0.
MUFmax          = 0.8
CEMFmax         = 0.99
NumConstMin     = 1
CHMmin          = 0
maxJets         = 50
bunchCrossing   = 0

filesInput = ["../outputFULL_AOD_1.root"]
fileOutput = "test.root"

def FillJetsAndBtag(offJets,offJet_num,offJet_pt,offJet_eta,offJet_phi,offJet_mass,btags=0,offJet_csv=0):
    offJet_num[0] = 0
    for jet in offJets.productWithCheck():
        if jet.pt()<pt_min: continue
        if offJet_num[0]<len(offJet_pt):                
            offJet_pt[offJet_num[0]] = jet.pt()
            offJet_eta[offJet_num[0]] = jet.eta()
            offJet_phi[offJet_num[0]] = jet.phi()
            offJet_mass[offJet_num[0]] = jet.mass()
            offlineCSV = -2.
            if not btags is 0:
                for j in range(0,btags.productWithCheck().size()):
                    jetB = btags.productWithCheck().key(j).get()
                    dR = deltaR(jetB.eta(),jetB.phi(),jet.eta(),jet.phi())
                    if dR<0.3:
                        offlineCSV = max(0.,btags.productWithCheck().value(j))
                        break
                offJet_csv[offJet_num[0]] = offlineCSV
            offJet_num[0] += 1

    #def BookVariable(tree,name="variable",type_='F'):
    #    var   = SetVariable(tree,name ,type_)
    #    return var

def WithFallback(product,method="pt"):
    if product.size()>0:
        return getattr(product[0],method)()
    else:
        return -10

def BookVector(tree,name="vector",listMembers=[]):
    obj = DummyClass()
    obj.num   = SetVariable(tree,name+'_num' ,'I')
    for member in listMembers:
        setattr(obj,member,SetVariable(tree,name+'_'+member  ,'F',name+'_num',maxJets))
    return obj

    ##########################################################################

def launchNtupleFromHLT(filesInput,fileOutput):
    bunchCrossing   = 12
    print "filesInput: ",filesInput
    print "fileOutput: ",fileOutput

    f = ROOT.TFile(fileOutput,"recreate")
    tree = ROOT.TTree("tree","tree")

    Signal = False
    if len(filesInput)>0 and ('AOD' in filesInput[0]):
        Signal = True
    print "Signal=",Signal

    if len(filesInput)==0: exit
    events = Events (filesInput)

    triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::AAA")

    pileUp_source, pileUp_label = Handle("vector<PileupSummaryInfo>"), ("addPileupInfo")

#recoMETs_hltPFMETProducer__AAA.
#recoMETs_hltPFMHTTightID__AAA.
#recoCaloMETs_hltMet__AAA.

#recoMETs_hltMHTNoPU__AAA.

#l1tJetBXVector_hltCaloStage2Digis_Jet_AAA.
#l1tEtSumBXVector_hltCaloStage2Digis_EtSum_AAA.
#l1tEGammaBXVector_hltCaloStage2Digis_EGamma_AAA.
#l1tMuonBXVector_hltGmtStage2Digis_Muon_AAA.

    generator_source, generator_label       = Handle("GenEventInfoProduct"), ("generator")

    l1HT_source, l1HT_label                 = Handle("BXVector<l1t::EtSum>"), ("hltCaloStage2Digis","EtSum")
    l1Jet_source, l1Jet_label               = Handle("BXVector<l1t::Jet>"), ("hltCaloStage2Digis","Jet")
#    l1JetFwd_source, l1JetFwd_label         = Handle("vector<l1extra::L1JetParticle>"), ("hltL1extraParticles","Forward")
#    l1JetCtr_source, l1JetCtr_label         = Handle("vector<l1extra::L1JetParticle>"), ("hltL1extraParticles","Central")

#    l1Met_source, l1Met_label              = Handle("vector<reco::CaloJet>"), ("hltAK4CaloJetsCorrectedIDPassed")
#    l1Mht_source, l1Mht_label              = Handle("vector<reco::CaloJet>"), ("hltAK4CaloJetsCorrectedIDPassed")

    offMet_source, offMet_label             = Handle("vector<reco::PFMET>"), ("pfMET")

    offMet_source, offMet_label             = Handle("vector<reco::PFMET>"), ("pfMET")

    pfMet_source, pfMet_label               = Handle("vector<reco::MET>"), ("hltPFMETProducer")
    pfMht_source, pfMht_label               = Handle("vector<reco::MET>"), ("hltPFMHTTightID")

    caloMet_source, caloMet_label           = Handle("vector<reco::CaloMET>"), ("hltMet")
    caloMht_source, caloMht_label           = Handle("vector<reco::MET>"), ("hltMht")
    caloMhtNoPU_source, caloMhtNoPU_label   = Handle("vector<reco::MET>"), ("hltMHTNoPU")

    caloJet_source, caloJet_label           = Handle("vector<reco::CaloJet>"), ("hltAK4CaloJetsCorrectedIDPassed")

    calobtag_source, calobtag_label         = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("hltCombinedSecondaryVertexBJetTagsCalo") #("pfCombinedSecondaryVertexBJetTags")

    pfJet_source, pfJet_label               = Handle("vector<reco::PFJet>"), ("hltAK4PFJetsLooseIDCorrected")
    pfbtag_source, pfbtag_label             = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("hltCombinedSecondaryVertexBJetTagsPF") #("pfCombinedSecondaryVertexBJetTags")

    if Signal:
        offJet_source, offJet_label         = Handle("vector<reco::PFJet>"), ("ak4PFJets")
        offbtag_source, offbtag_label       = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("pfCombinedInclusiveSecondaryVertexV2BJetTags") #("pfCombinedSecondaryVertexBJetTags")

    caloJet     = BookVector(tree,"caloJet",['pt','eta','phi','mass','csv'])
    pfJet       = BookVector(tree,"pfJet",['pt','eta','phi','mass','csv'])
    l1Jet       = BookVector(tree,"l1Jet",['pt','eta','phi','mass'])
#    l1JetFwd    = BookVector(tree,"l1JetFwd",['pt','eta','phi','mass'])
#    l1JetCtr    = BookVector(tree,"l1JetCtr",['pt','eta','phi','mass'])
    l1HT        = SetVariable(tree,'l1HT')
    caloMet     = SetVariable(tree,'caloMet')
    caloMht     = SetVariable(tree,'caloMht')
    caloMhtNoPU = SetVariable(tree,'caloMhtNoPU')
    pfMet       = SetVariable(tree,'pfMet')
    pfMht       = SetVariable(tree,'pfMht')
#    l1Met       = SetVariable(tree,'l1Met')
#    l1Met_phi       = SetVariable(tree,'l1Met_phi')
#    l1Mht       = SetVariable(tree,'l1Mht')
    if Signal:
        offJet  = BookVector(tree,"offJet",['pt','eta','phi','mass','csv'])
        offMet  = SetVariable(tree,'offMet')

    Detaqq_eta  = SetVariable(tree,'Detaqq_eta')
    Dphibb_eta  = SetVariable(tree,'Dphibb_eta')
    Mqq_eta     = SetVariable(tree,'Mqq_eta')
    Mbb_eta     = SetVariable(tree,'Mbb_eta')

    Detaqq_1b   = SetVariable(tree,'Detaqq_1b')
    Dphibb_1b   = SetVariable(tree,'Dphibb_1b')
    Mqq_1b      = SetVariable(tree,'Mqq_1b')
    Mbb_1b      = SetVariable(tree,'Mbb_1b')

    Detaqq_2b   = SetVariable(tree,'Detaqq_2b')
    Dphibb_2b   = SetVariable(tree,'Dphibb_2b')
    Mqq_2b      = SetVariable(tree,'Mqq_2b')
    Mbb_2b      = SetVariable(tree,'Mbb_2b')

    evt         = SetVariable(tree,'evt')
    lumi        = SetVariable(tree,'lumi')
    run         = SetVariable(tree,'run')
    
    pu          = SetVariable(tree,'pu')
    ptHat       = SetVariable(tree,'ptHat')
    maxPUptHat  = SetVariable(tree,'maxPUptHat')

    if Signal:
        Detaqq_off  = SetVariable(tree,'Detaqq_off')
        Dphibb_off  = SetVariable(tree,'Dphibb_off')
        Mqq_off     = SetVariable(tree,'Mqq_off')
        Mbb_off     = SetVariable(tree,'Mbb_off')

    f.cd()

    ##get trigger names
    events.to(0)
    for event in events: break
    event.getByLabel(triggerBitLabel, triggerBits)
    names = event.object().triggerNames(triggerBits.product())
    triggerNames = names.triggerNames()
    for name in triggerNames: name = name.split("_v")[0]
    nTriggers = len(triggerNames)
    triggerVars = {}
    for trigger in triggerNames:
        triggerVars[trigger]=array( 'i', [ 0 ] )
        tree.Branch( trigger, triggerVars[trigger], trigger+'/O' )

    ##event loop
    for iev,event in enumerate(events):
        event.getByLabel(triggerBitLabel, triggerBits)
        event.getByLabel(generator_label, generator_source)
        event.getByLabel(pileUp_label, pileUp_source)
        event.getByLabel(caloJet_label, caloJet_source)
        event.getByLabel(calobtag_label, calobtag_source)
        event.getByLabel(caloMet_label, caloMet_source)
        event.getByLabel(caloMht_label, caloMht_source)
        event.getByLabel(caloMhtNoPU_label, caloMhtNoPU_source)
        event.getByLabel(pfMet_label, pfMet_source)
        event.getByLabel(pfMht_label, pfMht_source)
#        event.getByLabel(l1Met_label, l1Met_source)
#        event.getByLabel(l1Mht_label, l1Mht_source)
        event.getByLabel(pfJet_label, pfJet_source)
        event.getByLabel(pfbtag_label, pfbtag_source)
        event.getByLabel(l1Jet_label, l1Jet_source)
#        event.getByLabel(l1JetFwd_label, l1JetFwd_source)
#        event.getByLabel(l1JetCtr_label, l1JetCtr_source)
        event.getByLabel(l1HT_label, l1HT_source)
        
        run[0]          = event.eventAuxiliary().run()
        lumi[0]         = event.eventAuxiliary().luminosityBlock()
        evt[0]          = event.eventAuxiliary().event()
        
        if Signal:
            event.getByLabel(offMet_label, offMet_source)
            event.getByLabel(offJet_label, offJet_source)
            event.getByLabel(offbtag_label, offbtag_source)

        caloMet[0]      = WithFallback( caloMet_source.productWithCheck() )
        caloMht[0]      = WithFallback( caloMht_source.productWithCheck() )
        caloMhtNoPU[0]  = WithFallback( caloMhtNoPU_source.productWithCheck() )
        pfMet[0]        = WithFallback( pfMet_source.productWithCheck() )
        pfMht[0]        = WithFallback( pfMht_source.productWithCheck() )

        FillJetsAndBtag(caloJet_source,caloJet.num,caloJet.pt,caloJet.eta,caloJet.phi,caloJet.mass,calobtag_source,caloJet.csv)
        FillJetsAndBtag(pfJet_source,pfJet.num,pfJet.pt,pfJet.eta,pfJet.phi,pfJet.mass,pfbtag_source,pfJet.csv)
        FillJetsAndBtag(l1Jet_source,l1Jet.num,l1Jet.pt,l1Jet.eta,l1Jet.phi,l1Jet.mass)
#        FillJetsAndBtag(l1JetFwd_source,l1JetFwd.num,l1JetFwd.pt,l1JetFwd.eta,l1JetFwd.phi,l1JetFwd.mass)
#        FillJetsAndBtag(l1JetCtr_source,l1JetCtr.num,l1JetCtr.pt,l1JetCtr.eta,l1JetCtr.phi,l1JetCtr.mass)
        l1HT_source.productWithCheck()
        l1HT[0] = WithFallback(l1HT_source.productWithCheck(),'pt')
#        l1Met[0] = WithFallback(l1HT_source.productWithCheck(),'MissingEt')
#        l1Met_phi[0] = WithFallback(l1HT_source.productWithCheck(),'MissingEtPhi')
#        l1Mht[0] = WithFallback(l1HT_source.productWithCheck(),'MissingHt')

        
        if Signal:
            offMet[0]       = WithFallback( offMet_source.productWithCheck() )
            FillJetsAndBtag(offJet_source,offJet.num,offJet.pt,offJet.eta,offJet.phi,offJet.mass,offbtag_source,offJet.csv)

        calojetswithcsv = []
        for i in range(caloJet.num[0]):
            jet = ROOT.TLorentzVector()
            jet.SetPtEtaPhiM(caloJet.pt[i],caloJet.eta[i],caloJet.phi[i],caloJet.mass[i])
            jet.csv = 0
            if caloJet.pt[i]>30:
                calojetswithcsv.append(jet)

        pfjetswithcsv = []
        for i in range(pfJet.num[0]):
            jet = ROOT.TLorentzVector()
            jet.SetPtEtaPhiM(pfJet.pt[i],pfJet.eta[i],pfJet.phi[i],pfJet.mass[i])
            jet.csv = pfJet.csv[i]
            if pfJet.pt[i]>30:
                pfjetswithcsv.append(jet)
        
        if Signal:
            offjetswithcsv = []
            for i in range(offJet.num[0]):
                jet = ROOT.TLorentzVector()
                jet.SetPtEtaPhiM(offJet.pt[i],offJet.eta[i],offJet.phi[i],offJet.mass[i])
                jet.csv = offJet.csv[i]
                if offJet.pt[i]>30:
                    offjetswithcsv.append(jet)
                
        (b1,b2,q1,q2) = Sort(calojetswithcsv,'Eta')
        (Detaqq_eta[0],Dphibb_eta[0],Mqq_eta[0],Mbb_eta[0]) = GetVariablesToFill(b1,b2,q1,q2)

        (b1,b2,q1,q2) = Sort(pfjetswithcsv,'1BTagAndEta')
        (Detaqq_1b[0],Dphibb_1b[0],Mqq_1b[0],Mbb_1b[0]) = GetVariablesToFill(b1,b2,q1,q2)

        (b1,b2,q1,q2) = Sort(pfjetswithcsv,'2BTagAndPt')
        (Detaqq_2b[0],Dphibb_2b[0],Mqq_2b[0],Mbb_2b[0]) = GetVariablesToFill(b1,b2,q1,q2)

        if Signal:
            (b1,b2,q1,q2) = Sort(offjetswithcsv,'2BTagAndPt')
            (Detaqq_off[0],Dphibb_off[0],Mqq_off[0],Mbb_off[0]) = GetVariablesToFill(b1,b2,q1,q2)
            
        ptHat[0]    = generator_source.product().qScale()
        
        if bunchCrossing>=pileUp_source.productWithCheck().size() or pileUp_source.productWithCheck().at(bunchCrossing).getBunchCrossing()!=0:
            found=False
            for bunchCrossing in range(pileUp_source.productWithCheck().size()):
                if pileUp_source.productWithCheck().at(bunchCrossing).getBunchCrossing() == 0 :
                    found=True;
                    break
            if not found:
                Exception("Check pileupSummaryInfos!")
            print "I'm using bunchCrossing=",bunchCrossing
        pu[0] = pileUp_source.productWithCheck().at(bunchCrossing).getTrueNumInteractions()
        
        maxPUptHat[0] = -1
        for ptHat in pileUp_source.productWithCheck().at(bunchCrossing).getPU_pT_hats():
            maxPUptHat[0] = max(maxPUptHat[0],ptHat)
        
        names = event.object().triggerNames(triggerBits.product())
        for i,triggerName in enumerate(triggerNames):
            index = names.triggerIndex(triggerName)
#            print "index=",index
            if checkTriggerIndex(triggerName,index,names.triggerNames()):
                triggerVars[triggerName][0] = triggerBits.product().accept(index)
#                print "acc:",triggerBits.product().accept(index)
            else:
                triggerVars[triggerName][0] = 0
        
        if iev%100==1: print "Event: ",iev," done."
        tree.Fill()

    f.Write()
    f.Close()

launchNtupleFromHLT(filesInput,fileOutput)
