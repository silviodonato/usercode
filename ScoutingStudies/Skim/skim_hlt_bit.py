import FWCore.ParameterSet.Config as cms

## python3 -u submitAllFiles.py >& log &

## take input file from argv[1]
import sys
if len(sys.argv) < 2:
    print("Usage: cmsRun skim_hlt_bit.py <input_file> (eg. file:/eos/cms/tier0/store/data/Run2024F/ScoutingPFRun3/HLTSCOUT/v1/000/382/504/00000/00b54a76-8ee0-4f82-a9a1-6f5450e47854.root)")
    sys.exit(1)

fileName = sys.argv[1]

process = cms.Process("SKIM")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)
process.MessageLogger.cerr.FwkReport.reportEvery = 100000
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '140X_dataRun3_HLT_v3')

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
process.hltFilter = hlt.hltHighLevel.clone(
    TriggerResultsTag = cms.InputTag('TriggerResults', '', "HLT"),
    HLTPaths = ['DST_PFScouting_ZeroBias_v2']
)

# import os
# folder = "/eos/cms/tier0/store/data/Run2024F/ScoutingPFRun3/HLTSCOUT/v1/000/382/504/00000"
# fileNames = [f"file:{folder}/{line.strip()}" for line in os.listdir(folder)]
runNumber = int(fileName.split("/")[-4]+fileName.split("/")[-3])
fName = fileName.split("/")[-1].replace(".root", "")
print("Run number: ", runNumber)
outputFile = "Skim_%d_%s.root"%(runNumber, fName)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        [fileName]
        # fileNames
    #    'file:c3e48beb-47ad-4f49-83e3-7be470fbd967.root'
    ),


)

process.SkimFilter = cms.Path(
    process.hltFilter
)

process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(outputFile),
    SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring('SkimFilter')
   )
)
process.ep = cms.FinalPath(process.output)

## enable multithreading
process.options.numberOfThreads = 1
process.options.numberOfStreams = 1

