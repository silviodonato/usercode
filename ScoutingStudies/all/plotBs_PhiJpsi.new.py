import ROOT
from DataFormats.FWLite import Handle, Events
from FWCore.ParameterSet.VarParsing import VarParsing

import math

muon_mass = 0.106
pion_mass = 0.140
kaon_mass = 0.494

jpsi_mass = 3.097
phi_mass = 1.019

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

def invariant_mass_(momentum1, momentum2):
    pt1, eta1, phi1, mass1 = momentum1
    pt2, eta2, phi2, mass2 = momentum2
    
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
    if ((E1 + E2)**2 - (px1 + px2)**2 - (py1 + py2)**2 - (pz1 + pz2)**2)<0:
        print(momentum1)
        print(momentum2)
    invariant_mass = math.sqrt((E1 + E2)**2 - (px1 + px2)**2 - (py1 + py2)**2 - (pz1 + pz2)**2)
#    if abs(invariant_mass - phi_mass) < (invariant_mass - best_phi_mass):
#        print(invariant_mass)
#        print(momentum1)
#        print(momentum2)
    
    return invariant_mass

def findBestPair(momenta, target_mass, mass1=-1, mass2=-1):
    best_pair = (1E9, 1E9) ## i < j
    best_mass = -1E9
    
    if len(momenta)<2: return [1E9, 1E9]
    
    for i, momentum1 in enumerate(momenta): 
        for j, momentum2 in enumerate(momenta):
            if j<=i: continue  ## i < j
            if mass1>0: momentum1 = forceMass(momentum1, mass1)
            if mass2>0: momentum2 = forceMass(momentum2, mass2)
            mass = invariant_mass_(momentum1, momentum2)
            if abs(mass - target_mass) < abs(mass - best_mass):
                best_mass = mass
                best_pair = (i, j)
    return best_pair

def forceMass(momentum, mass):
    momentum = (momentum[0], momentum[1], momentum[2], mass)
    return momentum

def forcePionMass(momentum):
    return forceMass(momentum, pion_mass)

def forceMuonMass(momentum):
    return forceMass(momentum, muon_mass)

def forceKaonMass(momentum):
    return forceMass(momentum, kaon_mass)

#def getInvariantMasses(momenta):
#    if len(momenta)<4:
#        return []
#    masses = []
#    best_jpsi_pair = (len(momenta)-1, len(momenta)-2)
##        best_jpsi_mass = 10000
#    
##        print(best_jpsi_pair)
##        print(momenta)
#    best_phi_pair = (100000, 100000)
#    best_phi_mass = 10000
#    
#    jpsi1 = ROOT.TLorentzVector()
#    jpsi2 = ROOT.TLorentzVector()
#    
##    print(best_jpsi_pair)
#    
#    jpsi1.SetPtEtaPhiM(*forceMuonMass(momenta[best_jpsi_pair[0]]))
#    jpsi2.SetPtEtaPhiM(*forceMuonMass(momenta[best_jpsi_pair[1]]))
#    
#    momenta.remove(momenta[max(best_jpsi_pair)])
#    momenta.remove(momenta[min(best_jpsi_pair)])
##        for i, momentum1 in enumerate(momenta):
##            for j, momentum2 in enumerate(momenta):
##                if j<=i: continue
##                
##                mass = invariant_mass_(forcePionMass(momentum1), forcePionMass(momentum2))
##                if abs(mass - jpsi_mass) < abs(mass - best_jpsi_mass):
##                    best_jpsi_mass = mass
##                    best_jpsi_pair = (i, j)
##        
##        for i, momentum1 in enumerate(momenta):
##            if i == best_jpsi_pair[0] or i == best_jpsi_pair[1] : continue
##            for j, momentum2 in enumerate(momenta):
##                if j == best_jpsi_pair[0] or j == best_jpsi_pair[1] : continue
##                if j<=i: continue
##                mass = invariant_mass_(forceKaonMass(momentum1), forceKaonMass(momentum2))
##                if abs(mass - phi_mass) < abs(mass - best_phi_mass):
##                    best_phi_mass = mass
##                    best_phi_pair = (i, j)
#    best_phi_pair = findBestPair(momenta, best_phi_mass, kaon_mass, kaon_mass)
#    
#    if best_phi_pair[1]<0: return []
#    
#    phi1 = ROOT.TLorentzVector()
#    phi2 = ROOT.TLorentzVector()
#    
##    print(best_phi_pair)
#    phi1.SetPtEtaPhiM(*forceKaonMass(momenta[best_phi_pair[0]]))
#    phi2.SetPtEtaPhiM(*forceKaonMass(momenta[best_phi_pair[1]]))
#    
##        print(phi1.Pt(), phi2.Pt())
##        masses.append((jpsi1+jpsi2).M())
#    masses.append((phi1+phi2).M())
##    masses.append((jpsi1+jpsi2+phi1+phi2).M())
##        print(masses)
#    return masses

