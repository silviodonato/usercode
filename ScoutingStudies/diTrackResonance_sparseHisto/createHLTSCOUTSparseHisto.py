import ROOT
from DataFormats.FWLite import Handle, Events
import math

maxEvents = -100000
fileName="Skim_381544.root"

axisDef = {
    "run": (500000, 0, 500000),
    "lumi": (10000, 0, 10000),
    "pt": (150, 0, 15),
    "eta": (200, -2.5, 2.5),
    "phi": (200, -3.15, 3.15),
    "charge": (19, -9.5, +9.5),
    "dxySig": (100, 0, 5),
    "dxy": (100, 0, 0.5),
    "dz": (100, 0, 0.5),
    "deltaR": (400, 0, 4.0),
    "deltaPhi": (400, 0, 4.0),
    "deltaEta": (400, 0, 4.0),
    "mass_ee": (10000, 0, 10),
    "mass_mumu": (10000, 0, 10),
    "mass_pipi": (10000, 0, 10),
    "mass_pipi_log": (12000, -2, 10),
    "mass_KK": (10000, 0, 10),
    "mass_Kpi": (10000, 0, 10),
    "mass_piK": (10000, 0, 10),
    "mass_ppi": (10000, 0, 10),
    "mass_pip": (10000, 0, 10),
    "mass_pK": (10000, 0, 10),
    "mass_Kp": (10000, 0, 10),
}

#((tracks[i].tk_vx() - vertexs[tracks[i].tk_vtxInd()].x())**2 + (tracks[i].tk_vy() - vertexs[tracks[i].tk_vtxInd()].y())**2)**0.5   if tracks[i].tk_vtxInd()>=0 else 0.0
def dxyTrack(track, vertexs):
    return ((track.tk_vx() - vertexs[track.tk_vtxInd()].x())**2 + (track.tk_vy() - vertexs[track.tk_vtxInd()].y())**2)**0.5   if track.tk_vtxInd()>=0 else 0.0

def trackSelection(track, vertexs):
    # if track.tk_pt()>1.5 and track.tk_ndof()>=10 and track.tk_chi2()/track.tk_ndof()<3: return True
    if track.tk_pt()>2 and track.tk_ndof()>=5 and track.tk_chi2()/track.tk_ndof()<3 and abs(dxyTrack(track,vertexs)/track.tk_dxy_Error())>0: return True
    # if abs(track.tk_dxy()/track.tk_dxy_Error())>60  and track.tk_dxy()>0.2 and track.tk_pt()>1 and track.tk_ndof()>=10 and track.tk_chi2()/track.tk_ndof()<3: return True
    # if abs(track.tk_dxy()/track.tk_dxy_Error())>60  and track.tk_pt()>1 and track.tk_ndof()>=10 and track.tk_chi2()/track.tk_ndof()<3: return True
    return False

# def trackPairSelection(track1, track2):
#     if abs(track1.tk_dz()-track2.tk_dz())>0.3: return False
#     if abs(track1.tk_eta()-track2.tk_eta())>1.5: return False
#     if abs(track1.tk_phi()-track2.tk_phi())>1.5: return False
#     # if track1.tk_charge()==track2.tk_charge(): return False
#     return True 


ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)  
ROOT.gROOT.LoadMacro("myFunction.C+")

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()

triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")

events = Events ([fileName])

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
    "DST_PFScouting_ZeroBias_v1" : 0,
}

