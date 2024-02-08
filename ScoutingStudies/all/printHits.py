import ROOT
from FWCore.ParameterSet.VarParsing import VarParsing


options = VarParsing ('analysis')

options.maxEvents = 1000000
#options.inputFiles = ["outputScoutingPF__.root"]
#options.inputFiles = ["outputScoutingPF.root"]
#options.inputFiles = ["outputScoutingPF_noAddTracks.root"]

#inputFile = "RAW-RECO-ZMu.root"
inputFiles = [
    "outputScoutingPF_test_full_pt0.root",
    "outputScoutingPF_test_secondHalf_pt0.root",
    "outputScoutingPF_test_firstHalf_pt0.root",
    "outputScoutingPF_test_full_pt0.root",
    "outputScoutingPF_test_pt0.root",
    ]

for inputFile in inputFiles:
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

    #edm::OwnVector<TrackingRecHit,edm::ClonePolicy<TrackingRecHit> >    "hltIter0PFlowTrackSelectionHighPurityForScouting"   ""               "HLTX"       

#    trackingRecHits, trackingRecHitLabel = Handle("edm::OwnVector<TrackingRecHit,edm::ClonePolicy<TrackingRecHit> >"), ("hltIter0PFlowTrackSelectionHighPurityForScouting","","HLTX")
    trackingRecHits, trackingRecHitLabel = Handle("edm::OwnVector<TrackingRecHit,edm::ClonePolicy<TrackingRecHit> >"), ("hltIter0PFlowCtfWithMaterialTracksForScouting","","HLTX")

    #hltIter0PFlowTrackSelectionHighPurityForScouting

    countSingle = 0
    countDouble = 0
    for iev,event in enumerate(events):
        event.getByLabel(trackingRecHitLabel, trackingRecHits)
        if iev%100==0: print(iev)
        for trackingRecHit in trackingRecHits.product():
            if trackingRecHit.isValid() and not trackingRecHit.isPixel():
                if trackingRecHit.isSingle():
                    countSingle+= 1
                else:
                    countDouble+= 1
                1/0
    
    print(inputFile)
    print("Double = %f %%. Double = %d. Single = %d."%(countDouble/(countDouble+countSingle)*100, countDouble, countSingle))
