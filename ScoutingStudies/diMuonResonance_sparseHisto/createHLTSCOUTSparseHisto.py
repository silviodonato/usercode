import ROOT
from DataFormats.FWLite import Handle, Events
import math

speedup = True

maxEvents = -100000
# maxEvents = 10000
# fileName="Skim_381544.root"
fileName="SkimOnlyMuons_test.root"
fileName="SkimOnlyMuons_test_filtered.root"
fileName="SkimOnlyMuons_test_filtered2.root"
fileName="skimmed2_output.root"
# fileName="Skim/SkimOnlyMuons_382343.root"
fileName="SkimOnlyMuons.root"
fileName="Skim/SkimOnlyMuons_382343.root"
# fileName="s_test.root"
# fileName="Skim_test.root"

axisDef = {
    "run": (500000, 0, 500000),
    "lumi": (10000, 0, 10000),
    "pt": (150, 0, 15),
    "ptmin": (150, 0, 15),
    "ptmax": (150, 0, 15),
    "eta": (200, -2.5, 2.5),
    "phi": (200, -3.15, 3.15),
    "charge": (19, -9.5, +9.5),
    "dxySig": (100, 0, 50),
    "dxy": (100, 0, 5),
    "dz": (100, 0, 0.5),
    "deltaR": (400, 0, 4.0),
    "deltaPhi": (400, 0, 4.0),
    "deltaEta": (400, 0, 4.0),
    # "mass_ee": (10000, 0, 10),
    "mass_mumu": (10000, 0, 10),
    "DST_PFScouting_DoubleMuon": (2, 0, 2),
    "DST_PFScouting_SingleMuon": (2, 0, 2),
    "DST_PFScouting_ZeroBias": (2, 0, 2),
    # "mass_pipi": (10000, 0, 10),
    # "mass_pipi_log": (12000, -2, 10),
    # "mass_KK": (10000, 0, 10),
    # "mass_Kpi": (10000, 0, 10),
    # "mass_piK": (10000, 0, 10),
    # "mass_ppi": (10000, 0, 10),
    # "mass_pip": (10000, 0, 10),
    # "mass_pK": (10000, 0, 10),
    # "mass_Kp": (10000, 0, 10),
}

vx = 0.0968
vy = -0.1925
#((muons[i].tk_vx() - vertexs[muons[i].tk_vtxInd()].x())**2 + (muons[i].tk_vy() - vertexs[muons[i].tk_vtxInd()].y())**2)**0.5   if muons[i].tk_vtxInd()>=0 else 0.0
def dxymuon(muon, vertexs):
    if vertexs is None:
        return ((muon.trk_vx()-vx)**2 + (muon.trk_vy()-vy)**2)**0.5 / muon.trk_dxyError()
    else: 
        return ((muon.tk_vx() - vertexs[muon.tk_vtxInd()].x())**2 + (muon.tk_vy() - vertexs[muon.tk_vtxInd()].y())**2)**0.5   if muon.tk_vtxInd()>=0 else 0.0

def muonSelection(muon, vertexs):
    # if muon.tk_pt()>1.5 and muon.tk_ndof()>=10 and muon.tk_chi2()/muon.tk_ndof()<3: return True
    # if muon.tk_pt()>2 and muon.tk_ndof()>=5 and muon.tk_chi2()/muon.tk_ndof()<3 and abs(dxymuon(muon,vertexs)/muon.tk_dxy_Error())>5: return True
    # if muon.trk_pt()>2 and muon.trk_ndof()>=5 and muon.trk_chi2()/muon.trk_ndof()<3 and abs(dxymuon(muon,vertexs)/muon.trk_dxy_Error())>5: return True
    # if muon.trk_pt()>2 and muon.trk_ndof()>=5 and muon.trk_chi2()/muon.trk_ndof()<3 and abs(dxymuon(muon,vertexs)/muon.trk_dxyError())<1: return True
    return True
    # if abs(muon.tk_dxy()/muon.tk_dxy_Error())>60  and muon.tk_dxy()>0.2 and muon.tk_pt()>1 and muon.tk_ndof()>=10 and muon.tk_chi2()/muon.tk_ndof()<3: return True
    # if abs(muon.tk_dxy()/muon.tk_dxy_Error())>60  and muon.tk_pt()>1 and muon.tk_ndof()>=10 and muon.tk_chi2()/muon.tk_ndof()<3: return True
    return False

