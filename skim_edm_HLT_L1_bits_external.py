import FWCore.ParameterSet.Config as cms

process = cms.Process("SKIM")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '126X_dataRun3_HLT_v1')

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
process.hltFilter = hlt.hltHighLevel.clone(
    TriggerResultsTag = cms.InputTag('TriggerResults', '', 'MYHLT'),
    HLTPaths = ['Dataset_HLTMonitor']
)

folder = "/eos/cms/store/group/dpg_trigger/comm_trigger/TriggerStudiesGroup/STEAM/savarghe/PU70/"
import os
files = []
for f in os.listdir("/eos/cms/store/group/dpg_trigger/comm_trigger/TriggerStudiesGroup/STEAM/savarghe/PU70/"):
    files.append("file:"+folder+f)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       'file:/eos/cms/store/group/dpg_trigger/comm_trigger/TriggerStudiesGroup/Tracking/DataValidation_HighPU/reHLT_GRunV188_part2/reHLT_GRunV188_112.root'
    ),
    secondaryFileNames = cms.untracked.vstring(
       files
    ),


)

process.load('L1Trigger.Skimmer.l1Filter_cfi')
process.l1Filter.algorithms = cms.vstring('L1_HTT125')

process.SkimFilter = cms.Path(
    process.hltFilter
#   +process.l1Filter
)

process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("aaa.root"),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring('SkimFilter')
   )
)
