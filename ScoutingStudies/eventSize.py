import os

value = str(os.environ['VAL'])
print(value)

tag = "longRun_EvSize"

import FWCore.ParameterSet.Config as cms

import importlib
hltMenu = importlib.import_module(value)
process = hltMenu.process

#process.hltL1sDSTRun3JetHTPFScoutingPixelTracking.L1SeedsLogicalExpression = "L1_AlwaysTrue"

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
process.options.numberOfThreads = 64
process.options.numberOfStreams = 0

process.hltOutputScoutingPF = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "outputEventSize_%s_%s.root"%(tag, value) ),
    compressionAlgorithm = cms.untracked.string( "ZSTD" ),
    compressionLevel = cms.untracked.int32( 3 ),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string( "" ),
        dataTier = cms.untracked.string( "RAW" )
    ),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'Dataset_ScoutingPFRun3' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltFEDSelectorL1_*_*',
      'keep *_hltScoutingEgammaPacker_*_*',
      'keep *_hltScoutingMuonPacker_*_*',
      'keep *_hltScoutingPFPacker_*_*',
      'keep *_hltScoutingPrimaryVertexPacker_*_*',
      'keep *_hltScoutingTrackPacker_*_*',
      'keep edmTriggerResults_*_*_*' ),
)

process.GlobalTag.globaltag = "133X_dataRun3_HLT_for2024TSGStudies_v1"

#process.hltIter0PFlowCkfTrackCandidatesForScouting.cleanTrajectoryAfterInOut = True
#process.hltIter0PFlowCkfTrackCandidatesForScouting.doSeedingRegionRebuilding = True
#process.hltIter0PFlowCkfTrackCandidatesForScouting.numHitsForSeedCleaner = 0
#process.hltIter0PFlowCkfTrackCandidatesForScouting.reverseTrajectories = True
##process.hltIter0PFlowCkfTrackCandidatesForScouting.MeasurementTrackerEvent = "hltMeasurementTrackerEventForScouting"

#process.hltIter0PFLowPixelSeedsFromPixelTracksForScouting.includeFourthHit = False
#process.hltIter0PFLowPixelSeedsFromPixelTracksForScouting.useEventsWithNoVertex = False

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

