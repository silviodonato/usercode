import FWCore.ParameterSet.Config as cms

process = cms.Process("TRIGREP")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
 wantSummary = cms.untracked.bool( True ),
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/134f5c18-980c-4b44-a749-f5ea08849ef1.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/1a04735a-3a86-4883-86ad-9cb3b96cc5d8.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/1f7634fc-a6dc-47df-872b-629b11eb7ca2.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/23b38662-23bb-4854-9731-a406d2b1a320.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/36164cb9-edf7-4bc3-b12c-e0d8b9ff8bcb.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/3e1570f4-522a-4a41-b688-2b251e95ff83.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/4f105c8b-4981-428b-9392-07d078190649.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/519ffbd9-2146-4aab-a88a-b4b01869fea7.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/5ce18f3d-abcd-48f6-877c-7588038f4a83.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/5d26dcd4-a73c-4d9f-89d8-83814ab4b7c1.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/6cfefc79-57f2-4248-936b-6b4107928bd0.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/7104a53a-b658-491c-9af5-b4e808bbf6c6.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/7824dcac-000a-46c5-9b2c-15fd66a5fce9.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/7bd92870-19c4-4910-938f-0b70b534cce7.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/7d972eac-2beb-4ea8-aeeb-695710ce5ce4.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/7db7e6f3-327f-44ea-bd2f-5c474da88e8c.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/8457bf33-7c4f-490e-8cdc-483dc2250577.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/93cb5438-6f2d-40f1-be6c-a52f31730ac8.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/96673a58-42be-4a04-9ebb-4c9d1e596ccf.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/96b2054e-3c3b-4f67-a28e-355062764c05.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/a44862d7-858b-406e-8b0c-89a0980995aa.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/b3d24976-3b1b-4533-b320-8f2e2bc28370.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/b55841f1-85e3-4550-9baa-d1f37b9815d5.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/b5dd76fd-07de-4a93-a786-6bf83677a8cf.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/bad13d1d-60b8-458d-897a-4f4cc75b890a.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/c015855e-c63b-4d2d-82cd-43fc0b1ea623.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/cc225e76-c602-478b-872c-7b2479ecfbf0.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/cc9c284f-9c9d-46f9-ab2b-6732a61584cf.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/d40042f2-409a-48c2-b4e7-fc51e492d356.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/dc7a24e2-12a1-48fd-b334-87cc5380820f.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/edf426c8-2a1e-4ec2-9924-9b5c13ff39e6.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/f16328a6-37e7-4322-be3a-a29caa6ad2ee.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/f19fb212-4869-49e3-b9cc-42f3d3bc7b50.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/f6d98b00-d838-4d0f-85f1-2b4d1c2bc98e.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/f6fa579e-e649-4f98-8d9f-8c8747856329.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/f73e32fc-f7b4-4be6-bd21-780c8f6cf7be.root",
"/store/express/Run2022A/ExpressPhysics/FEVT/Express-v1/000/352/572/00000/f760d2a1-09bb-4c01-820f-bbcc4566dda1.root"


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

#process.TrigR = cms.Path(process.hltTrigReport) # + process.hltTrigReportRECO)
process.TrigR = cms.Path(process.hltTrigReport + process.hltTrigReportRECO)


process.MessageLogger.cerr.HLTrigReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
