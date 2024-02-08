import os

value = str(os.environ['VAL'])
print(value)

tag = "longRunTopMuEG"

import FWCore.ParameterSet.Config as cms

import importlib
hltMenu = importlib.import_module(value)
process = hltMenu.process

process.schedule.remove(process.DQMOutput)


#User-defined customization functions
#from mycustomisation import replaceTrackMerger
#process = replaceTrackMerger(process)

#process.Wselector = cms.EDFilter("CandViewSelector",
#    src = cms.InputTag("genParticles"),
#    cut = cms.string("mass>80.26 & mass<80.46")
#)
#process.Wfilter = cms.EDFilter("CandViewCountFilter",
#    src = cms.InputTag("Wselector"),
#    minNumber = cms.uint32( 1 ),
#)

#process.HLTBeginSequence.insert(0, process.Wfilter)
#process.HLTBeginSequence.insert(0, process.Wselector)

process.hltL1sDSTRun3JetHTPFScoutingPixelTracking.L1SeedsLogicalExpression = "L1_AlwaysTrue"

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
process.options.numberOfThreads = 32
process.options.numberOfStreams = 0

#process.hltScoutingPixelTracksLowPt.cut = cms.string( "!(quality('highPurity') & pt >= 3)" )
#process.hltScoutingPixelTracksHighPt.cut = cms.string( "(quality('highPurity') & pt >= 3)" )

#process.hltScoutingTracks = cms.EDProducer( "TrackListMerger",
#    ShareFrac = cms.double( 0.19 ),
#    FoundHitBonus = cms.double( 5.0 ),
#    LostHitPenalty = cms.double( 20.0 ),
#    MinPT = cms.double( 0.05 ),
#    Epsilon = cms.double( -0.001 ),
#    MaxNormalizedChisq = cms.double( 1000.0 ),
#    MinFound = cms.int32( 3 ),
#    TrackProducers = cms.VInputTag( 'hltScoutingPixelTracksLowPt','hltIter0PFLowPixelSeedsFromPixelTracksForScouting','hltIter0PFlowTrackSelectionHighPurityForScouting' ),
#    hasSelector = cms.vint32( 0, 0, 0 ),
#    indivShareFrac = cms.vdouble( 1.0, 1.0, 1.0 ),
#    selectedTrackQuals = cms.VInputTag( 'hltScoutingPixelTracksLowPt','hltIter0PFLowPixelSeedsFromPixelTracksForScouting','hltIter0PFlowTrackSelectionHighPurityForScouting' ),
#    setsToMerge = cms.VPSet( 
#      cms.PSet(  pQual = cms.bool( False ),
#        tLists = cms.vint32( 0, 1, 2 )
#      )
#    ),
#    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
#    allowFirstHitShare = cms.bool( True ),
#    newQuality = cms.string( "confirmed" ),
#    copyExtras = cms.untracked.bool( True ),
#    writeOnlyTrkQuals = cms.bool( False ),
#    copyMVA = cms.bool( False )
#)

#process.hltPixelTracksZetaClean = cms.EDProducer( "TrackWithVertexSelector",
#    src = cms.InputTag( "hltScoutingTracks" ),
#    etaMin = cms.double( 0.0 ),
#    etaMax = cms.double( 5.0 ),
#    ptMin = cms.double( 0.3 ),
#    ptMax = cms.double( 500.0 ),
#    d0Max = cms.double( 999.0 ),
#    dzMax = cms.double( 999.0 ),
#    normalizedChi2 = cms.double( 999999.0 ),
#    numberOfValidHits = cms.uint32( 0 ),
#    numberOfLostHits = cms.uint32( 999 ),
#    numberOfValidPixelHits = cms.uint32( 3 ),
#    ptErrorCut = cms.double( 5.0 ),
#    quality = cms.string( "highPurity" ),
#    useVtx = cms.bool( True ),
#    vertexTag = cms.InputTag( "hltPixelVertices" ),
#    timesTag = cms.InputTag( "" ),
#    timeResosTag = cms.InputTag( "" ),
#    nVertices = cms.uint32( 2 ),
#    vtxFallback = cms.bool( True ),
#    zetaVtx = cms.double( 0.3 ),
#    rhoVtx = cms.double( 0.2 ),
#    nSigmaDtVertex = cms.double( 0.0 ),
#    copyExtras = cms.untracked.bool( False ),
#    copyTrajectories = cms.untracked.bool( False )
#)

process.GlobalTag.globaltag = "133X_dataRun3_HLT_for2024TSGStudies_v1"

process.hltOutputScoutingPF = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "outputScoutingPF_Bs_%s_%s.root"%(tag, value) ),
    compressionAlgorithm = cms.untracked.string( "ZSTD" ),
    compressionLevel = cms.untracked.int32( 3 ),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string( "" ),
        dataTier = cms.untracked.string( "RAW" )
    ),
