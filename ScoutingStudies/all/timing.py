import os

value = str(os.environ['VAL'])
print(value)

tag = "longRun"

import FWCore.ParameterSet.Config as cms

import importlib
hltMenu = importlib.import_module(value)
process = hltMenu.process

process.hltL1sDSTRun3JetHTPFScoutingPixelTracking.L1SeedsLogicalExpression = "L1_AlwaysTrue"

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
process.options.numberOfThreads = 64
process.options.numberOfStreams = 0

process.hltOutputScoutingPF = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "outputTiming_%s_%s.root"%(tag, value) ),
    compressionAlgorithm = cms.untracked.string( "ZSTD" ),
    compressionLevel = cms.untracked.int32( 3 ),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string( "" ),
        dataTier = cms.untracked.string( "RAW" )
    ),
#    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'Dataset_ScoutingPFRun3' ) ),
    outputCommands = cms.untracked.vstring( 
      'drop *',
      'keep edmTriggerResults_*_*_*' )
)


process.hltIter0PFlowCkfTrackCandidatesForScouting.cleanTrajectoryAfterInOut = True
process.hltIter0PFlowCkfTrackCandidatesForScouting.doSeedingRegionRebuilding = True
process.hltIter0PFlowCkfTrackCandidatesForScouting.numHitsForSeedCleaner = 0
process.hltIter0PFlowCkfTrackCandidatesForScouting.reverseTrajectories = True
#process.hltIter0PFlowCkfTrackCandidatesForScouting.MeasurementTrackerEvent = "hltMeasurementTrackerEventForScouting"

process.hltIter0PFLowPixelSeedsFromPixelTracksForScouting.includeFourthHit = False
process.hltIter0PFLowPixelSeedsFromPixelTracksForScouting.useEventsWithNoVertex = False

process.GlobalTag.globaltag = "133X_dataRun3_HLT_for2024TSGStudies_v1"
# = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
#    InputCollection = cms.InputTag("hltPixelTracksToBeExtended"),
#    InputVertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
#    SeedCreatorPSet = cms.PSet(
#        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
#    ),
#    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
#    includeFourthHit = cms.bool(True),
#    originHalfLength = cms.double(0.3),
#    originRadius = cms.double(0.1),
#    produceComplement = cms.bool(False),
#    useEventsWithNoVertex = cms.bool(True),

#process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer("TrajectoryCleanerESProducer",
#    ComponentName = cms.string('hltESPTrajectoryCleanerBySharedHits'),
#    ComponentType = cms.string('TrajectoryCleanerBySharedHits'),
#    MissingHitPenalty = cms.double(0.0),
#    ValidHitBonus = cms.double(100.0),
#    allowSharedFirstHit = cms.bool(False),
#    fractionShared = cms.double(0.5)
#)

#process.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
#    ComponentType = cms.string('CkfBaseTrajectoryFilter'),
#    chargeSignificance = cms.double(-1.0),
#    constantValueForLostHitsFractionFilter = cms.double(1.0),
#    extraNumberOfHitsBeforeTheFirstLoop = cms.int32(4),
#    highEtaSwitch = cms.double(5.0),
#    maxCCCLostHits = cms.int32(0),
#    maxConsecLostHits = cms.int32(1),
#    maxLostHits = cms.int32(1),
#    maxLostHitsFraction = cms.double(999.0),
#    maxNumberOfHits = cms.int32(100),
#    minGoodStripCharge = cms.PSet(
#        refToPSet_ = cms.string('HLTSiStripClusterChargeCutNone')
#    ),
#    minHitsAtHighEta = cms.int32(5),
#    minHitsMinPt = cms.int32(3),
#    minNumberOfHitsForLoopers = cms.int32(13),
#    minNumberOfHitsPerLoop = cms.int32(4),
#    minPt = cms.double(0.3),
#    minimumNumberOfHits = cms.int32(3),
#    nSigmaMinPt = cms.double(5.0),
#    pixelSeedExtension = cms.bool(False),
#    seedExtension = cms.int32(0),
#    seedPairPenalty = cms.int32(0),
#    strictSeedExtension = cms.bool(False)
#)

#process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer("Chi2ChargeMeasurementEstimatorESProducer",
#    ComponentName = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
#    MaxChi2 = cms.double(9.0),
#    MaxDisplacement = cms.double(0.5),
#    MaxSagitta = cms.double(2.0),
#    MinPtForHitRecoveryInGluedDet = cms.double(1000000.0),
#    MinimalTolerance = cms.double(0.5),
#    appendToDataLabel = cms.string(''),
#    clusterChargeCut = cms.PSet(
#        refToPSet_ = cms.string('HLTSiStripClusterChargeCutLoose')
#    ),
#    nSigma = cms.double(3.0),
#    pTChargeCutThreshold = cms.double(15.0)
#)

