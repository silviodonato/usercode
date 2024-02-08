import ROOT
from DataFormats.FWLite import Handle, Events
from FWCore.ParameterSet.VarParsing import VarParsing

import math

muon_mass = 0.106
pion_mass = 0.140
kaon_mass = 0.494

jpsi_mass = 3.097
#jpsi_mass = 3.00
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
    best_pair = None ## i < j
    best_mass = 1E9
    
    if len(momenta)<2:
        print("Problems in findBestPair")
        return [1E9, 1E9]
    
    for i, momentum1 in enumerate(momenta): 
        m1 = forceMass(momentum1, mass1) if mass1>0 else momentum1
        for j, momentum2 in enumerate(momenta):
            if j<=i: continue  ## i < j
            m2 = forceMass(momentum2, mass2) if mass2>0 else momentum2
            mass = invariant_mass_(m1, m2)
            if abs(mass - target_mass) < abs(best_mass - target_mass):
                best_mass = float(mass)
                best_pair = (i, j)
    if best_mass==None:
        print("Problems in findBestPair")
        return [1E9, 1E9]
    return best_pair

def findBestPairTwoCollections(momenta1, momenta2, target_mass, mass1=-1, mass2=-1):
    best_pair = (1E9, 1E9) ## i < j
    best_mass = -1E9
    
    if len(momenta1)<1 or len(momenta2)<1: return [1E9, 1E9]
    
    for i, momentum1 in enumerate(momenta1): 
        if mass1>0: m1 = forceMass(momentum1, mass1)
        for j, momentum2 in enumerate(momenta2):
            if mass2>0: m2 = forceMass(momentum2, mass2)
            mass = invariant_mass_(m1, m2)
            if abs(mass - target_mass) < abs(mass - best_mass):
                best_mass = float(mass)
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

def makeStack(histos, name="stack"):
    stack = ROOT.THStack(name, "")
    for histo in reversed(histos):
        stack.Add(histo)
    stack.SetMaximum(1.2 * stack.GetMaximum())
    return stack

def makeLegend(h2mu, h1mu, h0mu):
    leg = ROOT.TLegend(0.1,0.8,0.48,0.9)
    leg.AddEntry(h2mu, "J/#psi 2 muons", "f")
    leg.AddEntry(h1mu, "J/#psi 1 muon - 1 track", "f")
    leg.AddEntry(h0mu, "J/#psi 2 tracks", "f")
    return leg

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

counter1 = 0
counter2 = 0
counter3 = 0
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
    histoScouting2mu = ROOT.TH1F("histoScouting2mu","",100,5.1,5.6)
    histoScouting2mu.SetFillColor(ROOT.kMagenta)
    histoScouting1mu = histoScouting2mu.Clone("histoScouting1mu")
    histoScouting1mu.SetFillColor(ROOT.kRed)
    histoScouting0mu = histoScouting2mu.Clone("histoScouting0mu")
    histoScouting0mu.SetFillColor(ROOT.kGreen)
    histoJpsi2mu = ROOT.TH1F("histoJpsi2mu","",100,jpsi_mass*0.9, jpsi_mass*1.1)
    histoJpsi2mu.SetFillColor(ROOT.kMagenta)
    histoJpsi1mu = histoJpsi2mu.Clone("histoJpsi1mu")
    histoJpsi1mu.SetFillColor(ROOT.kRed)
    histoJpsi0mu = histoJpsi2mu.Clone("histoJpsi0mu")
    histoJpsi0mu.SetFillColor(ROOT.kGreen)
    histoPhi2mu = ROOT.TH1F("histoPhi2mu","",100,phi_mass*0.9, phi_mass*1.1)
    histoPhi2mu.SetFillColor(ROOT.kMagenta)
    histoPhi1mu = histoPhi2mu.Clone("histoPhi1mu")
    histoPhi1mu.SetFillColor(ROOT.kRed)
    histoPhi0mu = histoPhi2mu.Clone("histoPhi0mu")
    histoPhi0mu.SetFillColor(ROOT.kGreen)
#    histoScouting = ROOT.TH1F("histoScouting","",600,0,6)
    for iev,event in enumerate(events):
        if iev%1000==0: print(iev)
        if iev>1000000:
            break
#        event.getByLabel(simTrackLabel, simTracks)
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
        
        momenta_mu = [ (mu.pt(), mu.eta(), mu.phi(), muon_mass) for mu in scoutingMuons.product()]
#        momenta_mu = []
        momenta = [ (track.tk_pt(), track.tk_eta(), track.tk_phi(), pion_mass) for track in scoutingTracks.product()]
        