### obtained from edmDumpEventContent xxx.root
objectMap = {
    # "triggers" : ("edm::TriggerResults", ("TriggerResults","","HLT")),
    "triggers" :      ("edm::TriggerResults",               ("TriggerResults"            , ""               , "HLT")),
    "tracks" : ("vector<Run3ScoutingTrack>", ("hltScoutingTrackPacker","","HLTX")),
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
    "tracks" :        ("vector<Run3ScoutingTrack>",         ("hltScoutingTrackPacker"    , ""               , "HLT")),
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
track1 = ROOT.TLorentzVector()
track2 = ROOT.TLorentzVector()

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


def fillTriggerResults(event, triggerResults, triggerData):
    names = event.object().triggerNames(triggerData)
    for trigger in triggerResults:
        index = names.triggerIndex(trigger)
        if index>=len(names):
            for name in names: print(name)
            raise Exception("%s not found."%trigger)
        else:
            triggerResults[trigger] = triggerData.accept(index)

def getProduct(handle):
    event.getByLabel(handle.label, handle)
    if not handle.isValid: raise Exception("Problem with %s %s"%(handle, handle.label))
    else: return handle.product()

def getPtEtaPhiMass(partData, mass):
    return (partData.pt(), partData.eta(), partData.phi(), mass)

def getPtEtaPhiMassTrk(partData, mass):
    return (partData.tk_pt(), partData.tk_eta(), partData.tk_phi(), mass)



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

for iev,event in enumerate(events):
    run = event.object().id().run()
    lumi = event.object().id().luminosityBlock()
    eventNumber = event.object().id().event()
    if iev%1000==0: 
        print(iev, run, lumi, eventNumber)
    if iev>maxEvents and maxEvents>0: break
    data["triggers"] = getProduct(handles["triggers"])
    fillTriggerResults(event, triggerResults, data["triggers"])
    if not triggerResults["DST_PFScouting_ZeroBias_v1"]: continue ######### Selecting events with ZeroBias trigger
    # muons = getProduct(handles["muonNoVtxs"])
    # if muons.size()<2: continue ######### Selecting events with at least 2 muons
    # if abs(muons[0].trk_dz()-muons[1].trk_dz())>0.3: continue ######### Selecting events with 2 muons from the same vertex
    # # muon1 = getPtEtaPhiMass(data["muonVtxs"][0], mass_muon)
    # # muon2 = getPtEtaPhiMass(data["muonVtxs"][1], mass_muon)
    # muon1 = getPtEtaPhiMass(muons[0], mass_muon)
    # muon2 = getPtEtaPhiMass(muons[1], mass_muon)
    # invMass = compute_invariant_mass(muon1, muon2)
    # print(invMass, muons[0].trk_dxy(), muons[0].trk_dxy()/muons[0].trk_dxyError(), (muons[0].trk_vx()**2+muons[0].trk_vy()**2)**0.5, ((muons[0].trk_vx()-muons[1].trk_vx())**2+(muons[0].trk_vy()-muons[1].trk_vy())**2)**0.5)
    # hist.Fill(invMass)
    # hist2.Fill(muons[0].trk_dz()-muons[1].trk_dz())
    tracks = getProduct(handles["tracks"])
    vertexs = getProduct(handles["primaryVtxs"])
    count = 0

    goodTracks = []
    for i in range(len(tracks)):
        if trackSelection(tracks[i], vertexs):
            goodTracks.append(i)

    for count, i in enumerate(goodTracks):
        # if not trackSelection(tracks[i]): continue
        # track1 = getPtEtaPhiMassTrk(tracks[i], mass_kaon)
        track1.SetPtEtaPhiM(tracks[i].tk_pt(), tracks[i].tk_eta(), tracks[i].tk_phi(), mass_kaon)
        for j in goodTracks[count+1:]:
            # print(i,j)
            dEta =  tracks[i].tk_eta() - tracks[j].tk_eta()
            dPhi =  ROOT.TVector2.Phi_mpi_pi(tracks[i].tk_phi() - tracks[j].tk_phi())
            dR2 = (dEta**2 + dPhi**2)
            if dR2>1: continue
            dR = dR2**0.5
            dZ = abs(tracks[i].tk_dz()-tracks[j].tk_dz())
            if dZ>0.1: continue
            deltaXY = (tracks[i].tk_vx() - tracks[j].tk_vx())**2 + (tracks[i].tk_vy() - tracks[j].tk_vy())**2
            if deltaXY/max(tracks[i].tk_dxy_Error(),tracks[j].tk_dxy_Error())>3: continue
            # if not trackPairSelection(tracks[i], tracks[j]): continue
            track2.SetPtEtaPhiM(tracks[j].tk_pt(), tracks[j].tk_eta(), tracks[j].tk_phi(), mass_kaon)
            # if not trackSelection(tracks[j]): continue
            # track2 = getPtEtaPhiMassTrk(tracks[j], mass_kaon)
            # invMass = compute_invariant_mass(track1, track2)
            # print(invMass)
            count+=1
            if tracks[i].tk_charge()>0:
                trackP = tracks[i]
                trackN = tracks[j]
            else:
                trackN = tracks[i]
                trackP = tracks[j]
            hist2.Fill(trackP.tk_dz()-trackN.tk_dz())
            ditrack = track1+track2
            hist.Fill(ditrack.M())
            dxy = ((trackP.tk_vx() - vertexs[trackP.tk_vtxInd()].x())**2 + (trackP.tk_vy() - vertexs[trackP.tk_vtxInd()].y())**2)**0.5   if trackP.tk_vtxInd()>=0 else 0.0
            # print(dxy)

            mass_pipi = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_pion), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_pion))
            mass_KK = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_kaon), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_kaon))
            mass_mumu = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_muon), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_muon))
            mass_piK = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_pion), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_kaon))
            mass_Kpi = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_kaon), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_pion))
            mass_ee =  compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_ele), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_ele))
            mass_ppi = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_proton), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_pion))
            mass_pip = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_pion), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_proton))
            mass_pp = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_proton), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_proton))
            mass_pK = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_proton), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_kaon))
            mass_Kp = compute_invariant_mass((trackP.tk_pt(), trackP.tk_eta(), trackP.tk_phi(), mass_kaon), (trackN.tk_pt(), trackN.tk_eta(), trackN.tk_phi(), mass_proton))

            # print(ditrack.M(),mass_pipi, mass_KK, mass_mumu, mass_piK, mass_Kpi)
            # inputs["run"] = run
            # inputs["lumi"] = lumi
            # inputs["pt"] = ditrack.Pt()
            # inputs["eta"] = ditrack.Eta()
            # inputs["phi"] = ditrack.Phi()
            # inputs["charge"] = trackP.tk_charge()+trackN.tk_charge()
            # inputs["dxy"] = dxy / trackP.tk_dxy_Error()
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
                "pt": ditrack.Pt(),
                "eta": ditrack.Eta(),
                "phi": ditrack.Phi(),
                "charge": trackP.tk_charge()+trackN.tk_charge(),
                "dxySig": dxy / trackP.tk_dxy_Error(),
                "dxy": dxy,
                "dz": abs(dZ),
                "deltaR": abs(dR),
                "deltaPhi": abs(dPhi),
                "deltaEta": abs(dEta),
                "mass_ee": mass_ee,
                "mass_mumu": mass_mumu,
                "mass_pipi": mass_pipi,
                "mass_pipi_log": math.log(mass_pipi),
                "mass_KK": mass_KK,
                "mass_Kpi": mass_Kpi,
                "mass_piK": mass_piK,
                "mass_ppi": mass_pip,
                "mass_pip": mass_pip,
                "mass_pK": mass_pK,
                "mass_Kp": mass_Kp,
                }
            ## check goodness of inputs
            if iev==0: checkInputs(axisDef, inputs)
            sparseHisto.Fill(*inputs.values())


            # sparseHisto.Fill(
            #     run,
            #     lumi,
            #     ditrack.Pt(), 
            #     ditrack.Eta(), 
            #     ditrack.Phi(), 
            #     ditrack.M(), 
            #     trackP.tk_charge()+trackN.tk_charge(), 
            #     # trackP.tk_dxy(), 
            #     # trackP.tk_dxy() - (t.tk_vx()**2+t.tk_vx()**2)**0.5 , 
            #     dxy / trackP.tk_dxy_Error(), 
            #     abs(dZ),
            #     abs(dR),
            #     abs(dEta),
            #     abs(dPhi),
            #     mass_pipi,
            #     mass_mumu,
            #     mass_ee,
            #     math.log(mass_pipi),
            #     mass_Kpi,
            #     mass_ppi,
            #     mass_pip,
            #     mass_pK,
            # )
    # "run": (500000, 0, 500000),
    # "lumi": (10000, 0, 10000),
    # "pt": (150, 0, 15),
    # "eta": (200, -2.5, 2.5),
    # "phi": (200, -3.15, 3.15),
    # "charge": (19, -9.5, +9.5),
    # "dxy": (100, 0, 5),
    # "dz": (100, 0, 0.5),
    # "deltaR": (400, 0, 4.0),
    # "deltaPhi": (400, 0, 4.0),
    # "deltaEta": (400, 0, 4.0),
    # "mass_ee": (10000, 0, 10),
    # "mass_mumu": (10000, 0, 10),
    # "mass_pipi": (10000, 0, 10),
    # "mass_pipi_log": (12000, -2, 10),
    # "mass_KK": (10000, 0, 10),
    # "mass_Kpi": (10000, 0, 10),
    # "mass_piK": (10000, 0, 10),
    # "mass_ppi": (10000, 0, 10),
    # "mass_pip": (10000, 0, 10),
    # "mass_pK": (10000, 0, 10),
    # "mass_Kp": (10000, 0, 10),
    # print(count)
    if count>10:
        pass
        # break
    
    # if tracks.size()<2: continue ######### Selecting events with at least 2 tracks
    # if abs(tracks[0].trk_dz()-tracks[1].trk_dz())>0.3: continue ######### Selecting events with 2 tracks from the same vertex
    # # track1 = getPtEtaPhiMass(data["muonVtxs"][0], mass_muon)
    # # track2 = getPtEtaPhiMass(data["muonVtxs"][1], mass_muon)
    # track1 = getPtEtaPhiMass(tracks[0], mass_muon)
    # track2 = getPtEtaPhiMass(tracks[1], mass_muon)
    # invMass = compute_invariant_mass(track1, track2)
    # print(invMass)
    # hist.Fill(invMass)
    # hist2.Fill(tracks[0].trk_dz()-tracks[1].trk_dz())