files = [
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/000a69cc-f5bb-4897-bdd5-c9926a9f3e63.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/00cf24a3-c5b1-4036-aef2-107e147676eb.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/0242fd14-4555-411f-bd9f-c4e22f067c8f.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/02fd495f-791e-4c6a-b979-f00043121216.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/042e7110-9d6a-4b72-9b9d-fd2d9adea2bf.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/05db43c3-e248-4be5-86c1-e4c972c4758b.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/07150f8b-8e84-44fd-9de9-87b660b22919.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/0baeeb65-bd22-4081-a5bd-2b24afaa2de8.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/0d3cc8ad-c6e8-46d0-aaa0-93c0df476465.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/1965e67a-fede-47bf-bb54-352b7a2f62ca.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/1fe8192a-ff79-4379-8950-2c7219fb528f.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/1ff4d6b3-b9ae-481f-a269-7b83b733e496.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/22e79626-1743-4b52-adbb-e6f28814b604.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/2cb64357-6aec-46e8-b640-70473cee0dae.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/2cf4ce37-7d1a-419a-b08a-31fd488e6197.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/2fc877b8-42fd-4c05-a50a-ab7207964944.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/321cbc63-c6d5-4306-a88e-bcbb6b2d81fe.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/356ee3eb-f469-440e-98a2-361008164282.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/35f25d33-0b01-4052-84fb-7778c0df842c.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/36f6d2ab-f465-421b-90d9-76638d54ea95.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/377d0da2-fb0d-47f4-8d18-30a67bb6ad00.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/38129db2-8b62-4dcd-8917-ff6029a5c1e4.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/3ab0e06c-dad4-4f21-a02d-4484371d90eb.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/3bd2d447-3bbb-4ba7-b582-9597872c12db.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/445659ff-71e4-46b0-a45d-902a6a0fca01.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/46969f9d-f04d-4a05-a1cf-2410c3dbd728.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/4813c808-f312-46bb-868b-4af7245cdb69.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/4c45f9c5-61bc-44da-95ca-19ae68c0d731.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/4c6e2cd0-ba0c-4570-9b9d-a720cf55bdaa.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/5020d444-110a-4b8d-94c8-72b59238aae1.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/55a66c95-c6d9-46b5-ad2f-cec889ba3a5c.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/56738b4c-eddd-4b64-846f-afedd70fbeca.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/568bd7fd-1bf3-4180-888d-40d28e6ac4e5.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/585e7b34-fbe8-4b8e-9924-92e80ae51540.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/5ac794b5-75b4-407b-99de-f275a663b990.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/5c1a1acb-bbd9-4cdc-ada5-05ec5ba9b372.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/5fa52b15-2327-40e9-9bde-52b1167d09b3.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/6a70f680-7363-42b0-9474-92f7f63860fc.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/6a7ffb77-584b-4ced-9741-402a4205feff.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/6b52aff7-6e05-4bd6-8403-99cf32d382b8.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/6feefffe-df50-4427-96d4-b55d4f818131.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/701dafd6-3408-4b55-9e01-4a29694e6c73.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/7146eb1a-0de5-4f7d-828d-b7216d4553d1.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/77f6a4b6-e114-4d7c-adcf-7f2ab74b58fb.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/7c183e6a-38a3-4f22-872d-29c290037ade.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/834196fd-0adc-46f4-8e7d-9fb0a9dbf747.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/84a5cef0-10ad-4dd2-b42d-d239811b5689.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/887e968f-0e31-412a-9901-c703c0b81660.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/90d4cecf-fd29-470b-a4e0-d8734f63015a.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/916fa891-f1c8-43a5-ac4e-12461db717a0.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/92bf5eda-781b-4d47-804a-b77ba3b314d3.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/94f0114d-57d8-4756-b5ce-5ea04bafa5bc.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/9aaf73b1-a15a-4d34-8c05-bbf348544569.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/a034bcfc-c9a8-45d8-a634-6a58ca10d08c.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/a2bed350-be38-4052-be31-e74535339067.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/a3114c14-d8f1-45b7-9160-9ad4cea749f7.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/a4bf5a33-04dd-4ede-9a5d-af47f4d0bda1.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/a592e36c-1e2a-4271-9161-d406a5b6644e.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/a685cc5e-6cb6-4268-84d5-78721fdfb2d7.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/a6da9c2d-6eac-4131-9d1b-562dbe5bf88b.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/a8ed93b8-91cb-4abd-a86c-31f3a70609c7.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/a91f14fc-78f4-4ab8-acf5-84e700cb7fd6.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/aa286f89-b76c-412d-9e51-72aedbb6e09d.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/aadc68cd-9250-4932-955e-d4d9465ed0a0.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/ae92316f-6a81-4477-acd7-a7013b1117ac.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/b0a598b2-f3c1-44cf-9bd3-ffe8860676e0.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/b14bab8d-5a3d-4405-9aab-46fa7488bc85.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/b1a3b540-8e6f-4f23-8157-1a1c1808e56c.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/b2b6b6bb-59d2-4ce9-a090-3d3796ec286c.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/b4f8a941-57cb-41c3-acff-16bb62bfc3c1.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/b92d7137-5b01-4f7b-9078-76f60fd74bc5.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/bb89a806-54d1-470b-b48b-78d036a864bb.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/bcc933c4-600c-4e68-86f3-6348e2392f02.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/c1a12a92-f2f8-40e4-a5ce-f65513d2ab35.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/c2c3bfc6-d218-468c-9297-15d53ffcedaa.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/c577b5c0-517b-42ad-885c-6289e35bc278.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/c8804323-3277-4884-8530-96d4aafaba97.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/cad917f3-4cf0-4fae-87c6-80af1c421a2f.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/cd808e7d-f77d-457c-b913-8c9830c03817.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/d3d3779f-230b-4e00-8808-c856c08fe9c9.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/d5e2e45a-22d1-472b-8874-22b030b7048d.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/dcf4f9b0-8027-4f24-9c00-49335fbb7082.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/dd7c7c1e-5176-4d74-8dcf-0e5e2af7a108.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/e2d29528-afc9-455d-89c9-2f8ca4a7e55a.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/e5f19681-46b8-4a96-87d2-84a44f5871c7.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/e619bb5f-66c8-49e7-aacf-ae5e13d9e94a.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/eb552acf-d638-4054-8134-762f2b3cd4c5.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/f5c5e4e2-59b7-41f5-8d17-8165bc58c1c9.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/f64a937e-02f6-4073-a654-a7b2c3e1eb9f.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/fa968c19-b140-424a-b460-7e641b98be79.root',
'root://eoscms.cern.ch//store/data/Run2023D/EphemeralHLTPhysics4/RAW/v1/000/370/293/00000/fd654190-48c8-4435-b03a-bb43f5226d09.root'
#"file:/data/user/sdonato/02fd495f-791e-4c6a-b979-f00043121216.root"
]

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


for path in process.paths:
#    if "HLT_" in path or ("Dataset_" in path and not "Scouting" in path):
    if "HLT_" in path:
        p = process.paths[path]
        if p in process.schedule:
            process.schedule.remove(p)

