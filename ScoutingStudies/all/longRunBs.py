import os

value = str(os.environ['VAL'])
print(value)

tag = "longRun"

import FWCore.ParameterSet.Config as cms

import importlib
hltMenu = importlib.import_module(value)
process = hltMenu.process


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
process.options.numberOfThreads = 8
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
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/011ab3ae-e01d-4b2a-b0c1-de2e21538da2.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/02e30f66-9240-4573-8443-c19f3f490fb9.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/08ec7ca9-efbb-4a7a-a2a8-937f102276ad.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/091eaf87-f924-42fd-b429-40e1249f4dc6.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/0b0bb1f8-def3-4961-9187-4f7b9cfaba5a.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/0f283dd4-8259-4f47-92e7-85f557e9931e.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/19e91bc1-8b80-4cdb-bafc-f534f3898dbf.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/21a72136-634d-4377-9077-5d708302fc46.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/222a2de7-1104-4663-a515-35e692649dfc.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/24a7c3f0-d623-4059-9753-48bbe1ea73db.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/26ef9f1d-76fd-46ba-bebd-4f37532c2df4.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/2978894d-ce3a-4eb1-8596-6f97013d2d6d.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/2b7f92af-5ac5-49a7-b5c5-3fa2845fc928.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/327ae074-35fb-4993-a16d-03e690ea7520.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/339232a2-435a-4941-9ad3-a36ffaaa2273.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/34259972-4a8e-4e30-bc86-7ef7de084206.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/3dc8f6e3-d22b-484c-bce1-50b540e319eb.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/3e726905-93c6-44c9-b78e-e2324cee278f.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/3f6cb8fb-c85e-4f90-a428-22e2bd3b8e2b.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/4a487298-674e-47df-be70-d4195b609b8d.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/579ffc5f-a94c-42d6-bcc3-807d025a7a47.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/5b32f56a-aa74-4c23-8918-14e8f156323d.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/665e2d9e-a07b-41bf-b108-59afef13078f.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/69c523e9-aac6-44f0-bb88-f86c7c243ee0.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/74452310-4368-49cc-932c-4b6d245729a3.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/794569db-e035-4d40-a5bc-1ac80f9eb8f9.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/7e8f8e5a-1afb-47cf-994f-41daf26e6c50.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/8646f245-996b-4f70-a760-22f705fb3fe8.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/8a59afe1-e86d-4197-afeb-03c9c67b53e8.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/8bcf99b5-af1b-4384-8270-155ff73261cf.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/8bd724ef-6b70-48da-9a4f-336d6b2df9ca.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/8c80d1ad-7a86-4aba-bdfb-25515940fac6.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/8f19051e-874c-4cd7-8112-cde46a46aa7a.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/a1277f20-93d7-41e4-9c82-30c8a6237840.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/a58a8ec9-3af4-4fe7-80d2-806aad5ded62.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/a938a33a-c9ba-485f-b042-b5e7666d7b2d.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/b36536ef-a939-41a8-84b4-242a4fe15a47.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/b69603e4-281b-4abd-943f-7a9095b272ed.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/ba8ede53-b03e-40ad-8b8a-c82d4bd2ac89.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/badd4491-a7db-4138-892d-7339794184c2.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/be907155-bf55-44c1-afc1-9bf825ae0600.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/c367527b-cd57-4132-a450-8ea80e4ec561.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/c856fbb3-7b8e-4b85-b1f1-d21fcc890992.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/cea947df-2e65-42b1-af06-07964400bfee.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/df7ab2c6-5b41-4e06-9a18-10803579150f.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/e4cef512-791a-404e-bbe5-67708d60e05c.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/e666bc52-acce-4f9e-a4da-be7f6869c636.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/e71e0336-7780-4164-8768-b567f081a13c.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/ea705fa7-af0d-4e8c-bb3f-fe27db25b9d1.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/ef08386c-0517-453e-87ad-3819ba39f38b.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/f1e0a63a-6993-417d-b380-34fd4d678cc0.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/f35cd879-8b2a-49ba-a4ad-d37d780c3529.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/f3b2c8e5-3b84-40bf-be2f-3ad5163f51e0.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/f4de42fa-0eee-461b-862a-dfc97e3946d3.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/f9ce638f-7707-41ad-bbe5-534149123705.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/fa533162-af7c-430e-9736-b39ffe41804d.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/fce01230-12a7-4953-a7d0-5f822ce80c7b.root",
	"root://eoscms.cern.ch//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/fd7ef798-b80f-47d1-8f9f-00f19e884e2a.root"
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
