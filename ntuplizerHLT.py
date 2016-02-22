#!/usr/bin/python
import ROOT
import itertools
import resource
from array import array
from math import sqrt, pi, log10, log, exp
# load FWlite python libraries
from DataFormats.FWLite import Handle, Events
from utils import deltaR,SetVariable,DummyClass
from VBFutils import Sort,GetVariablesToFill


filesInput = ["/gpfs/ddn/srm/cms/store/user/sdonato/VBFHbb_trigger_v5/VBFHToBB_M-120_13TeV_powheg_pythia8/VBFHbbFlat/160221_162241/0000/outputFULL_2.root"]
fileOutput = "test.root"


pt_min=20
eta_max=2.4
NHFmax=0.9
NEMFmax=0.99
CHFmin=0.
MUFmax=0.8
CEMFmax=0.99
NumConstMin=1
CHMmin=0
maxJets = 50

def FillJetsAndBtag(offJets,offJet_num,offJet_pt,offJet_eta,offJet_phi,offJet_mass,btags=0,offJet_csv=0):
    offJet_num[0] = 0
    for jet in offJets.product():
        if jet.pt()<pt_min: continue
        if offJet_num[0]<len(offJet_pt):                
            offJet_pt[offJet_num[0]] = jet.pt()
            offJet_eta[offJet_num[0]] = jet.eta()
            offJet_phi[offJet_num[0]] = jet.phi()
            offJet_mass[offJet_num[0]] = jet.mass()
            offlineCSV = -2.
            if not btags is 0:
                for j in range(0,btags.product().size()):
                    jetB = btags.product().key(j).get()
                    dR = deltaR(jetB.eta(),jetB.phi(),jet.eta(),jet.phi())
                    if dR<0.3:
                        offlineCSV = max(0.,btags.product().value(j))
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

print "filesInput: ",filesInput
print "fileOutput: ",fileOutput

f = ROOT.TFile(fileOutput,"recreate")
tree = ROOT.TTree("tree","tree")

MC = False
if len(filesInput)>0 and ('AODSIM' in filesInput[0]):
    MC = True
print "MC=",MC

if len(filesInput)==0: exit
events = Events (filesInput)

offJet_source, offJet_label = Handle("vector<reco::PFJet>"), ("ak4PFJets")
offbtag_source, offbtag_label = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("pfCombinedInclusiveSecondaryVertexV2BJetTags") #("pfCombinedSecondaryVertexBJetTags")

caloJet_source, caloJet_label = Handle("vector<reco::CaloJet>"), ("hltAK4CaloJetsCorrectedIDPassed")
calobtag_source, calobtag_label = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("hltCombinedSecondaryVertexBJetTagsCalo") #("pfCombinedSecondaryVertexBJetTags")

pfJet_source, pfJet_label = Handle("vector<reco::PFJet>"), ("hltAK4PFJetsLooseIDCorrected")
pfbtag_source, pfbtag_label = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("hltCombinedSecondaryVertexBJetTagsPF") #("pfCombinedSecondaryVertexBJetTags")

filterVBFCalo_source, filterVBFCalo_label = Handle("trigger::TriggerFilterObjectWithRefs"), ("hltVBFCaloJetEtaSortedMqq150Deta1p5")
filterVBFSingleBtag_source, filterVBFSingleBtag_label = Handle("trigger::TriggerFilterObjectWithRefs"), ("hltVBFPFJetCSVSortedMqq460Detaqq4p1")
filterVBFDoubleBtag_source, filterVBFDoubleBtag_label = Handle("trigger::TriggerFilterObjectWithRefs"), ("hltVBFPFJetCSVSortedMqq200Detaqq1p2")

offJet = BookVector(tree,"offJet",['pt','eta','phi','mass','csv'])
caloJet = BookVector(tree,"caloJet",['pt','eta','phi','mass','csv'])
pfJet = BookVector(tree,"pfJet",['pt','eta','phi','mass','csv'])

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

Detaqq_off  = SetVariable(tree,'Detaqq_off')
Dphibb_off  = SetVariable(tree,'Dphibb_off')
Mqq_off     = SetVariable(tree,'Mqq_off')
Mbb_off     = SetVariable(tree,'Mbb_off')

f.cd()
##event loop
for iev,event in enumerate(events):
    if iev>=100000: break
    event.getByLabel(offJet_label, offJet_source)
    event.getByLabel(offbtag_label, offbtag_source)
    event.getByLabel(caloJet_label, caloJet_source)
    event.getByLabel(calobtag_label, calobtag_source)
    event.getByLabel(pfJet_label, pfJet_source)
    event.getByLabel(pfbtag_label, pfbtag_source)

    FillJetsAndBtag(offJet_source,offJet.num,offJet.pt,offJet.eta,offJet.phi,offJet.mass,offbtag_source,offJet.csv)
    FillJetsAndBtag(caloJet_source,caloJet.num,caloJet.pt,caloJet.eta,caloJet.phi,caloJet.mass,calobtag_source,caloJet.csv)
    FillJetsAndBtag(pfJet_source,pfJet.num,pfJet.pt,pfJet.eta,pfJet.phi,pfJet.mass,pfbtag_source,pfJet.csv)

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

    (b1,b2,q1,q2) = Sort(offjetswithcsv,'2BTagAndPt')
    (Detaqq_off[0],Dphibb_off[0],Mqq_off[0],Mbb_off[0]) = GetVariablesToFill(b1,b2,q1,q2)

    if iev%100==1: print "Event: ",iev," done."
    tree.Fill()

