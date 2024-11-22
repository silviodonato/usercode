'''
The outut of this script is the number of events passing a given trigger and a given filter.
It works with RAW or AOD data (no MINIAOD, NANOAOD).

Example:

Total number of events: 1955
Number of events passing hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking::HLT: 218
Number of events passing DST_PFScouting_DoubleMuon_v2: 64
Fraction of events passing hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking::HLT: 0.111509
Fraction of events passing DST_PFScouting_DoubleMuon_v2: 0.032737
Fraction of events passing DST_PFScouting_DoubleMuon_v2 after hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking::HLT: 0.293578
'''

import sys
from ROOT import *
from DataFormats.FWLite import Handle, Events

verbose = False
filesInput = [
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/2204f9f0-a26c-4447-89ab-67e45b3b61d4.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/273075a0-4385-49a4-995a-e8a5ad29c6bd.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/2e74fb08-d81f-4437-b6ad-10385b6afa22.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/5b789540-446d-441e-a7d5-56849df207b6.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/5bf46ba1-fd17-4ca2-8302-43017ed6393e.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/715a4d1b-88b2-41e3-997f-8f128e62ee2c.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/8819ff25-a50a-4a20-bc69-a364e12bfa64.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/94861a3c-6878-4995-9330-b3b6c827dca6.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/a42529d8-33ea-41a8-a450-de86ec251f61.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/af5f2671-5690-4ca6-b8a0-7c24367e6cc9.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/be75eb1b-c584-4b6c-8a34-ea41d9ac73f7.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics0/RAW/v1/000/386/813/00000/d73fd60b-3369-41b0-bc6e-c2ba9d993d83.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/09bfbc05-a8b4-456b-90c7-b4b3b6c07584.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/0f249f6e-ad84-4314-9f2b-28663dcc1e2f.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/27c87e1f-c954-4d98-a3c5-4948562702cc.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/2ea46d6b-18e4-4764-af8e-d6ce99c0a1fc.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/477489bc-09fc-4a9c-9d43-dff8bf2e3fd8.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/83e6dcfa-5d4f-4106-afb3-bba2cd05b9cc.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/bebac150-a377-4193-81e0-23f9200a819d.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/c0bab0e2-9bbf-4db9-a4b2-4990e91c9de2.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/c6d31431-5999-4dde-b2b9-26f18bea3cf4.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/d04e1350-3b72-4a30-89b7-f7aa3caead14.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/d3b167dd-886b-4c5c-bd40-6633e51db61b.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics1/RAW/v1/000/386/813/00000/dc851b89-49f1-47c5-8801-6ee72562038d.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/08290f39-6df7-48b6-89d6-9f3f710a2703.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/15e81e2c-955d-45a9-b661-41b5d2830ddb.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/28e119f0-643a-4415-a75e-dd78ec6c3a60.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/56563384-53b0-499d-89eb-7221f78c3498.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/62de94fd-b7f6-4d4a-aa4f-b30b961edbe0.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/64187417-b13b-4918-a8fd-f29230509815.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/69b23acb-bc6e-4309-b9c2-23071dd6a38f.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/6a1ad3c2-e4a7-4b2f-be9f-7833a73857cb.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/6cc8da84-8ffe-490f-bfbb-f9678eac6e2a.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/bfe9cc6b-0a31-4b1d-b130-8514d19f2af1.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/d37c8f7d-c00b-4651-bcc6-f8ac72c6573d.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics2/RAW/v1/000/386/813/00000/d3c5f21a-2422-4b4e-8b3f-4df942886334.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/1890e8d7-aafd-4d16-bb55-aa9e5aa2df0c.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/4d040138-190c-4f8c-87f3-316ce49702ff.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/5fecd56b-3a5a-4358-9248-fc52712a2169.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/63612dad-bd7d-4c15-862d-0ca0663f5f14.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/71f7ce10-c9c7-4a49-b574-0d5bcba93cdd.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/ad9d664d-fd0a-494f-87cc-28727b3051f4.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/c06f4fd4-0a42-422b-91d2-2a2b479d02c3.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/c2dded85-7ef4-40d6-9507-5423eb2b44d1.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/c4447260-7d7a-47aa-b32b-51d9d3a5ac47.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/c5d63340-0b38-4f44-90a8-ea8ea6a9ad97.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/f82c7cf8-f98c-43ca-b986-c766b0f68ca5.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics3/RAW/v1/000/386/813/00000/f8b34081-1b12-42be-a335-990931d63f5d.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/0478acd7-0d32-4cab-944c-97ef55c36ce8.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/2724dad9-ddcc-4461-ab8c-9b1da6a7f05c.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/47bd8441-ced0-4df2-80a6-2e9913d089b3.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/4e50f551-77bc-4658-9c7e-946b077bbf59.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/5e4cd809-cccc-4a5d-9cf3-bbb1e8b46c05.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/60f44423-bc48-4e81-ae4f-5094c42c8865.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/84854dae-5589-4c76-b8fa-a5eec4611fe8.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/85050fa4-e572-4353-a24c-938dfadbec86.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/892988cc-0030-45e9-990a-a6ef7222edb4.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/b3b2533e-b514-46f9-9c8a-ffbf1b42bfaa.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/b65e1d71-ccb4-4e3a-b5bd-6e2ad5a328a8.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics4/RAW/v1/000/386/813/00000/daa76cd2-ca16-4ad2-886a-1faa95d75331.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/086bef1c-f351-43e7-b391-72a0326fe712.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/0ab53ff5-68b4-4578-8d05-a69c5d536f90.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/18c070e2-ad7f-4610-8b42-b33ef2df0720.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/198f2be3-e17e-45ca-9ecf-d4f97f725664.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/412d656a-7183-4999-9390-1009a5bbc2cf.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/48c0a7aa-7422-4da3-8633-5807f379f9ff.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/7ba6f3a8-42ca-4701-9dd9-7187ca895ea7.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/a1bc7ad9-7c76-405b-904a-1021d9f19b71.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/cccbbe9c-cb71-4ea9-a510-23835acc025d.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/f004cacd-4e73-420b-93a9-c522823b167d.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/f2c6a2c9-3830-4402-afe1-ef77e4181b26.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics5/RAW/v1/000/386/813/00000/ff1509f7-2b0c-4628-8f9b-b39f4cc27f13.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/0284f51a-f50d-4b5b-b461-b43aab4d0426.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/1e46fc7e-990a-4562-b99a-b7119497a64d.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/21246339-7af1-4fd6-b3ca-27423f9c0465.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/47fc6621-b16a-4cb4-b469-fd8515cda5ff.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/77808812-6ae9-46a7-a031-84318b1c8eaa.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/85eaf31a-99bd-429d-bd0f-1ee834c36286.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/adb0fc95-7c20-482b-9c8e-e5377c2097ca.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/b684d0a2-c1eb-46e5-a0b3-4b84bfb59e50.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/b6d3cf8e-ca73-4392-b596-dd702d875b80.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/e3733e45-8a0d-47a0-8034-603fd7a19bbc.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/f74339c0-4bcc-4b52-bae1-075babed01d9.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics6/RAW/v1/000/386/813/00000/fe89b140-1658-4486-9395-0443a5ba938f.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/269de488-e379-46aa-8a73-f9742cf5b2bd.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/34eb1a6c-4fc2-49a5-9549-7730a19ee5e1.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/38d760b9-f1d1-4895-85eb-810b7504be2c.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/6901eab6-2dda-4bf5-989c-5ad732247bd0.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/72f9a0c9-e229-4010-aeac-241b513686b0.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/977913ca-8909-484a-8674-7731cae4529f.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/a4cf73e8-45d8-40b9-bc06-1d8ca2115bea.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/a548c2b1-d0de-4549-af79-d880fba4b3c9.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/afcf7281-d717-4a84-9671-5c9fd4016b46.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/c9e81ae2-4e96-4e07-a055-79c744b93ecc.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/e523447f-6fcf-43fc-b50b-8a51053a2b43.root",
	"/eos/cms/store/data/Run2024I/EphemeralHLTPhysics7/RAW/v1/000/386/813/00000/e89eddff-cb65-4450-8346-04d0691f0b22.root",
    ]

