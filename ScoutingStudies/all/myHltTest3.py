import os

value = int(os.environ['VAL'])
print(value)

tag = "test3_fix_allFED_HP_test_4"

import FWCore.ParameterSet.Config as cms

# hltGetConfiguration /users/sdonato/2024Jan/ScoutingTracking/HLT --globaltag 124X_mcRun3_2022_realistic_v12 --mc --unprescale --output none --max-events 100 --input file:/eos/user/p/pellicci/MesonGamma_root/2023/Wpipipi_RAW/Wpluspipipi_RAW2023_27.root --eras Run3 --output none --paths DST_Run3_*,HLT_PFJet40_*  --l1-emulator uGT --l1 L1Menu_Collisions2023_v1_3_0_xml --dbproxy > hltMC.py

# /users/sdonato/2024Jan/ScoutingTracking/HLT/V5

# /dev/CMSSW_13_3_0/GRun/V14 (CMSSW_13_3_0)

from hltMC2 import process

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')
process.options.numberOfThreads = 64
process.options.numberOfStreams = 0
process.hltRawFewStripFED.fedsToExclude = []


process.hltPixelTracksToBeExtended.cut = "quality('highPurity') & pt >= %d"%value
process.hltPixelTracksToNotBeExtended.cut = "!(quality('highPurity') & pt >= %d)"%value
#process.hltPixelTracksToNotBeExtended.cut = "!(%s)"%process.hltPixelTracksToBeExtended.cut.value()

#process.hltIter0PFLowPixelSeedsFromPixelTracksForScouting.produceComplement = True
process.hltIter0PFLowPixelSeedsFromPixelTracksComplementForScouting = process.hltIter0PFLowPixelSeedsFromPixelTracksForScouting.clone(produceComplement = True)
process.HLTIterativeTrackingIteration0ForScouting.insert(4 , process.hltIter0PFLowPixelSeedsFromPixelTracksComplementForScouting)

process.hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking.L1SeedsLogicalExpression = "L1_ZeroBias"
process.hltL1sDSTRun3JetHTPFScoutingPixelTracking.L1SeedsLogicalExpression = "L1_AlwaysTrue"

process.hltOutputScoutingPF = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "outputScoutingPF_%s_pt%d.root"%(tag, value) ),
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
      'keep *_*genPart*_*_*',
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


#process.hltScoutingTracks = cms.EDProducer('TrackSimpleMerger',
#       src = cms.VInputTag(cms.InputTag('hltPixelTracksToNotBeExtended'), cms.InputTag('hltIter0PFlowTrackSelectionHighPurityForScouting'))
#)

#process.hltPixelTracksToBeExtended = cms.EDProducer( "TrackWithVertexSelector",
#    src = cms.InputTag( "hltPixelTracks" ),
#    etaMin = cms.double( 0.0 ),
#    etaMax = cms.double( 2.5 ),
#    ptMin = cms.double( value ),
#    ptMax = cms.double( 1E20 ),
#    d0Max = cms.double( 10.0 ),
#    dzMax = cms.double( 15.0 ),
#    normalizedChi2 = cms.double( 1E20 ),
#    numberOfValidHits = cms.uint32( 0 ),
#    numberOfLostHits = cms.uint32( 999 ),
#    numberOfValidPixelHits = cms.uint32( 0 ),
#    ptErrorCut = cms.double( 1E20 ),
#    quality = cms.string( "loose" ),
##    quality = cms.string( "highPurity" ),
#    useVtx = cms.bool( True ),
##    vertexTag = cms.InputTag( "hltPixelVertices" ),
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


#process.hltScoutingTracks = cms.EDProducer( "TrackListMerger",
#    ShareFrac = cms.double( 0.19 ),
#    FoundHitBonus = cms.double( 5.0 ),
#    LostHitPenalty = cms.double( 5.0 ),
#    MinPT = cms.double( 0.05 ),
#    Epsilon = cms.double( -0.001 ),
#    MaxNormalizedChisq = cms.double( 1000.0 ),
#    MinFound = cms.int32( 3 ),
#    TrackProducers = cms.VInputTag( 'hltPixelTracksToNotBeExtended','hltIter0PFlowTrackSelectionHighPurityForScouting' ),
#    hasSelector = cms.vint32( 0, 0 ),
#    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
#    selectedTrackQuals = cms.VInputTag( 'hltPixelTracksToNotBeExtended','hltIter0PFlowTrackSelectionHighPurityForScouting' ),
#    setsToMerge = cms.VPSet( 
#      cms.PSet(  tLists = cms.vint32( 0, 1 ),
#        pQual = cms.bool( False )
#      )
#    ),
#    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
#    allowFirstHitShare = cms.bool( False ),
#    newQuality = cms.string( "" ),
#    copyExtras = cms.untracked.bool( False ),
#    writeOnlyTrkQuals = cms.bool( False ),
#    copyMVA = cms.bool( False )
#)


