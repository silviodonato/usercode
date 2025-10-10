import FWCore.ParameterSet.Config as cms

from rawSecond import process
#process.hltSiStripClusters2ApproxClusters.version = cms.uint32( 1 )
#process.hltSiStripClusters2ApproxClustersV2.version = cms.uint32( 2 )
process.hltOutputPhysicsHIPhysicsRawSecond.outputCommands.append("keep SiStripClusteredmNewDetSetVector_*_*_*")
process.hltOutputPhysicsHIPhysicsRawSecond.outputCommands.append("keep *_hltSiStripClusters2ApproxClusters_*_*")

del process.DQMOutput
del process.PhysicsHIPhysicsRawPrimeOutput

process.hltSiStripClustersFromRawPrimev1.v1 = True
process.maxEvents.input = 1


process.hltOutputPhysicsHIPhysicsRawPrime.compressionAlgorithm = "LZMA"
process.hltOutputPhysicsHIPhysicsRawPrime.compressionLevel = 4

process.hltOutputPhysicsHIPhysicsRawSecond.compressionAlgorithm = "LZMA"
process.hltOutputPhysicsHIPhysicsRawSecond.compressionLevel = 4
