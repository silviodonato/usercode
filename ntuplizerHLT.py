#!/usr/bin/python
import ROOT
import itertools
import resource
from array import array
from math import sqrt, pi, log10, log, exp
# load FWlite python libraries
from DataFormats.FWLite import Handle, Events
from utils import deltaR,SetVariable,DummyClass,productWithCheck
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

filesInput = ["/gpfs/ddn/srm/cms/store/user/sdonato/VBFHbb_trigger_v5/VBFHToBB_M-120_13TeV_powheg_pythia8/VBFHbbFlat/160221_162241/0000/outputFULL_2.root"]
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
    if len(filesInput)>0 and ('VBFHToBB' in filesInput[0]):
        Signal = True
    print "Signal=",Signal

    if len(filesInput)==0: exit
    events = Events (filesInput)

    pileUp_source, pileUp_label = Handle("vector<PileupSummaryInfo>"), ("addPileupInfo")

    l1JetFwd_source, l1JetFwd_label = Handle("vector<l1extra::L1JetParticle>"), ("hltL1extraParticles","Forward")
    l1JetCtr_source, l1JetCtr_label = Handle("vector<l1extra::L1JetParticle>"), ("hltL1extraParticles","Central")
    caloJet_source, caloJet_label = Handle("vector<reco::CaloJet>"), ("hltAK4CaloJetsCorrectedIDPassed")
    calobtag_source, calobtag_label = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("hltCombinedSecondaryVertexBJetTagsCalo") #("pfCombinedSecondaryVertexBJetTags")

    pfJet_source, pfJet_label = Handle("vector<reco::PFJet>"), ("hltAK4PFJetsLooseIDCorrected")
    pfbtag_source, pfbtag_label = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("hltCombinedSecondaryVertexBJetTagsPF") #("pfCombinedSecondaryVertexBJetTags")

    if Signal:
        offJet_source, offJet_label = Handle("vector<reco::PFJet>"), ("ak4PFJets")
        offbtag_source, offbtag_label = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("pfCombinedInclusiveSecondaryVertexV2BJetTags") #("pfCombinedSecondaryVertexBJetTags")

    caloJet = BookVector(tree,"caloJet",['pt','eta','phi','mass','csv'])
    pfJet = BookVector(tree,"pfJet",['pt','eta','phi','mass','csv'])
    l1JetFwd = BookVector(tree,"l1JetFwd",['pt','eta','phi','mass'])
    l1JetCtr = BookVector(tree,"l1JetCtr",['pt','eta','phi','mass'])
    if Signal:
        offJet = BookVector(tree,"offJet",['pt','eta','phi','mass','csv'])

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

    if Signal:
        Detaqq_off  = SetVariable(tree,'Detaqq_off')
        Dphibb_off  = SetVariable(tree,'Dphibb_off')
        Mqq_off     = SetVariable(tree,'Mqq_off')
        Mbb_off     = SetVariable(tree,'Mbb_off')

    f.cd()
    ##event loop
    for iev,event in enumerate(events):
        event.getByLabel(pileUp_label, pileUp_source)
        event.getByLabel(caloJet_label, caloJet_source)
        event.getByLabel(calobtag_label, calobtag_source)
        event.getByLabel(pfJet_label, pfJet_source)
        event.getByLabel(pfbtag_label, pfbtag_source)
        event.getByLabel(l1JetFwd_label, l1JetFwd_source)
        event.getByLabel(l1JetCtr_label, l1JetCtr_source)
        
        run[0]          = event.eventAuxiliary().run()
        lumi[0]         = event.eventAuxiliary().luminosityBlock()
        evt[0]          = event.eventAuxiliary().event()
        
        if Signal:
            event.getByLabel(offJet_label, offJet_source)
            event.getByLabel(offbtag_label, offbtag_source)


        FillJetsAndBtag(caloJet_source,caloJet.num,caloJet.pt,caloJet.eta,caloJet.phi,caloJet.mass,calobtag_source,caloJet.csv)
        FillJetsAndBtag(pfJet_source,pfJet.num,pfJet.pt,pfJet.eta,pfJet.phi,pfJet.mass,pfbtag_source,pfJet.csv)
        FillJetsAndBtag(l1JetFwd_source,l1JetFwd.num,l1JetFwd.pt,l1JetFwd.eta,l1JetFwd.phi,l1JetFwd.mass)
        FillJetsAndBtag(l1JetCtr_source,l1JetCtr.num,l1JetCtr.pt,l1JetCtr.eta,l1JetCtr.phi,l1JetCtr.mass)

        
        if Signal:
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
        
        if iev%100==1: print "Event: ",iev," done."
        tree.Fill()

    f.Write()
    f.Close()
