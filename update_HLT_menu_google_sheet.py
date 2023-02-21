streams = "GRun.csv" # hltGetConfiguration /dev/CMSSW_13_0_0/GRun/V16 > hlt.py && cat hlt.py | hltDumpStream --mode csv > GRun.csv
refLumi = 2.4E34
maxPath = 10000

import gspread
from oauth2client.service_account import ServiceAccountCredentials
api_json_credentials = '/home/sdonato/private/sdonato-tsg-d2a8d20b682c.json'
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(api_json_credentials, scope)
gc = gspread.authorize(credentials)

spreadsheetId='1yaj9Za8pcXknuO25O5Jpa565FiC425g4g6ACqI32gkU'
worksheetId=1253663040

def dropVersionNumber(pathName):
    if "_v" in pathName: pathName = pathName[0:pathName.rfind("_v")+2]
    if pathName[0] == ' ': pathName = pathName[1:]
    return pathName

def getRates2018(rates):
    rates = open(rates)
    import csv
    rates_ = csv.reader(rates)
    rates_header = next(rates_)
    STEAM_rates = {}
    for values in rates_:
        pathName = dropVersionNumber(values[0])
        rate = values[1]
        if len(rate)>0 :
            STEAM_rates[pathName] = float(rate)
    rates.close()
    return STEAM_rates

def getRates(rates):
    rates = open(rates)
    import csv
    rates_ = csv.reader(rates)
    rates_header = next(rates_)
    STEAM_rates = {}
    for values in rates_:
        pathName = dropVersionNumber(values[rates_header.index("Path")])
        rate = values[rates_header.index("Total Rate (Hz)")]
        pure_rate = values[rates_header.index("Pure Rate (Hz)")]
        if len(rate)>0 and len(pure_rate)>0:
            STEAM_rates[pathName] = [float(rate), float(pure_rate)]
    rates.close()
    return STEAM_rates

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

def getOMSRates(paths, run=322079, minLS=39, maxLS=42, removeDeadtime=True, scale=1.):
    import sys
    sys.path.insert(1, 'OMSRatesNtuple/OMS_ntuplizer')
    from getHLTpathRate import getHLTpaths, getPathNameWithVersion, getTriggerRate, omsapi, getDeadtime #stripVersion
    omsRates = {}
    HLTPaths = getHLTpaths(omsapi, run)
    if removeDeadtime: 
        scale = scale / (1.-getDeadtime(omsapi, run, minLS, maxLS))
    for path in paths:
#        path = stripVersion(path)
        path = dropVersionNumber(path)
        HLT_path = getPathNameWithVersion(path, HLTPaths)
        omsRates[path] = -1
        if HLT_path in HLTPaths:
            omsRates[path] = getTriggerRate(omsapi, run, HLT_path, minLS, maxLS) * scale
        print(path, omsRates[path])
    return omsRates

def getRatesFromSpreadsheet(spreadsheetId='1Cr60H1Q1PJov2ADo0Q3kVqxvXhr8NEInGgTVxV5c0ec', worksheetId=551224544, labelPath="Path (w/ version number)", labelColumns=["Total Rate (Hz)", "Pure Rate (Hz)"]):
    sh = gc.open_by_key(spreadsheetId)
    ws = sh.get_worksheet_by_id(worksheetId) ##Example: https://docs.google.com/spreadsheets/d/1Cr60H1Q1PJov2ADo0Q3kVqxvXhr8NEInGgTVxV5c0ec/edit#gid=1154525798
    ws = ws.get()
    col_path = ws[0].index(labelPath)
    cols = [ws[0].index(label) for label in labelColumns]
    rates = {}
    for line in ws[1:]:
        rates[dropVersionNumber(line[col_path])] = [line[col]  if col<len(line) else -1 for col in cols]
    return rates

STEAM_pure_rates = getRatesFromSpreadsheet(spreadsheetId='1Cr60H1Q1PJov2ADo0Q3kVqxvXhr8NEInGgTVxV5c0ec', worksheetId=551224544, labelPath="Path (w/ version number)", labelColumns=["Pure Rate (Hz)"])
STEAM_rates = getRatesFromSpreadsheet(spreadsheetId='1Cr60H1Q1PJov2ADo0Q3kVqxvXhr8NEInGgTVxV5c0ec', worksheetId=1154525798, labelPath="Path (w/ version number)", labelColumns=["PU64"])

