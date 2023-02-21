#older version of update_HLT_menu_google_sheet.py
oldFile = "HLT menu - HLT paths.csv" # https://docs.google.com/spreadsheets/d/1UIR0YISWX1r2wfk-r7bPlVmHwguoVgjvGEw3nTgZd-c
rates2018 = "OMS_rates.csv" # https://cmsoms.cern.ch/cms/triggers/hlt_trigger_rates/fullscreen/11281?cms_run=325170&props.11280_11278.selectedCells=Physics:2&props.11281_11278.selectedCells=HLT_TripleMu_5_3_3_Mass3p8_DZ_v8:2&filterBy=cms_fullrun PU~40
rates = "CMSSW_12_3_0_HLTRates - Rates of Paths.csv" # https://docs.google.com/spreadsheets/d/1If1IZuJn_C2Xl8tlXIcpCOymu5MwNipeaKPc9TGoSdAstreams = "GRun.csv"
streams = "GRun.csv" # hltGetConfiguration /dev/CMSSW_12_3_0/GRun | hltDumpStream  --csv > GRun.txt
newFile = "new.csv" 

def dropVersionNumber(pathName):
    if "_v" in pathName: pathName = pathName[0:pathName.rfind("_v")+2]
    if pathName[0] == ' ': pathName = pathName[1:]
    return pathName

def getRates2018(rates):
    rates = open(rates)
    import csv
    rates_ = csv.reader(rates)
    rates_header = next(rates_)
    rates_paths = {}
    for values in rates_:
        pathName = dropVersionNumber(values[0])
        rate = values[1]
        if len(rate)>0 :
            rates_paths[pathName] = float(rate)
    rates.close()
    return rates_paths

def getRates(rates):
    rates = open(rates)
    import csv
    rates_ = csv.reader(rates)
    rates_header = next(rates_)
    rates_paths = {}
    for values in rates_:
        pathName = dropVersionNumber(values[rates_header.index("Path")])
        rate = values[rates_header.index("Total Rate (Hz)")]
        pure_rate = values[rates_header.index("Pure Rate (Hz)")]
        if len(rate)>0 and len(pure_rate)>0:
            rates_paths[pathName] = [float(rate), float(pure_rate)]
    rates.close()
    return rates_paths

def getStreams(streams):
    streams = open(streams)
    import csv
    streams_ = csv.reader(streams)
    streams_header = next(streams_)
    streams_paths = {}
    for values in streams_:
        if "EndPath not found" in values[0]: continue
        if "PhysicsScoutingPFMonitor" in values[0]: continue
        pathName = dropVersionNumber(values[streams_header.index(" path")])
        if pathName in streams_paths and "Physics" in streams_paths[pathName]["stream"]: 
            if not "Physics" in values[streams_header.index("stream")]: continue
            print("OVERWRITING!",values)
            print(pathName, streams_paths[pathName])
        streams_paths[pathName] = {}
        for el in streams_header:
            if el == " path": continue
            streams_paths[pathName][el] = values[streams_header.index(el)]
    streams.close()
    return streams_paths

def getMenu(menu):
    menu = open(menu)
    import csv
    menu_ = csv.reader(menu)
    menu_header = next(menu_)
    menu_paths = []
    for values in menu_:
        menu_el = {}
        for el in menu_header:
            menu_el[el] = values[menu_header.index(el)]
        menu_paths.append(menu_el)
    menu.close()
    return menu_paths


newFile = open(newFile,'w')
rates_paths = getRates(rates)
rates_paths_2018 = getRates2018(rates2018)
streams_paths = getStreams(streams)
old_paths = getMenu(oldFile)

import pprint
pprint.pprint(old_paths[0])
pprint.pprint(rates_paths["HLT_Ele28_WPTight_Gsf_v"])
pprint.pprint(streams_paths["HLT_Ele28_WPTight_Gsf_v"])



columns = ["path", "HIG", "EXO", "TOP", "SUS", "SMP", "EXO", "BPH", "B2G", "HIN", "TRK", "JME", "MUO", "EGM", "TAU", "BTV", "PF", "AlCa", "DPG", "TSG", "Owners", "Rate", "Pure Rate", "Rate18", "PS", "stream", "dataset", "L1 seed"]

newFile.write(",".join(columns)+"\n")