inputFiles = [
    "outputScoutingPF_Bs_longRun_highPt_delta_Pt3GeV.root",
]

def matching(dR, eta1, eta2, phi1, phi2):
    deta = eta1-eta2
    dphi = ROOT.TVector2.Phi_mpi_pi(phi1 - phi2)
    return deta**2 + dphi**2 < dR**2

import sys
if ".root" in sys.argv[-1]:
    inputFiles = [sys.argv[-1]]


options = VarParsing ('analysis')

options.maxEvents = 1000000

for inputFile in inputFiles:
    options.inputFiles.clear()
    options.inputFiles = [inputFile]
    
    print(options.maxEvents)
    print(options.inputFiles)
    print(options.secondaryInputFiles)
    
    #file_ = ROOT.TFile.Open("/eos/cms//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/21a72136-634d-4377-9077-5d708302fc46.root")
    #events = file_.Get("Events")
    #events.SetBranchStatus("*", 0)
    #events.SetBranchStatus("*SimTrack*g4SimHits*", 1)
    
    
    #                print(i)
    
    events = Events (options)
    
    simTracks, simTrackLabel = Handle("vector<SimTrack>"), ("g4SimHits","","SIM")
    scoutingTracks, scoutingTrackLabel = Handle("vector<Run3ScoutingTrack>"), ("hltScoutingTrackPacker","","HLTX")
    scoutingMuons, scoutingMuonLabel = Handle("vector<Run3ScoutingMuon>"), ("hltScoutingMuonPacker","","HLTX")
#    genParticles, genParticleLabel = Handle("vector<reco::GenParticle>"), ("genParticles","","HLT")

    histo = ROOT.TH1F("histo","",1000,0,10)
    histoScouting = ROOT.TH1F("histoScouting","",300,2,20)
    histoJpsi = ROOT.TH1F("histoJpsi","",200,jpsi_mass*0.6, jpsi_mass*1.4)
    histoPhi = ROOT.TH1F("histoPhi","",200,phi_mass*0.6, phi_mass*1.4)
#    histoScouting = ROOT.TH1F("histoScouting","",600,0,6)
    for iev,event in enumerate(events):
        if iev%1000==0: print(iev)
        event.getByLabel(simTrackLabel, simTracks)
        event.getByLabel(scoutingTrackLabel, scoutingTracks)
        event.getByLabel(scoutingMuonLabel, scoutingMuons)
#        print("Muons: %s" %str([muon.pt() for muon in scoutingMuons.product()]))
        
#        momenta = []
#        try:
#            for simTrack in simTracks.product():
#                if simTrack.momentum().pt()>2.5 and simTrack.charge()!=0:
#                    pt = simTrack.momentum().pt()
#                    eta = simTrack.momentum().eta()
#                    phi = simTrack.momentum().phi()
#                    mass = max(1E-9, simTrack.momentum().mass())
#        #            mass = 0.14
#                    momenta.append((pt, eta, phi, mass))
#            masses = getInvariantMasses(momenta)
#            for mass in masses: histo.Fill(mass)
#        except:
#            pass
        
        momenta_mu = []
        if len(scoutingMuons.product())>=2:
            mu1 = max([obj for obj in scoutingMuons.product()], key=lambda obj: obj.pt())
            mu2 = max([obj for obj in scoutingMuons.product() if obj!=mu1], key=lambda obj: obj.pt())
            mass =invariant_mass_((mu1.pt(), mu1.eta(), mu1.phi(), muon_mass), (mu2.pt(), mu2.eta(), mu2.phi(), muon_mass))
