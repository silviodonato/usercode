fileName = "root://eoscms.cern.ch//store/data/Run2022F/ParkingSingleMuon0/AOD/PromptReco-v1/000/362/064/00000/767f3644-6bca-4fa4-ba4a-98f77ea3a3bb.root"
triggerFilter="hltPFmuonForBtagSelector"

# load FWlite python libraries
import ROOT
from DataFormats.FWLite import Handle, Events

def getCollectionKeys(triggerEvent,inputTag):
    collectionKeys = []
    collectionIndex = triggerEvent.collectionIndex(inputTag)
    if collectionIndex<triggerEvent.sizeCollections():
        start = 0
        if collectionIndex>0: start = triggerEvent.collectionKey(collectionIndex-1)
        stop = triggerEvent.collectionKey(collectionIndex)
        collectionKeys = range(start, stop)
        del start
        del stop
    
    del collectionIndex
    return collectionKeys


triggerEvent, triggerEventLabel = Handle("trigger::TriggerEvent"), ("hltTriggerSummaryAOD::HLT")
#triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
events = Events ([fileName])

#get first event
for iev,event in enumerate(events): break 


event.getByLabel(triggerEventLabel, triggerEvent) ## AOD
#trigEvent = triggerEvent.product()
trigObjColl = triggerEvent.product().getObjects()

############ Print collections ##############################

## print all trigger collections produced in this events
for collection in triggerEvent.product().collectionTags():
    print(collection)

## print trigger muons available in muonTrigColl
muonTrigColl = ROOT.edm.InputTag("hltGtStage2Digis","Muon","HLT")  ## L1 muons
#muonTrigColl = ROOT.edm.InputTag("hltL2MuonCandidates","Muon","HLT")  ## L2 muons
collectionKeysL2muons = getCollectionKeys(triggerEvent.product(),muonTrigColl)

for key in collectionKeysL2muons:
    muon = trigObjColl[key]
    print(muon.pt())

############ Print Filters ##############################

## print all trigger filters which ran in this event, and the number of trigger objects passing each filter
for i in range(triggerEvent.product().sizeFilters()):
    print(triggerEvent.product().filterLabel(i),triggerEvent.product().filterKeys(i).size())

muonTriggerFilter = ROOT.edm.InputTag("hltL2fL1sMu5EG20orMu20EG15L1f5L2NoVtxFiltered16","","HLT")
filterIndex = triggerEvent.product().filterIndex(muonTriggerFilter)
filterKeys = triggerEvent.product().filterKeys(filterIndex)

print("Pt of muons passing muonTriggerFilter:")
for key in filterKeys:
    muon = trigObjColl[key]
    print(muon.pt())

