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
            for tr in names: print tr
            print
            print name," not found!"
            print
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
        print triggerBits.product().accept(index),
    else:
        print "-1",
    print triggerName
