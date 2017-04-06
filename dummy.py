# /users/sdonato/Hbb2017/HLT/V24 (CMSSW_9_0_0)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "TEST" )


from HLTrigger.Configuration.CustomConfigs import L1REPACK
process = L1REPACK(process,"FullSimHcalTP")


process.SimL1Emulator = cms.Sequence(process.unpackEcal+process.unpackCSC+process.unpackDT+process.unpackRPC+process.unpackEmtf+process.unpackCsctf+process.unpackBmtf+process.simHcalTriggerPrimitiveDigis+process.
simCaloStage2Layer1Digis+process.simCaloStage2Digis+process.simDtTriggerPrimitiveDigis+process.simCscTriggerPrimitiveDigis+process.simTwinMuxDigis+process.simBmtfDigis+process.simEmtfDigis+process.simOmtfDigis+process.simGmtCaloSumDigis+process.simGmtStage2Digis+process.simGtExtFakeStage2Digis+process.simGtStage2Digis+process.
packCaloStage2+process.packGmtStage2+process.packGtStage2+process.rawDataCollector)
