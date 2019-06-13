from ROOT import *
from DataFormats.FWLite import Handle, Events

filesInput = "root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/DarkPhotonToMuMu_M50_madgraph_pythia8_TuneCP5/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/10000/CABCDDC4-1072-534B-86A1-C0FA82780AF1.root"
events = Events (filesInput)
for iev,event in enumerate(events): break

genHandle = Handle("GenEventInfoProduct")
event.getByLabel("generator", genHandle)

GenEventInfoProduct, GenEventInfoProductLabel = Handle("GenEventInfoProduct"), ("generator::SIM")
event.getByLabel(GenEventInfoProductLabel, GenEventInfoProduct)
weights = GenEventInfoProduct.product().weights()
for i in range(weights.size()):
    print("weights()[%d] = %f"%(i,weights.at(i)))
