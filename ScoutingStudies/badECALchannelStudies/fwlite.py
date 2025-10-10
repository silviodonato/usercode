import ROOT
import os, sys

## ls -1 out_ECAL_*.root
fileList = []
for f in os.listdir("."):
    if f.startswith("out_ECAL_") and f.endswith(".root"):
        fileList.append(f)
# fileList = [
# "out_ECAL_no.root",
# "out_ECAL_noNoisy_.root",
# "out_ECAL_noNoisy_FixedG1_.root",
# "out_ECAL_noNoisy_FixedG1_DeadVFE_.root",
# "out_ECAL_noNoisy_FixedG1_DeadVFE_NoDataNoTP_.root",
# "out_ECAL_noNoisy_FixedG1_DeadVFE_NoDataNoTP_NonRespondingIsolated_.root",
# "out_ECAL_noNoisy_FixedG1_DeadVFE_NoDataNoTP_NonRespondingIsolated_DAC_.root",
# "out_ECAL_noNoisy_FixedG1_DeadVFE_NoDataNoTP_NonRespondingIsolated_DAC_FixedG6_.root",
# "out_ECAL_noNoisy_FixedG1_DeadVFE_NoDataNoTP_NonRespondingIsolated_DAC_FixedG6_FixedG0_.root",
# "out_ECAL_noNoisy_FixedG1_DeadVFE_NoDataNoTP_NonRespondingIsolated_DAC_FixedG6_FixedG0_DeadFE_.root",
# "out_ECAL_noNoisy_FixedG1_DeadVFE_NoDataNoTP_NonRespondingIsolated_DAC_FixedG6_FixedG0_DeadFE_NNoisy_.root"
# ]

fileList = list(sorted(fileList))
from pprint import pprint
pprint("Files to be processed: ")
pprint(fileList)

branches = [
"Run3ScoutingEERecHits_hltScoutingRecHitPacker_EE_HLTX.obj",
"Run3ScoutingEERecHits_hltScoutingRecHitPacker_EECleaned_HLTX.obj",
"Run3ScoutingEBRecHits_hltScoutingRecHitPacker_EB_HLTX.obj",
"Run3ScoutingEBRecHits_hltScoutingRecHitPacker_EBCleaned_HLTX.obj",
]

graphs = {}
for branch in branches:
    graphs[branch] = ROOT.TGraph(len(fileList))

# MET graphs - only one per type since branches don't affect MET
graphMET = ROOT.TGraph(len(fileList))
graphMET_withZ = ROOT.TGraph(len(fileList))
graphMET_withW = ROOT.TGraph(len(fileList))

for fName in fileList:
#fName  = fileList[0]
    file_ = ROOT.TFile.Open(fName)

    from DataFormats.FWLite import Handle, Events

    events = Events (file_)
    if events.size() < 1000:
        print("File ", fName, " is empty! ")
        continue
    for ievt,event in enumerate(events): 
        if ievt>=1:
            break

#    1/0
    scoutingMETLabel = ("hltScoutingPFPacker:pfMetPt:HLTX")
    scoutingMET = Handle("double")
    scoutingMETphi = Handle("double")
    scoutingMETphiLabel = ("hltScoutingPFPacker:pfMetPhi:HLTX")
    scoutingMuonLabel = ("hltScoutingMuonPackerVtx::HLTX")
    scoutingMuon = Handle("std::vector<Run3ScoutingMuon>")
    scoutingPhotonLabel = ("hltScoutingEgammaPacker::HLTX")
    scoutingPhoton = Handle("std::vector<Run3ScoutingPhoton>")

    events.getByLabel(scoutingMETLabel, scoutingMET)
    events.getByLabel(scoutingMETphiLabel, scoutingMETphi)

    met = scoutingMET.product()[0]
    met_phi = scoutingMETphi.product()[0]