# def muonPairSelection(muon1, muon2):
#     if abs(muon1.tk_dz()-muon2.tk_dz())>0.3: return False
#     if abs(muon1.tk_eta()-muon2.tk_eta())>1.5: return False
#     if abs(muon1.tk_phi()-muon2.tk_phi())>1.5: return False
#     # if muon1.tk_charge()==muon2.tk_charge(): return False
#     return True 


ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)  
# ROOT.gROOT.LoadMacro("myFunction.C+")

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")

print("Opening file: ", fileName)
events = Events ([fileName])
if speedup:
    # chain = ROOT.TChain("Events")
    # chain.Add(fileName)
    file_ = ROOT.TFile.Open(fileName)
    chain = file_.Get("Events")
    chain.SetBranchStatus("*", 0)



# file = ROOT.TFile.Open("step2_NANO.root")

def makeSparseHisto(axis):
    from array import array
    dim = 0
    nBins = array("i")
    xmins = array("d")
    xmaxs = array("d")
    for name in axis:
        (nBin, xmin, xmax) = axis[name]
        print("Adding: ", name, nBin, xmin, xmax)
        nBins.insert(len(nBins), nBin)
        xmins.insert(len(xmins), xmin)
        xmaxs.insert(len(xmaxs), xmax)
    sparseHisto = ROOT.THnSparseD("sparseHisto", "", len(nBins), nBins, xmins, xmaxs)
    for i, name in enumerate(axis):
        sparseHisto.GetAxis(i).SetTitle(name)
        sparseHisto.GetAxis(i).SetName(name)
    return sparseHisto



cuts = {
    5:ROOT.kRed, 
    10:ROOT.kBlue, 
    15:ROOT.kGreen, 
    20:ROOT.kMagenta,
    30:ROOT.kBlack,
}

triggerResults = {
    "DST_PFScouting_ZeroBias" : 0,
    "DST_PFScouting_DoubleMuon" : 0,
    "DST_PFScouting_DoubleEG" : 0,
    "DST_PFScouting_JetHT" : 0,
    "DST_PFScouting_DatasetMuon" : 0,
    "DST_PFScouting_AXOVLoose" : 0,
    "DST_PFScouting_AXOLoose" : 0,
    "DST_PFScouting_AXONominal" : 0,
    "DST_PFScouting_AXOTight" : 0,
    "DST_PFScouting_AXOVTight" : 0,
    "DST_PFScouting_SingleMuon" : 0,
    "DST_PFScouting_ZeroBias" : 0,   
}

### obtained from edmDumpEventContent xxx.root
objectMap = {
    # "triggers" : ("edm::TriggerResults", ("TriggerResults","","HLT")),
    "triggers" :      ("edm::TriggerResults",               ("TriggerResults"            , ""               , "HLT")),
    "muons" : ("vector<Run3ScoutingCandidateWrapper>", ("hltScoutingmuonPacker","","HLTX")),
    "L1FEDs" :        ("FEDRawDataCollection",              ("hltFEDSelectorL1"          , ""               , "HLT")),
    "pfMetPhi" :      ("double",                            ("hltScoutingPFPacker"       , "pfMetPhi"       , "HLT")),
    "pfMetPt" :       ("double",                            ("hltScoutingPFPacker"       , "pfMetPt"        , "HLT")),
    "rho" :           ("double",                            ("hltScoutingPFPacker"       , "rho"            , "HLT")),
    "electrons" :     ("vector<Run3ScoutingElectron>",      ("hltScoutingEgammaPacker"   , ""               , "HLT")),
    "muonNoVtxs" :    ("vector<Run3ScoutingMuon>",          ("hltScoutingMuonPackerNoVtx", ""               , "HLT")),
    "muonVtxs" :      ("vector<Run3ScoutingMuon>",          ("hltScoutingMuonPackerVtx"  , ""               , "HLT")),
    "PFJets" :        ("vector<Run3ScoutingPFJet>",         ("hltScoutingPFPacker"       , ""               , "HLT")),
    "PFCands" :       ("vector<Run3ScoutingParticle>",      ("hltScoutingPFPacker"       , ""               , "HLT")),
    "photons" :       ("vector<Run3ScoutingPhoton>",        ("hltScoutingEgammaPacker"   , ""               , "HLT")),
    "muons" :        ("vector<Run3ScoutingMuon>",           ("hltScoutingMuonPacker"     , ""               , "HLT")),
    "displacedVtxs" : ("vector<Run3ScoutingVertex>",        ("hltScoutingMuonPackerNoVtx", "displacedVtx"   , "HLT")),
    "displacedVtxs" : ("vector<Run3ScoutingVertex>",        ("hltScoutingMuonPackerVtx"  , "displacedVtx"   , "HLT")),
    "primaryVtxs" :   ("vector<Run3ScoutingVertex> ",       ("hltScoutingPrimaryVertexPacker", "primaryVtx" , "HLT")),
}

