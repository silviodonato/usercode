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
        FEVTDEBUGHLToutput.outputCommands.append("hltCPUPixelTracks")
        FEVTDEBUGHLToutput.outputCommands.append("hltGPUPixelTracks")
        FEVTDEBUGHLToutput.outputCommands.append("hltCPUPixelVertices")
        FEVTDEBUGHLToutput.outputCommands.append("hltGPUPixelVertices")

def addLegacySoArechits(process): ##does not work!
    process.hltSiPixelRecHitSoAFromGPU = cms.EDProducer( "SiPixelRecHitSoAFromCUDA",
        pixelRecHitSrc = cms.InputTag( "hltSiPixelRecHitsFromGPU" )
    )
    process.DQM_PixelReconstruction_v1.insert(-2, process.hltSiPixelRecHitSoAFromGPU)
    if hasattr(process,"FEVTDEBUGHLToutput"):
        FEVTDEBUGHLToutput.outputCommands.append("hltCPUPixelTracks")
        FEVTDEBUGHLToutput.outputCommands.append("hltGPUPixelTracks")
        FEVTDEBUGHLToutput.outputCommands.append("hltCPUPixelVertices")
        FEVTDEBUGHLToutput.outputCommands.append("hltGPUPixelVertices")

def addGPUrechitsDQM(process): ##require 37969 and addLegacySoArechits
    from DQM.SiPixelPhase1Heterogeneous.siPixelPhase1CompareRecHitsSoA_cfi import *
    process.hltGPUsiPixelPhase1CompareRecHitsSoA = siPixelPhase1CompareRecHitsSoA.clone(
        pixelHitsSrcCPU = ("hltSiPixelRecHitsLegacy"), #ie. hltSiPixelRecHits@cpu
        pixelHitsSrcGPU = ("hltSiPixelRecHitSoAFromGPU"), #ie. hltSiPixelRecHits@cuda
        topFolderName = 'SiPixelHeterogeneous/HLTPixelRecHitsCompareGPUvsCPU'
    )
    process.DQM_PixelReconstruction_v1.insert(-2, process.hltGPUsiPixelPhase1CompareRecHitsSoA)

def addGPUtrackDQM(process):
    from DQM.SiPixelPhase1Heterogeneous.siPixelPhase1CompareTrackSoA_cfi import *
    process.hltGPUsiPixelPhase1CompareTrackSoA = siPixelPhase1CompareTrackSoA.clone(
        pixelTrackSrcCPU = ("hltPixelTracksCPU"), #ie. hltPixelTracksSoA@cpu
        pixelTrackSrcGPU = ("hltPixelTracksFromGPU"), #ie. hltPixelTracksSoA@cuda
        topFolderName = 'SiPixelHeterogeneous/HLTPixelTrackCompareGPUvsCPU',
    )
    from DQM.SiPixelPhase1Heterogeneous.siPixelPhase1CompareVertexSoA_cfi import *
    process.hltGPUsiPixelPhase1CompareVertexSoA = siPixelPhase1CompareVertexSoA.clone(
        pixelVertexSrcCPU = ("hltPixelVerticesCPU"), #ie. hltPixelVerticesSoA@cpu
        pixelVertexSrcGPU = ("hltPixelVerticesFromGPU"), #ie. hltPixelVerticesSoA@cuda
        topFolderName = 'SiPixelHeterogeneous/HLTPixelTrackCompareGPUvsCPU',
    )
    process.DQM_PixelReconstruction_v1.insert(-2, process.hltGPUsiPixelPhase1CompareTrackSoA)
    process.DQM_PixelReconstruction_v1.insert(-2, process.hltGPUsiPixelPhase1CompareVertexSoA)

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


process.FEVTDEBUGHLToutput = process.FEVTDEBUGHLToutput.clone(
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'Dataset_DQMGPUvsCPU' , ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
  'keep *_hltCPUPixelTracks_*_*',
  'keep *_hltGPUPixelTracks_*_*',
  'keep *_hltCPUPixelVertices_*_*',
  'keep *_hltGPUPixelVertices_*_*',
  'keep *_hltEcalDigisFromGPU_*_*',
  'keep *_hltEcalDigisLegacy_*_*',
  'keep *_hltEcalRecHitWithTPs_*_*',
  'keep *_hltEcalRecHitWithoutTPs_*_*',
  'keep *_hltEcalUncalibRecHitFromSoA_*_*',
  'keep *_hltEcalUncalibRecHitLegacy_*_*',
  'keep *_hltHbherecoFromGPU_*_*',
  'keep *_hltHbherecoLegacy_*_*',
#  'keep *_hltPixelTracks@cuda_*_*',
#  'keep *_hltPixelTracks@cpu_*_*',
  'keep *_hltPixelTracksCPU_*_*',
  'keep *_hltPixelTracksGPU_*_*',
#  'keep *_hltPixelTracksSoA_*_*',
  'keep *_hltPixelTracksTrackingRegions_*_*',
  'keep *_hltPixelTracksFromGPU_*_*',
#  'keep *_hltPixelVertices@cuda_*',
#  'keep *_hltPixelVertices@cpu_*',
  'keep *_hltPixelVerticesCPU_*_*',
  'keep *_hltPixelVerticesGPU_*_*',
  'keep *_hltTrimmedPixelVertices_*_*',
#  'keep *_hltPixelVerticesSoA_*_*',
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


process.options.wantSummary = True
process.maxEvents.input = 10000