evMax = -1
evMax = 100000
evReportEvery = 1000

filterNames = {
    "DST_PFScouting_DoubleMuon_v5": ["hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking"],
    "DST_PFScouting_DoubleEG_v5":  ["hltL1sDSTRun3DoubleEGPFScoutingPixelTracking"],
    "DST_PFScouting_JetHT_v5":  ["hltL1sDSTRun3JetHTPFScoutingPixelTracking"],
    # "DST_PFScouting_DatasetMuon_v5": ["hltMuonTriggerResultsFilter"],
    "DST_PFScouting_AXOVLoose_v3":  ["hltL1sDSTRun3AXOVLoosePFScoutingTracking"],
    "DST_PFScouting_AXOLoose_v3":  ["hltL1sDSTRun3AXOLoosePFScoutingTracking"],
    "DST_PFScouting_AXONominal_v5":  ["hltL1sDSTRun3AXONominalPFScoutingTracking"],
    "DST_PFScouting_AXOTight_v5":  ["hltL1sDSTRun3AXOTightPFScoutingTracking"],
    "DST_PFScouting_AXOVTight_v3":  ["hltL1sDSTRun3AXOVTightPFScoutingTracking"],
    "DST_PFScouting_CICADAVLoose_v1":  ["hltL1sDSTRun3CICADAVLoosePFScoutingTracking"],
    "DST_PFScouting_CICADALoose_v1":  ["hltL1sDSTRun3CICADALoosePFScoutingTracking"],
    "DST_PFScouting_CICADAMedium_v1":  ["hltL1sDSTRun3CICADAMediumPFScoutingTracking"],
    "DST_PFScouting_CICADATight_v1":  ["hltL1sDSTRun3CICADATightPFScoutingTracking"],
    "DST_PFScouting_CICADAVTight_v1":  ["hltL1sDSTRun3CICADAVTightPFScoutingTracking"],
    "DST_PFScouting_SingleMuon_v5":  ["hltL1sSingleMuScouting"],
    "DST_PFScouting_SinglePhotonEB_v2":  ["hltL1sSingleEGor"],
    "DST_PFScouting_ZeroBias_v3":  ["hltL1sZeroBias"],
}

