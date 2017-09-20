from hlt import *

from HLTrigger.Configuration.customizeHLTforCMSSW import *

seedChanges = {
    'L1_DoubleJet40er3p0':'L1_DoubleJet40er2',
    'L1_DoubleJet50er3p0':'L1_DoubleJet50er2',
    'L1_DoubleJet60er3p0':'L1_DoubleJet60er2',
    'L1_DoubleJet80er3p0':'L1_DoubleJet80er2',
    'L1_DoubleJet100er3p0':'L1_DoubleJet100er2',
    'L1_DoubleJet112er3p0':'L1_DoubleJet112er2',
    'L1_DoubleJet120er3p0':'L1_DoubleJet120er2',
    'L1_DoubleJet150er3p0':'L1_DoubleJet150er2',
    'L1_QuadJet40er3p0':'L1_QuadJet40er2',
    'L1_QuadJet50er3p0':'L1_QuadJet50er2',
    'L1_QuadJet60er3p0':'L1_QuadJet60er2',
    'L1_SingleJet20er3p0_NotBptxOR':'L1_SingleJet20er2p7_NotBptxOR',
    'L1_SingleJet20er3p0_NotBptxOR_3BX':'L1_SingleJet20er2p7_NotBptxOR_3BX',
    'L1_SingleJet43er3p0_NotBptxOR_3BX':'L1_SingleJet43er2p7_NotBptxOR_3BX',
    'L1_SingleJet46er3p0_NotBptxOR_3BX':'L1_SingleJet46er2p7_NotBptxOR_3BX',
    'L1_LooseIsoEG24er2p1_Jet26er3p0_dR_Min0p3':'L1_LooseIsoEG24er2p1_Jet26er2p7_dR_Min0p3',
    'L1_LooseIsoEG26er2p1_Jet34er3p0_dR_Min0p3':'L1_LooseIsoEG26er2p1_Jet34er2p7_dR_Min0p3',
    'L1_LooseIsoEG28er2p1_Jet34er3p0_dR_Min0p3':'L1_LooseIsoEG28er2p1_Jet34er2p7_dR_Min0p3',
    'L1_LooseIsoEG30er2p1_Jet34er3p0_dR_Min0p3':'L1_LooseIsoEG30er2p1_Jet34er2p7_dR_Min0p3',
    'L1_LooseIsoEG24er2p1_TripleJet_26er3p0_26_26er3p0':'L1_LooseIsoEG24er2p1_TripleJet_26er2p7_26_26er2',
    'L1_Mu18_Jet24er3p0':'L1_Mu18_Jet24er2',
    'L1_QuadJet36er3p0_Tau52':'L1_QuadJet36er2p7_Tau52',
    'L1_QuadJet36er3p0_IsoTau52er2p1':'L1_QuadJet36er2p7_IsoTau52er2p1',
    'L1_DoubleJet60er3p0_ETM60':'L1_DoubleJet60er2p7_ETM60',
    'L1_DoubleJet60er3p0_ETM70':'L1_DoubleJet60er2p7_ETM70',
    'L1_DoubleJet60er3p0_ETM80':'L1_DoubleJet60er2p7_ETM80',
    'L1_DoubleJet60er3p0_ETM90':'L1_DoubleJet60er2p7_ETM90',
    'L1_DoubleJet60er3p0_ETM100':'L1_DoubleJet60er2p7_ETM100',
    'L1_Mu3_JetC16_dEta_Max0p4_dPhi_Max0p4':'L1_Mu3_Jet16er2p7_dEta_Max0p4_dPhi_Max0p4',
    'L1_Mu3_JetC60_dEta_Max0p4_dPhi_Max0p4':'L1_Mu3_Jet60er2p7_dEta_Max0p4_dPhi_Max0p4',
    'L1_Mu3_JetC120_dEta_Max0p4_dPhi_Max0p4':'L1_Mu3_Jet120er2p7_dEta_Max0p4_dPhi_Max0p4'
}

output = '''
# update of L1 seed to V4

import FWCore.ParameterSet.Config as cms

process = cms.Process( "MYHLT" )

'''

fakeSequence = "process.HLT_FakePath_v1 = cms.Path(" 
for filter_ in filters_by_type(process, "HLTL1TSeed"):
    fakeSequence += ("process."+str(filter_) + " + ")
    L1seeds = str(filter_.L1SeedsLogicalExpression.value())
    for (oldSeed,newSeed) in seedChanges.items():
        L1seeds = L1seeds.replace(oldSeed,newSeed)
        
    filter_.L1SeedsLogicalExpression = L1seeds
    output += ("process.%s = "%filter_ + filter_.dumpPython())

fakeSequence =  fakeSequence[:-2] + ")\n"

newFile = file('newL1seeds.py','w')
newFile.write(output)
newFile.write(fakeSequence)
newFile.close()