map2022to2018 = {
 'AlCa_LumiPixelsCounts_Random_v': 'AlCa_LumiPixels_Random',
 'HLT_BTagMu_AK4DiJet110_Mu5_v': 'HLT_BTagMu_AK4DiJet110_Mu5_noalgo_v',
 'HLT_BTagMu_AK4DiJet170_Mu5_v': 'HLT_BTagMu_AK4DiJet170_Mu5_noalgo_v',
 'HLT_BTagMu_AK4DiJet20_Mu5_v': 'HLT_BTagMu_AK4DiJet20_Mu5_noalgo_v',
 'HLT_BTagMu_AK4DiJet40_Mu5_v': 'HLT_BTagMu_AK4DiJet40_Mu5_noalgo_v',
 'HLT_BTagMu_AK4DiJet70_Mu5_v': 'HLT_BTagMu_AK4DiJet70_Mu5_noalgo_v',
 'HLT_BTagMu_AK4Jet300_Mu5_v': 'HLT_BTagMu_AK4Jet300_Mu5_noalgo_v',
 'HLT_BTagMu_AK8DiJet170_Mu5_v': 'HLT_BTagMu_AK8DiJet170_Mu5_noalgo_v',
 'HLT_BTagMu_AK8Jet170_DoubleMu5_v': 'HLT_BTagMu_AK8Jet170_DoubleMu5_noalgo_v',
 'HLT_BTagMu_AK8Jet300_Mu5_v': 'HLT_BTagMu_AK8Jet300_Mu5_noalgo_v',
 'HLT_CaloMET300_NotCleaned_v': 'HLT_CaloMET300_HBHECleaned_v',
 'HLT_CaloMET350_NotCleaned_v': 'HLT_CaloMET350_HBHECleaned_v',
 'HLT_DiPFJet15_FBEta3_NoCaloMatched_v': 'HLT_DiPFJet15_FBEta3_NoCaloMatched_v',
 'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_v': 'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v',
 'HLT_DoubleMediumDeepTauIsoPFTauHPS35_L2NN_eta2p1_v': 'HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v',
 'HLT_DoublePFJets100_PFBTagDeepCSV_p71_v': 'HLT_DoublePFJets100_CaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets100_PFBTagDeepJet_p71_v': 'HLT_DoublePFJets100_CaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepCSV_p71_v': 'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets116MaxDeta1p6_DoublePFBTagDeepJet_p71_v': 'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepCSV_p71_v': 'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets128MaxDeta1p6_DoublePFBTagDeepJet_p71_v': 'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets200_PFBTagDeepCSV_p71_v': 'HLT_DoublePFJets200_CaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets200_PFBTagDeepJet_p71_v': 'HLT_DoublePFJets200_CaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets350_PFBTagDeepCSV_p71_v': 'HLT_DoublePFJets350_CaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets350_PFBTagDeepJet_p71_v': 'HLT_DoublePFJets350_CaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets40_PFBTagDeepCSV_p71_v': 'HLT_DoublePFJets40_CaloBTagDeepCSV_p71_v',
 'HLT_DoublePFJets40_PFBTagDeepJet_p71_v': 'HLT_DoublePFJets40_CaloBTagDeepCSV_p71_v',
 'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_v': 'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v',
 'HLT_Ele24_eta2p1_WPTight_Gsf_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v': 'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_v',
 'HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v': 'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1_v',
 'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v': 'HLT_IsoMu24_eta2p1_MediumChargedIsoPFTauHPS30_Trk1_eta2p1_Reg_CrossL1_v',
 'HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS50_eta2p1_v': 'HLT_IsoMu24_eta2p1_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v',
 'HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v': 'HLT_IsoMu24_eta2p1_MediumChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_CrossL1_v',
 'HLT_IsoMu27_LooseChargedIsoPFTau20_Trk1_eta2p1_SingleL1_v': 'HLT_IsoMu27_LooseChargedIsoPFTauHPS20_Trk1_eta2p1_SingleL1_v',
 'HLT_LooseDeepTauPFTauHPS180_L2NN_eta2p1_v': 'HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v',
 'HLT_LooseDeepTauPFTauHPS50_eta2p1_MET100_v': 'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET100_v',
 'HLT_Mu12_DoublePFJets100_PFBTagDeepCSV_p71_v': 'HLT_Mu12_DoublePFJets100_CaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets100_PFBTagDeepJet_p71_v': 'HLT_Mu12_DoublePFJets100_CaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets200_PFBTagDeepCSV_p71_v': 'HLT_Mu12_DoublePFJets200_CaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets200_PFBTagDeepJet_p71_v': 'HLT_Mu12_DoublePFJets200_CaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets350_PFBTagDeepCSV_p71_v': 'HLT_Mu12_DoublePFJets350_CaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets350_PFBTagDeepJet_p71_v': 'HLT_Mu12_DoublePFJets350_CaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepCSV_p71_v': 'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoublePFBTagDeepJet_p71_v': 'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets40_PFBTagDeepCSV_p71_v': 'HLT_Mu12_DoublePFJets40_CaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets40_PFBTagDeepJet_p71_v': 'HLT_Mu12_DoublePFJets40_CaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepCSV_p71_v': 'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
 'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoublePFBTagDeepJet_p71_v': 'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoubleCaloBTagDeepCSV_p71_v',
 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepJet_1p5_v': 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_PFDiJet30_PFBtagDeepCSV_1p5_v',
 'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepJet_4p5_v': 'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5_v',
 'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepJet_4p5_v': 'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v',
 'HLT_PFHT400_FivePFJet_120_120_60_30_30_DoublePFBTagDeepJet_4p5_v': 'HLT_PFHT400_FivePFJet_100_100_60_30_30_DoublePFBTagDeepCSV_4p5_v',
 'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepJet_2p94_v': 'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94_v',
 'HLT_PFHT450_SixPFJet36_PFBTagDeepJet_1p59_v': 'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59_v',
 'HLT_PFMET200_BeamHaloCleaned_v': 'HLT_PFMET200_HBHE_BeamHaloCleaned_v',
 'HLT_PFMET250_NotCleaned_v': 'HLT_PFMET250_HBHECleaned_v',
 'HLT_PFMET300_NotCleaned_v': 'HLT_PFMET300_HBHECleaned_v',
 'HLT_PFMETTypeOne200_BeamHaloCleaned_v': 'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v',
 'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v': 'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
 'HLT_QuadPFJet103_88_75_15_PFBTagDeepJet_1p3_VBF2_v': 'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2_v',
 'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v': 'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
 'HLT_QuadPFJet105_88_76_15_PFBTagDeepJet_1p3_VBF2_v': 'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2_v',
 'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v': 'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
 'HLT_QuadPFJet111_90_80_15_PFBTagDeepJet_1p3_VBF2_v': 'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2_v',
 'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepJet_1p3_7p7_VBF1_v': 'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1_v',
 'HLT_QuadPFJet98_83_71_15_PFBTagDeepJet_1p3_VBF2_v': 'HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2_v',
 'HLT_VBF_DoubleLooseChargedIsoPFTau20_Trk1_eta2p1_v': 'HLT_VBF_DoubleLooseChargedIsoPFTauHPS20_Trk1_eta2p1_v'
 }



