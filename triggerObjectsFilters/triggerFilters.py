'''
The outut of this script is the number of events passing a given trigger and a given filter.
It works with RAW or AOD data (no MINIAOD, NANOAOD).

Example:

Total number of events: 1955
Number of events passing hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking::HLT: 218
Number of events passing DST_PFScouting_DoubleMuon_v2: 64
Fraction of events passing hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking::HLT: 0.111509
Fraction of events passing DST_PFScouting_DoubleMuon_v2: 0.032737
Fraction of events passing DST_PFScouting_DoubleMuon_v2 after hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking::HLT: 0.293578
'''

import sys
from ROOT import *
from DataFormats.FWLite import Handle, Events

filesInput = ["/eos/cms/store/data/Run2024D/EphemeralHLTPhysics1/RAW/v1/000/380/648/00000/a0f9f0fa-ea35-47c9-b7bd-77f1d35d7e1f.root"]

evMax = -1
evReportEvery = 1000

triggerName = "DST_PFScouting_DoubleMuon_v2"
HLTFilter = "hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking::HLT"

triggerBitLabel = ("TriggerResults","","HLT")
triggerEventLabel = ("hltTriggerSummaryAOD","","HLT")
triggerBitsH = Handle("edm::TriggerResults")
triggerEventH = Handle("trigger::TriggerEvent")



def getFiterSize(triggerEvent,filterName):
    filterIndex = triggerEvent.filterIndex(filterName)
    if filterIndex<triggerEvent.sizeFilters():
        filterKeys = triggerEvent.filterKeys(filterIndex)
        return len(filterKeys)
    else:
        for i in range(triggerEvent.sizeFilters()):
            print(triggerEvent.filterTag(i))
        raise Exception("Filter %s not found in event."%filterName) 

def getTriggerBitResult(triggerBits,triggerName, names):
    pathIndex = names.triggerIndex(triggerName)
    if pathIndex>=triggerBits.size():
        for i in range(triggerBits.size()):
            print(names.triggerName(i))
        raise Exception("Path %s not found in event."%triggerName)
    return triggerBits.accept(pathIndex)

events = Events (filesInput)
#Check only first event interactively
#for iev,event in enumerate(events): break

#Run a loop over all events
count_total = 0
count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking = 0
count_passing_DST_PFScouting_DoubleMuon_v5 = 0
names = None

for iev,event in enumerate(events):
    if iev>evMax and evMax>0: break
    if iev%evReportEvery==0: print("Processing event %d"%iev)
    count_total += 1
    event.getByLabel(triggerBitLabel, triggerBitsH)
    event.getByLabel(triggerEventLabel, triggerEventH)
    triggerBits = triggerBitsH.product()
    triggerEvent = triggerEventH.product()
    if not names: names = event.object().triggerNames(triggerBits)
    if getFiterSize(triggerEvent,HLTFilter)>0:
        count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking += 1
        print("Event %d passes %s."%(iev,HLTFilter))
    if getTriggerBitResult(triggerBits,triggerName, names):
        count_passing_DST_PFScouting_DoubleMuon_v5 += 1
        print("Event %d passes %s."%(iev,triggerName))

print("Total number of events: %d"%count_total)
print("Number of events passing %s: %d"%(HLTFilter,count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking))
print("Number of events passing %s: %d"%(triggerName,count_passing_DST_PFScouting_DoubleMuon_v5))
print("Fraction of events passing %s: %f"%(HLTFilter,float(count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking)/count_total))
print("Fraction of events passing %s: %f"%(triggerName,float(count_passing_DST_PFScouting_DoubleMuon_v5)/count_total))
print("Fraction of events passing %s after %s: %f"%(triggerName,HLTFilter,float(count_passing_DST_PFScouting_DoubleMuon_v5)/count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking))

#     triggerBits.product()
#     names = event.object().triggerNames(triggerBits.product())
#     pathIndex = names.triggerIndex("DST_PFScouting_DoubleMuon_v5")
#     filterIndex = triggerEvent.product().filterIndex(edm.InputTag(HLTFilter,"","HLT"))
# #    print(filterIndex)
#     if filterIndex<triggerEvent.product().sizeFilters():
#  #       print("Filter %s found in event."%HLTFilter)
#         filterKeys = triggerEvent.product().filterKeys(filterIndex)
#         if len(filterKeys)>0:
#             print("Number of objects passing filter: %d"%len(filterKeys))
#             for key in filterKeys:
#                 obj = trigObjColl[key]
#                 print(obj.pt())
# #        print("Number of objects passing filter: %d"%len(filterKeys))
#     else:
#         raise Exception("Filter %s not found in event."%HLTFilter)
# #        print("Filter %s not found in event."%HLTFilter)



# def getCollectionKeys(triggerEvent,inputTag):
#     collectionKeys = []
#     collectionIndex = triggerEvent.collectionIndex(inputTag)
#     if collectionIndex<triggerEvent.sizeCollections():
#         start = 0
#         if collectionIndex>0: start = triggerEvent.collectionKey(collectionIndex-1)
#         stop = triggerEvent.collectionKey(collectionIndex)
#         collectionKeys = range(start, stop)
#         del start
#         del stop
    
#     del collectionIndex
#     return collectionKeys


# HLTprocess = "HLT"
# triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::%s"%HLTprocess)
# event.getByLabel(triggerBitLabel, triggerBits)
# triggerBits.product()
# names = event.object().triggerNames(triggerBits.product())

# triggerEvent, triggerEventLabel = Handle("trigger::TriggerEvent"), ("hltTriggerSummaryAOD::HLT")
# event.getByLabel(triggerEventLabel, triggerEvent) ## AOD
# trigObjColl = triggerEvent.product().getObjects()

# pathIndex = names.triggerIndex("DST_PFScouting_DoubleMuon_v5")

# #calojetCollectionForBtag = "hltSelector8CentralJetsL1FastJet"
# #collectionKeysForBtag = getCollectionKeys(triggerEvent.product(),edm.InputTag(calojetCollectionForBtag,"","HLT2"))

# #for key in collectionKeysForBtag:
# #    jet = trigObjColl[key]
# #    print jet.pt()

# HLTFilter = "hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking"
# #HLTFilter = "hltPreDSTPFScoutingDoubleMuon"
# #HLTFilter = "HLTDoubleMuonScoutingNoVtx"
# #"hltPreDSTPFScoutingDoubleMuon"
# #"HLTDoubleMuonScoutingNoVtx"

# filterIndex = triggerEvent.product().filterIndex(edm.InputTag(HLTFilter,"","HLT"))
# print(filterIndex)
# if filterIndex<triggerEvent.product().sizeFilters():
#     print("Filter %s found in event."%HLTFilter)
#     filterKeys = triggerEvent.product().filterKeys(filterIndex)
#     print("Number of objects passing filter: %d"%len(filterKeys))