#process.hltPixelTracksToBeExtended.quality = "loose"
#process.hltPixelTracksToBeExtended.useVtx = False
#process.hltPixelTracksToBeExtended.vertexTag = ["hltTrimmedPixelVertices"]

#hltPixelTracksAndExtended

#process.hltPixelTracksToBeExtended = cms.EDFilter('TrackSelector',
#    src = cms.InputTag('hltPixelTracks'),
#    cut = cms.string("quality('highPurity') & pt >= %d"%value)
#)

#process.hltPixelTracksToBeNotExtended = cms.EDFilter('TrackSelector',
#    src = cms.InputTag('hltPixelTracks'),
#    cut = cms.string("!(quality('highPurity') & pt >= %d)"%value)
#)

#process.HLTIterativeTrackingIteration0ForScouting.insert(2, process.hltPixelTracksToBeNotExtended)

#process.hltPixelTracksAndExtended.TrackProducers = [ 'hltPixelTracksToBeNotExtended', 'hltIter0PFlowTrackSelectionHighPurityForScouting' ]
#process.hltPixelTracksAndExtended.selectedTrackQuals = [ 'hltPixelTracksToBeNotExtended', 'hltIter0PFlowTrackSelectionHighPurityForScouting' ]


#process.hltPixelTracksToBeExtended = cms.EDProducer('DuplicateListMerger',
#0003 DuplicateListMerger = cms.EDProducer('DuplicateListMerger',
#0004   mergedSource = cms.InputTag(''),
#0005   originalSource = cms.InputTag(''),
#0006   mergedMVAVals = cms.InputTag(''),
#0007   originalMVAVals = cms.InputTag(''),
#0008   candidateSource = cms.InputTag(''),
#0009   candidateComponents = cms.InputTag(''),
#0010   trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
#0011   diffHitsCut = cms.int32(5),
#0012   copyExtras = cms.untracked.bool(True),
#0013   copyTrajectories = cms.untracked.bool(False),
#0014   mightGet = cms.optional.untracked.vstring
#0015 )

#process.hltPixelTracksAndExtended = cms.EDProducer('TrackSimpleMerger',
#       src = cms.VInputTag(cms.InputTag('hltPixelTracksToBeNotExtended'), cms.InputTag('hltIter0PFlowTrackSelectionHighPurityForScouting'))
#)

#process.hltPixelTracksToBeExtended = cms.EDProducer( "TrackWithVertexSelector",
#    src = cms.InputTag( "hltPixelTracks" ),
#    etaMin = cms.double( 0.0 ),
#    etaMax = cms.double( 2.5 ),
#    ptMin = cms.double( 7.0 ),
#    ptMax = cms.double( 1.0E20 ),
#    d0Max = cms.double( 10.0 ),
#    dzMax = cms.double( 15.0 ),
#    normalizedChi2 = cms.double( 1.0E20 ),
#    numberOfValidHits = cms.uint32( 0 ),
#    numberOfLostHits = cms.uint32( 999 ),
#    numberOfValidPixelHits = cms.uint32( 3 ),
#    ptErrorCut = cms.double( 1.0E20 ),
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

#process.hltPixelTracksAndExtended = cms.EDProducer( "TrackListMerger",
#    ShareFrac = cms.double( 0.19 ),
#    FoundHitBonus = cms.double( 5.0 ),
#    LostHitPenalty = cms.double( 20.0 ),
#    MinPT = cms.double( 0.05 ),
#    Epsilon = cms.double( -0.001 ),
#    MaxNormalizedChisq = cms.double( 1000.0 ),
#    MinFound = cms.int32( 3 ),
#    TrackProducers = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurityForScouting','hltPixelTracks' ),
#    hasSelector = cms.vint32( 0, 0 ),
#    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
#    selectedTrackQuals = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurityForScouting','hltPixelTracks' ),
#    setsToMerge = cms.VPSet( 
#      cms.PSet(  pQual = cms.bool( False ),
#        tLists = cms.vint32( 0, 1 )
#      )
#    ),
#    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
#    allowFirstHitShare = cms.bool( True ),
#    newQuality = cms.string( "confirmed" ),
#    copyExtras = cms.untracked.bool( True ),
#    writeOnlyTrkQuals = cms.bool( False ),
#    copyMVA = cms.bool( False )
#)

##process.hltIter0PFlowTrackSelectionHighPurityForScouting.copyTrajectories = False
#process.hltIter0PFlowTrackSelectionHighPurityForScouting.copyTrajectories = False

#process.hltPixelTracksAndExtended.TrackProducers = [ 'hltPixelTracks', 'hltIter0PFlowTrackSelectionHighPurityForScouting' ]
#process.hltPixelTracksAndExtended.selectedTrackQuals = [ 'hltPixelTracks', 'hltIter0PFlowTrackSelectionHighPurityForScouting' ]
#process.hltPixelTracksAndExtended.allowFirstHitShare = False
#process.hltPixelTracksAndExtended.copyExtras = False
#process.hltPixelTracksAndExtended.hasSelector = [1, 1]

#    hasSelector = cms.vint32( 0, 0 ),
#    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
#    selectedTrackQuals = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurityForScouting','hltPixelTracks' ),




