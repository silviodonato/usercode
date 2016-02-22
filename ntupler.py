# /users/sdonato/TriggerVBF2/V27 (CMSSW_7_1_6_HLT1)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLTX" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/sdonato/TriggerVBF2/V27')
)


process.TFileService = cms.Service("TFileService", fileName = cms.string("ntupla_V5.root") )
process.n=cms.EDProducer("NtuplerVBF3")

process.ntupler = cms.Path(  process.n)


process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
		'file:/gpfs/ddn/srm/cms/store/user/sdonato/VBF_HToBB_M-125_13TeV-powheg-pythia6/VBFHLT_V3_PU40_Sept14_L1HadronicSkim_CRAB3/141006_180440/0000/keepinfos_1.root',
		'file:/gpfs/ddn/srm/cms/store/user/sdonato/VBF_HToBB_M-125_13TeV-powheg-pythia6/VBFHLT_V3_PU40_Sept14_L1HadronicSkim_CRAB3/141006_180440/0000/keepinfos_2.root',
		'file:/gpfs/ddn/srm/cms/store/user/sdonato/VBF_HToBB_M-125_13TeV-powheg-pythia6/VBFHLT_V3_PU40_Sept14_L1HadronicSkim_CRAB3/141006_180440/0000/keepinfos_3.root',
    ),
    secondaryFileNames = cms.untracked.vstring(
    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    ),
    skipEvents =  cms.untracked.uint32(58),
)

