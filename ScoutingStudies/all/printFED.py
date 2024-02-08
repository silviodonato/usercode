import ROOT
from FWCore.ParameterSet.VarParsing import VarParsing


options = VarParsing ('analysis')

options.maxEvents = 1000000
#options.inputFiles = ["outputScoutingPF__.root"]
#options.inputFiles = ["outputScoutingPF.root"]
#options.inputFiles = ["outputScoutingPF_noAddTracks.root"]

inputFile = "RAW-RECO-ZMu.root"
options.inputFiles.clear()
options.inputFiles = [inputFile]
#options.inputFiles = ["outputScoutingPF_original.root"]

#options.secondaryInputFiles = [
#]

print(options.maxEvents)
print(options.inputFiles)
print(options.secondaryInputFiles)

#file_ = ROOT.TFile.Open("/eos/cms//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/21a72136-634d-4377-9077-5d708302fc46.root")
#events = file_.Get("Events")
#events.SetBranchStatus("*", 0)
#events.SetBranchStatus("*scoutingPfCandidate*g4SimHits*", 1)

#def twoLeadingCandidates(collection):
#    
from DataFormats.FWLite import Handle, Events
events = Events (options)

siclusters, siclusterLabel = Handle("edmNew::DetSetVector<SiStripCluster>"), ("siStripClusters","","RECO")


for iev,event in enumerate(events):
    event.getByLabel(siclusterLabel, siclusters)
    if iev%100==0: print(iev)
    for siclusterdet in siclusters.product():
        print(siclusterdet.detId())
        for sicluster in siclusterdet:
            1
            break
    event.getByLabel(siclusterLabel, siclusters)
    if iev>1:
        break

del events
ROOT.gROOT.SetBatch(1)
c1 = ROOT.TCanvas("c1")

first = "ScoutingPF"
histos[first].SetMaximum(histos[first].GetMaximum()*2)
histos[first].Draw()

for i, histo in enumerate(histos.values()):
    if histo!=first:
        histo.Draw("same")

leg = ROOT.TLegend(0.1,0.7,0.48,0.9)
for name in histos:
    leg.AddEntry(histos[name], name, "l")

leg.Draw()

fName = inputFile
fName = fName.replace("output","plot")
c1.SaveAs(fName)
c1.SaveAs(fName.replace(".root",".png"))