handles = {}

for obj in objectMap:
    handles[obj] = Handle(objectMap[obj][0])
    handles[obj].label = objectMap[obj][1]

data = {}

muon1 = ROOT.TLorentzVector()
muon2 = ROOT.TLorentzVector()
muon1 = ROOT.TLorentzVector()
muon2 = ROOT.TLorentzVector()

def compute_invariant_mass(muon1, muon2):
    pt1, eta1, phi1, mass1 = muon1
    pt2, eta2, phi2, mass2 = muon2
    # Calculate energy and momentum components for particle 1
    E1 = math.sqrt(pt1**2 * math.cosh(eta1)**2 + mass1**2)
    px1 = pt1 * math.cos(phi1)
    py1 = pt1 * math.sin(phi1)
    pz1 = pt1 * math.sinh(eta1)
    
    # Calculate energy and momentum components for particle 2
    E2 = math.sqrt(pt2**2 * math.cosh(eta2)**2 + mass2**2)
    px2 = pt2 * math.cos(phi2)
    py2 = pt2 * math.sin(phi2)
    pz2 = pt2 * math.sinh(eta2)
    
    # Calculate the components of the total 4-momentum
    E = E1 + E2
    px = px1 + px2
    py = py1 + py2
    pz = pz1 + pz2
    
    # Calculate the invariant mass
    invariant_mass = math.sqrt(E**2 - px**2 - py**2 - pz**2)
    
    return invariant_mass

def createTriggerIndexTable(event, triggerResults, triggerData):
    triggerIndex = {}
    names = event.object().triggerNames(triggerData)
    for trigger in triggerResults:
        for i in range(len(names.triggerNames())):
            if str(trigger) in names.triggerName(i):
                if not (trigger in triggerIndex):
                    triggerIndex[trigger] = i
                else:
                    raise Exception("Duplicate trigger %s"%trigger)
        if not (trigger in triggerIndex):
            for name in names.triggerNames():
                print(trigger, name, trigger in name)
            raise Exception("%s not found."%trigger)
    print("New trigger index table created")
    print(triggerIndex)
    return triggerIndex

def fillTriggerResults(event, triggerResults, triggerIndex, triggerData):
    names = event.object().triggerNames(triggerData)
    for trigger in list(triggerResults):
        if not (trigger in triggerIndex) or not (trigger in names.triggerName(triggerIndex[trigger])):
            triggerIndex.clear() 
            triggerIndex.update(createTriggerIndexTable(event, triggerResults, triggerData))
        triggerResults[trigger] = triggerData.accept(triggerIndex[trigger])

def getProduct(handle):
    event.getByLabel(handle.label, handle)
    if not handle.isValid: raise Exception("Problem with %s %s"%(handle, handle.label))
    else: return handle.product()

def getPtEtaPhiMass(partData, mass):
    return (partData.pt(), partData.eta(), partData.phi(), mass)

def getPtEtaPhiMassTrk(partData, mass):
    return (partData.trk_pt(), partData.trk_eta(), partData.trk_phi(), mass)



def checkInputs(inputs, axisDef):
    keys_axisDef = list(axisDef.keys())
    keys_inputs = list(inputs.keys())
    if keys_axisDef!=keys_inputs:
        print(len(axisDef), len(inputs))
        for i in range(max(len(axisDef), len(inputs))):
            if i<len(axisDef) and i<len(inputs):
                print(keys_axisDef[i], keys_inputs[i], "  DIFF " if keys_axisDef[i]!=keys_inputs[i] else "")
            else:
                if len(keys_axisDef)<=i:
                    print(keys_axisDef[i],"---")
                else:
                    print("---", keys_inputs[i])
        raise Exception("Mismatch in input keys.")
    return True


