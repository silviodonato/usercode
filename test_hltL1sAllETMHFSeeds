
fileName = 'root://eoscms.cern.ch//eos/cms/store/data/Run2017F/MET/MINIAOD/PromptReco-v1/000/306/095/00000/7A98DCC2-8BC4-E711-AA79-02163E01340A.root'
filterName = "hltL1sAllETMHFSeeds"
#filterName = "hltL1sAllETMHFHTT60Seeds"

HLTpath = "HLT_PFMETTypeOne140_PFMHT140_IDTight_v8"
import ROOT
ROOT.gROOT.SetBatch(True)
#sys.argv = oldargv

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "slimmedPatTrigger"

events = Events(fileName)

print "Events accepted by %s:"%HLTpath
for iev,event in enumerate(events):
    event.getByLabel(triggerBitLabel, triggerBits)
    event.getByLabel(triggerObjectLabel, triggerObjects)
    
    names = event.object().triggerNames(triggerBits.product())
    for i in xrange(triggerBits.product().size()):
        if names.triggerName(i) == HLTpath and triggerBits.product().accept(i):
            counter = 0
            for j,to in enumerate(triggerObjects.product()):
                to.unpackNamesAndLabels(event.object(), triggerBits.product())
                if filterName in to.filterLabels():
                    counter += 1
#                for flts in to.filterLabels():
#                    if "hltL1s" in flts:
#                        print flts
            print "# of objects associated to %s: "%filterName,counter
    if iev > 10: break
