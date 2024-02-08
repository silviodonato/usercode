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
inputFile = "outputScoutingPF_TopMuE_pt0.root"
options.inputFiles = [ inputFile ]
#options.secondaryInputFiles = [
#]

print(options.maxEvents)
print(options.inputFiles)
print(options.secondaryInputFiles)

#file_ = ROOT.TFile.Open("/eos/cms//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/21a72136-634d-4377-9077-5d708302fc46.root")
#events = file_.Get("Events")
#events.SetBranchStatus("*", 0)
#events.SetBranchStatus("*offlineTrack*g4SimHits*", 1)

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
    
    momenta = sorted(momenta)
    
    if len(momenta)<4: return []
    
    mass = invariant_mass_(forcePionMass(momenta[1]), forcePionMass(momenta[2]))
    masses.append(mass)
    return masses
    
    for i, momentum1 in enumerate(momenta):
        for j, momentum2 in enumerate(momenta):
            if j<=i: continue
            if abs(momentum1[1] - momentum2[1])>0.5 or abs(momentum1[2] - momentum2[2])>0.5: continue
            mass = invariant_mass_(forcePionMass(momentum1), forcePionMass(momentum2))
            if abs(mass - jpsi_mass) < abs(mass - best_jpsi_mass):
                best_jpsi_mass = mass
                best_jpsi_pair = (i, j)
    
    return masses

    
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
    
#    masses.append((jpsi1+jpsi2).M())
#    masses.append((phi1+phi2).M())
#    masses.append((jpsi1+jpsi2+phi1+phi2).M())
    return masses
#                print(i)


events = Events (options)

#offlineTracks, offlineTrackLabel = Handle("vector<offlineTrack>"), ("g4SimHits","","SIM")
scoutingTracks, scoutingTrackLabel = Handle("vector<Run3ScoutingTrack>"), ("hltScoutingTrackPacker","","HLTX")
offlineTracks, offlineTrackLabel = Handle("vector<reco::Track>"), ("generalTracks","","RECO")
primaryVertexs, primaryVertexLabel = Handle("vector<reco::Vertex>"), ("offlinePrimaryVertices","","RECO")

histo = ROOT.TH1F("histo","",200,0,20)
histoScouting = ROOT.TH1F("histoScouting","",200,0,20)
for iev,event in enumerate(events):
    if iev%100==0: print(iev)
    event.getByLabel(offlineTrackLabel, offlineTracks)
    event.getByLabel(scoutingTrackLabel, scoutingTracks)
    event.getByLabel(primaryVertexLabel, primaryVertexs)
    if not scoutingTracks.isValid(): continue
    
    pv = primaryVertexs.product().at(0).z()
    momenta = []
    for offlineTrack in offlineTracks.product():
        if offlineTrack.pt()>1 and offlineTrack.charge()!=0 and abs(offlineTrack.vz()-pv)<0.1 and abs(offlineTrack.dxy()/offlineTrack.dxyError())>20 and  abs(offlineTrack.dxy())>0 and offlineTrack.ndof()>0 and offlineTrack.chi2()/offlineTrack.ndof()<2000:
            pt = offlineTrack.pt()
            eta = offlineTrack.eta()
            phi = offlineTrack.phi()
            mass = pion_mass
#            mass = max(1E-9, offlineTrack.mass())
            mass = 0.14
            momenta.append((pt, eta, phi, mass))
#            histo.Fill(mass)
    masses = getInvariantMasses(momenta)
    for mass in masses: histo.Fill(mass)
    
    momenta = []
    for scoutingTrack in scoutingTracks.product():
        if scoutingTrack.tk_pt()>0  and scoutingTrack.tk_vtxInd() == 0: #  and abs(scoutingTrack.tk_dxy()/scoutingTrack.tk_dxy_Error())<15
            pt = scoutingTrack.tk_pt()
            eta = scoutingTrack.tk_eta()
            phi = scoutingTrack.tk_phi()
            mass = 0.14
            momenta.append((pt, eta, phi, mass))
    masses = getInvariantMasses(momenta)
    for mass in masses: histoScouting.Fill(mass)
    
#        if offlineTrack.momentum().pt()>2 and offlineTrack.charge()!=0:
#            print(offlineTrack.momentum().pt(), offlineTrack.type(), offlineTrack.trackId(), offlineTrack.genpartIndex())
#            for offlineTrack2 in offlineTracks.product():
#                if offlineTrack2.momentum().pt()>2 and offlineTrack2.charge()!=0 and offlineTrack2!=offlineTrack:
#                    for offlineTrack3 in offlineTracks.product():
#                        if offlineTrack3.momentum().pt()>2 and offlineTrack3.charge()!=0 and offlineTrack3!=offlineTrack and offlineTrack3!=offlineTrack2:
#                            for offlineTrack4 in offlineTracks.product():
#                                if offlineTrack4.momentum().pt()>2 and offlineTrack4.charge()!=0 and offlineTrack4!=offlineTrack and offlineTrack4!=offlineTrack2 and offlineTrack4!=offlineTrack3:
#                                    histo.Fill((offlineTrack.momentum()+offlineTrack2.momentum()+offlineTrack3.momentum()+offlineTrack4.momentum()).M())
#                    histo.Fill(invariant_mass(offlineTrack.momentum().pt(), offlineTrack2.momentum().pt(), offlineTrack.momentum().eta(), offlineTrack2.momentum().eta(), offlineTrack.momentum().phi(), offlineTrack2.momentum().phi(), max(1E-3, offlineTrack.momentum().mass()), max(1E-3, offlineTrack2.momentum().mass())))
#                for offlineTrack2 in offlineTracks.product():
#                    if offlineTrack2.momentum().pt()>2 and offlineTrack2.charge()!=0:
#                    histo.Fill(invariant_mass(offlineTrack.momentum().pt(), offlineTrack2.momentum().pt(), offlineTrack.momentum().eta(), offlineTrack2.momentum().eta(), offlineTrack.momentum().phi(), offlineTrack2.momentum().phi(), 0, 1E-3))
    
#    for scoutingTrack in scoutingTracks.product():
#        if scoutingTrack.tk_pt()>2:
##            print(scoutingTrack.momentum().pt(), scoutingTrack.type(), scoutingTrack.trackId(), scoutingTrack.genpartIndex())
#            for scoutingTrack2 in scoutingTracks.product():
#                if scoutingTrack2.tk_pt()>2 and scoutingTrack2!=scoutingTrack:
#                    tk1 = scoutingTrack
#                    tk2 = scoutingTrack2
#                    histoScouting.Fill(invariant_mass(tk1.tk_pt(), tk2.tk_pt(), tk1.tk_eta(), tk2.tk_eta(), tk1.tk_phi(), tk2.tk_phi(), 0.14, 0.14))
    
    if iev>10000000:
        break

ROOT.gROOT.SetBatch(1)
c1 = ROOT.TCanvas("c1")
histoScouting.Draw()
fName = inputFile
fName = fName.replace("output","plot_scouting")
c1.SaveAs(fName)
c1.SaveAs(fName.replace(".root",".png"))


histo.Draw()
fName = inputFile
fName = fName.replace("output","plot")
c1.SaveAs(fName)
c1.SaveAs(fName.replace(".root",".png"))

