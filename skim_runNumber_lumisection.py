import FWCore.ParameterSet.Config as cms
from FWCore.PythonUtilities.LumiList import LumiList

process = cms.Process("SKIM")

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            'file:///gpfs/ddn/srm/cms/store/user/snandan/HIPhysicsRawSecond/HIPhysicsRawSecond_Lumibased/251218_170354/0001/step3_RAW2DIGI_L1Reco_RECO_1529.root',
            'file:///gpfs/ddn/srm/cms/store/user/snandan/HIPhysicsRawSecond/HIPhysicsRawSecond_Lumibased/251218_170354/0001/step3_RAW2DIGI_L1Reco_RECO_1530.root'),
    lumisToProcess = cms.untracked.VLuminosityBlockRange(
        '399468:1-399468:1',
        '399469:1-399469:1',
        #'297050:1-297050:10',   # Run 297050, Lumi 1 through 10
        #'297050:15-297050:15',  # Run 297050, Lumi 15 only
        #'297100:1-297100:MAX'   # Run 297100, all lumis from 1 to the end
    )
)

# 3. Define the output (copies everything in selected events)
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("rawSecondSkim.root")
)

process.endpath = cms.EndPath(process.out)
