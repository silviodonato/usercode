import FWCore.ParameterSet.Config as cms

process = cms.Process("TRIGREP")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)
)

process.options = cms.untracked.PSet(
 wantSummary = cms.untracked.bool( True ),
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       '/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/b5dd76fd-07de-4a93-a786-6bf83677a8cf.root'
    ),
)

process.hltTrigReport = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','HLT' )
)

process.hltTrigReportRECO = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','RECO' )
)

process.TrigR = cms.Path(process.hltTrigReport) # + process.hltTrigReportRECO)


process.MessageLogger.cerr.HLTrigReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
)
