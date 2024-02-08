import os

value = str(os.environ['VAL'])
print(value)

tag = "longRun_WpiGamma"

import FWCore.ParameterSet.Config as cms

import importlib
hltMenu = importlib.import_module(value)
process = hltMenu.process


#User-defined customization functions
#from mycustomisation import replaceTrackMerger
#process = replaceTrackMerger(process)

process.Wselector = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("genParticles"),
    cut = cms.string("mass>80.26 & mass<80.46")
)
process.Wfilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("Wselector"),
    minNumber = cms.uint32( 1 ),
)

process.HLTBeginSequence.insert(0, process.Wfilter)
process.HLTBeginSequence.insert(0, process.Wselector)

process.hltL1sDSTRun3JetHTPFScoutingPixelTracking.L1SeedsLogicalExpression = "L1_AlwaysTrue"

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
process.options.numberOfThreads = 64
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

process.hltOutputScoutingPF = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "outputScoutingPF_%s_%s.root"%(tag, value) ),
    compressionAlgorithm = cms.untracked.string( "ZSTD" ),
    compressionLevel = cms.untracked.int32( 3 ),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string( "" ),
        dataTier = cms.untracked.string( "RAW" )
    ),
#    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'Dataset_ScoutingPFRun3' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltSiStripExcludedFEDListProducer_*_*',
      'keep *_hltMeasurementTrackerEvent_*_*',
      'keep *_hltFEDSelectorL1_*_*',
      'keep *_hltScoutingEgammaPacker_*_*',
      'keep *_hltScoutingMuonPacker_*_*',
      'keep *_hltScoutingPFPacker_*_*',
      'keep *_hltScoutingPrimaryVertexPacker_*_*',
      'keep *_hltScoutingTrackPacker_*_*',
      'keep *_hltPixelTracks_*_*',
#      'keep *Hit*_*_*_*',
      'keep *Pos*_*_*_*',
#      'keep *_*Strip*_*_*',
      'keep *_*genParticle*_*_*',
      'keep *_hltPixelTracksAnd*_*_*',
      'keep *_hltPixelTracksToBeExtended_*_*',
      'keep *_hltPixelTracksToBeNotExtended_*_*',
      'keep *_hltPixelTracksToNotBeExtended_*_*',
      'keep *_hltScoutingTracks_*_*',
      'keep *_hltMergedTracks_*_*',
      'keep *_hltIter0PFlowTrackSelectionHighPurity*_*_*',
      'keep *_*ForScouting_*_*',
      'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
      'keep *_hltParticleFlow_*_*',
      'keep *_hltPixelVertices_*_*',
      'keep edmTriggerResults_*_*_*' )
)

process.ScoutingPFOutput = cms.FinalPath( process.hltOutputScoutingPF )
process.schedule.insert(-1, process.ScoutingPFOutput)

files = []
for i in range(50):
    files.append('file:/eos/user/p/pellicci/MesonGamma_root/2023/Wpigamma_RAW/Wpluspigamma_RAW2023_%d.root'%i)
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
