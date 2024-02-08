import ROOT
from DataFormats.FWLite import Handle, Events
from FWCore.ParameterSet.VarParsing import VarParsing


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
        "Jets1bin": ROOT.TH1F("Jets1bin","",60,-150,150),
        "Jets": ROOT.TH2F("Jets","",60,0,300,60,-1,1),
        "MET": ROOT.TH2F("MET","",60,0,300,60,-1,1),
#        "MET" : ROOT.TH2F("MET","",60,0,300,60,0,300),
    }
    
    histos["MET"].SetLineColor(ROOT.kRed)
    histos["Jets"].SetLineColor(ROOT.kBlue)
    
    for iev,event in enumerate(events):
        event.getByLabel(scoutingJetLabel, scoutingJets)
        if iev%100==0: print(iev)
        if not scoutingJets.isValid(): continue ##skip events without scoutin tracks
        event.getByLabel(offlineJetLabel, offlineJets)
        event.getByLabel(scoutingMetPhiLabel, scoutingMetPhi)
        event.getByLabel(scoutingMetPtLabel, scoutingMetPt)
        event.getByLabel(offlineMetLabel, offlineMet)
        
        histos["MET"].Fill(offlineMet.product().at(0).pt(), (scoutingMetPt.product()[0] - offlineMet.product().at(0).pt())/offlineMet.product().at(0).pt() )
#        histos["MET"].Fill(scoutingMetPt.product()[0], offlineMet.product().at(0).pt())
#        histos["Jets"].Fill(offjet.pt(), (scoutingjet_best.pt() - offjet.pt())/offjet.pt())
        for offjet in offlineJets.product():
            if offjet.pt()>20:
                found = False
                dRmax = 0.3
                dR = dRmax
                dR2 = dR*dR
                scoutingjet_best = None
                for scoutingjet in scoutingJets.product():
                    if scoutingjet.pt()>20 and scoutingjet.pt() < (2*offjet.pt() - 20):
                        dr2_ = deltaR2(offjet.eta(), scoutingjet.eta(), offjet.phi(), scoutingjet.phi())
                        if dr2_ < dR2:
                            dR2 = dr2_
                            scoutingjet_best = scoutingjet
                if scoutingjet_best:
                    histos["Jets"].Fill(offjet.pt(), (scoutingjet_best.pt() - offjet.pt())/offjet.pt())
                    histos["JetsDR"].Fill(dR2**0.5)
                    if offjet.pt()>80 and offjet.pt()<100:
                        histos["Jets1bin"].Fill(scoutingjet_best.pt() - offjet.pt())
        
        
        if iev>10000000:
            break
    
    
    ROOT.gROOT.SetBatch(1)
    c1 = ROOT.TCanvas("c1")
    
    fName = inputFile
    fName = fName.replace("output","plot")
    
    histos["MET"].Draw("COLZ")
    
    fName = fName.replace(".", "MET2D.")
    c1.SaveAs(fName.replace(".root",".png"))
    c1.SaveAs(fName.replace(".root",".png"))
    
    histos["Jets"].Draw("COLZ")
    
    fName = fName.replace(".", "Jet2D.")
    c1.SaveAs(fName.replace(".root",".png"))
    c1.SaveAs(fName.replace(".root",".png"))

#    prof = histos["Jets"].ProfileX("_pfx",  -1, -1, "s")
    prof = histos["Jets"].ProfileX("_pfx",  -1, -1, "")
    prof.SetMaximum(0.5)
    prof.SetMinimum(-0.5)
    prof.Draw("COLZ")
    
    fName = fName.replace(".", "JetProf.")
    c1.SaveAs(fName.replace(".root",".png"))
    c1.SaveAs(fName.replace(".root",".png"))
    
    histos["JetsDR"].Draw("")
    
    fName = fName.replace(".", "JetDR.")
    c1.SaveAs(fName.replace(".root",".png"))
    c1.SaveAs(fName.replace(".root",".png"))
    
    histos["Jets1bin"].Draw("")
    
    fName = fName.replace(".", "Jets1bin.")
    c1.SaveAs(fName.replace(".root",".png"))
    c1.SaveAs(fName.replace(".root",".png"))
    

