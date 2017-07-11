import FWCore.ParameterSet.Config as cms

process = cms.Process("TRIGREP")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(30)
)

process.options = cms.untracked.PSet(
 wantSummary = cms.untracked.bool( True ),
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       'file:trigRes_1.root'
    ),
)

process.hltTrigReport = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','MYHLT' )
)

process.TrigR = cms.Path(process.hltTrigReport)
process.MessageLogger.categories.append("HLTrigReport")
