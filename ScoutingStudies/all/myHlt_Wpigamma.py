import os

value = int(os.environ['VAL'])
print(value)

import FWCore.ParameterSet.Config as cms

# hltGetConfiguration /users/sdonato/2024Jan/ScoutingTracking/HLT --globaltag 124X_mcRun3_2022_realistic_v12 --mc --unprescale --output none --max-events 100 --input file:/eos/user/p/pellicci/MesonGamma_root/2023/Wpipipi_RAW/Wpluspipipi_RAW2023_27.root --eras Run3 --output none --paths DST_Run3_*,HLT_PFJet40_*  --l1-emulator uGT --l1 L1Menu_Collisions2023_v1_3_0_xml --dbproxy > hltMC.py

# /users/sdonato/2024Jan/ScoutingTracking/HLT/V5

# /dev/CMSSW_13_3_0/GRun/V14 (CMSSW_13_3_0)

from hltMC import process

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.options.numberOfThreads = 64
process.options.numberOfStreams = 0

#process.hltPixelTracksInRegionIter0L3MuonNoVtx.tracks = "hltPixelTracks" 
#process.hltPixelTracksInRegionIter0L3Muon.tracks = "hltPixelTracks" 


#process.hltPixelTracksInRegionL2NoVtx.tracks = "hltPixelTracks"
#process.hltPixelVertices.TrackCollection = "hltPixelTracks"
#process.hltPixelTracksInRegionL1NoVtx.tracks = "hltPixelTracks"

#process.hltPixelTracksInRegionL2.tracks = "hltPixelTracks"
#process.hltPixelTracksInRegionL1.tracks = "hltPixelTracks"
#process.hltPixelTracksAndExtended.TrackProducers = ('hltIter0PFlowTrackSelectionHighPurityForScouting','hltPixelTracks' )
#process.hltPixelTracksAndExtended.selectedTrackQuals = ('hltIter0PFlowTrackSelectionHighPurityForScouting','hltPixelTracks' )


#del process.HLT_PFJet40_GPUvsCPU_v3

#for fp in list(process.finalPaths_().keys()):
#    if fp != "ScoutingPFOutput":
#        delattr(process, fp)
##        process.outputModules_().remove(om)

#process.DST_Run3_DoubleMuon_PFScoutingPixelTracking_v2.remove(process.hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking)
#process.DST_Run3_DoubleEG_PFScoutingPixelTracking_v2.remove(process.hltL1sDSTRun3DoubleEGPFScoutingPixelTracking)
#process.DST_Run3_EG30_PFScoutingPixelTracking_v22.remove(process.hltL1sDSTRun3EG30PFScoutingPixelTracking)
#process.DST_Run3_JetHT_PFScoutingPixelTracking_v22.remove(process.hltL1sDSTRun3JetHTPFScoutingPixelTracking)
#process.DST_Run3_DoubleMu3_PFScoutingPixelTracking_v22.remove(process.hltL1sDSTRun3DoubleMu3PFScoutingPixelTracking)
#process.DST_Run3_EG16_EG12_PFScoutingPixelTracking_v22.remove(process.hltL1sDSTRun3EG16EG12PFScoutingPixelTracking)

#process.hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking.L1SeedsLogicalExpression = "L1_ZeroBias"
#process.hltL1sDSTRun3JetHTPFScoutingPixelTracking.L1SeedsLogicalExpression = "L1_AlwaysTrue"

process.hltPixelTracksToBeExtended = cms.EDProducer( "TrackWithVertexSelector",
    src = cms.InputTag( "hltPixelTracks" ),
    etaMin = cms.double( 0.0 ),
    etaMax = cms.double( 2.5 ),
    ptMin = cms.double( value ),
    ptMax = cms.double( 1E20 ),
    d0Max = cms.double( 10.0 ),
    dzMax = cms.double( 15.0 ),
    normalizedChi2 = cms.double( 1E20 ),
    numberOfValidHits = cms.uint32( 0 ),
    numberOfLostHits = cms.uint32( 999 ),
    numberOfValidPixelHits = cms.uint32( 0 ),
    ptErrorCut = cms.double( 1E20 ),
    quality = cms.string( "loose" ),
#    quality = cms.string( "highPurity" ),
    useVtx = cms.bool( True ),
#    vertexTag = cms.InputTag( "hltPixelVertices" ),
    vertexTag = cms.InputTag( "hltTrimmedPixelVertices" ),
    timesTag = cms.InputTag( "" ),
    timeResosTag = cms.InputTag( "" ),
    nVertices = cms.uint32( 2 ),
    vtxFallback = cms.bool( True ),
    zetaVtx = cms.double( 0.3 ),
    rhoVtx = cms.double( 0.2 ),
    nSigmaDtVertex = cms.double( 0.0 ),
    copyExtras = cms.untracked.bool( False ),
    copyTrajectories = cms.untracked.bool( False )
)