#    print("MET: ", met, " phi: ", met_phi)


    MET_plot = ROOT.TH1F("MET", "MET", 100, 0, 200)
    MET_plot_withZ = ROOT.TH1F("MET_withZ", "MET with Z selection", 100, 0, 200)
    MET_plot_withW = ROOT.TH1F("MET_withW", "MET with W selection", 100, 0, 200)
    
    # Z selection plots
    DimuonMass_plot = ROOT.TH1F("DimuonMass", "Dimuon Mass (Z selection)", 100, 50, 130)
    DimuonMass_plot.GetXaxis().SetTitle("M_{#mu#mu} [GeV]")
    DimuonMass_plot.GetYaxis().SetTitle("Events")
    
    MuonPt1_Z_plot = ROOT.TH1F("MuonPt1_Z", "Leading Muon p_{T} (Z selection)", 100, 0, 200)
    MuonPt1_Z_plot.GetXaxis().SetTitle("p_{T}^{#mu1} [GeV]")
    MuonPt1_Z_plot.GetYaxis().SetTitle("Events")
    
    MuonPt2_Z_plot = ROOT.TH1F("MuonPt2_Z", "Subleading Muon p_{T} (Z selection)", 100, 0, 200)
    MuonPt2_Z_plot.GetXaxis().SetTitle("p_{T}^{#mu2} [GeV]")
    MuonPt2_Z_plot.GetYaxis().SetTitle("Events")
    
    # W selection plots
    MuonPt_W_plot = ROOT.TH1F("MuonPt_W", "Muon p_{T} (W selection)", 100, 0, 100)
    MuonPt_W_plot.GetXaxis().SetTitle("p_{T}^{#mu} [GeV]")
    MuonPt_W_plot.GetYaxis().SetTitle("Events")
    
    TransverseMass_W_plot = ROOT.TH1F("TransverseMass_W", "Transverse Mass (W selection)", 100, 0, 150)
    TransverseMass_W_plot.GetXaxis().SetTitle("M_{T} [GeV]")
    TransverseMass_W_plot.GetYaxis().SetTitle("Events")
    
    # Photon plots
    PhotonEta_plot = ROOT.TH1F("PhotonEta", "Photon #eta", 100, -3, 3)
    PhotonEta_plot.GetXaxis().SetTitle("#eta")
    PhotonEta_plot.GetYaxis().SetTitle("Photons")
    
    PhotonPhi_plot = ROOT.TH1F("PhotonPhi", "Photon #phi", 100, -3.2, 3.2)
    PhotonPhi_plot.GetXaxis().SetTitle("#phi")
    PhotonPhi_plot.GetYaxis().SetTitle("Photons")
    
    PhotonEtaPhi_plot = ROOT.TH2F("PhotonEtaPhi", "Photon #eta vs #phi", 100, -3, 3, 100, -3.2, 3.2)
    PhotonEtaPhi_plot.GetXaxis().SetTitle("#eta")
    PhotonEtaPhi_plot.GetYaxis().SetTitle("#phi")
    
    # Function to check if muon is isolated and prompt
    def isGoodMuon(muon):
        # Normalized Chi2 < 10
        if muon.normalizedChi2() >= 10:
            return False
        # Track dxy < 0.2
        if abs(muon.trk_dxy()) >= 0.2:
            return False
        # Track dz < 0.5
        if abs(muon.trk_dz()) >= 0.5:
            return False
        # Isolation: (Track Iso + Ecal Iso + Hcal Iso) / muon_pt < 0.15
        rel_iso = (muon.trackIso() + muon.ecalIso() + muon.hcalIso()) / muon.pt()
        if rel_iso >= 0.15:
            return False
        return True
    
    for ev in events:
        ev.getByLabel(scoutingMETLabel, scoutingMET)
        ev.getByLabel(scoutingMuonLabel, scoutingMuon)
        ev.getByLabel(scoutingPhotonLabel, scoutingPhoton)
        met = scoutingMET.product()[0]
        
        # Fill MET plot without selection
        MET_plot.Fill(met)
        
        # Fill photon plots
        photons = scoutingPhoton.product()
        for photon in photons:
            PhotonEta_plot.Fill(photon.eta())
            PhotonPhi_plot.Fill(photon.phi())
            PhotonEtaPhi_plot.Fill(photon.eta(), photon.phi())
        
        # Get muons
        muons = scoutingMuon.product()
        
        # W boson selection: exactly 1 muon with pT 30-40 GeV, no other muons with pT > 5 GeV
        found_w = False
        w_muon = None
        if len(muons) >= 1:
            n_muons_30_40 = 0
            n_muons_above_5 = 0
            for muon in muons:
                # Apply muon quality and isolation cuts
                if not isGoodMuon(muon):
                    continue
                    
                if 30 < muon.pt() < 40:
                    n_muons_30_40 += 1
                    w_muon = muon
                if muon.pt() > 5:
                    n_muons_above_5 += 1
            
            # Require exactly 1 muon in 30-40 GeV range and exactly 1 muon above 5 GeV (the same one)
            if n_muons_30_40 == 1 and n_muons_above_5 == 1:
                found_w = True
        
        if found_w:
            MET_plot_withW.Fill(met)
            MuonPt_W_plot.Fill(w_muon.pt())
            
            # Calculate transverse mass: MT = sqrt(2 * pT_mu * MET * (1 - cos(dphi)))
            ev.getByLabel(scoutingMETphiLabel, scoutingMETphi)
            met_phi = scoutingMETphi.product()[0]
            dphi = abs(w_muon.phi() - met_phi)
            if dphi > ROOT.TMath.Pi():
                dphi = 2 * ROOT.TMath.Pi() - dphi
            transverse_mass = ROOT.TMath.Sqrt(2 * w_muon.pt() * met * (1 - ROOT.TMath.Cos(dphi)))
            TransverseMass_W_plot.Fill(transverse_mass)
        
        # Z boson selection: two muons with opposite charge and mass compatible with Z boson
        if len(muons) < 2:
            continue
        
        # Find opposite-sign muon pairs compatible with Z mass
        found_z = False
        best_dimuon_mass = 0
        z_muon1_idx = -1
        z_muon2_idx = -1
        for i in range(len(muons)):
            # Apply muon quality and isolation cuts
            if not isGoodMuon(muons[i]):
                continue
                
            for j in range(i+1, len(muons)):
                # Apply muon quality and isolation cuts
                if not isGoodMuon(muons[j]):
                    continue
                    
                if muons[i].charge() * muons[j].charge() < 0:  # opposite charge
                    # Calculate invariant mass
                    mu1 = ROOT.TLorentzVector()
                    mu2 = ROOT.TLorentzVector()
                    mu1.SetPtEtaPhiM(muons[i].pt(), muons[i].eta(), muons[i].phi(), 0.1057)  # muon mass in GeV
                    mu2.SetPtEtaPhiM(muons[j].pt(), muons[j].eta(), muons[j].phi(), 0.1057)
                    dimuon_mass = (mu1 + mu2).M()
                    # Z boson mass window: 60-120 GeV
                    if 60 < dimuon_mass < 120:
                        found_z = True
                        best_dimuon_mass = dimuon_mass
                        z_muon1_idx = i
                        z_muon2_idx = j
                        break
            if found_z:
                break
        
        if found_z:
            MET_plot_withZ.Fill(met)
            DimuonMass_plot.Fill(best_dimuon_mass)
            
            # Fill muon pT plots (leading and subleading)
            pt1 = max(muons[z_muon1_idx].pt(), muons[z_muon2_idx].pt())
            pt2 = min(muons[z_muon1_idx].pt(), muons[z_muon2_idx].pt())
            MuonPt1_Z_plot.Fill(pt1)
            MuonPt2_Z_plot.Fill(pt2)

    #c1 = ROOT.TCanvas()
    MET_plot.Draw()
    #c1.SaveAs("MET.png")
    #c1.SaveAs("MET.root")

    print(" MET mean: ", MET_plot.GetMean(), " RMS: ", MET_plot.GetRMS(), "fName=", fName, )
    print(" MET (with Z) mean: ", MET_plot_withZ.GetMean(), " RMS: ", MET_plot_withZ.GetRMS(), " entries: ", MET_plot_withZ.GetEntries(), "fName=", fName, )
    print(" MET (with W) mean: ", MET_plot_withW.GetMean(), " RMS: ", MET_plot_withW.GetRMS(), " entries: ", MET_plot_withW.GetEntries(), "fName=", fName, )

    for branch in branches:
        print("Size: ", file_.Get("Events").GetBranch(branch).GetZipBytes("*"), " bytes. Branch: ", branch)
        graphs[branch].SetPoint(fileList.index(fName), fileList.index(fName), float(file_.Get("Events").GetBranch(branch).GetZipBytes("*")))
    
    # Set MET values once per file (not per branch)
    graphMET.SetPoint(fileList.index(fName), fileList.index(fName), MET_plot.GetMean())
    graphMET_withZ.SetPoint(fileList.index(fName), fileList.index(fName), MET_plot_withZ.GetMean())
    graphMET_withW.SetPoint(fileList.index(fName), fileList.index(fName), MET_plot_withW.GetMean())


ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)
c1 = ROOT.TCanvas("c1","c1",1280,800)
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kBlack, ROOT.kMagenta, ROOT.kCyan+2]
min_, max_ = 1e9, -1e9
for g in graphs.values():
    for y in g.GetY():
        if y < min_:
            min_ = y
        if y > max_:
            max_ = y