#        ## debug, all jpsi pairs
#        mass1 = muon_mass
#        mass2 = muon_mass
#        if len(momenta)>=4 :
#            for i, momentum1 in enumerate(momenta): 
#                m1 = forceMass(momentum1, mass1) if mass1>0 else momentum1
#                for j, momentum2 in enumerate(momenta):
#                    if j<=i: continue  ## i < j
#                    m2 = forceMass(momentum2, mass2) if mass2>0 else momentum2
#                    mass = invariant_mass_(m1, m2)
#                    histoJpsi2mu.Fill(mass)
        
        mass = -1
        n_mu = -1
        ## search j/psi peak between 2 muons
        if len(momenta_mu)>=2 and len(momenta)>=2:
            mu_1, mu_2 = findBestPair(momenta_mu, jpsi_mass, muon_mass, muon_mass)
            mass = invariant_mass_(momenta_mu[mu_1], momenta_mu[mu_2])
            if abs(mass - jpsi_mass)>0.1:
                mass = -1
            else:
                n_mu = 2
                mu1 = momenta_mu [mu_1]
                mu2 = momenta_mu [mu_2]
        
        ## search j/psi peak between 1 muon and 1 track
        if n_mu < 0 and len(momenta_mu)>=1 and len(momenta)>=3:
            mu_1, mu_2 = findBestPairTwoCollections(momenta_mu, momenta, jpsi_mass, muon_mass, muon_mass)
            mass = invariant_mass_(momenta_mu[mu_1], forceMuonMass(momenta[mu_2]))
            if abs(mass - jpsi_mass)>0.1:
                mass = -1
            else:
                n_mu = 1
                mu1 = momenta_mu [mu_1]
                mu2 = momenta [mu_2]
        
        ## search j/psi peak between 2 tracks
        if n_mu < 0 and len(momenta)>=4 :
            mu_1, mu_2 = findBestPair(momenta, jpsi_mass, muon_mass, muon_mass)
            mass = invariant_mass_(forceMuonMass(momenta[mu_1]), forceMuonMass(momenta[mu_2]))
            mass = invariant_mass_(momenta[mu_1], momenta[mu_2])
            if abs(mass - jpsi_mass)>0.1:
                mass = -1
            else:
                n_mu = 0
                mu1 = momenta [mu_1]
                mu2 = momenta [mu_2]
        
        if n_mu == 2:
            histoJpsi2mu.Fill(mass)
        elif n_mu == 1:
            histoJpsi1mu.Fill(mass)
        elif n_mu == 0:
            histoJpsi0mu.Fill(mass)
        

        
        
        counter1 += 1
        ## reject events if none J/psi is found
        if mass<0: continue
        counter2 += 1
        
#        mu1 = scoutingMuons.product().at(0)
#        mu2 = scoutingMuons.product().at(1)
        
            
        mu1_trk = None
        mu2_trk = None
        for track in list(momenta):
#            if scoutingTrack.tk_pt()>0.:
#                if matching(0.03, mu2.trk_eta(), scoutingTrack.tk_eta(), mu2.trk_eta(), scoutingTrack.tk_eta()):
#                    print("Found Muon2")
#                    continue
#                pt = scoutingTrack.tk_pt()
#                eta = scoutingTrack.tk_eta()
#                phi = scoutingTrack.tk_phi()
#                mass = 0.14
                ### track[1] = eta, track[2] = phi
                if matching(0.0001, mu1[1], track[1], mu1[2], track[2]) and not mu1_trk: 
                    momenta.remove(track)
                    mu1_trk = 1
                elif matching(0.0001, mu2[1], track[1], mu2[2], track[2]) and not mu2_trk: 
                    momenta.remove(track)
                    mu2_trk = 1
        
        jpsi1 = ROOT.TLorentzVector()
        jpsi1.SetPtEtaPhiM(*mu1)
        jpsi2 = ROOT.TLorentzVector()
        jpsi2.SetPtEtaPhiM(*mu2)
        
        if len(momenta)<2: continue
        masses = []
        
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
        best_phi_pair = findBestPair(momenta, phi_mass, kaon_mass, kaon_mass)
        
        phi1 = ROOT.TLorentzVector()
        phi2 = ROOT.TLorentzVector()
        
    #    print(best_phi_pair)
        phi1.SetPtEtaPhiM(*forceKaonMass(momenta[best_phi_pair[0]]))
        phi2.SetPtEtaPhiM(*forceKaonMass(momenta[best_phi_pair[1]]))
        
    #        print(phi1.Pt(), phi2.Pt())
    #        masses.append((jpsi1+jpsi2).M())
#        masses.append((phi1+phi2).M())
    #    masses.append((jpsi1+jpsi2+phi1+phi2).M())
    #        print(masses)
        
        if n_mu == 2: histoPhi2mu.Fill((phi1+phi2).M())
        if n_mu == 1: histoPhi1mu.Fill((phi1+phi2).M())
        if n_mu == 0: histoPhi0mu.Fill((phi1+phi2).M())
        if abs(phi_mass - (phi1+phi2).M())>0.01: continue
        counter3 += 1