#process.hltPixelTracksCleanForBTag = cms.EDProducer( "TrackWithVertexSelector",
#    src = cms.InputTag( "hltPixelTracks" ),
#    etaMin = cms.double( 0.0 ),
#    etaMax = cms.double( 5.0 ),
#    ptMin = cms.double( 0.3 ),
#    ptMax = cms.double( 9999.0 ),
#    d0Max = cms.double( 999.0 ),
#    dzMax = cms.double( 999.0 ),
#    normalizedChi2 = cms.double( 999999.0 ),
#    numberOfValidHits = cms.uint32( 0 ),
#    numberOfLostHits = cms.uint32( 999 ),
#    numberOfValidPixelHits = cms.uint32( 3 ),
#    ptErrorCut = cms.double( 5.0 ),
#    quality = cms.string( "loose" ),
#    useVtx = cms.bool( True ),
#    vertexTag = cms.InputTag( "hltTrimmedPixelVertices" ),
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
#process.hltPixelTracksForBTag = cms.EDProducer( "TrackSelectorByRegion",
#    tracks = cms.InputTag( "hltPixelTracksCleanForBTag" ),
#    regions = cms.InputTag( "hltBTaggingRegion" ),
#    produceTrackCollection = cms.bool( True ),
#    produceMask = cms.bool( True )
#)
#process.hltIter0PFLowPixelSeedsFromPixelTracksForBTag = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
#    InputCollection = cms.InputTag( "hltPixelTracksForBTag" ),
#    InputVertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
#    originHalfLength = cms.double( 0.3 ),
#    originRadius = cms.double( 0.1 ),
#    useProtoTrackKinematics = cms.bool( False ),
#    useEventsWithNoVertex = cms.bool( True ),
#    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
#    usePV = cms.bool( False ),
#    includeFourthHit = cms.bool( True ),
#    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) )
#)

process.hltOutputScoutingPF = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "outputScoutingPF_Wpigamma_pt%d.root"%value ),
    compressionAlgorithm = cms.untracked.string( "ZSTD" ),
    compressionLevel = cms.untracked.int32( 3 ),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string( "" ),
        dataTier = cms.untracked.string( "RAW" )
    ),
#    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'Dataset_ScoutingPFRun3' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltFEDSelectorL1_*_*',
      'keep *_hltScoutingEgammaPacker_*_*',
      'keep *_hltScoutingMuonPacker_*_*',
      'keep *_hltScoutingPFPacker_*_*',
      'keep *_hltScoutingPrimaryVertexPacker_*_*',
      'keep *_hltScoutingTrackPacker_*_*',
      'keep *_hltPixelTracks_*_*',
      'keep *_hltPixelTracksAnd*_*_*',
      'keep *_hltPixelTracksToBeExtended_*_*',
      'keep *_hltMergedTracks_*_*',
      'keep *_hltIter0PFlowTrackSelectionHighPurity*_*_*',
      'keep *_hltDoubletRecoveryPFlowTrackSelectionHighPurity_*_*',
      'keep *_hltParticleFlow_*_*',
      'keep *_hltPixelVertices_*_*',
      'keep edmTriggerResults_*_*_*' )
)

process.ScoutingPFOutput = cms.FinalPath( process.hltOutputScoutingPF )
process.schedule.insert(-1, process.ScoutingPFOutput)

# add specific customizations
_customInfo = {}
_customInfo['menuType'  ]= "GRun"
_customInfo['globalTags']= {}
_customInfo['globalTags'][True ] = "auto:run3_hlt_GRun"
_customInfo['globalTags'][False] = "auto:run3_mc_GRun"
_customInfo['inputFiles']={}
_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
_customInfo['maxEvents' ]=  1000
_customInfo['globalTag' ]= "124X_mcRun3_2022_realistic_v12"
files = []
for i in range(50):
    files.append('file:/eos/user/p/pellicci/MesonGamma_root/2023/Wpigamma_RAW/Wpluspigamma_RAW2023_%d.root'%i)
_customInfo['inputFile' ]=  files
_customInfo['realData'  ]=  False

from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process,"GRun",_customInfo)