for branch in branches:
    graphs[branch].SetTitle(branch)
    graphs[branch].SetMarkerColor(colors[branches.index(branch)])
    graphs[branch].SetLineColor(colors[branches.index(branch)])
    graphs[branch].GetXaxis().SetTitle("Config")
    graphs[branch].GetYaxis().SetTitle("Size [bytes]")
    graphs[branch].SetMarkerStyle(20+branches.index(branch))
    graphs[branch].SetMarkerColor(1+branches.index(branch))
    graphs[branch].SetLineColor(1+branches.index(branch))
    if branch==branches[0]:
        graphs[branch].SetMinimum(0.8*min_)
        graphs[branch].SetMaximum(1.2*max_)
        graphs[branch].Draw("APL")
    else:
        graphs[branch].Draw("PL")
c1.SetLogy()
c1.BuildLegend()
c1.SaveAs("size_vs_config.png")
c1.SaveAs("size_vs_config.root")

# Plot MET without Z selection
c2 = ROOT.TCanvas()
graphMET.SetTitle("MET (no selection)")
graphMET.SetMarkerColor(ROOT.kBlue)
graphMET.SetLineColor(ROOT.kBlue)
graphMET.GetXaxis().SetTitle("Config")
graphMET.GetYaxis().SetTitle("MET mean [GeV]")
graphMET.SetMarkerStyle(20)
graphMET.Draw("APL")
c2.BuildLegend()
c2.SaveAs("MET_vs_config.png")
c2.SaveAs("MET_vs_config.root")