f.Write()
f.Close()

""" 
import ROOT
from array import array

#maxEvents = 100000
#maxEvents = 1000
maxEvents = -1

def GetVariablesToFill(b1,b2,q1,q2):
    return ( abs(q1.Eta() - q2.Eta()), abs(b1.DeltaPhi(b2)), (q1+q2).M(), (b1+b2).M())

def SetVariable(tree,name,option='F',lenght=1):
    if option is 'F': arraytype='f'
    elif option is 'O': arraytype='i'
    elif option is 'I': arraytype='i'
    else:
        print 'option ',option,' not recognized.'
        return

    variable = array(arraytype,[0]*lenght)
    if lenght>1: name = name + '['+str(lenght)+']'
    tree.Branch(name,variable,name+'/'+option)
    return variable

def SortByEta(vect):
    vect.sort(key=lambda x: x.Eta(), reverse=True)

def SortByPt(vect):
    vect.sort(key=lambda x: x.Pt(), reverse=True)

def SortByCSV(vect):
    vect.sort(key=lambda x: x.csv, reverse=True)

def Sort(lorentzvectorswithcsv,method=''):
    (b1,b2,q1,q2) = [ROOT.TLorentzVector()]*4
    if len(lorentzvectorswithcsv)>=4:
        if method is '1BTagAndEta':

            SortByPt(lorentzvectorswithcsv)
            maxElementsPt = 4
            lorentzvectorswithcsv = lorentzvectorswithcsv[:maxElementsPt]
            SortByCSV(lorentzvectorswithcsv)
            b1 = lorentzvectorswithcsv[0]
            del lorentzvectorswithcsv[0]

            SortByEta(lorentzvectorswithcsv)
            q1 = lorentzvectorswithcsv[0]
            b2 = lorentzvectorswithcsv[1]
            q2 = lorentzvectorswithcsv[2]

        elif method is '2BTagAndPt':

            SortByPt(lorentzvectorswithcsv)
            maxElementsPt = 6
            lorentzvectorswithcsv = lorentzvectorswithcsv[:maxElementsPt]
            SortByCSV(lorentzvectorswithcsv)
            b1 = lorentzvectorswithcsv[0]
            b2 = lorentzvectorswithcsv[1]
            del lorentzvectorswithcsv[1]
            del lorentzvectorswithcsv[0]

            SortByPt(lorentzvectorswithcsv)
            q1 = lorentzvectorswithcsv[0]
            q2 = lorentzvectorswithcsv[1]

        elif method is 'Eta':

            SortByPt(lorentzvectorswithcsv)
            maxElementsPt = 4
            lorentzvectorswithcsv = lorentzvectorswithcsv[:maxElementsPt]
            SortByEta(lorentzvectorswithcsv)
            q1 = lorentzvectorswithcsv[0]
            b1 = lorentzvectorswithcsv[1]
            b2 = lorentzvectorswithcsv[2]
            q2 = lorentzvectorswithcsv[3]

        elif method is 'Gen':

            SortByPt(lorentzvectorswithcsv)
            for i,jet in enumerate(lorentzvectorswithcsv):
                if jet.mcMatchId==25 and jet.mcFlavour==5:
                    break

            b1_ = lorentzvectorswithcsv[i]
            del lorentzvectorswithcsv[i]

            for i,jet in enumerate(lorentzvectorswithcsv):
                if jet.mcMatchId==25 and jet.mcFlavour==-5:
                    break

            b2_ = lorentzvectorswithcsv[i]
            del lorentzvectorswithcsv[i]

            mjj = 0
            for i,jet in enumerate(lorentzvectorswithcsv):
                if jet.mcFlavour!=0 and jet.mcFlavour!=21 and (abs(jet.mcFlavour)<=2):
                    for j,jet2 in enumerate(lorentzvectorswithcsv):
                        if j>i and jet2.mcFlavour!=0 and jet2.mcFlavour!=21 and (abs(jet2.mcFlavour)<=2):
                            if (jet+jet2).M()>mjj:
                                mjj = (jet+jet2).M()
                                q1_ = jet
                                q2_ = jet2

            try:
                (b1,b2,q1,q2) = (b1_,b2_,q1_,q2_)
            except:
#                print "excption"
                pass

        else:
            print 'method:',method,' not found'
    else:
#        print 'less than 4 jets!'
        pass

    if b2.Pt()>b1.Pt(): (b1,b2) = (b2,b1)
    if q2.Pt()>q1.Pt(): (q1,q2) = (q2,q1)
    return (b1,b2,q1,q2)

tree = ROOT.TChain("tree")
tree.Add('/gpfs/ddn/srm/cms/store/user/arizzi/VHBBHeppyV13/VBFHToBB_M-125_13TeV_powheg_pythia8_weightfix/VHBB_HEPPY_V13_VBFHToBB_M-125_13TeV_powheg_pythia8_weightfix__RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/151002_084651/0000/tree_*.root')
output = ROOT.TFile.Open('mytree.root','recreate')
output.cd()
nEntries = tree.GetEntries()
tree.SetBranchStatus('*',0)
tree.SetBranchStatus('nJet',1)
tree.SetBranchStatus('Jet_pt',1)
tree.SetBranchStatus('Jet_eta',1)
tree.SetBranchStatus('Jet_phi',1)
tree.SetBranchStatus('Jet_mass',1)
tree.SetBranchStatus('Jet_btagCSV',1)
tree.SetBranchStatus('Jet_mcPt',1)
tree.SetBranchStatus('Jet_mcFlavour',1)
tree.SetBranchStatus('Jet_mcMatchId',1)
tree.SetBranchStatus('HLT_*VBF*',1)
newtree = tree.CloneTree(0)

Detaqq_eta = SetVariable(newtree,'Detaqq_eta')
Dphibb_eta = SetVariable(newtree,'Dphibb_eta')
Mqq_eta = SetVariable(newtree,'Mqq_eta')
Mbb_eta = SetVariable(newtree,'Mbb_eta')

Detaqq_1b = SetVariable(newtree,'Detaqq_1b')
Dphibb_1b = SetVariable(newtree,'Dphibb_1b')
Mqq_1b = SetVariable(newtree,'Mqq_1b')
Mbb_1b = SetVariable(newtree,'Mbb_1b')

Detaqq_2b = SetVariable(newtree,'Detaqq_2b')
Dphibb_2b = SetVariable(newtree,'Dphibb_2b')
Mqq_2b = SetVariable(newtree,'Mqq_2b')
Mbb_2b = SetVariable(newtree,'Mbb_2b')

Detaqq_gen = SetVariable(newtree,'Detaqq_gen')
Dphibb_gen = SetVariable(newtree,'Dphibb_gen')
Mqq_gen = SetVariable(newtree,'Mqq_gen')
Mbb_gen = SetVariable(newtree,'Mbb_gen')

arrayMax = 10
CSV = SetVariable(newtree,'CSV','F',arrayMax)

if maxEvents<0: maxEvents = nEntries
nEntries = min(nEntries,maxEvents)
for entry in range(0,nEntries):
    tree.GetEntry(entry)

    CSV = []

    if entry%1000==0: print "entry: ",entry

    lorentzvectorswithcsv = []
    for i in range(tree.nJet):
        jet = ROOT.TLorentzVector()
        jet.SetPtEtaPhiM(tree.Jet_pt[i],tree.Jet_eta[i],tree.Jet_phi[i],tree.Jet_mass[i])
        jet.csv = tree.Jet_btagCSV[i]
        jet.mcMatchId = tree.Jet_mcMatchId[i]
        jet.mcFlavour = tree.Jet_mcFlavour[i]
        if tree.Jet_pt[i]>30:
            lorentzvectorswithcsv.append(jet)

    SortByCSV(lorentzvectorswithcsv)
    for i,jet in enumerate(lorentzvectorswithcsv):
        if i>=arrayMax: break
        CSV[i]=jet.csv

    (b1,b2,q1,q2) = Sort(lorentzvectorswithcsv,'Eta')
    (Detaqq_eta[0],Dphibb_eta[0],Mqq_eta[0],Mbb_eta[0]) = GetVariablesToFill(b1,b2,q1,q2)

    (b1,b2,q1,q2) = Sort(lorentzvectorswithcsv,'1BTagAndEta')
    (Detaqq_1b[0],Dphibb_1b[0],Mqq_1b[0],Mbb_1b[0]) = GetVariablesToFill(b1,b2,q1,q2)

    (b1,b2,q1,q2) = Sort(lorentzvectorswithcsv,'2BTagAndPt')
    (Detaqq_2b[0],Dphibb_2b[0],Mqq_2b[0],Mbb_2b[0]) = GetVariablesToFill(b1,b2,q1,q2)

    (b1,b2,q1,q2) = Sort(lorentzvectorswithcsv,'Gen')
    (Detaqq_gen[0],Dphibb_gen[0],Mqq_gen[0],Mbb_gen[0]) = GetVariablesToFill(b1,b2,q1,q2)

    newtree.Fill()

newtree.AutoSave()
output.Write()
output.Close()
 """