outFile = ROOT.TFile("sparseHisto.root", "RECREATE")
outFile.cd()
sparseHisto.Write()
outFile.Write()
outFile.Close()

1/0
plotDefs = { ## plot name: (variable , selection)
    "eta-1" : ( "eta" , {
            "phi" : [0, 2.5]
        }),
    "eta-2" : ( "eta" ,{
            "phi" : [-2.5, 0]
        }),
    "eta-3" : ( "eta" ,{
            "pt" : [5, 100]
        }),
}

def makePlot(sparseHisto, plotDef):
    varPlot, selection = plotDef
    for varSel in selection:
        (xmin, xmax) = selection[varSel]
        print(varPlot, varSel, xmin, xmax)
        ax = sparseHisto.GetAxis(variables.index(varSel))
        ax.SetRange(ax.FindBin(xmin), ax.FindBin(xmax))
    histo = sparseHisto.Projection(variables.index(varPlot))
    ## revert changes
    for varSel in selection:
        ax = sparseHisto.GetAxis(variables.index(varSel))
        ax.SetRange()
    return histo


plots = {}
for plotName in plotDefs:
    plotDef = plotDefs[plotName]
    plots[plotName] = makePlot(sparseHisto, plotDef)       

canvas = ROOT.TCanvas("canvas", "canvas", 800, 800)
plots["eta-3"].Draw()
canvas.SaveAs("eta-3.png")