hist = ROOT.TH1F("hist", "hist", 100, 0.8, 1.2)
hist2 = ROOT.TH1F("hist2", "hist2", 200, 0, 0.5)

sparseHisto = makeSparseHisto(axisDef)
## from defHLTSCOUTSparseHisto import axisDef
#  inputs = clone(axisDef)
# for input in inputs:
#     inputs[input] = None

mass_pion = 0.139
mass_kaon = 0.493
mass_muon = 0.105
mass_ele = 0.000511
mass_proton = 0.938

histdxy = ROOT.TH1F("histdxy", "histdxy", 100, 0, 10)

triggerIndex = {}
histoVtx = ROOT.TH1F("histoVtx", "histoVtx", 26, 0, 13)
histoVtx.SetLineColor(ROOT.kRed)
histoVtx.SetLineWidth(2)
histoVtx.SetFillColorAlpha(ROOT.kRed, 0.5)
histoVtx.SetFillStyle(3004)

histoNoVtx = histoVtx.Clone("histoNoVtx")
histoNoVtx.SetLineColor(ROOT.kBlue)
histoNoVtx.SetFillColorAlpha(ROOT.kBlue, 0.5)
histoNoVtx.SetFillStyle(3005)

histoMix = histoVtx.Clone("histoMix")
histoMix.SetLineColor(ROOT.kGreen)
histoMix.SetFillColorAlpha(ROOT.kGreen, 0.5)
histoMix.SetFillStyle(3006)

histoMixSS = histoVtx.Clone("histoMixSS")
histoMixSS.SetLineColor(ROOT.kMagenta)
histoMixSS.SetFillColorAlpha(ROOT.kMagenta, 0.5)
histoMixSS.SetFillStyle(3007)



def getRunLumiEvent(event):
    run = event.object().id().run()
    lumi = event.object().id().luminosityBlock()
    eventNumber = event.object().id().event()
    return run, lumi, eventNumber

event = events
import time
mytime = time.time()
if speedup:
    # chain.SetBranchStatus("*", 0)
    chain.SetBranchStatus("Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.obj.charge_", 1)
    chain.SetBranchStatus("Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.obj.charge_", 1)
    selection = ROOT.TTreeFormula("selection", """\
                                  (Sum$(Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.obj.charge_>0) + Sum$(Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.obj.charge_>0))>0 &&\
                                  (Sum$(Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.obj.charge_<0) + Sum$(Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.obj.charge_<0))>0\
                                   """, chain)

                                #   (Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.@obj.size() + Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.@obj.size())>=2 &&\
                                #   (Sum$(Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.obj.charge()>0) + Sum$(Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.obj.charge()>0))>0 &&\
                                #   (Sum$(Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.obj.charge()<0) + Sum$(Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.obj.charge()<0))>0\
    # selection = ROOT.TTreeFormula("selection", "1", chain)
    ##SetLeafStatus

if speedup:
    nevents = chain.GetEntries()
else:
    nevents = events.size()