def updateValue(el, path, streams_paths, rates_paths, rates_paths_2018, column):
    if column == "PS":
        el = streams_paths[path][" 2.0e34+ZB+HLTPhysics"]
    elif column == "stream":
        el = streams_paths[path]["stream"]
    elif column == "dataset":
        el = streams_paths[path][" dataset"]
    elif column == "L1 seed":
        el = streams_paths[path][" L1 trigger"]
    elif column == "Rate":
        el = rates_paths[path][0] if path in rates_paths else ""
    elif column == "Pure Rate":
        el = rates_paths[path][1] if path in rates_paths else ""
    elif column == "Owners":
        el = ""
    elif column == "path":
        el = path
    elif column == "Rate18":
        path2018 = path[:]
        if path2018 in map2022to2018:
            path2018 = map2022to2018[path2018]
        el = rates_paths_2018[path2018] if path2018 in rates_paths_2018 else ""
    return el

deletedPaths = []
new_paths = list(streams_paths.keys())
for old_path in old_paths:
    path = old_path["path"]
    if path in streams_paths:
        new_paths.remove(path)
        for column in columns:
            el = updateValue(old_path[column] if column in old_path else "", path, streams_paths, rates_paths, rates_paths_2018, column) 
            newFile.write(str(el)+",")
        newFile.write("\n")
    else:
        deletedPaths.append(path)

for path in new_paths:
    for column in columns:
        el = updateValue("", path, streams_paths, rates_paths, rates_paths_2018, column)
        newFile.write(str(el)+",")
    newFile.write("\n")

print()
print("Deleted Paths:")
for path in deletedPaths:
    print(path)

print()
print("New Paths:")
for path in new_paths:
    print(path)

newFile.close()