1/0

canvas = ROOT.TCanvas("canvas", "canvas", 800, 800)
hist.Draw()
canvas.SaveAs("invMass.png")
hist2.Draw()
canvas.SaveAs("dZ.png")

    # for object in objectMap:
    #     if object=="triggers": continue
    #     if object=="muonVtxs": continue
    #     data[object] = getProduct(handles[object])
    # print(data["muonVtxs"].size())

# # trigger = "DST_PFScouting_ZeroBias"
# triggerDen = "DST_PFScouting_JetHT"
# preselection = "%s"%triggerDen

# triggerNum = "DST_PFScouting_DoubleMuon"
# varY = triggerNum

# name = "%s_Vs_MuonVtx_Eta2p0"%triggerNum
# varX = "Sum$(selectNobject(ScoutingMuonVtx_pt, abs(ScoutingMuonVtx_eta)<2.0, 1, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "%s_Vs_MuonVtx_Eta1p4"%triggerNum
# varX = "Sum$(selectNobject(ScoutingMuonVtx_pt, abs(ScoutingMuonVtx_eta)<1.4, 1, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)


# name = "%s_Vs_MuonNoVtx_Eta2p0"%triggerNum
# varX = "Sum$(selectNobject(ScoutingMuonNoVtx_pt, abs(ScoutingMuonNoVtx_eta)<2.0, 1, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "%s_Vs_MuonNoVtx_Eta1p4"%triggerNum
# varX = "Sum$(selectNobject(ScoutingMuonNoVtx_pt, abs(ScoutingMuonNoVtx_eta)<1.4, 1, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# ################################

# triggerDen = "DST_PFScouting_JetHT"
# preselection = "%s"%triggerDen

# triggerNum = "DST_PFScouting_DoubleEG"
# varY = triggerNum

