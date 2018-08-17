import ROOT
import itertools
from array import array
from math import sqrt, pi, log10, log, exp
# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

from math import sqrt, pi, log10, log, exp
from utils import deltaR,SetVariable,DummyClass,productWithCheck,checkTriggerIndex,FillVector,BookVector,Matching,getHLTindexes

Handle.productWithCheck = productWithCheck

filterFunctionJets = lambda x: x.pt()>20 and x.bDiscriminator("pfDeepCSVJetTags:probbb")>0.2
maxJets = 20
triggerNames = [
'HLT_PFHT1050_v',
]

def launchNtupleFromMINIAOD(fileOutput,filesInput,maxEvents,  secondaryFiles=None, preProcessing=False):
    f = ROOT.TFile(fileOutput,"recreate")
    tree = ROOT.TTree("tree","tree")
    
    evt         = SetVariable(tree,'evt',"I")
    lumi        = SetVariable(tree,'lumi',"I")
    run         = SetVariable(tree,'run',"I")
    jets        = BookVector(tree, "jets", ['pt','eta','phi','mass','muonMatch','muonMatchDR','btag','btaglight','btagCSV'],maxJets)
    hltmuons    = BookVector(tree, "hltmuons", ['pt','eta','phi','mass'],maxJets)
    
    hltObject = ("hltIterL3MuonCandidates::HLT","hltL3fL1sMu22OrParkL1f0L2f10QL3Filtered12Q")
    
    triggerBits_source, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::HLT")
    triggerObjects_source, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "slimmedPatTrigger"
    #    triggerPrescales, triggerPrescaleLabel  = Handle("pat::PackedTriggerPrescales"), "patTrigger"
    patJets_source, patJetLabel = Handle("vector<pat::Jet>"), ("slimmedJets") #AOD
    l1Muons_source, l1MuonLabel = Handle("BXVector<l1t::Muon>"), ("gmtStage2Digis:Muon") #AOD
    
    #    triggerEvent, triggerEventLabel = Handle("trigger::TriggerEvent"), ("hltTriggerSummaryAOD::HLT")
    
    events = Events (filesInput)
    events.to(0)
    
    firstEvent = 0
    
    tree.Print()
    eventSize = events.size()
    if maxEvents<0: maxEvents = eventSize
    
    hltIndexRun = -1
    for iev in range(firstEvent,min(firstEvent+maxEvents,eventSize)):
        events.to(iev)
        run[0] = events.eventAuxiliary().run()
        lumi[0] = events.eventAuxiliary().luminosityBlock()
        evt[0] = events.eventAuxiliary().event()
        if iev%1000==1: print "Event: ",iev," done. Run=",run[0], " Lumi=",lumi[0], " EventNumber=",evt[0]
        
        events.getByLabel(triggerBitLabel, triggerBits_source)
        names = events.object().triggerNames(triggerBits_source.product())
        if hltIndexRun != run[0]:
            hltIndexRun = run[0]
            triggerIndexes = getHLTindexes (triggerNames, names)
        triggerValues = [triggerBits_source.product().accept(triggerIndex) for triggerIndex in triggerIndexes]
        triggerOR = max(triggerValues)
        
        if triggerOR<1: continue ##drop events not passing the triggers
        
        events.getByLabel(patJetLabel, patJets_source)
        events.getByLabel(l1MuonLabel, l1Muons_source)
        events.getByLabel(triggerObjectLabel, triggerObjects_source)
        FillVector(patJets_source,jets,filterFunctionJets)
        FillVector(patJets_source,jets,filterFunctionJets)
        
        hltmuons.num[0] = 0
        for j,to in enumerate(triggerObjects_source.product()):
            to.unpackPathNames(names)
            to.unpackFilterLabels(events.object(),triggerBits_source.product())
            (hltCollection,hltFilter) = hltObject
            if hltCollection in to.collection():
                if hltFilter in to.filterLabels():
                    hltmuons.pt[hltmuons.num[0]] = to.pt()
                    hltmuons.eta[hltmuons.num[0]] = to.eta()
                    hltmuons.phi[hltmuons.num[0]] = to.phi()
                    hltmuons.mass[hltmuons.num[0]] = to.mass()
                    hltmuons.num[0] += 1
        
        for i in range(jets.num[0]):
            idx, dR = Matching(jets.eta[i], jets.phi[i], hltmuons)
            jets.muonMatch[i] = idx 
            jets.muonMatchDR[i] = dR 
        tree.Fill()
    
    f.Write()
    f.Close()




if __name__ == "__main__":
    maxEvents=10000
    fileOutput = 'tree.root'
    filesInput=[
    "0A5DE6E9-74A0-E811-8E29-FA163E225AB4.root",
    #"TT_Spring15_AODSIM.root",
    ]




    print "fileOutput=",fileOutput
    print
    print "filesInput=",filesInput
    print
    print "maxEvents=",maxEvents
    print
    launchNtupleFromMINIAOD(fileOutput,filesInput,maxEvents, secondaryFiles=None, preProcessing=False)

