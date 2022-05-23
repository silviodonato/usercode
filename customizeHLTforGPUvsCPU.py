'''
Run DQM CPU vs GPU in HLT 
Works with CMSSW_12_4_0_pre4 + #37979

wget https://raw.githubusercontent.com/silviodonato/usercode/customizeHLTforGPUvsCPU/customizeHLTforGPUvsCPU.py

cmsDriver.py step2 --process reHLT -s L1REPACK:uGT,HLT:@relval2021 --conditions auto:run3_hlt_relval --data --eventcontent FEVTDEBUGHLT --nThreads 8 --datatier FEVTDEBUGHLT --era Run3 -n -1 --filein /store/data/Commissioning2021/MinimumBias/RAW/v1/000/346/512/00000/be4e0e99-6d25-4b6f-8648-1adefb79c7bf.root --fileout file:step2.root

add
"
from customizeHLTforGPUvsCPU import customizeHLTforGPUvsCPU
customizeHLTforGPUvsCPU(process)
"

might be useful
"
process.options.wantSummary = True
process.maxEvents.input = 10000
"

to convert the DQMIO in the ROOT plots:

cmsDriver.py harvesting -s HARVESTING:@hlt --conditions auto:run3_hlt_relval --data --filein file:DQMIO.root --filetype DQM --scenario pp
'''

import FWCore.ParameterSet.Config as cms
from HeterogeneousCore.CUDACore.SwitchProducerCUDA import SwitchProducerCUDA

def resetFEVTDEBUGHLToutput(process):
    process.FEVTDEBUGHLToutput = process.FEVTDEBUGHLToutput.clone(
        SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'Dataset_DQMGPUvsCPU' , ) ),
        outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltEcalDigisFromGPU_*_*',
      'keep *_hltEcalDigisLegacy_*_*',
      'keep *_hltEcalRecHitWithTPs_*_*',
      'keep *_hltEcalRecHitWithoutTPs_*_*',
      'keep *_hltEcalUncalibRecHitFromSoA_*_*',
      'keep *_hltEcalUncalibRecHitLegacy_*_*',
      'keep *_hltHbherecoFromGPU_*_*',
      'keep *_hltHbherecoLegacy_*_*',
      'keep *_hltPixelTracksCPU_*_*',
      'keep *_hltPixelTracksFromGPU_*_*',
      'keep *_hltPixelVerticesCPU_*_*',
      'keep *_hltPixelVerticesFromGPU_*_*',
      'keep *_hltSiPixelClustersFromSoA_*_*',
      'keep *_hltSiPixelClustersLegacy_*_*',
      'keep *_hltSiPixelDigisFromSoA_*_*',
      'keep *_hltSiPixelDigisLegacy_*_*',
      'keep *_hltSiPixelRecHitsFromGPU_*_*',
      'keep *_hltSiPixelRecHitsFromLegacy_*_*',

            'keep edmTriggerResults_*_*_*',
            'keep triggerTriggerEvent_*_*_*',
            'keep GlobalAlgBlkBXVector_*_*_*',                  
            'keep GlobalExtBlkBXVector_*_*_*',
            'keep l1tEGammaBXVector_*_EGamma_*',
            'keep l1tEtSumBXVector_*_EtSum_*',
            'keep l1tJetBXVector_*_Jet_*',
            'keep l1tMuonBXVector_*_Muon_*',
            'keep l1tTauBXVector_*_Tau_*',
     )
    )