# name = "%s_Vs_Electron_Eta1p5"%triggerNum
# varX = "Sum$(selectNobject(ScoutingElectron_pt, abs(ScoutingElectron_eta)<1.5, 1, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "%s_Vs_Photon_Eta1p5"%triggerNum
# varX = "Sum$(selectNobject(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.5, 1, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "%s_Vs_Electron_Eta1p5_WithTrkIso"%triggerNum
# varX = "Sum$(selectNobject(ScoutingElectron_pt, abs(ScoutingElectron_eta)<1.5 && ScoutingElectron_trackIso!=0, 1, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)


# ################################ 
# # DST_PFScouting_SingleMuon
# # DST_PFScouting_JetHT


# triggerDen = "DST_PFScouting_DoubleMuon"
# preselection = "%s"%triggerDen

# triggerNum = "DST_PFScouting_JetHT"
# varY = triggerNum

# name = "%s_Vs_HT2p4"%triggerNum
# varX = "Sum$(ScoutingJet_pt * (abs(ScoutingJet_eta)<2.4))"
# events.Draw("%s:%s >> %s(50,0,1000,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "%s_Vs_HT3p0"%triggerNum
# varX = "Sum$(ScoutingJet_pt * (abs(ScoutingJet_eta)<3.0))"
# events.Draw("%s:%s >> %s(50,0,1000,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "%s_Vs_HT5p0"%triggerNum
# varX = "Sum$(ScoutingJet_pt * (abs(ScoutingJet_eta)<5.0))"
# events.Draw("%s:%s >> %s(50,0,1000,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# ################################


# triggerDen = "DST_PFScouting_JetHT"
# preselection = "%s"%triggerDen

# triggerNum = "DST_PFScouting_SingleMuon"
# varY = triggerNum

# name = "%s_Vs_MuonVtx_Eta0p8"%triggerNum
# varX = "Sum$(selectNobject(ScoutingMuonVtx_pt, abs(ScoutingMuonVtx_eta)<0.8, 0, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "%s_Vs_MuonVtx_Eta1p6"%triggerNum
# varX = "Sum$(selectNobject(ScoutingMuonVtx_pt, abs(ScoutingMuonVtx_eta)<1.6, 0, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "%s_Vs_MuonNoVtx_Eta0p8"%triggerNum
# varX = "Sum$(selectNobject(ScoutingMuonNoVtx_pt, abs(ScoutingMuonNoVtx_eta)<0.8, 0, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "%s_Vs_MuonVNotx_Eta1p6"%triggerNum
# varX = "Sum$(selectNobject(ScoutingMuonNoVtx_pt, abs(ScoutingMuonNoVtx_eta)<1.6, 0, Iteration$, Length$))"
# events.Draw("%s:%s >> %s(40,0,40,40,0,40)"%(varY, varX, name),"(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)
# 1/0

# name = "DST_PFScouting_DoubleMuonVsMuonNoVtx"
# events.Draw("DST_PFScouting_DoubleMuon:MaxIf$(ScoutingMuonNoVtx_pt,ScoutingMuonNoVtx_pt!=Max$(ScoutingMuonNoVtx_pt)) >> Muon2d(40,0,40,40,0,40)","(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "L1_DoubleMu0_SQVsMuonVtx"
# events.Draw("L1_DoubleMu0_SQ:MaxIf$(ScoutingMuonVtx_pt,ScoutingMuonVtx_pt!=Max$(ScoutingMuonVtx_pt)) >> Muon2d(40,0,40,40,0,40)","(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "L1_DoubleMu0_SQVsMuonNoVtx"
# events.Draw("L1_DoubleMu0_SQ:MaxIf$(ScoutingMuonNoVtx_pt,ScoutingMuonNoVtx_pt!=Max$(ScoutingMuonNoVtx_pt))","(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "L1_DoubleMu0_SQ_OSVsMuonVtx"
# events.Draw("L1_DoubleMu0_SQ:MaxIf$(ScoutingMuonVtx_pt,ScoutingMuonVtx_pt!=Max$(ScoutingMuonVtx_pt)) >> Muon2d(40,0,40,40,0,40)","(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)

# name = "L1_DoubleMu0_SQ_OSVsMuonNoVtx"
# events.Draw("L1_DoubleMu0_SQ:MaxIf$(ScoutingMuonNoVtx_pt,ScoutingMuonNoVtx_pt!=Max$(ScoutingMuonNoVtx_pt))","(%s)"%preselection,"prof")
# canvas.SaveAs("%s_eff.png"%name)