triggerNames = filterNames.keys()

## Add process name to filters
processName = "HLT"
for triggerName in filterNames:
    for i in range(len(filterNames[triggerName])):
        filterNames[triggerName][i] = filterNames[triggerName][i] + "::" + processName

triggerBitLabel = ("TriggerResults","","HLT")
triggerEventLabel = ("hltTriggerSummaryAOD","","HLT")
triggerBitsH = Handle("edm::TriggerResults")
triggerEventH = Handle("trigger::TriggerEvent")



def getFiterSize(triggerEvent,filterName):
    filterIndex = triggerEvent.filterIndex(filterName)
    if filterIndex<triggerEvent.sizeFilters():
        filterKeys = triggerEvent.filterKeys(filterIndex)
        return len(filterKeys)
    else:
        for i in range(triggerEvent.sizeFilters()):
            print(triggerEvent.filterTag(i).encode())
        raise Exception("Filter %s not found in event."%filterName) 

def getTriggerBitResult(triggerBits,triggerName, names):
    pathIndex = names.triggerIndex(triggerName)
    if pathIndex>=triggerBits.size():
        for i in range(triggerBits.size()):
            print(names.triggerName(i))
        raise Exception("Path %s not found in event."%triggerName)
    return triggerBits.accept(pathIndex)

events = Events (filesInput)
#Check only first event interactively
#for iev,event in enumerate(events): break

#Run a loop over all events
count_total = 0
counts_passing_L1filters = {}
counts_passing_HLTpaths = {}
for triggerName in triggerNames:
    counts_passing_HLTpaths[triggerName] = 0
    for filterName in filterNames[triggerName]:
        counts_passing_L1filters[filterName] = 0
# count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking = 0
# count_passing_DST_PFScouting_DoubleMuon_v5 = 0
names = None

for iev,event in enumerate(events):
    if iev>evMax and evMax>0: break
    if iev%evReportEvery==0: print("Processing event %d"%iev)
    count_total += 1
    event.getByLabel(triggerBitLabel, triggerBitsH)
    event.getByLabel(triggerEventLabel, triggerEventH)
    triggerBits = triggerBitsH.product()
    triggerEvent = triggerEventH.product()
    if not names: names = event.object().triggerNames(triggerBits)
    # if getFiterSize(triggerEvent,HLTFilter)>0:
    #     count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking += 1
    #     print("Event %d passes %s."%(iev,HLTFilter))
    for triggerName in triggerNames:
        if getTriggerBitResult(triggerBits,triggerName, names):
            counts_passing_HLTpaths[triggerName] += 1
            if verbose: print("Event %d passes %s."%(iev,triggerName))
        for filterName in filterNames[triggerName]:
            if getFiterSize(triggerEvent,filterName)>0:
                counts_passing_L1filters[filterName] += 1
                if verbose: print("Event %d passes %s."%(iev,filterName))

