import sys
from ROOT import *
from DataFormats.FWLite import Handle, Events

filesInput = [sys.argv[1]]
events = Events (filesInput)
for iev,event in enumerate(events): break

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


####################

l1tBits, l1tBitLabel = Handle("GlobalObjectMapRecord"), ("hltGtStage2ObjectMap::%s"%HLTprocess)
event.getByLabel(l1tBitLabel, l1tBits)
gtMap = l1tBits.product().gtObjectMap()
for obj in gtMap:
    print(obj.algoBitNumber(), obj.algoName(), obj.algoGtlResult())


######################3
for iev,event in enumerate(events):
    try:
        event.getByLabel(l1tBitLabel, l1tBits)
        l1tBits.product()
#        print("OK")
    except:
#        print("NO L1T MAP")
        continue
    event.getByLabel(triggerBitLabel, triggerBits)
    triggerBits.product()
#    names = event.object().triggerNames(triggerBits.product())
#    index = names.triggerIndex("HLT_Random_v3")
    index = names.triggerIndex("HLT_Physics_v7")
    if triggerBits.product().accept(index):
#        print("Trigger Accepted")
        ZeroBias = l1tBits.product().getObjectMap("L1_ZeroBias")
        ETT35 = l1tBits.product().getObjectMap("L1_ETT35")
        ETT20 = l1tBits.product().getObjectMap("L1_ETT20")
        print(ZeroBias.algoGtlResult(), ETT35.algoGtlResult(), ETT20.algoGtlResult())
