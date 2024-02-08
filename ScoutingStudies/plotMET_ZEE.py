import ROOT
from DataFormats.FWLite import Handle, Events
from FWCore.ParameterSet.VarParsing import VarParsing

import math
def invariant_mass(pt1, pt2, eta1, eta2, phi1, phi2, mass1, mass2):
    # Convert eta and phi to Cartesian coordinates
    px1 = pt1 * math.cos(phi1)
    py1 = pt1 * math.sin(phi1)
    pz1 = pt1 * math.sinh(eta1)
    E1 = math.sqrt(px1**2 + py1**2 + pz1**2 + mass1**2)
    
    px2 = pt2 * math.cos(phi2)
    py2 = pt2 * math.sin(phi2)
    pz2 = pt2 * math.sinh(eta2)
    E2 = math.sqrt(px2**2 + py2**2 + pz2**2 + mass2**2)
    
    # Calculate invariant mass
    invariant_mass = math.sqrt((E1 + E2)**2 - (px1 + px2)**2 - (py1 + py2)**2 - (pz1 + pz2)**2)
    
    return invariant_mass

options = VarParsing ('analysis')

options.maxEvents = 1000000
#options.inputFiles = ["outputScoutingPF__.root"]
options.inputFiles = ["outputScoutingPF.root"]
#options.secondaryInputFiles = [
#]

print(options.maxEvents)
print(options.inputFiles)
print(options.secondaryInputFiles)

events = Events (options)

def deltaR2(eta1, eta2, phi1, phi2):
    deta = eta1-eta2
    dphi = ROOT.TVector2.Phi_mpi_pi(phi1 - phi2)
    return deta**2 + dphi**2

def matching(dR, eta1, eta2, phi1, phi2):
    return deltaR2(eta1, eta2, phi1, phi2) < dR**2

#pixelTracks, pixelTrackLabel = Handle("vector<reco::Track>"), ("hltPixelTracks","","HLTX")
#tracks, trackLabel = Handle("vector<reco::Track>"), ("hltMergedTracks","","HLTX")
#photons, photonLabel = Handle("vector<Run3ScoutingPhoton>"), ("hltScoutingEgammaPacker","","HLTX")
#scoutingPfCandidates, scoutingPfCandidateLabel = Handle("vector<Run3ScoutingParticle>"), ("hltScoutingPFPacker","","HLTX")
#pfCandidates, pfCandidateLabel = Handle("vector<reco::PFCandidate>"), ("hltParticleFlow","","HLTX")
#scoutingTracks, scoutingTrackLabel = Handle("vector<Run3ScoutingTrack>"), ("hltScoutingTrackPacker","","HLTX")

#scoutingElectrons, scoutingElectronLabel = Handle("vector<Run3ScoutingElectron>"), ("hltScoutingEgammaPacker","","HLTX")
scoutingElectrons, scoutingElectronLabel = Handle("vector<reco::GsfElectron>"), ("gedGsfElectrons","","RECO")

scoutingJets, scoutingJetLabel = Handle("vector<Run3ScoutingPFJet>"), ("hltScoutingPFPacker","","HLTX")
offlineJets, offlineJetLabel = Handle("vector<reco::PFJet>"), ("ak4PFJetsPuppi","","RECO")
#offlineJets, offlineJetLabel = Handle("vector<reco::PFJet>"), ("ak4PFJets","","RECO")

scoutingMetPhi, scoutingMetPhiLabel = Handle("double"), ("hltScoutingPFPacker","pfMetPhi","HLTX")
scoutingMetPt, scoutingMetPtLabel = Handle("double"), ("hltScoutingPFPacker","pfMetPt","HLTX")
offlineMet, offlineMetLabel = Handle("vector<reco::PFMET>"), ("pfMetPuppi","","RECO")
#offlineMet, offlineMetLabel = Handle("vector<reco::PFMET>"), ("pfMet","","RECO")

inputFiles = [
    "outputScoutingPF_Bs_longRun_highPt_delta_Pt3GeV.root",
]

import sys
if ".root" in sys.argv[-1]:
    inputFiles = [sys.argv[-1]]