first = True
for iev in range(nevents):
# for iev,event in enumerate(events):
    if iev%1000000==0: 
        # run, lumi, eventNumber = getRunLumiEvent(event)
        print(iev, "/", nevents)
        # print(iev, run, lumi, eventNumber)

    if speedup: 
        chain.GetEntry(iev)
        if selection.EvalInstance()==0: continue
        # chain.SetBranchStatus("Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.@obj.size*", 1)
        # chain.SetBranchStatus("Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.@obj.size*", 1)
        # chain.GetEntry(iev)
        # sizeMuonNoVtx = chain.GetLeaf("Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.obj.pt_").GetNdata()
        # sizeMuonVtx = chain.GetLeaf("Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.obj.pt_").GetNdata()
        # if sizeMuonNoVtx+sizeMuonVtx<2: continue ######### Selecting events with at least 2 muons

    events.to(iev)

    muonVtxs = getProduct(handles["muonVtxs"])
    muonNoVtxs = getProduct(handles["muonNoVtxs"])
    if speedup:
        assert(chain.GetLeaf("Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.obj.charge_").GetNdata() == muonNoVtxs.size())
    
    # if (muonVtxs.size() + muonNoVtxs.size())<2: continue ######### Selecting events with at least 2 muons
    p , n = 0, 0
    for muon in muonVtxs:
        if muon.charge()>0: p+=1
        else: n+=1
    for muon in muonNoVtxs:
        if muon.charge()>0: p+=1
        else: n+=1
    if p==0 or n==0: continue ######### Selecting events with at least 2 muons
    if muonNoVtxs.size()>=5: print(muonNoVtxs.size())
    # print (chain.GetLeaf("Run3ScoutingMuons_hltScoutingMuonPackerNoVtx__HLT.obj.pt_").GetNdata(), muonNoVtxs.size())
    run, lumi, eventNumber = getRunLumiEvent(event)

    if iev>maxEvents and maxEvents>0: break
    try:
        data["triggers"] = getProduct(handles["triggers"])
    except:
        continue
    fillTriggerResults(event, triggerResults, triggerIndex, data["triggers"])
    if not triggerResults["DST_PFScouting_ZeroBias"]: continue ######### Selecting events with ZeroBias trigger
    if muonVtxs.size()>=2:
        mass_mm_Vtxs = compute_invariant_mass(getPtEtaPhiMass(muonVtxs[0], mass_muon), getPtEtaPhiMass(muonVtxs[1], mass_muon))
        histoVtx.Fill(mass_mm_Vtxs)
    if muonNoVtxs.size()>=2:
        mass_mm_NoVtx = compute_invariant_mass(getPtEtaPhiMass(muonNoVtxs[0], mass_muon), getPtEtaPhiMass(muonNoVtxs[1], mass_muon))
        histoNoVtx.Fill(mass_mm_NoVtx)
    muons = []
    vx = 0.0968
    vy = -0.1925
    for muon in muonVtxs:
        dxy = ((muon.trk_vx()-vx)**2 + (muon.trk_vy()-vy)**2)**0.5 / muon.trk_dxyError()
        histdxy.Fill(min(9.9, dxy/muon.trk_dxyError()))
        if muonSelection(muon, None):
            muons.append(muon)
        # if dxy>1 or muon.trk_chi2()/muon.trk_ndof(): continue
        # if muonSelection(muon, None):
        #     muons.append((getPtEtaPhiMass(muon, mass_muon),muon.charge()))
        # muons.append((getPtEtaPhiMass(muon, mass_muon),muon.charge()))
        # dxy = ((Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.obj.trk_vy_+0.1925)**2+(Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.obj.trk_vx_-0.0968)**2)**0.5 / Run3ScoutingMuons_hltScoutingMuonPackerVtx__HLT.obj.trk_dxyError()
    for muon in muonNoVtxs:
        dR2 = 1
        for m2 in muonVtxs:
            dR2 = min(dR2, (m2.eta() - muonNoVtxs[0].eta())**2 + ROOT.TVector2.Phi_mpi_pi(m2.phi() - muonNoVtxs[0].phi())**2)
        if dR2>0.1**2:
            # print(dR2**0.5)
            dxy = ((muon.trk_vx()-vx)**2 + (muon.trk_vy()-vy)**2)**0.5 / muon.trk_dxyError()
            histdxy.Fill(min(9.9, dxy/muon.trk_dxyError()))
            if muonSelection(muon, None):
                muons.append(muon)
        # if muonSelection(muon, None):
        #         muons.append((getPtEtaPhiMass(muon, mass_muon),muon.charge()))
        # else:
        #     pass
    # if len(muons)>=2:
    #     mass_mm = compute_invariant_mass(muons[0][0], muons[1][0])
    #     charge = muons[0][1]+muons[1][1]
    #     if charge==0:
    #         histoMix.Fill(mass_mm)
    #     else:
    #         histoMixSS.Fill(mass_mm)
    #         if mass_mm < 0.8:
    #             dR = ((muons[0][0][1] - muons[1][0][1])**2 + ROOT.TVector2.Phi_mpi_pi(muons[0][0][2] - muons[1][0][2])**2)**0.5
            # 1/0
                # print(mass_mm, dR)
                # print(muons[0][0])
                # print(muons[1][0])
            # print("Remove duplicate muon")
        # print(mass_mm)


    # goodMuons = []
    # for i in range(len(muons)):
    #     if muonSelection(muons[i], None):
    #         goodMuons.append(i)
    goodMuons = range(len(muons))
    if len(goodMuons)<2: continue
    # print(goodMuons)
    for count, i in enumerate(goodMuons):
        # if not muonSelection(muons[i]): continue
        # muon1 = getPtEtaPhiMassTrk(muons[i], mass_kaon)
        muon1.SetPtEtaPhiM(muons[i].trk_pt(), muons[i].trk_eta(), muons[i].trk_phi(), mass_muon)
        for j in goodMuons[count+1:]:
            # print(i,j)
            dEta =  muons[i].trk_eta() - muons[j].trk_eta()
            dPhi =  ROOT.TVector2.Phi_mpi_pi(muons[i].trk_phi() - muons[j].trk_phi())
            dR2 = (dEta**2 + dPhi**2)
            if dR2>1: continue
            dR = dR2**0.5
            dZ = abs(muons[i].trk_dz()-muons[j].trk_dz())
            if dZ>0.1: continue
            deltaXY = (muons[i].trk_vx() - muons[j].trk_vx())**2 + (muons[i].trk_vy() - muons[j].trk_vy())**2
            if deltaXY/max(muons[i].trk_dxyError(),muons[j].trk_dxyError())>3: continue
            # if not muonPairSelection(muons[i], muons[j]): continue
            muon2.SetPtEtaPhiM(muons[j].trk_pt(), muons[j].trk_eta(), muons[j].trk_phi(), mass_kaon)
            # if not muonSelection(muons[j]): continue
            # muon2 = getPtEtaPhiMassTrk(muons[j], mass_kaon)
            # invMass = compute_invariant_mass(muon1, muon2)
            # print(invMass)
            count+=1
            if muons[i].charge()>0:
                muonP = muons[i]
                muonN = muons[j]
            else:
                muonN = muons[i]
                muonP = muons[j]
            hist2.Fill(muonP.trk_dz()-muonN.trk_dz())
            dimuon = muon1+muon2
            hist.Fill(dimuon.M())
            dxy = dxymuon(muonP, None)
            mass_mumu = (muon1 + muon2).M()

            # dxy = ((muonP.tk_vx() - vertexs[muonP.tk_vtxInd()].x())**2 + (muonP.tk_vy() - vertexs[muonP.tk_vtxInd()].y())**2)**0.5   if muonP.tk_vtxInd()>=0 else 0.0
            # print(dxy)

            # mass_pipi = compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_pion), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_pion))
            # mass_KK = compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_kaon), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_kaon))
            # mass_mumu = compute_invariant_mass((muonP.trk_pt(), muonP.trk_eta(), muonP.tk_phi(), mass_muon), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_muon))
            # mass_piK = compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_pion), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_kaon))
            # mass_Kpi = compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_kaon), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_pion))
            # mass_ee =  compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_ele), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_ele))
            # mass_ppi = compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_proton), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_pion))
            # mass_pip = compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_pion), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_proton))
            # mass_pp = compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_proton), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_proton))
            # mass_pK = compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_proton), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_kaon))
            # mass_Kp = compute_invariant_mass((muonP.tk_pt(), muonP.tk_eta(), muonP.tk_phi(), mass_kaon), (muonN.tk_pt(), muonN.tk_eta(), muonN.tk_phi(), mass_proton))

            # print(dimuon.M(),mass_pipi, mass_KK, mass_mumu, mass_piK, mass_Kpi)
            # inputs["run"] = run
            # inputs["lumi"] = lumi
            # inputs["pt"] = dimuon.Pt()
            # inputs["eta"] = dimuon.Eta()
            # inputs["phi"] = dimuon.Phi()
            # inputs["charge"] = muonP.tk_charge()+muonN.tk_charge()
            # inputs["dxy"] = dxy / muonP.tk_dxy_Error()
            # inputs["dz"] = abs(dZ)
            # inputs["deltaR"] = abs(dR)
            # inputs["deltaPhi"] = abs(dPhi)
            # inputs["deltaEta"] = abs(dEta)
            # inputs["mass_ee"] = mass
            # inputs["mass_mumu"] = mass_mumu
            # inputs["mass_pipi"] = mass_pipi
            # inputs["mass_pipi_log"] = math.log(mass_pipi)
            # inputs["mass_KK"] = mass
            # inputs["mass_Kpi"] = mass_Kpi
            # inputs["mass_piK"] = mass_piK
            # inputs["mass_ppi"] = mass_ppi
            # inputs["mass_pip"] = mass_pip
            # inputs["mass_pK"] = mass
    
            inputs = {
                "run": run,
                "lumi": lumi,
                "pt": dimuon.Pt(),
                "ptmin": min(muonP.trk_pt(), muonN.trk_pt()),
                "ptmax": max(muonP.trk_pt(), muonN.trk_pt()),
                "eta": dimuon.Eta(),
                "phi": dimuon.Phi(),
                "charge": muonP.charge()+muonN.charge(),
                "dxySig": dxy / muonP.trk_dxyError(),
                "dxy": dxy,
                "dz": abs(dZ),
                "deltaR": abs(dR),
                "deltaPhi": abs(dPhi),
                "deltaEta": abs(dEta),
                # "mass_ee": mass_ee,
                "mass_mumu": mass_mumu,
                "DST_PFScouting_DoubleMuon": triggerResults["DST_PFScouting_DoubleMuon"],
                "DST_PFScouting_SingleMuon": triggerResults["DST_PFScouting_SingleMuon"],
                "DST_PFScouting_ZeroBias": triggerResults["DST_PFScouting_ZeroBias"],
                # "mass_pipi": mass_pipi,
                # "mass_pipi_log": math.log(mass_pipi),
                # "mass_KK": mass_KK,
                # "mass_Kpi": mass_Kpi,
                # "mass_piK": mass_piK,
                # "mass_ppi": mass_pip,
                # "mass_pip": mass_pip,
                # "mass_pK": mass_pK,
                # "mass_Kp": mass_Kp,
                }
            ## check goodness of inputs
            if first: checkInputs(axisDef, inputs)
            if mass_mumu>3:
                print(inputs)
            first = False
            sparseHisto.Fill(*inputs.values())
            # print(inputs)

    
                                     
    # if muonVtxs.size()>1 and muonNoVtxs.size()>1:
    #     dR = ((muonVtxs[0].eta() - muonNoVtxs[0].eta())**2 + ROOT.TVector2.Phi_mpi_pi(muonVtxs[0].phi() - muonNoVtxs[0].phi())**2)**0.5
    #     if dR<0.3:
    #         print(dR)
    #         histo.Fill(dR)


