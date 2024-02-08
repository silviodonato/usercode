import ROOT
from DataFormats.FWLite import Handle, Events
from FWCore.ParameterSet.VarParsing import VarParsing

import math

pion_mass = 0.140
kaon_mass = 0.494

jpsi_mass = 3.097
phi_mass = 0.95

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


options = VarParsing ('analysis')

options.maxEvents = 1000000
options.inputFiles = ["/eos/cms//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/21a72136-634d-4377-9077-5d708302fc46.root"]
#options.secondaryInputFiles = [
#]

print(options.maxEvents)
print(options.inputFiles)
print(options.secondaryInputFiles)

#file_ = ROOT.TFile.Open("/eos/cms//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/21a72136-634d-4377-9077-5d708302fc46.root")
#events = file_.Get("Events")
#events.SetBranchStatus("*", 0)
#events.SetBranchStatus("*SimTrack*g4SimHits*", 1)

def forceMass(momentum, mass):
    momentum = (momentum[0], momentum[1], momentum[2], mass)
    return momentum

def forcePionMass(momentum):
    return forceMass(momentum, pion_mass)

def forceKaonMass(momentum):
    return forceMass(momentum, kaon_mass)

def getInvariantMasses(momenta):
    masses = []
    best_jpsi_pair = (-1, -1)
    best_jpsi_mass = 10000
    
    best_phi_pair = (-1, -1)
    best_phi_mass = 10000

    for i, momentum1 in enumerate(momenta):
        for j, momentum2 in enumerate(momenta):
            if j<=i: continue
            
            mass = invariant_mass_(forcePionMass(momentum1), forcePionMass(momentum2))
            if abs(mass - jpsi_mass) < abs(mass - best_jpsi_mass):
                best_jpsi_mass = mass
                best_jpsi_pair = (i, j)
    
    for i, momentum1 in enumerate(momenta):
        if i == best_jpsi_pair[0] or i == best_jpsi_pair[1] : continue
        for j, momentum2 in enumerate(momenta):
            if j == best_jpsi_pair[0] or j == best_jpsi_pair[1] : continue
            if j<=i: continue
            mass = invariant_mass_(forceKaonMass(momentum1), forceKaonMass(momentum2))
            if abs(mass - phi_mass) < abs(mass - best_phi_mass):
                best_phi_mass = mass
                best_phi_pair = (i, j)
    
    jpsi1 = ROOT.TLorentzVector()
    jpsi2 = ROOT.TLorentzVector()
    phi1 = ROOT.TLorentzVector()
    phi2 = ROOT.TLorentzVector()
    
    if best_phi_pair[1]<0: return []
    
    jpsi1.SetPtEtaPhiM(*forcePionMass(momenta[best_jpsi_pair[0]]))
    jpsi2.SetPtEtaPhiM(*forcePionMass(momenta[best_jpsi_pair[1]]))
    phi1.SetPtEtaPhiM(*forceKaonMass(momenta[best_phi_pair[0]]))
    phi2.SetPtEtaPhiM(*forceKaonMass(momenta[best_phi_pair[1]]))
    
    masses.append((jpsi1+jpsi2).M())
    masses.append((phi1+phi2).M())
    masses.append((jpsi1+jpsi2+phi1+phi2).M())
    return masses
#                print(i)


events = Events (options)

simTracks, simTrackLabel = Handle("vector<SimTrack>"), ("g4SimHits","","SIM")
scoutingTracks, scoutingTrackLabel = Handle("vector<Run3ScoutingTrack>"), ("hltScoutingTrackPacker","","HLT")

histo = ROOT.TH1F("histo","",1000,0,10)
histoScouting = ROOT.TH1F("histoScouting","",1000,0,20)
for iev,event in enumerate(events):
    print(iev)
    event.getByLabel(simTrackLabel, simTracks)
    event.getByLabel(scoutingTrackLabel, scoutingTracks)
    
    momenta = []
    for simTrack in simTracks.product():
        if simTrack.momentum().pt()>2.5 and simTrack.charge()!=0:
            pt = simTrack.momentum().pt()
            eta = simTrack.momentum().eta()
            phi = simTrack.momentum().phi()
            mass = max(1E-9, simTrack.momentum().mass())
#            mass = 0.14
            momenta.append((pt, eta, phi, mass))
    masses = getInvariantMasses(momenta)
    for mass in masses: histo.Fill(mass)
    
    momenta = []
    for scoutingTrack in scoutingTracks.product():
        if scoutingTrack.tk_pt()>2.5 and scoutingTrack.tk_vtxInd() == 0 :
            pt = scoutingTrack.tk_pt()
            eta = scoutingTrack.tk_eta()
            phi = scoutingTrack.tk_phi()
            mass = 0.14
            momenta.append((pt, eta, phi, mass))
    masses = getInvariantMasses(momenta)
    for mass in masses: histoScouting.Fill(mass)
    
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
    
    if iev>1000:
        break

ROOT.gROOT.SetBatch(1)
c1 = ROOT.TCanvas("c1")
histo.Draw()
c1.SaveAs("plot.png")
c1.SaveAs("plot.root")

histoScouting.Draw()
c1.SaveAs("plotScouting.png")
c1.SaveAs("plotScouting.root")

