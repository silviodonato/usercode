#trigger="HLT_Ele27_eta2p1_WPLoose_Gsf_v1"
fileName = "root://eoscms.cern.ch//eos/cms/store/data/Run2022F/EphemeralHLTPhysics5/MINIAOD/PromptReco-v1/000/361/468/00000/42bcb3ce-5a3c-4868-a196-53e3bde4664b.root"
triggerFilter="hltPFJetForBtagSelector"

import ROOT
# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "slimmedPatTrigger"

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
events = Events ([fileName])

#get first event
for iev,event in enumerate(events): break 

event.getByLabel(triggerObjectLabel, triggerObjects)
event.getByLabel(triggerBitLabel, triggerBits)
names = event.object().triggerNames(triggerBits.product())

############ Print collections ##############################
### print all trigger objects in the event
print("All trigger objects in the event:")
for j,to in enumerate(triggerObjects.product()):
#    to.unpackPathNames(names)
#    to.unpackNamesAndLabels(event.object(), triggerBits.product())
    to.unpackFilterLabels(event.object(), triggerBits.product())
    print()
    print("Trigger object from collection %s (pt=%f, eta=%f, phi=%f) passed filters:"%(to.collection(),to.pt(),to.eta(),to.phi()))
    for filt in to.filterLabels(): print(filt)

### print all trigger objects of collection muonTrigColl passing muonFilter 

############ Print collections ##############################

## print trigger muons available in muonTrigColl
#muonTrigColl = ROOT.edm.InputTag("hltGtStage2Digis","Muon","HLT")  ## L1 muons
muonTrigColl = ROOT.edm.InputTag("hltL2MuonCandidates","","HLT")  ## L2 muons
muonFilter = 'hltL2fL1sL1DoubleMu0er1p5SQOSdR1p4L1f0L2PreFiltered0'

print("Trigger objects of collection %s passing filter %s:"%(muonTrigColl, muonFilter))
for j,to in enumerate(triggerObjects.product()):
#    to.unpackPathNames(names)
#    to.unpackNamesAndLabels(event.object(), triggerBits.product())
    to.unpackFilterLabels(event.object(), triggerBits.product())
    if to.collection() == muonTrigColl.encode() and muonFilter in to.filterLabels():
        print("Trigger object (pt=%f, eta=%f, phi=%f)"%(to.pt(),to.eta(),to.phi()))