# # name = "EG_vs_Photon"
# # nameCut = "EG"
# # # events.Draw("MaxIf$(L1EG_pt, abs(L1EG_eta)<1.6)>10:MaxIf$(ScoutingElectron_pt, abs(ScoutingElectron_eta)<1.6) >> aaa(40,0,40,40,0,40)","","prof")
# # events.Draw("MaxIf$(L1EG_pt, abs(L1EG_eta)<1.6):MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6) >> photon2d(40,0,40,40,0,40)","MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)>0","COLZ")
# # canvas.SaveAs("%s_2D.png"%name)
# # photon2d = ROOT.gDirectory.Get("photon2d").Clone("photon2d")
# # make1Dplots(photon2d, cuts)


# # name = "EG_vs_Electron"
# # nameCut = "EG"
# # # events.Draw("MaxIf$(L1EG_pt, abs(L1EG_eta)<1.6)>10:MaxIf$(ScoutingElectron_pt, abs(ScoutingElectron_eta)<1.6) >> aaa(40,0,40,40,0,40)","","prof")
# # events.Draw("MaxIf$(L1EG_pt, abs(L1EG_eta)<1.6):MaxIf$(ScoutingElectron_pt, abs(ScoutingElectron_eta)<1.6) >> electron2d(40,0,40,40,0,40)","MaxIf$(ScoutingElectron_pt, abs(ScoutingElectron_eta)<1.6)>0","COLZ")
# # canvas.SaveAs("%s_2D.png"%name)
# # electron2d = ROOT.gDirectory.Get("electron2d").Clone("electron2d")
# # make1Dplots(electron2d, cuts)

# # name = "MuonVtx"
# # nameCut = "Muon"
# # events.Draw("MaxIf$(L1Mu_pt, abs(L1Mu_eta)<1.6):MaxIf$(ScoutingMuonVtx_pt, abs(ScoutingMuonVtx_eta)<1.6) >> Muon2d(40,0,40,40,0,40)","MaxIf$(ScoutingMuonVtx_pt, abs(ScoutingMuonVtx_eta)<1.6)>0","COLZ")
# # canvas.SaveAs("%s_2D.png"%name)
# # Muon2d = ROOT.gDirectory.Get("Muon2d").Clone("Muon2d")
# # make1Dplots(Muon2d, cuts)

# # name = "MuonNoVtx"
# # nameCut = "Muon_ptUnconstrained"
# # events.Draw("MaxIf$(L1Mu_ptUnconstrained, abs(L1Mu_eta)<1.6):MaxIf$(ScoutingMuonNoVtx_pt, abs(ScoutingMuonNoVtx_eta)<1.6) >> Muon2dNoVtx(40,0,40,40,0,40)","MaxIf$(ScoutingMuonNoVtx_pt, abs(ScoutingMuonNoVtx_eta)<1.6)>0","COLZ")
# # canvas.SaveAs("%s_2D.png"%name)
# # Muon2d = ROOT.gDirectory.Get("Muon2dNoVtx").Clone("Muon2dNoVtx")
# # make1Dplots(Muon2d, cuts)

# cuts = {
#     30:ROOT.kRed, 
#     50:ROOT.kBlue, 
#     70:ROOT.kGreen, 
#     100:ROOT.kMagenta,
#     150:ROOT.kBlack,
# }

# # name = "PFJet"
# # nameCut = "Jet_vs_ScoutingPFJet"
# # events.Draw("MaxIf$(L1Jet_pt, abs(L1Jet_eta)<1.6):MaxIf$(ScoutingPFJet_pt, abs(ScoutingPFJet_eta)<1.6) >> Jet2D(40,0,200,40,0,200)","MaxIf$(ScoutingPFJet_pt, abs(ScoutingPFJet_eta)<1.6)>0","COLZ")
# # canvas.SaveAs("%s_2D.png"%name)
# # Jet2D = ROOT.gDirectory.Get("Jet2D").Clone("Jet2D")
# # make1Dplots(Jet2D, cuts)