#        histoJpsi.Fill((jpsi1+jpsi2).M())
#        histoScouting.Fill((jpsi1+jpsi2+phi1+phi2).M())
        if n_mu == 2: histoScouting2mu.Fill((jpsi1+jpsi2+phi1+phi2).M())
        if n_mu == 1: histoScouting1mu.Fill((jpsi1+jpsi2+phi1+phi2).M())
        if n_mu == 0: histoScouting0mu.Fill((jpsi1+jpsi2+phi1+phi2).M())
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
        

    
    ROOT.gROOT.SetBatch(1)
    ROOT.gStyle.SetOptStat(0)
    c1 = ROOT.TCanvas("c1","",1280,1280)
    c1.SetGridx()
    c1.SetGridy()
    
    fName = inputFile
    fName = fName.replace("output","plotAllCases")
#    histo.Draw()
#    c1.SaveAs(fName)
#    c1.SaveAs(fName.replace(".root",".png"))
    
    fName = fName.replace(".", "Scouting.")
    
    
    Xmin, Xmax = 4.5, 6.5
#    f1 = ROOT.TF1("f1","gaus(0)+[3]+[4]*x", Xmin, Xmax)
    f1 = ROOT.TF1("f1","gaus(0)+gaus(3)", Xmin, Xmax)
    f1.SetParLimits(0,0,100000)
    f1.SetParLimits(3,0,100000)
    f1.SetParLimits(2,0,10)
    f1.SetParLimits(5,0,100)
    f1.SetParameters(50, 5.5, 0.05, 30, 5.5, 1)
    ## remove second gaussian
    f1.FixParameter(3,0)
    f1.FixParameter(4,0)
    
    first = "ScoutingPF"
    stack = makeStack([histoScouting2mu, histoScouting1mu, histoScouting0mu], "stack")
    hist = stack.GetStack().At(stack.GetNhists()-1)
#    hist.Draw()
    hist.Fit(f1, "", "", Xmin, Xmax)
    m, s = f1.GetParameter(1), f1.GetParameter(2)
    f1.SetRange(m-1.75*s, m+1.75*s) 
    hist.Fit(f1, "", "", m-1.75*s, m+1.75*s)
    m, s = f1.GetParameter(1), f1.GetParameter(2)
    f1.SetRange(m-1.75*s, m+1.75*s) 
    hist.Fit(f1, "", "", m-1.75*s, m+1.75*s)
#    f1.SetRange(m-1.75*s, m+1.75*s)
    f1.SetLineColor(hist.GetFillColor()+2)
    f2 = ROOT.TF1("f2","gaus(0)+gaus(3)", Xmin, Xmax)
    f2.SetParLimits(0,0,100000)
    f2.SetParLimits(3,0,100000)
    f2.SetParLimits(2,0,10)
    f2.SetParLimits(5,0,100)
    f2.SetParameters(50, 5.5, 0.05, 30, 5.5, 1)
    ## remove second gaussian
    f2.FixParameter(3,0)
    f2.FixParameter(4,0)
    
    print("Fit All: m, s: %f %f"%(f1.GetParameter(1), f1.GetParameter(2)))
    print("Integral: %f"%(f2.Integral(-1000, 1000)))
    histoScouting1mu.Fit(f2, "", "", m-1.75*s, m+1.75*s)
    m, s = f2.GetParameter(1), f2.GetParameter(2)
    f2.SetLineColor(histoScouting1mu.GetFillColor()+2)
    f2.SetRange(m-1.75*s, m+1.75*s)
    histoScouting0mu.Fit(f2, "", "", m-1.75*s, m+1.75*s)
    m, s = f2.GetParameter(1), f2.GetParameter(2)
    f2.SetRange(m-1.75*s, m+1.75*s)
    histoScouting0mu.Fit(f2, "", "", m-1.75*s, m+1.75*s)
    print("Fit 1-mu category: m, s: %f %f"%(f2.GetParameter(1), f2.GetParameter(2)))
    print("Integral: %f"%(f2.Integral(-1000, 1000)))
    
#    histoScouting0mu.Draw()
#    histoScouting2mu.Draw()
#    histoScouting1mu.Draw("same")
#    histoScouting0mu.Draw("same")
    
    print(counter1, counter2, counter3, hist.Integral())

    stack.Draw()
    
    leg = makeLegend(histoScouting2mu, histoScouting1mu, histoScouting0mu)
    leg.Draw()
    f1.Draw("same")
    f2.Draw("same")
    
    c1.SaveAs(fName)
    c1.SaveAs(fName.replace(".root",".png"))

    fName = fName.replace("Scouting","Jpsi")
    
    stack = makeStack([histoJpsi2mu, histoJpsi1mu, histoJpsi0mu], "stackJpsi")
    stack.Draw()
    
    leg = makeLegend(histoJpsi2mu, histoJpsi1mu, histoJpsi0mu)
    leg.Draw()
    c1.SaveAs(fName)
    c1.SaveAs(fName.replace(".root",".png"))
    
    fName = fName.replace("Jpsi","Phi")
    
    stack = makeStack([histoPhi2mu, histoPhi1mu, histoPhi0mu], "stackPhi")
    stack.Draw()
    
    leg = makeLegend(histoPhi2mu, histoPhi1mu, histoPhi0mu)
    leg.Draw()
    c1.SaveAs(fName)
    c1.SaveAs(fName.replace(".root",".png"))
    
    