#            print(mass)
            histoJpsi.Fill(mass)
            if abs(mass - jpsi_mass)>0.1:
                continue
        else:
            continue
            
        momenta = []
        mu1_trk = None
        mu2_trk = None
        best = scoutingTracks.product().at(0)
#        print("Hello")
        for scoutingTrack in scoutingTracks.product():
            if scoutingTrack.tk_pt()>0.:
#                if matching(0.03, mu2.trk_eta(), scoutingTrack.tk_eta(), mu2.trk_eta(), scoutingTrack.tk_eta()):
#                    print("Found Muon2")
#                    continue
                pt = scoutingTrack.tk_pt()
                eta = scoutingTrack.tk_eta()
                phi = scoutingTrack.tk_phi()
#                mass = 0.14
                if matching(0.03, mu1.trk_eta(), scoutingTrack.tk_eta(), mu1.trk_eta(), scoutingTrack.tk_eta()) and not mu1_trk: 
#                    print("Found Muon1")
                    mu1_trk = (pt, eta, phi, muon_mass)
                elif matching(0.03, mu2.trk_eta(), scoutingTrack.tk_eta(), mu2.trk_eta(), scoutingTrack.tk_eta()) and not mu2_trk: 
#                    print("Found Muon2")
                    mu2_trk = (pt, eta, phi, muon_mass)
                else:
                    momenta.append((pt, eta, phi, mass))
        jpsi1 = ROOT.TLorentzVector()
        jpsi1.SetPtEtaPhiM(mu1.trk_pt(), mu1.trk_eta(), mu1.trk_phi(), muon_mass)
        jpsi2 = ROOT.TLorentzVector()
        jpsi2.SetPtEtaPhiM(mu2.trk_pt(), mu2.trk_eta(), mu2.trk_phi(), muon_mass)
#        jpsi1.SetPtEtaPhiM(mu1.trk_pt(), mu1.trk_eta(), mu1.trk_phi(), muon_mass)
#        jpsi2.SetPtEtaPhiM(mu2.trk_pt(), mu2.trk_eta(), mu2.trk_phi(), muon_mass)
#        momenta.append((mu1.trk_pt(), mu1.trk_eta(), mu1.trk_phi(), muon_mass))
#        momenta.append((mu2.trk_pt(), mu2.trk_eta(), mu2.trk_phi(), muon_mass))
#        print("Done")
#        print(mu1.trk_eta()- best.tk_eta(), mu1.trk_phi()- best.tk_phi(), mu1.trk_pt() - best.tk_pt())
#        masses = getInvariantMasses(momenta)
        if len(momenta)<2: continue
        masses = []