for inputFile in inputFiles:
    options.inputFiles.clear()
    options.inputFiles = [inputFile]
    tmp = ROOT.TH2F("tmp","",60,0,300,60,0,300)

    histos = {
        "JetsDR": ROOT.TH1F("JetsDR","",100, 0, 2),
#        "Jets1Ax": ROOT.TH1F("Jets1Ax","",60,0,300,60,-150,150),
        "ZEE": ROOT.TH1F("ZEE","",200,0,200),
        "offMET70": ROOT.TH1F("MET","",200,-1,1),
        "offMETFake": ROOT.TH1F("MET","",100,0, 200),
        "MET70": ROOT.TH1F("MET","",200,-1,1),
        "METFake": ROOT.TH1F("MET","",100,0, 200),
        "Jet1bin50": ROOT.TH1F("Jet1bin50","",200,-0.5,0.5),
        "Jet1bin100": ROOT.TH1F("Jet1bin100","",200,-0.5,0.5),
        "Jets": ROOT.TH2F("Jets","",60,0,300,60,-1,1),
#        "MET": ROOT.TH2F("MET","",60,0,300,60,-1,1),
        "offMET": ROOT.TH2F("offMET","",60,0,300,60,0,300),
        "MET" : ROOT.TH2F("MET","",60,0,300,60,0,300),
    }
    
    histos["MET"].SetLineColor(ROOT.kRed)
    histos["Jets"].SetLineColor(ROOT.kBlue)
    
    for iev,event in enumerate(events):
        event.getByLabel(scoutingElectronLabel, scoutingElectrons)
        if iev%100==0: print(iev)
        if not scoutingElectrons.isValid(): continue ##skip events without scoutin tracks
        event.getByLabel(offlineJetLabel, offlineJets)
        event.getByLabel(scoutingJetLabel, scoutingJets)
        event.getByLabel(scoutingMetPhiLabel, scoutingMetPhi)
        event.getByLabel(scoutingMetPtLabel, scoutingMetPt)
        event.getByLabel(offlineMetLabel, offlineMet)
        
        if len(scoutingElectrons.product())>=2:
            eles = scoutingElectrons.product()
            Z1 = ROOT.TLorentzVector()
            Z2 = ROOT.TLorentzVector()
            MET = ROOT.TLorentzVector()
            offMET = ROOT.TLorentzVector()
            Z1.SetPtEtaPhiM(eles[0].pt(), eles[0].eta(), eles[0].phi(), 0.5)
            Z2.SetPtEtaPhiM(eles[1].pt(), eles[1].eta(), eles[1].phi(), 0.5)
            Zcand = Z1 + Z2
            histos["ZEE"].Fill(Zcand.M())
            if Zcand.M()>80 and Zcand.M()<100:
                mass = invariant_mass(eles[0].pt(), eles[1].pt(), eles[0].eta(), eles[1].eta(), eles[0].phi(), eles[1].phi(), 0.5, 0.5)
                MET.SetPtEtaPhiM(scoutingMetPt.product()[0], 0, scoutingMetPhi.product()[0], 0)
                offMET.SetPtEtaPhiM(offlineMet.product()[0].pt(), 0, offlineMet.product()[0].phi(), 0)
                METnoZEE = MET + Zcand
                offMETnoZEE = offMET + Zcand
#                histos["MET"].Fill(Zcand.Pt(), (METnoZEE.Pt() - Zcand.Pt())/Zcand.Pt() )
                histos["MET"].Fill(Zcand.Pt(), METnoZEE.Pt() )
                histos["offMET"].Fill(Zcand.Pt(), offMETnoZEE.Pt() )
#                histos["MET"].Fill(Zcand.Pt(), MET.Pt() )
                if Zcand.Pt()>70:
                    histos["MET70"].Fill((METnoZEE.Pt() - Zcand.Pt())/Zcand.Pt() )
                    histos["offMET70"].Fill((offMETnoZEE.Pt() - Zcand.Pt())/Zcand.Pt() )
                if Zcand.Pt()<10:
                    histos["METFake"].Fill(METnoZEE.Pt())
                    histos["offMETFake"].Fill(offMETnoZEE.Pt())
                MET.SetPtEtaPhiM(offlineMet.product()[0].pt(), 0, offlineMet.product()[0].phi(), 0)
                METnoZEE = MET + Zcand
                histos["offMET"].Fill(Zcand.Pt(), METnoZEE.Pt() )
                    