#process.HLTIter0GroupedCkfTrajectoryBuilderIT = cms.PSet(
#    ComponentType = cms.string('GroupedCkfTrajectoryBuilder'),
#    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
#    alwaysUseInvalidHits = cms.bool(False),
#    bestHitOnly = cms.bool(True),
#    estimator = cms.string('hltESPChi2ChargeMeasurementEstimator9'),
#    foundHitBonus = cms.double(5.0),
#    inOutTrajectoryFilter = cms.PSet(
#        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
#    ),
#    intermediateCleaning = cms.bool(True),
#    keepOriginalIfRebuildFails = cms.bool(False),
#    lockHits = cms.bool(True),
#    lostHitPenalty = cms.double(30.0),
#    maxCand = cms.int32(2),
#    maxDPhiForLooperReconstruction = cms.double(2.0),
#    maxPtForLooperReconstruction = cms.double(0.0),
#    minNrOfHitsForRebuild = cms.int32(5),
#    propagatorAlong = cms.string('PropagatorWithMaterialParabolicMf'),
#    propagatorOpposite = cms.string('PropagatorWithMaterialParabolicMfOpposite'),
#    requireSeedHitsInRebuild = cms.bool(True),
#    seedAs5DHit = cms.bool(False),
#    trajectoryFilter = cms.PSet(
#        refToPSet_ = cms.string('HLTIter0PSetTrajectoryFilterIT')
#    ),
#    updator = cms.string('hltESPKFUpdator'),
#    useSameTrajFilter = cms.bool(True)
#)


#process.hltIter0PFLowPixelSeedsFromPixelTracksForScouting = cms.EDProducer("SeedGeneratorFromProtoTracksEDProducer",
#    InputCollection = cms.InputTag("hltPixelTracksToBeExtended"),
#    InputVertexCollection = cms.InputTag("hltTrimmedPixelVertices"),
#    SeedCreatorPSet = cms.PSet(
#        refToPSet_ = cms.string('HLTSeedFromProtoTracks')
#    ),
#    TTRHBuilder = cms.string('hltESPTTRHBuilderPixelOnly'),
#    includeFourthHit = cms.bool(True),
#    originHalfLength = cms.double(0.3),
#    originRadius = cms.double(0.1),
#    produceComplement = cms.bool(False),
#    useEventsWithNoVertex = cms.bool(True),
#    usePV = cms.bool(False),
#    useProtoTrackKinematics = cms.bool(False)
#)

#process.hltIter0PFlowCkfTrackCandidatesForScouting.doSeedingRegionRebuilding = True

#process.hltIter0PFlowCkfTrackCandidatesForScouting = cms.EDProducer( "CkfTrackCandidateMaker",
#    cleanTrajectoryAfterInOut = cms.bool( False ),
#    doSeedingRegionRebuilding = cms.bool( False ),
#    onlyPixelHitsForSeedCleaner = cms.bool( False ),
#    reverseTrajectories = cms.bool( False ),
#    useHitsSplitting = cms.bool( False ),
#    MeasurementTrackerEvent = cms.InputTag( "hltMeasurementTrackerEventForScouting" ),
#    src = cms.InputTag( "hltIter0PFLowPixelSeedsFromPixelTracksForScouting" ),
#    clustersToSkip = cms.InputTag( "" ),
#    phase2clustersToSkip = cms.InputTag( "" ),
#    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0GroupedCkfTrajectoryBuilderIT" ) ),
#    TransientInitialStateEstimatorParameters = cms.PSet( 
#      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
#      numberMeasurementsForFit = cms.int32( 4 ),
#      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
#    ),
#    numHitsForSeedCleaner = cms.int32( 4 ),
#    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
#    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
#    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
#    maxNSeeds = cms.uint32( 100000 ),
#    maxSeedsBeforeCleaning = cms.uint32( 1000 )
#)
process.ScoutingPFOutput = cms.FinalPath( process.hltOutputScoutingPF )
process.schedule.insert(-1, process.ScoutingPFOutput)

files = ["file:/data/user/sdonato/02fd495f-791e-4c6a-b979-f00043121216.root"]

process.source.fileNames = files
process.maxEvents.input = 500

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