#        best_jpsi_pair = (len(momenta)-1, len(momenta)-2)
    #        best_jpsi_mass = 10000
        
    #        print(best_jpsi_pair)
    #        print(momenta)
        best_phi_pair = (100000, 100000)
        best_phi_mass = 10000
        
        
    #    print(best_jpsi_pair)
        
    #        for i, momentum1 in enumerate(momenta):
    #            for j, momentum2 in enumerate(momenta):
    #                if j<=i: continue
    #                
    #                mass = invariant_mass_(forcePionMass(momentum1), forcePionMass(momentum2))
    #                if abs(mass - jpsi_mass) < abs(mass - best_jpsi_mass):
    #                    best_jpsi_mass = mass
    #                    best_jpsi_pair = (i, j)
    #        
    #        for i, momentum1 in enumerate(momenta):
    #            if i == best_jpsi_pair[0] or i == best_jpsi_pair[1] : continue
    #            for j, momentum2 in enumerate(momenta):
    #                if j == best_jpsi_pair[0] or j == best_jpsi_pair[1] : continue
    #                if j<=i: continue
    #                mass = invariant_mass_(forceKaonMass(momentum1), forceKaonMass(momentum2))
    #                if abs(mass - phi_mass) < abs(mass - best_phi_mass):
    #                    best_phi_mass = mass
    #                    best_phi_pair = (i, j)
        best_phi_pair = findBestPair(momenta, best_phi_mass, kaon_mass, kaon_mass)
        
        phi1 = ROOT.TLorentzVector()
        phi2 = ROOT.TLorentzVector()
        
    #    print(best_phi_pair)
        phi1.SetPtEtaPhiM(*forceKaonMass(momenta[best_phi_pair[0]]))
        phi2.SetPtEtaPhiM(*forceKaonMass(momenta[best_phi_pair[1]]))
        
    #        print(phi1.Pt(), phi2.Pt())
    #        masses.append((jpsi1+jpsi2).M())
        masses.append((phi1+phi2).M())
    #    masses.append((jpsi1+jpsi2+phi1+phi2).M())
    #        print(masses)
        
        mass2k = (phi1+phi2).M()
        histoPhi.Fill(mass2k)
#        histoScouting.Fill((jpsi1+jpsi2+phi1+phi2).M())
        histoScouting.Fill((jpsi1+jpsi2+phi1+phi2).M())
#        for mass in masses: histoScouting.Fill(mass)
        
        
#        momenta = []
#        mu1_trk = None
#        mu2_trk = None
#        best = genParticles.product().at(0)
##        print("Hello")
#        for genParticle in genParticles.product():
#            if genParticle.pt()>0. and abs(genParticle.charge())==1 and abs(genParticle.mass() - 0.495)<0.003:
#                pt = genParticle.pt()
#                eta = genParticle.eta()
#                phi = genParticle.phi()
#                mass = 0.14
#                if matching(1.0, mu1.trk_eta(), genParticle.eta(), mu1.trk_eta(), genParticle.eta()) and not mu1_trk: 
##                    print("Found Muon1")
#                    mu1_trk = (pt, eta, phi, mass)
#                elif matching(1.0, mu2.trk_eta(), genParticle.eta(), mu2.trk_eta(), genParticle.eta()) and not mu2_trk: 
##                    print("Found Muon2")
#                    mu2_trk = (pt, eta, phi, mass)
#                else:
#                    momenta.append((pt, eta, phi, mass))
#        momenta.append((mu1.trk_pt(), mu1.trk_eta(), mu1.trk_phi(), muon_mass))
#        momenta.append((mu2.trk_pt(), mu2.trk_eta(), mu2.trk_phi(), muon_mass))
##        print("Done")
##        print(mu1.trk_eta()- best.tk_eta(), mu1.trk_phi()- best.tk_phi(), mu1.trk_pt() - best.tk_pt())
#        masses = getInvariantMasses(momenta)
#        for mass in masses: histoScouting.Fill(mass)
        
    #        if simTrack.momentum().pt()>2 and simTrack.charge()!=0:
    #            print(simTrack.momentum().pt(), simTrack.type(), simTrack.trackId(), simTrack.genpartIndex())
    #            for simTrack2 in simTracks.product():
    #                if simTrack2.momentum().pt()>2 and simTrack2.charge()!=0 and simTrack2!=simTrack:
    #                    for simTrack3 in simTracks.product():
    #                        if simTrack3.momentum().pt()>2 and simTrack3.charge()!=0 and simTrack3!=simTrack and simTrack3!=simTrack2:
    #                            for simTrack4 in simTracks.product():
    #                                if simTrack4.momentum().pt()>2 and simTrack4.charge()!=0 and simTrack4!=simTrack and simTrack4!=simTrack2 and simTrack4!=simTrack3:
    #                                    histo.Fill((simTrack.momentum()+simTrack2.momentum()+simTrack3.momentum()+simTrack4.momentum()).M())
    #                    histo.Fill(invariant_mass(simTrack.momentum().pt(), simTrack2.momentum().pt(), simTrack.momentum().eta(), simTrack2.momentum().eta(), simTrack.momentum().phi(), simTrack2.momentum().phi(), max(1E-3, simTrack.momentum().mass()), max(1E-3, simTrack2.momentum().mass())))
    #                for simTrack2 in simTracks.product():
    #                    if simTrack2.momentum().pt()>2 and simTrack2.charge()!=0:
    #                    histo.Fill(invariant_mass(simTrack.momentum().pt(), simTrack2.momentum().pt(), simTrack.momentum().eta(), simTrack2.momentum().eta(), simTrack.momentum().phi(), simTrack2.momentum().phi(), 0, 1E-3))
        
    #    for scoutingTrack in scoutingTracks.product():
    #        if scoutingTrack.tk_pt()>2:
    ##            print(scoutingTrack.momentum().pt(), scoutingTrack.type(), scoutingTrack.trackId(), scoutingTrack.genpartIndex())
    #            for scoutingTrack2 in scoutingTracks.product():
    #                if scoutingTrack2.tk_pt()>2 and scoutingTrack2!=scoutingTrack:
    #                    tk1 = scoutingTrack
    #                    tk2 = scoutingTrack2
    #                    histoScouting.Fill(invariant_mass(tk1.tk_pt(), tk2.tk_pt(), tk1.tk_eta(), tk2.tk_eta(), tk1.tk_phi(), tk2.tk_phi(), 0.14, 0.14))
        