streams_paths = getStreams(streams)
OMS_rates_2018 = getOMSRates(list(streams_paths)[:maxPath], run=322079, minLS=39, maxLS=42, removeDeadtime=True, scale=refLumi/2.055E34*0.96)  ##PU57.49 2.055E34 4% deadtime
OMS_rates_2022 = getOMSRates(list(streams_paths)[:maxPath], run=362616, minLS=302, maxLS=306, removeDeadtime=True, scale=refLumi/21.19E33*0.96) ##PU61.5 21.19E33 4% deadtime

import pprint
pprint.pprint(STEAM_rates["HLT_PFJet200_v"])
pprint.pprint(streams_paths["HLT_PFJet200_v"])



#columns = ["path", "HIG", "EXO", "TOP", "SUS", "SMP", "EXO", "BPH", "B2G", "HIN", "TRK", "JME", "MUO", "EGM", "TAU", "BTV", "PF", "AlCa", "DPG", "TSG", "Owners", "Rate", "Pure Rate", "Rate18", "PS", "stream", "dataset", "L1 seed"]

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


def updatedLine(headers, line, path, streams_paths, STEAM_rates, OMS_rates_2018, OMS_rates_2022):
    newLine = line[:]
    for i, column in enumerate(headers):
        if column == "PS":
            newLine[i] = streams_paths[path][" 2p0E34+ZeroBias+HLTPhysics"]
        elif column == "stream":
            newLine[i]  = streams_paths[path]["stream"]
        elif column == "dataset":
            newLine[i]  = streams_paths[path][" dataset"]
        elif column == "L1 seed":
            newLine[i]  = streams_paths[path][" seed"]
        elif column == "STEAM":
            newLine[i]  = STEAM_rates[path][0] if path in STEAM_rates else ""
        elif column == "Pure Rate":
            newLine[i]  = STEAM_pure_rates[path][0] if path in STEAM_pure_rates else ""
#        elif column == "Owners": ## keep the original formula in Owners
#            newLine[i]  = ''
        elif column == "path":
            newLine[i]  = path
        elif column == "OMS18":
            path2018 = path[:]
            if path2018 in map2022to2018:
                path2018 = map2022to2018[path2018]
            newLine[i]  = OMS_rates_2018[path2018] if path2018 in OMS_rates_2018 else ''
        elif column == "OMS22":
            newLine[i]  = OMS_rates_2022[path] if path in OMS_rates_2022 else ''
    return newLine

deletedPaths = []
new_paths = list(streams_paths.keys())


### Read current google spread sheet
sh = gc.open_by_key(spreadsheetId)
ws_ = sh.get_worksheet_by_id(worksheetId) 
ws = ws_.get(value_render_option='FORMULA') ##preserve formulas
#1/0
menu_header = ws [0]

for i, line in enumerate(ws[:]):
    if i==0: continue
    path = line[menu_header.index("path")]
    if path in streams_paths:
        new_paths.remove(path)
#        print(ws[i])
#        print(updatedLine(menu_header, ws[i], path, streams_paths, STEAM_rates, OMS_rates_2018, OMS_rates_2022))
        ws[i] = updatedLine(menu_header, ws[i], path, streams_paths, STEAM_rates, OMS_rates_2018, OMS_rates_2022)
    else:
        ws[i] = ['DELETED '+path] + ['']*10
        deletedPaths.append(path)

for path in new_paths:
    ws.append(updatedLine(menu_header, [""]*len(menu_header), path, streams_paths, STEAM_rates, OMS_rates_2018, OMS_rates_2022))

print()
print("Deleted Paths:")
for path in deletedPaths:
    print(path)

print()
print("New Paths:")
for path in new_paths:
    print(path)

print("Uploading spreadsheet %s ."%sh.url)

sh.values_update(
    ws_.title,
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values': ws}
)