# Plot MET with Z selection
c3 = ROOT.TCanvas()
graphMET_withZ.SetTitle("MET (with Z selection)")
graphMET_withZ.SetMarkerColor(ROOT.kRed)
graphMET_withZ.SetLineColor(ROOT.kRed)
graphMET_withZ.GetXaxis().SetTitle("Config")
graphMET_withZ.GetYaxis().SetTitle("MET mean [GeV] (with Z)")
graphMET_withZ.SetMarkerStyle(21)
graphMET_withZ.Draw("APL")
c3.BuildLegend()
c3.SaveAs("MET_withZ_vs_config.png")
c3.SaveAs("MET_withZ_vs_config.root")

min_, max_ = 1e9, -1e9
for g in [graphMET, graphMET_withZ, graphMET_withW]:
    for y in g.GetY():
        if y < min_:
            min_ = y
        if y > max_:
            max_ = y
# Plot both MET graphs together for comparison
c4 = ROOT.TCanvas()
graphMET.SetTitle("MET (no selection)")
graphMET.SetMinimum(0.8*min_)
graphMET.SetMaximum(1.2*max_)
graphMET.Draw("APL")
graphMET_withZ.SetTitle("MET (with Z selection)")
graphMET_withZ.Draw("PL same")
graphMET_withW.SetTitle("MET (with W selection)")
graphMET_withW.SetMarkerColor(ROOT.kGreen+2)
graphMET_withW.SetLineColor(ROOT.kGreen+2)
graphMET_withW.SetMarkerStyle(22)
graphMET_withW.Draw("PL same")
c4.BuildLegend()
c4.SaveAs("MET_comparison.png")
c4.SaveAs("MET_comparison.root")

# Plot MET with W selection
c6 = ROOT.TCanvas()
graphMET_withW.SetTitle("MET (with W selection)")
graphMET_withW.SetMarkerColor(ROOT.kGreen+2)
graphMET_withW.SetLineColor(ROOT.kGreen+2)
graphMET_withW.GetXaxis().SetTitle("Config")
graphMET_withW.GetYaxis().SetTitle("MET mean [GeV] (with W)")
graphMET_withW.SetMarkerStyle(22)
graphMET_withW.Draw("APL")
c6.BuildLegend()
c6.SaveAs("MET_withW_vs_config.png")
c6.SaveAs("MET_withW_vs_config.root")

