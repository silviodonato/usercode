'''
This code is supposed to work with the L1Accept dataset (DST_Physics and DST_ZeroBias)
python3 -i printTriggerBit.py  /eos/cms/tier0/store/data/Run2022D/L1Accept/RAW/v1/000/357/895/00000/e4e0c2b4-99ec-493c-9e7c-d9d54e2924e1.root 

It will print the L1 trigger bit before PS, afert mask, after prescale, and allows you to apply a selection based on HLT.

It was used to demostrate that apply a prescale of 2 to all the L1 seeds does not decrease the L1 trigger rate of a factor of 2. (August 2022)
 
''' 

import sys
from ROOT import *
from DataFormats.FWLite import Handle, Events

filesInput = [sys.argv[1]]
events = Events (filesInput)
for iev,event in enumerate(events): break

#def checkTriggerIndex(name,index, names):
#    if not 'firstTriggerError' in globals():
#        global firstTriggerError
#        firstTriggerError = True
#    if index>=names.size():
#        if firstTriggerError:
#            for tr in names: print(tr)
#            print()
#            print()
#            print(name," not found!")
#            firstTriggerError = False
#            return False
#        else:
#            return False
#    else:
#        return True

#HLTprocess = "HLT"
#triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::%s"%HLTprocess)
#event.getByLabel(triggerBitLabel, triggerBits)
#triggerBits.product()
#names = event.object().triggerNames(triggerBits.product())
#triggerNames = names.triggerNames()
#for triggerName in triggerNames:
#    index = names.triggerIndex(triggerName)
#    if checkTriggerIndex(triggerName,index,names.triggerNames()):
#        print(triggerBits.product().accept(index)),
#    else:
#        print("-1",)
#    print(triggerName)


#####################

#l1tBits, l1tBitLabel = Handle("GlobalObjectMapRecord"), ("hltGtStage2ObjectMap::%s"%HLTprocess)
#event.getByLabel(l1tBitLabel, l1tBits)
#gtMap = l1tBits.product().gtObjectMap()
#for obj in gtMap:
#    print(obj.algoBitNumber(), obj.algoName(), obj.algoGtlResult())


#print("Run=%d Lumi=%d"%(event.eventAuxiliary().run(),event.eventAuxiliary().luminosityBlock()))
#######################3
#oldLumi = -1
#for iev,event in enumerate(events):
#    lumi = event.eventAuxiliary().luminosityBlock()
#    if oldLumi != lumi:
#        oldLumi = lumi
#        rates=[0]*triggerBits.product().size()
#    if not iev%10==0: continue
#    try:
#        event.getByLabel(l1tBitLabel, l1tBits)
#        l1tBits.product()
##        print("OK")
#    except:
##        print("NO L1T MAP")
#        continue
#    event.getByLabel(triggerBitLabel, triggerBits)
#    triggerBits.product()
##    names = event.object().triggerNames(triggerBits.product())
##    index = names.triggerIndex("HLT_Random_v3")
#    DST_ZeroBias = names.triggerIndex("HLT_ZeroBias_v7")
#    if triggerBits.product().accept(DST_ZeroBias):
#        L1_SingleIsoEG30er2p5 = l1tBits.product().getObjectMap("L1_SingleIsoEG30er2p5")
#        if(L1_SingleIsoEG30er2p5.algoGtlResult())
#        print(L1_SingleIsoEG30er2p5.algoGtlResult())
#        if triggerBits.product().accept(index):
#            FINOR = True
#    if not FINOR:
#        print(FINOR)
#    elif iev%10000==0:
#        print("Run=%d Lumi=%d"%(event.eventAuxiliary().run(),event.eventAuxiliary().luminosityBlock()))
#        print(iev, FINOR)
#        
#        
#        


#GlobalAlgBlkBXVector_hltGtStage2Digis__HLT.


HLTprocess = "HLT"
triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::%s"%HLTprocess)
event.getByLabel(triggerBitLabel, triggerBits)
names = event.object().triggerNames(triggerBits.product())
triggerNames = names.triggerNames()

DST_ZeroBias = names.triggerIndex("DST_ZeroBias_v3")
DST_Physics = names.triggerIndex("DST_Physics_v8")
HLT_Ele30_WPTight_Gsf_v2 = names.triggerIndex("HLT_Ele30_WPTight_Gsf_v2")
count = 0
for iev,event in enumerate(events):
    if iev>5000: break
    if event.eventAuxiliary().luminosityBlock()!=34: continue
    val = event.getByLabel(triggerBitLabel, triggerBits)
    if triggerBits.product().accept(HLT_Ele30_WPTight_Gsf_v2) and triggerBits.product().accept(DST_Physics):
        count+=1
        lumi = event.eventAuxiliary().luminosityBlock()
        l1tBits, l1tBitLabel = Handle("BXVector<GlobalAlgBlk> "), ("hltGtStage2Digis")
        val = event.getByLabel(l1tBitLabel, l1tBits)
        l1Bits_inTime = l1tBits.product().at(0,0)
        print("Run=%d Lumi=%d Event=%d"%(event.eventAuxiliary().run(),event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event()))
        print("PS column = ",l1Bits_inTime.getPreScColumn())
        for bit in range(159,197):
            print("bit = %d %d %d %d"%(bit, l1Bits_inTime.getAlgoDecisionInitial()[bit], l1Bits_inTime.getAlgoDecisionInterm()[bit], l1Bits_inTime.getAlgoDecisionFinal()[bit]))
