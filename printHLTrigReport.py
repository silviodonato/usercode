import FWCore.ParameterSet.Config as cms

process = cms.Process("TRIGREP")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
 wantSummary = cms.untracked.bool( True ),
)

# source module (EDM inputs)
process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
#        'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/01dd8ead-99ed-4bbe-aad7-34ece94fbcd3.root',

#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/01dd8ead-99ed-4bbe-aad7-34ece94fbcd3.root',
#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/22337640-b5d8-4d34-a3ce-5b5d467239cb.root',
#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/2d20baca-53b4-49e2-bede-dd0d15befa23.root',
#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/7581574b-764c-4850-b296-7842d9774369.root',
#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/7d0067db-a1aa-4ff0-a715-2535c4bf6ad0.root',
#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/8f856c45-c60b-4dff-8145-0d5694c72e84.root',

#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v1/2580000/28a5878b-b13d-42fa-aa31-2e5f07e8140a.root',
#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v1/2580000/5e27ecf6-6e48-4977-929d-b633e7df4a25.root',
#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v1/2580000/5e3a1980-4d6c-4c41-b29d-f39690a11c58.root',
#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v1/2580000/7572d26b-0b2e-4a85-8344-9d49e2fca08d.root',
#    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3/RelValH125GGgluonfusion_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v1/2580000/fee8de7f-ab53-4442-a85f-88714a744d4c.root',
    
#    'root://eoscms.cern.ch//store//relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValH125GGgluonfusion_14/GEN-SIM-RECO/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v3/2580000/44e09e7d-0d25-4ff4-a258-568f17dfa976.root',


    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/5848cd07-d48c-466a-8646-e77806a4bda9.root',
    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/5b16742e-5785-4f69-801d-9f8ca2745504.root',
    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/8532bc4a-b0eb-4e96-8b91-9035f6ead51e.root',
    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/c7a528e8-38f5-4777-adc8-cc00d87fd08d.root',
    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/cff4071f-c321-47fd-ad6a-2fdb0608e224.root',
    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/e1380d58-f0d0-486a-9453-d88b47de6084.root',
    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/e6c520b0-2a56-4f5b-9b9a-d59b00250387.root',
    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/edce0d75-e5cc-433e-958c-afb8f566899d.root',
    'root://eoscms.cern.ch//store/relval/CMSSW_14_0_0_pre3_MULTIARCHS/RelValQCD_Pt15To7000_Flat_14/GEN-SIM-DIGI-RAW/140X_mcRun3_2024_realistic_v1_STD_2024_noPU-v2/2580000/ff576025-79ef-49aa-b0ed-ff0474897859.root',

    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
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

process.hltTrigReportSIM = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','SIM' )
)

process.TrigR = cms.Path(process.hltTrigReport) # + process.hltTrigReportRECO)
#process.TrigR = cms.Path(process.hltTrigReport + process.hltTrigReportRECO + process.hltTrigReportSIM)


process.MessageLogger.cerr.HLTrigReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'auto:phase1_2024_realistic')



### Re-run all alca reco streams
#from Configuration.StandardSequences.AlCaRecoStreams_cff import *
#process.load("Configuration.StandardSequences.AlCaRecoStreams_cff")

#process.TrigR = cms.EndPath(process.hltTrigReport + process.hltTrigReportRECO  + process.hltTrigReportTEST)