mytime = time.time()-mytime
print("Time: ", mytime)

canvas = ROOT.TCanvas("canvas", "canvas", 800, 800)
histoNoVtx.SetMaximum(max(histoNoVtx.GetMaximum(), histoVtx.GetMaximum(), histoMix.GetMaximum(), histoMixSS.GetMaximum())*1.2)
histoNoVtx.Draw()
histoVtx.Draw("same")
histoMix.Draw("same")
histoMixSS.Draw("same")
leg = ROOT.TLegend(0.6, 0.6, 0.9, 0.9)
leg.AddEntry(histoVtx, "With vertex", "l")
leg.AddEntry(histoNoVtx, "Without vertex", "l")
leg.AddEntry(histoMix, "Mixed", "l")
leg.AddEntry(histoMixSS, "Mixed SS", "l")
leg.Draw()
canvas.SetLogy()
canvas.SaveAs("dR.png")

histdxy.Draw()
canvas.SaveAs("dxy.png")


outFile = ROOT.TFile("sparseHisto.root", "RECREATE")
outFile.cd()
sparseHisto.Write()
outFile.Write()
outFile.Close()


    # if muons.size()<2: continue ######### Selecting events with at least 2 muons
    # if abs(muons[0].trk_dz()-muons[1].trk_dz())>0.3: continue ######### Selecting events with 2 muons from the same vertex
    # # muon1 = getPtEtaPhiMass(data["muonVtxs"][0], mass_muon)
    # # muon2 = getPtEtaPhiMass(data["muonVtxs"][1], mass_muon)
    # muon1 = getPtEtaPhiMass(muons[0], mass_muon)
    # muon2 = getPtEtaPhiMass(muons[1], mass_muon)
    # invMass = compute_invariant_mass(muon1, muon2)
    # print(invMass, muons[0].trk_dxy(), muons[0].trk_dxy()/muons[0].trk_dxyError(), (muons[0].trk_vx()**2+muons[0].trk_vy()**2)**0.5, ((muons[0].trk_vx()-muons[1].trk_vx())**2+(muons[0].trk_vy()-muons[1].trk_vy())**2)**0.5)