print("Total number of events: %d"%count_total)
for triggerName in triggerNames:
    print ()
    print("################# %s #################"%triggerName)
    print("Number of events passing %s: %d"%(triggerName,counts_passing_HLTpaths[triggerName]))
    for filterName in filterNames[triggerName]:
        print("Number of events passing %s: %d"%(filterName,counts_passing_L1filters[filterName]))
        if counts_passing_L1filters[filterName]>0:
            print("Fraction of events passing trigger %s after filter %s: %.2f %% +/- %.2f %% "%(triggerName,filterName,float(counts_passing_HLTpaths[triggerName])/counts_passing_L1filters[filterName]*100, 1.96*sqrt(float(counts_passing_HLTpaths[triggerName])*(1-float(counts_passing_HLTpaths[triggerName])/counts_passing_L1filters[filterName]))/counts_passing_L1filters[filterName]*100))
        else:
            print("Fraction of events passing trigger %s after filter %s: 0.0"%(triggerName,filterName))


# print("Number of events passing %s: %d"%(HLTFilter,count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking))
# print("Number of events passing %s: %d"%(triggerName,count_passing_DST_PFScouting_DoubleMuon_v5))
# print("Fraction of events passing %s: %f"%(HLTFilter,float(count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking)/count_total))
# print("Fraction of events passing %s: %f"%(triggerName,float(count_passing_DST_PFScouting_DoubleMuon_v5)/count_total))
# print("Fraction of events passing %s after %s: %f"%(triggerName,HLTFilter,float(count_passing_DST_PFScouting_DoubleMuon_v5)/count_passing_L1sDSTRun3DoubleMuonPFScoutingPixelTracking))

#     triggerBits.product()
#     names = event.object().triggerNames(triggerBits.product())
#     pathIndex = names.triggerIndex("DST_PFScouting_DoubleMuon_v5")
#     filterIndex = triggerEvent.product().filterIndex(edm.InputTag(HLTFilter,"","HLT"))
# #    print(filterIndex)
#     if filterIndex<triggerEvent.product().sizeFilters():
#  #       print("Filter %s found in event."%HLTFilter)
#         filterKeys = triggerEvent.product().filterKeys(filterIndex)
#         if len(filterKeys)>0:
#             print("Number of objects passing filter: %d"%len(filterKeys))
#             for key in filterKeys:
#                 obj = trigObjColl[key]
#                 print(obj.pt())
# #        print("Number of objects passing filter: %d"%len(filterKeys))
#     else:
#         raise Exception("Filter %s not found in event."%HLTFilter)
# #        print("Filter %s not found in event."%HLTFilter)



# def getCollectionKeys(triggerEvent,inputTag):
#     collectionKeys = []
#     collectionIndex = triggerEvent.collectionIndex(inputTag)
#     if collectionIndex<triggerEvent.sizeCollections():
#         start = 0
#         if collectionIndex>0: start = triggerEvent.collectionKey(collectionIndex-1)
#         stop = triggerEvent.collectionKey(collectionIndex)
#         collectionKeys = range(start, stop)
#         del start
#         del stop
    
#     del collectionIndex
#     return collectionKeys


# HLTprocess = "HLT"
# triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::%s"%HLTprocess)
# event.getByLabel(triggerBitLabel, triggerBits)
# triggerBits.product()
# names = event.object().triggerNames(triggerBits.product())

# triggerEvent, triggerEventLabel = Handle("trigger::TriggerEvent"), ("hltTriggerSummaryAOD::HLT")
# event.getByLabel(triggerEventLabel, triggerEvent) ## AOD
# trigObjColl = triggerEvent.product().getObjects()

# pathIndex = names.triggerIndex("DST_PFScouting_DoubleMuon_v5")

# #calojetCollectionForBtag = "hltSelector8CentralJetsL1FastJet"
# #collectionKeysForBtag = getCollectionKeys(triggerEvent.product(),edm.InputTag(calojetCollectionForBtag,"","HLT2"))

# #for key in collectionKeysForBtag:
# #    jet = trigObjColl[key]
# #    print jet.pt()

# HLTFilter = "hltL1sDSTRun3DoubleMuonPFScoutingPixelTracking"
# #HLTFilter = "hltPreDSTPFScoutingDoubleMuon"
# #HLTFilter = "HLTDoubleMuonScoutingNoVtx"
# #"hltPreDSTPFScoutingDoubleMuon"
# #"HLTDoubleMuonScoutingNoVtx"

# filterIndex = triggerEvent.product().filterIndex(edm.InputTag(HLTFilter,"","HLT"))
# print(filterIndex)
# if filterIndex<triggerEvent.product().sizeFilters():
#     print("Filter %s found in event."%HLTFilter)
#     filterKeys = triggerEvent.product().filterKeys(filterIndex)
#     print("Number of objects passing filter: %d"%len(filterKeys))
