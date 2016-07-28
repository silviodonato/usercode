import sys
from ROOT import *
from DataFormats.FWLite import Handle, Events

filesInput = [sys.argv[1]]
events = Events (filesInput)
for iev,event in enumerate(events): break

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


triggerEvent, triggerEventLabel = Handle("trigger::TriggerEvent"), ("hltTriggerSummaryAOD::HLT2")
event.getByLabel(triggerEventLabel, triggerEvent) ## AOD
trigObjColl = triggerEvent.product().getObjects()

#calojetCollectionForBtag = "hltSelector8CentralJetsL1FastJet"
#collectionKeysForBtag = getCollectionKeys(triggerEvent.product(),edm.InputTag(calojetCollectionForBtag,"","HLT2"))

#for key in collectionKeysForBtag:
#    jet = trigObjColl[key]
#    print jet.pt()

BTagFilter = "hltBTagCaloCSVp087Triple"

filterIndex = triggerEvent.product().filterIndex(edm.InputTag(BTagFilter,"","HLT2"))
filterKeys = triggerEvent.product().filterKeys(filterIndex)

print "Pt of jets passing BTagFilter:"
for key in filterKeys:
    jet = trigObjColl[key]
    print jet.pt()