#    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'Dataset_ScoutingPFRun3' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
#      'keep *_hltSiStripExcludedFEDListProducer_*_*',
#      'keep *_hltMeasurementTrackerEvent_*_*',
#      'keep *_hltFEDSelectorL1_*_*',
      'keep *_hltScoutingEgammaPacker_*_*',
      'keep *_hltScoutingMuonPacker_*_*',
      'keep *_hltScoutingPFPacker_*_*',
      'keep *_hltScoutingPrimaryVertexPacker_*_*',
      'keep *_hltScoutingTrackPacker_*_*',
##      'keep *_hltPixelTracks_*_*',
##      'keep *Hit*_*_*_*',
#      'keep *Pos*_*_*_*',
##      'keep *_*Strip*_*_*',
      'keep *_*genParticle*_*_*',
      'keep *_*Jet*_*_RECO',
      'keep *_*Tau*_*_RECO',
      'keep *Muon*_*_*_RECO',
      'keep *Photon*_*_*_RECO',
      'keep *Electr*_*_*_RECO',
      'keep *MET*_*_*_RECO',
      'keep recoCandidateedmPtrsrecoJetTagInforecoIPTagInforecoVertexCompositePtrCandidaterecoTemplatedSecondaryVertexTagInfos_*_*_RECO',
      'drop *_*trackRefsForJets*_*_RECO',
      
#      'keep *_hltPixelTracksAnd*_*_*',
#      'keep *_hltPixelTracksToBeExtended_*_*',
#      'keep *_hltPixelTracksToBeNotExtended_*_*',
#      'keep *_hltPixelTracksToNotBeExtended_*_*',
##      'keep *_hltScoutingTracks_*_*',
#      'keep *_hltMergedTracks_*_*',
#      'keep *_hltIter0PFlowTrackSelectionHighPurity*_*_*',
#      'keep *_*ForScouting_*_*',
#      'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
#      'keep *_hltParticleFlow_*_*',
#      'keep *_hltPixelVertices_*_*',
      'keep edmTriggerResults_*_*_*' 
      )
)

process.ScoutingPFOutput = cms.FinalPath( process.hltOutputScoutingPF )
process.schedule.insert(-1, process.ScoutingPFOutput)

#files = ["file:/data/user/sdonato/ScoutingTracking/21a72136-634d-4377-9077-5d708302fc46.root"]
files = [
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/0fed70e1-9230-4a9f-813a-0176fa291c42.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/2b1158ff-b5ec-4c9d-b08c-ce7654cc28d8.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/58ff3041-7b11-430e-8f72-6746aefc9470.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/5a3d1017-211d-4208-b70a-17a6843830ad.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/667a0832-d7ec-4305-a161-8658641d1fa5.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/7137d0cf-f2a6-44e8-a9b6-65fd7da643a5.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/73f92331-0c93-4a8b-a1c4-578ac7c66d91.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/79342ee9-428e-4602-8d2e-7f7d06f321cb.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/a5f08c0c-a59d-4c0f-b363-ba541343e0cc.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/c6ace126-41c4-4d5d-b2d7-e946c961a86c.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/c96f9612-03b3-4df8-b68d-64422c76a15e.root",
    "/store/data/Run2023D/MuonEG/RAW-RECO/TopMuEG-PromptReco-v2/000/370/725/00000/d647fc2f-51d4-437b-830f-3d107cc155d9.root"
    #    "root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/21a72136-634d-4377-9077-5d708302fc46.root",
]
#for i in range(50):
##    files.append('file:/eos/user/p/pellicci/MesonGamma_root/2023/Wpipipi_RAW/Wpluspipipi_RAW2023_%d.root'%i)
#    files.append('file:/data/user/sdonato/Wpipipi_RAW/Wpipipi_RAW/Wpluspipipi_RAW2023_%d.root'%i)

process.source.fileNames = files
process.maxEvents.input = -1


## add specific customizations
#_customInfo = {}
#_customInfo['menuType'  ]= "GRun"
#_customInfo['globalTags']= {}
#_customInfo['globalTags'][True ] = "auto:run3_hlt_GRun"
#_customInfo['globalTags'][False] = "auto:run3_mc_GRun"
#_customInfo['inputFiles']={}
#_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
#_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
#_customInfo['maxEvents' ]=  1000
#_customInfo['globalTag' ]= "124X_mcRun3_2022_realistic_v12"
#_customInfo['realData'  ]=  False

#from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
#process = customizeHLTforAll(process,"GRun",_customInfo)


#process.MessageLogger.cerr.FwkReport.limit = 1000000000000000