def addLegacyGPUtracks(process):
    process.hltCPUPixelTracks = cms.EDProducer( "PixelTrackProducerFromSoA",
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        trackSrc = cms.InputTag( "hltPixelTracksSoA@cpu" ),
        pixelRecHitLegacySrc = cms.InputTag( "hltSiPixelRecHits@cpu" ),
        minNumberOfHits = cms.int32( 0 ),
        minQuality = cms.string( "loose" )
    )
    process.hltCPUPixelVertices = cms.EDProducer( "PixelVertexProducerFromSoA",
        TrackCollection = cms.InputTag( "hltCPUPixelTracks" ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        src = cms.InputTag( "hltPixelVerticesSoA" )
    )
    process.hltGPUPixelTracks = cms.EDProducer( "PixelTrackProducerFromSoA",
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        trackSrc = cms.InputTag( "hltPixelTracksSoA@cuda" ),
        pixelRecHitLegacySrc = cms.InputTag( "hltSiPixelRecHits@cuda" ),
        minNumberOfHits = cms.int32( 0 ),
        minQuality = cms.string( "loose" )
    )
    process.hltGPUPixelVertices = cms.EDProducer( "PixelVertexProducerFromSoA",
        TrackCollection = cms.InputTag( "hltGPUPixelTracks" ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        src = cms.InputTag( "hltPixelVerticesSoA" )
    )
    process.DQM_PixelReconstruction_v1.insert(-2, process.hltCPUPixelTracks)
    process.DQM_PixelReconstruction_v1.insert(-2, process.hltGPUPixelTracks)
    process.DQM_PixelReconstruction_v1.insert(-2, process.hltCPUPixelVertices)
    process.DQM_PixelReconstruction_v1.insert(-2, process.hltGPUPixelVertices)
    if hasattr(process,"FEVTDEBUGHLToutput"):
        process.FEVTDEBUGHLToutput.outputCommands.append("keep *_hltCPUPixelTracks_*_*")
        process.FEVTDEBUGHLToutput.outputCommands.append("keep *_hltGPUPixelTracks_*_*")
        process.FEVTDEBUGHLToutput.outputCommands.append("keep *_hltCPUPixelVertices_*_*")
        process.FEVTDEBUGHLToutput.outputCommands.append("keep *_hltGPUPixelVertices_*_*")

def addSoArechits(process): #does not work!
    process.hltSiPixelRecHitsSoAFromGPU = cms.EDProducer( "SiPixelRecHitSoAFromCUDA",
    pixelRecHitSrc = cms.InputTag( "hltSiPixelRecHitsGPU" )
)
    
    process.hltSiPixelRecHitsSoA = SwitchProducerCUDA(
    cpu = cms.EDAlias(
        hltSiPixelRecHitsFromLegacy = cms.VPSet( 
            cms.PSet(  type = cms.string( "cmscudacompatCPUTraitsTrackingRecHit2DHeterogeneous" )         ),
            cms.PSet(  type = cms.string( "uintAsHostProduct" )         )
        )
    ),
    cuda = cms.EDAlias(
        hltSiPixelRecHitsSoAFromGPU = cms.VPSet( 
            cms.PSet(  type = cms.string( "*" )         )
        )
    )
)
    
    process.HLTDoLocalPixelTask = cms.Task( process.hltOnlineBeamSpotToGPU , process.hltSiPixelDigiErrorsSoA , process.hltSiPixelDigisLegacy , process.hltSiPixelDigisSoA , process.hltSiPixelDigisFromSoA , process.hltSiPixelDigis , process.hltSiPixelClustersLegacy , process.hltSiPixelClustersGPU , process.hltSiPixelClustersFromSoA , process.hltSiPixelClusters , process.hltSiPixelClustersCache , process.hltSiPixelRecHitsFromLegacy , process.hltSiPixelRecHitsGPU , process.hltSiPixelRecHitsFromGPU , process.hltSiPixelRecHits , process.hltSiPixelRecHitsSoAFromGPU , process.hltSiPixelRecHitsSoA )
    if hasattr(process,"FEVTDEBUGHLToutput"):
        process.hltPixelConsumerCPU.eventProducts.append("hltSiPixelRecHitsSoA@cpu")
        process.hltPixelConsumerGPU.eventProducts.append("hltSiPixelRecHitsSoA@cuda")
        process.FEVTDEBUGHLToutput.outputCommands.append("keep *_hltSiPixelRecHitsSoAFromGPU_*_*")
        process.FEVTDEBUGHLToutput.outputCommands.append("keep *_hltCPUPixelTracks_*_*")
        process.FEVTDEBUGHLToutput.outputCommands.append("keep *_hltGPUPixelTracks_*_*")
        process.FEVTDEBUGHLToutput.outputCommands.append("keep *_hltCPUPixelVertices_*_*")
        process.FEVTDEBUGHLToutput.outputCommands.append("keep *_hltGPUPixelVertices_*_*")

def updateGPUpixelrecoDQM(process):
    process.hltSiPixelRecHitsSoAMonitorGPUvsCPU = cms.EDProducer('SiPixelPhase1CompareRecHitsSoA', #require #37969 and addSoArechits
      pixelHitsSrcCPU = cms.InputTag('hltSiPixelRecHitsSoA@cpu'),
      pixelHitsSrcGPU = cms.InputTag('hltSiPixelRecHitsSoA@cuda'),
      topFolderName = cms.string('SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU'),
      minD2cut = cms.double(0.0001)
    )
    process.hltPixelTracksSoAMonitorCPU = cms.EDProducer('SiPixelPhase1MonitorTrackSoA',
      pixelTrackSrc = cms.InputTag('hltPixelTracksSoA@cpu'),
      topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackCPU'),
      useQualityCut = cms.bool(True),
      minQuality = cms.string('loose')
    )
    process.hltPixelTracksSoAMonitorGPU = cms.EDProducer('SiPixelPhase1MonitorTrackSoA',
      pixelTrackSrc = cms.InputTag('hltPixelTracksSoA@cuda'),
      topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackGPU'),
      useQualityCut = cms.bool(True),
      minQuality = cms.string('loose')
    )
    process.hltPixelTracksSoAMonitorGPUvsCPU = cms.EDProducer('SiPixelPhase1CompareTrackSoA',
      pixelTrackSrcCPU = cms.InputTag('hltPixelTracksSoA@cpu'),
      pixelTrackSrcGPU = cms.InputTag('hltPixelTracksSoA@cuda'),
      topFolderName = cms.string('SiPixelHeterogeneous/PixelTrackGPUvsCPU'),
      useQualityCut = cms.bool(True),
      minQuality = cms.string('loose'),
      deltaR2cut = cms.double(0.04)
    )
    process.hltPixelVertexMonitorCPU = cms.EDProducer('SiPixelPhase1MonitorVertexSoA',
      beamSpotSrc = cms.InputTag('hltOnlineBeamSpot'),
      pixelVertexSrc = cms.InputTag('hltPixelVerticesSoA@cpu'),
      topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexCPU'),
    )
    process.hltPixelVertexMonitorGPU = cms.EDProducer('SiPixelPhase1MonitorVertexSoA',
      beamSpotSrc = cms.InputTag('hltOnlineBeamSpot'),
      pixelVertexSrc = cms.InputTag('hltPixelVerticesSoA@cuda'),
      topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexGPU'),
    )
    process.hltPixelVertexMonitorGPUvsCPU = cms.EDProducer('SiPixelPhase1CompareVertexSoA',
      beamSpotSrc = cms.InputTag('hltOnlineBeamSpot'),
      pixelVertexSrcCPU = cms.InputTag('hltPixelVerticesSoA@cpu'),
      pixelVertexSrcGPU = cms.InputTag('hltPixelVerticesSoA@cuda'),
      topFolderName = cms.string('SiPixelHeterogeneous/PixelVertexGPUvsCPU'),
      dzCut = cms.double(1)
    )
    process.DQM_PixelReconstruction_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDQMPixelReconstruction + process.hltPreDQMPixelReconstruction + process.statusOnGPU + process.statusOnGPUFilter + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequence + process.hltPixelConsumerCPU + process.hltPixelConsumerGPU + process.hltSiPixelRecHitsSoAMonitorGPUvsCPU + process.hltPixelTracksSoAMonitorCPU + process.hltPixelTracksSoAMonitorGPU + process.hltPixelTracksSoAMonitorGPUvsCPU + process.hltPixelVertexMonitorCPU + process.hltPixelVertexMonitorGPU + process.hltPixelVertexMonitorGPUvsCPU + process.HLTEndSequence )

def addGPUecalDQM(process):
    ###### ECAL #####################
    from DQM.EcalMonitorTasks.EcalMonitorTask_cfi import ecalMonitorTask
    from DQM.EcalMonitorTasks.ecalGpuTask_cfi import ecalGpuTask

    # renaming and enable only GPU-CPU comparison plot
    process.hltGPUecalMonitorTask = ecalMonitorTask.clone(
        moduleName = "HLT Ecal Monitor Source GPU vs CPU",
        workers = ["GpuTask"],
        workerParameters = cms.untracked.PSet(
            GpuTask = ecalGpuTask.clone(
                params = dict(
                    dict(
                        gpuOnlyPlots = False,
                        runGpuTask = True
                    )
                ), 
            ),
        ),
    )
    
    # replace offline inputtag with the online input tag
    for par in process.hltGPUecalMonitorTask.collectionTags.parameterNames_():
        par = getattr(process.hltGPUecalMonitorTask.collectionTags,par)
        
        par.setValue(par.value().replace("ecalMultiFitUncalibRecHit@cpu","hltEcalUncalibRecHitLegacy"))
        par.setValue(par.value().replace("ecalMultiFitUncalibRecHit@cuda","hltEcalUncalibRecHitFromSoA"))
        par.setValue(par.value().replace("ecalMultiFitUncalibRecHit","hltEcalUncalibRecHitFromSoA"))
        
        par.setValue(par.value().replace("ecalDigis@cpu","hltEcalDigisLegacy"))
        par.setValue(par.value().replace("ecalDigis@cuda","hltEcalDigisFromGPU"))
        par.setValue(par.value().replace("ecalDigis","hltEcalDigisLegacy"))
        
        par.setValue(par.value().replace("ecalRecHit@cpu","hltEcalRecHitWithTPs"))
        par.setValue(par.value().replace("ecalRecHit@cuda","hltEcalRecHitWithoutTPs"))
        par.setValue(par.value().replace("ecalRecHit","hltEcalRecHitWithoutTPs"))

    process.DQM_EcalReconstruction_v1.insert(-2, process.hltGPUecalMonitorTask)

def addGPUhcalDQM(process):
    ###### HCAL #####################
    from DQM.HcalTasks.hcalGPUComparisonTask_cfi import hcalGPUComparisonTask
    # replace offline inputtag with the online input tag
    process.hltGPUhcalMonitorTask = hcalGPUComparisonTask.clone(
        name = ('hltHcalGPUComparisonTask'),
        tagHBHE_ref = ("hltHbherecoLegacy"),
        tagHBHE_target = ("hltHbherecoFromGPU"),
    )
    process.DQM_HcalReconstruction_v1.insert(-2, process.hltGPUhcalMonitorTask)

def enableDQM(process): ##for the harvesting: cmsDriver.py harvesting -s HARVESTING:@hlt --conditions auto:run3_hlt_relval --data --filein file:DQMIO.root --filetype DQM --scenario pp
    # load the DQMStore and DQMRootOutputModule
    process.load( "DQMServices.Core.DQMStore_cfi" )
    process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
        fileName = cms.untracked.string("DQMIO.root")
    )
    process.DQMOutput = cms.FinalPath( process.dqmOutput )
    process.schedule.insert(-1, process.DQMOutput)


def customizeHLTforGPUvsCPU(process):
    resetFEVTDEBUGHLToutput(process)
    enableDQM(process)
    addGPUhcalDQM(process)
    addGPUecalDQM(process)
    addSoArechits(process)
    updateGPUpixelrecoDQM(process)
    addLegacyGPUtracks(process)
    