#highPurityPtRange1to10 = trackSelector.clone(
#    cut = "quality('highPurity') & pt >= 1 & pt < 10 "
#)

#'TEC+' : [
#range(260, 356),
#],
#'TEC-' : [
#range(164, 260),
#],
#'TIBTID' : [
#range(50, 59),
#range(60, 103),
#range(104, 164),
#],
#'TOB' : [
#range(356, 388),
#range(389, 434),
#range(435, 490),
#],

#tec_p = list(range(260, 356))
#tec_m = list(range(164, 260))
#tibtid = list(range(50, 59)) + list(range(60, 103)) + list(range(104, 490))
#tob = list(range(356, 388)) + list(range(389, 434)) + list(range(435, 490))

#tec_p = tec_p[int(len(tec_p)/2):]
#tec_m = tec_m[int(len(tec_m)/2):]
#tibtid = tibtid[int(len(tibtid)/2):]
#tob = tob[int(len(tob)/2):]

#tec_p = []
#tec_m = []
#tibtid = []
#tob = []

#singleModules = [
##    "TIBminus_3", "TIBplus_3", "TIBminus_4", "TIBplus_4", 
##    "TIDminus_7", "TIDplus_7", "TIDminus_8", "TIDplus_8", 
##    "TOBminus_3", "TOBplus_3", "TOBminus_4", "TOBplus_4", "TOBminus_5", "TOBplus_5", "TOBminus_6", "TOBplus_6", 
##    "TOBminus_1", "TOBplus_1", "TOBminus_2", "TOBplus_2", "TOBminus_3", "TOBplus_3", "TOBminus_4", "TOBplus_4", "TOBminus_5", "TOBplus_5", 
#    #, "TOBminus_2", "TOBplus_2"
#    "TEC",
#    "TOB",
##    "TECminus_*_7", "TECminus_*_4", "TECminus_*_2", "TECminus_*_9", "TECminus_*_8", "TECminus_*_5", "TECminus_*_3", 
##    "TECplus_*_7",  "TECplus_*_4",  "TECplus_*_2",  "TECplus_*_9",  "TECplus_*_8",  "TECplus_*_5",  "TECplus_*_3", 
#    "TIB", 
#    "TID"
#]

#l = []
#for s in singleModules:
#    if "*" in s:
#        for i in range(0,9):
#            l.append(s.replace("*",str(i)))
#    else:
#        l.append(s)


##print(singleModules)
##1/0
##removed = tec_p + tec_m + tibtid + tob

#from TrackingScheme import trackingScheme

#removed = []
#notRemoved = []
#for FED in trackingScheme:
#    allMatches = True
#    for name in trackingScheme[FED]:
#        matches = [s for s in singleModules if s in name]
#        if len(matches) == 0:
#            allMatches = False
#        elif len(matches) == 1:
#            pass
#        else:
#            raise Exception("%d %s %s"%(FED, name, str(matches)))
#    if allMatches:
#         removed.append(FED)
#    else:
#         notRemoved.append(FED)

#print(removed)
#print(notRemoved)

#1/0

#process.rawNoSingleStrip = cms.EDProducer( "EvFFEDExcluder",
#    src = cms.InputTag( "rawDataCollector" ),
#    fedsToExclude = ( cms.vuint32( removed ))
#)

#process.HLTDoLocalStripSequence.insert( 0, process.rawNoSingleStrip )
#process.hltSiStripExcludedFEDListProducer.ProductLabel = "rawNoSingleStrip"
#process.hltSiStripRawToClustersFacility.ProductLabel = "rawNoSingleStrip"

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


#process.hltPixelTracksToBeExtended = cms.EDProducer( "TrackWithVertexSelector",
#    src = cms.InputTag( "hltPixelTracks" ),
#    etaMin = cms.double( 0.0 ),
#    etaMax = cms.double( 2.5 ),
#    ptMin = cms.double( value ),
#    ptMax = cms.double( 1E20 ),
#    d0Max = cms.double( 10.0 ),
#    dzMax = cms.double( 15.0 ),
#    normalizedChi2 = cms.double( 1E20 ),
#    numberOfValidHits = cms.uint32( 0 ),
#    numberOfLostHits = cms.uint32( 999 ),
#    numberOfValidPixelHits = cms.uint32( 0 ),
#    ptErrorCut = cms.double( 1E20 ),
#    quality = cms.string( "loose" ),
##    quality = cms.string( "highPurity" ),
#    useVtx = cms.bool( True ),
##    vertexTag = cms.InputTag( "hltPixelVertices" ),
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
    files.append('file:/eos/user/p/pellicci/MesonGamma_root/2023/Wpipipi_RAW/Wpluspipipi_RAW2023_%d.root'%i)
_customInfo['inputFile' ]=  files
_customInfo['realData'  ]=  False

from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
process = customizeHLTforAll(process,"GRun",_customInfo)


#process.MessageLogger.cerr.FwkReport.limit = 1000000000000000