#     # hist.Fill(invMass)
#     # hist2.Fill(muons[0].trk_dz()-muons[1].trk_dz())
#     muons = getProduct(handles["muons"])
#     vertexs = getProduct(handles["primaryVtxs"])
#     count = 0



#             # sparseHisto.Fill(
#             #     run,
#             #     lumi,
#             #     dimuon.Pt(), 
#             #     dimuon.Eta(), 
#             #     dimuon.Phi(), 
#             #     dimuon.M(), 
#             #     muonP.tk_charge()+muonN.tk_charge(), 
#             #     # muonP.tk_dxy(), 
#             #     # muonP.tk_dxy() - (t.tk_vx()**2+t.tk_vx()**2)**0.5 , 
#             #     dxy / muonP.tk_dxy_Error(), 
#             #     abs(dZ),
#             #     abs(dR),
#             #     abs(dEta),
#             #     abs(dPhi),
#             #     mass_pipi,
#             #     mass_mumu,
#             #     mass_ee,
#             #     math.log(mass_pipi),
#             #     mass_Kpi,
#             #     mass_ppi,
#             #     mass_pip,
#             #     mass_pK,
#             # )
#     # "run": (500000, 0, 500000),
#     # "lumi": (10000, 0, 10000),
#     # "pt": (150, 0, 15),
#     # "eta": (200, -2.5, 2.5),
#     # "phi": (200, -3.15, 3.15),
#     # "charge": (19, -9.5, +9.5),
#     # "dxy": (100, 0, 5),
#     # "dz": (100, 0, 0.5),
#     # "deltaR": (400, 0, 4.0),
#     # "deltaPhi": (400, 0, 4.0),
#     # "deltaEta": (400, 0, 4.0),
#     # "mass_ee": (10000, 0, 10),
#     # "mass_mumu": (10000, 0, 10),
#     # "mass_pipi": (10000, 0, 10),
#     # "mass_pipi_log": (12000, -2, 10),
#     # "mass_KK": (10000, 0, 10),
#     # "mass_Kpi": (10000, 0, 10),
#     # "mass_piK": (10000, 0, 10),
#     # "mass_ppi": (10000, 0, 10),
#     # "mass_pip": (10000, 0, 10),
#     # "mass_pK": (10000, 0, 10),
#     # "mass_Kp": (10000, 0, 10),
#     # print(count)
#     if count>10:
#         pass
#         # break
    
