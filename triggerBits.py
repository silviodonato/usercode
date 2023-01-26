from ROOT import *
from DataFormats.FWLite import Handle, Events

fileName = "root://eoscms.cern.ch//store/data/Run2022F/ParkingDoubleMuonLowMass6/AOD/PromptReco-v1/000/360/486/00000/3799b9b5-e9d4-4a0e-946d-876115a9a716.root"
filesInput = [fileName]
events = Events (filesInput)
## get the first event
for iev,event in enumerate(events): break


############# print all HLT trigger bits #############################
def checkTriggerIndex(name,index, names):
    if not 'firstTriggerError' in globals():
        global firstTriggerError
        firstTriggerError = True
    if index>=names.size():
        if firstTriggerError:
            for tr in names: print(tr)
            print()
            print()
            print(name," not found!")
            firstTriggerError = False
            return False
        else:
            return False
    else:
        return True

HLTprocess = "HLT"
triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::%s"%HLTprocess)
event.getByLabel(triggerBitLabel, triggerBits)
triggerBits.product()
names = event.object().triggerNames(triggerBits.product())
triggerNames = names.triggerNames()
for triggerName in triggerNames:
    index = names.triggerIndex(triggerName)
    if checkTriggerIndex(triggerName,index,names.triggerNames()):
        print(triggerBits.product().accept(index)),
    else:
        print("-1",)
    print(triggerName)


############# print all L1 trigger bits (from RAW/AOD) #############################

l1tBits, l1tBitLabel = Handle("GlobalObjectMapRecord"), ("hltGtStage2ObjectMap::%s"%HLTprocess)
event.getByLabel(l1tBitLabel, l1tBits)
gtMap = l1tBits.product().gtObjectMap()
for obj in gtMap:
    print(obj.algoBitNumber(), obj.algoName(), obj.algoGtlResult())