#        histos["MET"].Fill(offlineMet.product().at(0).pt(), (scoutingMetPt.product()[0] - offlineMet.product().at(0).pt())/offlineMet.product().at(0).pt() )
##        histos["MET"].Fill(scoutingMetPt.product()[0], offlineMet.product().at(0).pt())
##        histos["Jets"].Fill(offjet.pt(), (scoutingjet_best.pt() - offjet.pt())/offjet.pt())
                for offjet in offlineJets.product():
                    if offjet.pt()>20 and abs(offjet.eta())<2.6 and offjet.neutralHadronEnergyFraction()<0.9  and offjet.neutralEmEnergyFraction()<0.9 and offjet.nConstituents()>1 and offjet.muonEnergyFraction()<0.8  and offjet.chargedHadronEnergyFraction()>0.01  and offjet.chargedMultiplicity()>0      and offjet.chargedEmEnergyFraction()<0.8 :
                        found = False
                        dRmax = 0.1
                        dR = dRmax
                        dR2 = dR*dR
                        scoutingjet_best = None
                        for scoutingjet in scoutingJets.product():
                            if scoutingjet.pt()>20 and scoutingjet.pt() < (2*offjet.pt() - 20):
                                if matching(0.8, eles[0].eta(), scoutingjet.eta(), eles[0].phi(), scoutingjet.phi()): continue
                                if matching(0.8, eles[1].eta(), scoutingjet.eta(), eles[1].phi(), scoutingjet.phi()): continue
                                dr2_ = deltaR2(offjet.eta(), scoutingjet.eta(), offjet.phi(), scoutingjet.phi())
                                if dr2_ < dR2:
                                    dR2 = dr2_
                                    scoutingjet_best = scoutingjet
                        if scoutingjet_best:
                            histos["Jets"].Fill(offjet.pt(), (scoutingjet_best.pt() - offjet.pt())/offjet.pt())
                            histos["JetsDR"].Fill(dR2**0.5)
                            if offjet.pt()>50 and offjet.pt()<100:
                                histos["Jet1bin50"].Fill((scoutingjet_best.pt() - offjet.pt())/offjet.pt())
                            elif offjet.pt()>100:
                                histos["Jet1bin100"].Fill((scoutingjet_best.pt() - offjet.pt())/offjet.pt())
        #                    if offjet.pt()>80 and offjet.pt()<100:
        if iev>187800:
            break
    
    
    ROOT.gROOT.SetBatch(1)
    ROOT.gStyle.SetOptStat(0)
    c1 = ROOT.TCanvas("c1")
    c1.SetGridx()
    c1.SetGridy()
    c1.SetLogz()
    
    fName = inputFile
    fName = fName.replace("output","plot")
    
    histos["MET"].Draw("COLZ")
    
    pName = fName.replace(".", "MET2D.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))

    prof = histos["MET"].ProfileX("_pfx",  -1, -1, "s")
#    prof.SetMaximum(0.3)
#    prof.SetMinimum(-0.3)
    prof.Draw("COLZ")
    
    pName = fName.replace(".", "METprofile.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))

    histos["offMET"].Draw("COLZ")
    
    pName = fName.replace(".", "offMET2D.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))

    prof = histos["offMET"].ProfileX("_pfx",  -1, -1, "s")
#    prof.SetMaximum(0.3)
#    prof.SetMinimum(-0.3)
    prof.Draw("COLZ")
    
    pName = fName.replace(".", "offMETprofile.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))
    
    histos["Jets"].Draw("COLZ")
    
    pName = fName.replace(".", "Jet2D.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))

    prof = histos["Jets"].ProfileX("_pfx",  -1, -1, "s")
#    prof = histos["Jets"].ProfileX("_pfx",  -1, -1, "")
    prof.SetMaximum(0.3)
    prof.SetMinimum(-0.3)
    prof.Draw("COLZ")
    
    pName = fName.replace(".", "JetProf.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))
    
    histos["JetsDR"].Draw("")
    
    pName = fName.replace(".", "JetDR.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))
    
    histos["ZEE"].Draw("")
    
    pName = fName.replace(".", "ZEE.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))
    
    histos["Jet1bin50"].Draw("")
    
    pName = fName.replace(".", "Jet1bin50.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))
    
    histos["Jet1bin100"].Draw("")
    
    pName = fName.replace(".", "Jet1bin100.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))

    histos["MET70"].Draw("")
    
    pName = fName.replace(".", "MET70.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))

    histos["METFake"].Draw("")
    
    pName = fName.replace(".", "METFake.")
    c1.SetLogy()
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))
    c1.SetLogy(0)

    histos["offMET70"].Draw("")
    
    pName = fName.replace(".", "offMET70.")
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))

    histos["offMETFake"].Draw("")
    
    pName = fName.replace(".", "offMETFake.")
    c1.SetLogy()
    c1.SaveAs(pName)
    c1.SaveAs(pName.replace(".root",".png"))
    c1.SetLogy(0)