# # name = "PFJetRec"
# # nameCut = "Jet_vs_ScoutingPFJetRecluster_pt"
# # events.Draw("MaxIf$(L1Jet_pt, abs(L1Jet_eta)<1.6):MaxIf$(ScoutingPFJetRecluster_pt, abs(ScoutingPFJetRecluster_eta)<1.6) >> Jet2DRec(40,0,200,40,0,200)","MaxIf$(ScoutingPFJetRecluster_pt, abs(ScoutingPFJetRecluster_eta)<1.6)>0","COLZ")
# # canvas.SaveAs("%s_2D.png"%name)
# # Jet2DRec = ROOT.gDirectory.Get("Jet2DRec").Clone("Jet2DRec")
# # make1Dplots(Jet2DRec, cuts)

# # name = "JetCHS"
# # nameCut = "Jet_vs_ScoutingCHSJetRecluster_pt"
# # events.Draw("MaxIf$(L1Jet_pt, abs(L1Jet_eta)<1.6):MaxIf$(ScoutingCHSJetRecluster_pt, abs(ScoutingCHSJetRecluster_eta)<1.6) >> Jet2DCHS(40,0,200,40,0,200)","MaxIf$(ScoutingCHSJetRecluster_pt, abs(ScoutingCHSJetRecluster_eta)<1.6)>0","COLZ")
# # canvas.SaveAs("%s_2D.png"%name)
# # Jet2DCHS = ROOT.gDirectory.Get("Jet2DCHS").Clone("Jet2DCHS")
# # make1Dplots(Jet2DCHS, cuts)

# # name = "JetPhoton"
# # nameCut = "Jet_vs_ScoutingPhoton"
# # events.Draw("MaxIf$(ScoutingPFJet_pt, abs(ScoutingPFJet_eta)<1.6):MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6) >> JetPhoton2D(40,0,200,40,0,200)","MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)>0 && (MaxIf$(ScoutingPFJet_pt, abs(ScoutingPFJet_eta)<1.6)/Sum$(ScoutingPFJet_pt))>0.3 ","COLZ")
# # canvas.SaveAs("%s_2D.png"%name)
# # JetPhoton2D = ROOT.gDirectory.Get("JetPhoton2D").Clone("JetPhoton2D")
# # make1Dplots(JetPhoton2D, cuts)



# 1/0

# plot2d.ProjectionX().Draw()


# events.Draw("MaxIf$(L1EG_pt, abs(L1EG_eta)<1.6)>10:MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)  >> a1(40,0,40,40,0,40)","MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)>0","prof")
# events.Draw("MaxIf$(L1EG_pt, abs(L1EG_eta)<1.6)>20:MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)  >> a2(40,0,40,40,0,40)","MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)>0","prof")
# events.Draw("MaxIf$(L1EG_pt, abs(L1EG_eta)<1.6)>30:MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)  >> a3(40,0,40,40,0,40)","MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)>0","prof")
# events.Draw("MaxIf$(L1EG_pt, abs(L1EG_eta)<1.6)>40:MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)  >> a4(40,0,40,40,0,40)","MaxIf$(ScoutingPhoton_pt, abs(ScoutingPhoton_eta)<1.6)>0","prof")

# a1 = ROOT.gDirectory.Get("a1")
# a2 = ROOT.gDirectory.Get("a2")
# a3 = ROOT.gDirectory.Get("a3")
# a4 = ROOT.gDirectory.Get("a4")

# a1.SetLineColor(ROOT.kRed)
# a2.SetLineColor(ROOT.kBlue)
# a3.SetLineColor(ROOT.kGreen)
# a4.SetLineColor(ROOT.kMagenta)

# a1.Draw()
# a2.Draw("same")
# a3.Draw("same")
# a4.Draw("same")

# canvas.SaveAs("EG_vs_Photon_1D.png")

# # events.Draw("Max$(L1Jet_pt[0])>30:ScoutingPFJet_pt[0] >> aaa(100,0,200,100,0,200)","","prof")
# # events.Draw("Max$(L1Mu_pt):Max$(ScoutingMuonVtx_pt) >> aaa(100,100,0,40,0,40)","","COLZ")
# # events.Draw("Max$(L1Jet_pt[0])>30:ScoutingPFJet_pt[0] >> aaa(100,0,200,100,0,200)","","prof")


# for ev in events:
#     print(ev.run, ev.luminosityBlock, ev.event)
#     break

# # ScoutingMET_pt
# # ScoutingRawCHSMETRecluster_pt
# # ScoutingRawCHSMETRecluster_sumEt
