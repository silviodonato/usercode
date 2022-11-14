#trigger="HLT_Ele27_eta2p1_WPLoose_Gsf_v1"
fileName = "/eos/cms/store/data/Run2022F/EphemeralHLTPhysics5/MINIAOD/PromptReco-v1/000/361/468/00000/42bcb3ce-5a3c-4868-a196-53e3bde4664b.root"
triggerFilter="hltPFJetForBtagSelector"

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()

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
for j,to in enumerate(triggerObjects.product()):
#    to.unpackPathNames(names)
    to.unpackFilterLabels(event.object(), triggerBits.product())
    if triggerFilter in to.filterLabels():
        print("Trigger objects passing filter %s. pt=%f, eta=%f, phi=%f"%(triggerFilter,to.pt(),to.eta(),to.phi()))
    else:
        print("Trigger objects passing filter %s."%(to.filterLabels()))
    
