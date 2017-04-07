import FWCore.ParameterSet.Config as cms

process = cms.Process("FAKE")

#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('root://dc2-grid-64.brunel.ac.uk//dpm/brunel.ac.uk/home/cms/store/mc/PhaseIFall16DR/GluGluToRSGravitonToHHTo4B_M-900_narrow_13TeV-madgraph/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/80000/9812F6D5-C511-E711-9D5D-001E67E6F7C4.root'),
#    secondaryFileNames = cms.untracked.vstring('root://dc2-grid-64.brunel.ac.uk//dpm/brunel.ac.uk/home/cms/store/mc/PhaseIFall16DR/GluGluToRSGravitonToHHTo4B_M-900_narrow_13TeV-madgraph/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/80000/A8F990B6-B810-E711-B530-001E677926A8.root')
#)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:///mnt/t3nfs01/data01/shome/sdonato/tth/Trigger2017/HLT/CMSSW_9_0_0/src/ntuples/crab/ZH2_AODSIM.root'),
    secondaryFileNames = cms.untracked.vstring('file:////mnt/t3nfs01/data01/shome/sdonato/tth/Trigger2017/HLT/CMSSW_9_0_0/src/ntuples/crab/ZH2_RAW.root')
)


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/PhaseIFall16DR/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG087_90X_upgrade2017_realistic_v6_C1-v1/120000/009CCEA5-7815-E711-BA6C-0CC47A7C346E.root.root'),
    secondaryFileNames = cms.untracked.vstring('/store/mc/PhaseIFall16DR/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG087_90X_upgrade2017_realistic_v6_C1-v1/120001/ACC1E2DB-6615-E711-9AD6-0025905A60AA.root')
)



process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.options = cms.PSet(
    numberOfThreads = cms.untracked.uint32(4)
)

process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('tree.root')
)


process.out = cms.EndPath(process.output)