#     # if muons.size()<2: continue ######### Selecting events with at least 2 muons
#     # if abs(muons[0].trk_dz()-muons[1].trk_dz())>0.3: continue ######### Selecting events with 2 muons from the same vertex
#     # # muon1 = getPtEtaPhiMass(data["muonVtxs"][0], mass_muon)
#     # # muon2 = getPtEtaPhiMass(data["muonVtxs"][1], mass_muon)
#     # muon1 = getPtEtaPhiMass(muons[0], mass_muon)
#     # muon2 = getPtEtaPhiMass(muons[1], mass_muon)
#     # invMass = compute_invariant_mass(muon1, muon2)
#     # print(invMass)
#     # hist.Fill(invMass)
#     # hist2.Fill(muons[0].trk_dz()-muons[1].trk_dz())

# 1/0
# plotDefs = { ## plot name: (variable , selection)
#     "eta-1" : ( "eta" , {
#             "phi" : [0, 2.5]
#         }),
#     "eta-2" : ( "eta" ,{
#             "phi" : [-2.5, 0]
#         }),
#     "eta-3" : ( "eta" ,{
#             "pt" : [5, 100]
#         }),
# }

# def makePlot(sparseHisto, plotDef):
#     varPlot, selection = plotDef
#     for varSel in selection:
#         (xmin, xmax) = selection[varSel]
#         print(varPlot, varSel, xmin, xmax)
#         ax = sparseHisto.GetAxis(variables.index(varSel))
#         ax.SetRange(ax.FindBin(xmin), ax.FindBin(xmax))
#     histo = sparseHisto.Projection(variables.index(varPlot))
#     ## revert changes
#     for varSel in selection:
#         ax = sparseHisto.GetAxis(variables.index(varSel))
#         ax.SetRange()
#     return histo


# plots = {}
# for plotName in plotDefs:
#     plotDef = plotDefs[plotName]
#     plots[plotName] = makePlot(sparseHisto, plotDef)       

# canvas = ROOT.TCanvas("canvas", "canvas", 800, 800)
# plots["eta-3"].Draw()
# canvas.SaveAs("eta-3.png")

# 1/0

# canvas = ROOT.TCanvas("canvas", "canvas", 800, 800)
# hist.Draw()
# canvas.SaveAs("invMass.png")
# hist2.Draw()
# canvas.SaveAs("dZ.png")