#        if iev>1000:
#            break
    
    ROOT.gROOT.SetBatch(1)
    ROOT.gStyle.SetOptStat(0)
    leg = ROOT.TLegend(0.1,0.8,0.48,0.9)
    c1 = ROOT.TCanvas("c1","",1280,1280)
    c1.SetGridx()
    c1.SetGridy()
    
    fName = inputFile
    fName = fName.replace("output","plot")
    histo.Draw()
    c1.SaveAs(fName)
    c1.SaveAs(fName.replace(".root",".png"))
    
    fName = fName.replace(".", "Scouting.")
    histoScouting.Draw()
    
    
    Xmin, Xmax = 4.5, 6.5
#    f1 = ROOT.TF1("f1","gaus(0)+[3]+[4]*x", Xmin, Xmax)
    f1 = ROOT.TF1("f1","gaus(0)+gaus(3)", Xmin, Xmax)
    f1.SetParLimits(0,0,100000)
    f1.SetParLimits(3,0,100000)
    f1.SetParLimits(2,0,10)
    f1.SetParLimits(5,0,100)
    f1.SetParameters(50, 5.5, 0.05, 30, 5.5, 1)
    
    first = "ScoutingPF"
    histoScouting.SetMaximum(histoScouting.GetMaximum()*1.2)
    histoScouting.Draw()
    histoScouting.Fit(f1, "", "", Xmin, Xmax)
    m, s = f1.GetParameter(1), f1.GetParameter(2)
    f1.SetRange(Xmin, Xmax) 
    histoScouting.Fit(f1, "", "", Xmin, Xmax)
    m, s = f1.GetParameter(1), f1.GetParameter(2)
    f1.SetRange(Xmin, Xmax) 
    f1.Draw("same")
    
    leg.AddEntry(histoScouting, "ScoutingTracks (%.3f GeV)"%f1.GetParameter(2), "l")
    leg.Draw()
    
    c1.SaveAs(fName)
    c1.SaveAs(fName.replace(".root",".png"))

    fName = fName.replace("Scouting","Jpsi")
    histoJpsi.Draw()
    c1.SaveAs(fName)
    c1.SaveAs(fName.replace(".root",".png"))
    
    fName = fName.replace("Jpsi","Phi")
    histoPhi.Draw()
    c1.SaveAs(fName)
    c1.SaveAs(fName.replace(".root",".png"))
    
    