# Plot dimuon mass distribution for Z candidates
c5 = ROOT.TCanvas()
DimuonMass_plot.SetLineColor(ROOT.kBlue)
DimuonMass_plot.SetLineWidth(2)
DimuonMass_plot.SetFillColor(ROOT.kBlue)
DimuonMass_plot.SetFillStyle(3004)
DimuonMass_plot.Draw("HIST")
# Add a line at the Z mass
line_z = ROOT.TLine(91.2, 0, 91.2, DimuonMass_plot.GetMaximum())
line_z.SetLineColor(ROOT.kRed)
line_z.SetLineWidth(2)
line_z.SetLineStyle(2)
line_z.Draw("same")
c5.SaveAs("DimuonMass_Zselection.png")
c5.SaveAs("DimuonMass_Zselection.root")

# Plot leading muon pT for Z selection
c7 = ROOT.TCanvas()
MuonPt1_Z_plot.SetLineColor(ROOT.kBlue)
MuonPt1_Z_plot.SetLineWidth(2)
MuonPt1_Z_plot.SetFillColor(ROOT.kBlue)
MuonPt1_Z_plot.SetFillStyle(3004)
MuonPt1_Z_plot.Draw("HIST")
c7.SaveAs("MuonPt1_Zselection.png")
c7.SaveAs("MuonPt1_Zselection.root")

# Plot subleading muon pT for Z selection
c8 = ROOT.TCanvas()
MuonPt2_Z_plot.SetLineColor(ROOT.kGreen+2)
MuonPt2_Z_plot.SetLineWidth(2)
MuonPt2_Z_plot.SetFillColor(ROOT.kGreen+2)
MuonPt2_Z_plot.SetFillStyle(3004)
MuonPt2_Z_plot.Draw("HIST")
c8.SaveAs("MuonPt2_Zselection.png")
c8.SaveAs("MuonPt2_Zselection.root")

# Plot muon pT for W selection
c9 = ROOT.TCanvas()
MuonPt_W_plot.SetLineColor(ROOT.kRed)
MuonPt_W_plot.SetLineWidth(2)
MuonPt_W_plot.SetFillColor(ROOT.kRed)
MuonPt_W_plot.SetFillStyle(3004)
MuonPt_W_plot.Draw("HIST")
c9.SaveAs("MuonPt_Wselection.png")
c9.SaveAs("MuonPt_Wselection.root")

# Plot transverse mass for W selection
c10 = ROOT.TCanvas()
TransverseMass_W_plot.SetLineColor(ROOT.kMagenta)
TransverseMass_W_plot.SetLineWidth(2)
TransverseMass_W_plot.SetFillColor(ROOT.kMagenta)
TransverseMass_W_plot.SetFillStyle(3004)
TransverseMass_W_plot.Draw("HIST")
# Add a line at the W mass
line_w = ROOT.TLine(80.4, 0, 80.4, TransverseMass_W_plot.GetMaximum())
line_w.SetLineColor(ROOT.kRed)
line_w.SetLineWidth(2)
line_w.SetLineStyle(2)
line_w.Draw("same")
c10.SaveAs("TransverseMass_Wselection.png")
c10.SaveAs("TransverseMass_Wselection.root")

# Plot photon eta
c11 = ROOT.TCanvas()
PhotonEta_plot.SetLineColor(ROOT.kOrange)
PhotonEta_plot.SetLineWidth(2)
PhotonEta_plot.SetFillColor(ROOT.kOrange)
PhotonEta_plot.SetFillStyle(3004)
PhotonEta_plot.Draw("HIST")
c11.SaveAs("PhotonEta.png")
c11.SaveAs("PhotonEta.root")

# Plot photon phi
c12 = ROOT.TCanvas()
PhotonPhi_plot.SetLineColor(ROOT.kOrange+2)
PhotonPhi_plot.SetLineWidth(2)
PhotonPhi_plot.SetFillColor(ROOT.kOrange+2)
PhotonPhi_plot.SetFillStyle(3004)
PhotonPhi_plot.Draw("HIST")
c12.SaveAs("PhotonPhi.png")
c12.SaveAs("PhotonPhi.root")

# Plot photon eta vs phi
c13 = ROOT.TCanvas()
PhotonEtaPhi_plot.Draw("COLZ")
c13.SaveAs("PhotonEtaPhi.png")
c13.SaveAs("PhotonEtaPhi.root")
