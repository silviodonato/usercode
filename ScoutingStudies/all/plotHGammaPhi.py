import ROOT
from DataFormats.FWLite import Handle, Events
from FWCore.ParameterSet.VarParsing import VarParsing

pion_mass = 0.140
kaon_mass = 0.494

jpsi_mass = 3.097
phi_mass = 0.95

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
#options.inputFiles = ["outputScoutingPF__.root"]
options.inputFiles = ["outputScoutingPF.root"]
#options.secondaryInputFiles = [
#]

print(options.maxEvents)
print(options.inputFiles)
print(options.secondaryInputFiles)

#file_ = ROOT.TFile.Open("/eos/cms//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/21a72136-634d-4377-9077-5d708302fc46.root")
#events = file_.Get("Events")
#events.SetBranchStatus("*", 0)
#events.SetBranchStatus("*scoutingPfCandidate*g4SimHits*", 1)

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


def get_two_largest_objects(objs):
    # Check if the collection is empty
    if not objs:
        return None, None
    
    # Get the two objects with the largest pt() values
    largest_obj = max(objs, key=lambda obj: obj.pt())
    objs.remove(largest_obj)  # Remove the first largest object
    second_largest_obj = max(objs, key=lambda obj: obj.pt())
    
    return largest_obj, second_largest_obj

#def twoLeadingCandidates(collection):
#    

events = Events (options)

pixelTracks, pixelTrackLabel = Handle("vector<reco::Track>"), ("hltPixelTracks","","HLTX")
tracks, trackLabel = Handle("vector<reco::Track>"), ("hltMergedTracks","","HLTX")
photons, photonLabel = Handle("vector<Run3ScoutingPhoton>"), ("hltScoutingEgammaPacker","","HLTX")
scoutingPfCandidates, scoutingPfCandidateLabel = Handle("vector<Run3ScoutingParticle>"), ("hltScoutingPFPacker","","HLTX")
pfCandidates, pfCandidateLabel = Handle("vector<reco::PFCandidate>"), ("hltParticleFlow","","HLTX")
scoutingTracks, scoutingTrackLabel = Handle("vector<Run3ScoutingTrack>"), ("hltScoutingTrackPacker","","HLTX")

tmp = ROOT.TH1F("tmp","",20,0,160)
histos = {}
for name in ["ScoutingPF", "ScoutingTrack", "ScoutingPFtrk", "HLTPFlow", "HLTtrack", "HLTpixelTrack"]:
    histos[name] = tmp.Clone(name)

histos["ScoutingPF"].SetLineColor(ROOT.kRed)
histos["ScoutingTrack"].SetLineColor(ROOT.kBlue)
histos["ScoutingPFtrk"].SetLineColor(ROOT.kBlack)
histos["HLTPFlow"].SetLineColor(ROOT.kGreen)
histos["HLTtrack"].SetLineColor(ROOT.kGray)
histos["HLTpixelTrack"].SetLineColor(ROOT.kMagenta)

for iev,event in enumerate(events):
    event.getByLabel(scoutingTrackLabel, scoutingTracks)
    if not scoutingTracks.isValid(): continue ##skip events without scoutin tracks
    print(iev)
    event.getByLabel(pfCandidateLabel, pfCandidates)
    event.getByLabel(scoutingPfCandidateLabel, scoutingPfCandidates)
    event.getByLabel(photonLabel, photons)
    event.getByLabel(trackLabel, tracks)
    event.getByLabel(pixelTrackLabel, pixelTracks)
    if len([obj for obj in scoutingTracks.product() if obj.tk_charge()==-1])==0: continue
    if len([obj for obj in scoutingTracks.product() if obj.tk_charge()==+1])==0: continue
#    scoutingTracks = scoutingTracks.product()
#    scoutingPfCandidates = scoutingPfCandidates.product()
#    photons = photons.product()
    
    print("ScoutingPF")
    pion_p = max([obj for obj in scoutingPfCandidates.product() if obj.pdgId()==211], key=lambda obj: obj.pt())
    pion_m = max([obj for obj in scoutingPfCandidates.product() if obj.pdgId()==-211], key=lambda obj: obj.pt())
    pion_3 = max([obj for obj in scoutingPfCandidates.product() if obj!=pion_m and obj!=pion_p], key=lambda obj: obj.pt())
    mass = invariant_mass(pion_p.pt(), pion_m.pt(), pion_p.eta(), pion_m.eta(), pion_p.phi(), pion_m.phi(), pion_mass, pion_mass)
    print(mass , pion_p.pt(), pion_m.pt())
    histos["ScoutingPF"].Fill(mass)
    
    print("ScoutingPFtrk")
    pion_p = max([obj for obj in scoutingPfCandidates.product() if obj.pdgId()==211], key=lambda obj: obj.trk_pt())
    pion_m = max([obj for obj in scoutingPfCandidates.product() if obj.pdgId()==-211], key=lambda obj: obj.trk_pt())
    pion_3 = max([obj for obj in scoutingPfCandidates.product() if obj!=pion_m and obj!=pion_p], key=lambda obj: obj.trk_pt())
    mass = invariant_mass(pion_p.trk_pt(), pion_m.trk_pt(), pion_p.trk_eta(), pion_m.trk_eta(), pion_p.trk_phi(), pion_m.trk_phi(), pion_mass, pion_mass)
    print(mass , pion_p.pt(), pion_m.pt())
    histos["ScoutingPFtrk"].Fill(mass)
    
    print("ScoutingTrack")
    pion_p = max([obj for obj in scoutingTracks.product() if obj.tk_charge()==1], key=lambda obj: obj.tk_pt())
    pion_m = max([obj for obj in scoutingTracks.product() if obj.tk_charge()==-1], key=lambda obj: obj.tk_pt())
    pion_3 = max([obj for obj in scoutingTracks.product() if obj!=pion_m and obj!=pion_p], key=lambda obj: obj.trk_pt())
    mass = invariant_mass(pion_p.tk_pt(), pion_m.tk_pt(), pion_p.tk_eta(), pion_m.tk_eta(), pion_p.tk_phi(), pion_m.tk_phi(), pion_mass, pion_mass)
    print(mass , pion_p.tk_pt(), pion_m.tk_pt())
    histos["ScoutingTrack"].Fill(mass)
    
    print("HLTPFlow")
    pion_p = max([obj for obj in pfCandidates.product() if obj.pdgId()==211], key=lambda obj: obj.pt())
    pion_m = max([obj for obj in pfCandidates.product() if obj.pdgId()==-211], key=lambda obj: obj.pt())
    pion_3 = max([obj for obj in pfCandidates.product() if obj!=pion_m and obj!=pion_p], key=lambda obj: obj.pt())
    mass = invariant_mass(pion_p.pt(), pion_m.pt(), pion_p.eta(), pion_m.eta(), pion_p.phi(), pion_m.phi(), pion_mass, pion_mass)
    print(mass , pion_p.pt(), pion_m.pt())
    histos["HLTPFlow"].Fill(mass)
    
    print("HLTtrack")
    pion_p = max([obj for obj in tracks.product() if obj.charge()==1], key=lambda obj: obj.pt())
    pion_m = max([obj for obj in tracks.product() if obj.charge()==-1], key=lambda obj: obj.pt())
    pion_3 = max([obj for obj in tracks.product() if obj!=pion_m and obj!=pion_p], key=lambda obj: obj.pt())
    mass = invariant_mass(pion_p.pt(), pion_m.pt(), pion_p.eta(), pion_m.eta(), pion_p.phi(), pion_m.phi(), pion_mass, pion_mass)
    print(mass , pion_p.pt(), pion_m.pt())
    histos["HLTtrack"].Fill(mass)
    
    print("HLTpixelTrack")
    pion_p = max([obj for obj in pixelTracks.product() if obj.charge()==1], key=lambda obj: obj.pt())
    pion_m = max([obj for obj in pixelTracks.product() if obj.charge()==-1], key=lambda obj: obj.pt())
    pion_3 = max([obj for obj in pixelTracks.product() if obj!=pion_m and obj!=pion_p], key=lambda obj: obj.pt())
    mass = invariant_mass(pion_p.pt(), pion_m.pt(), pion_p.eta(), pion_m.eta(), pion_p.phi(), pion_m.phi(), pion_mass, pion_mass)
    print(mass , pion_p.pt(), pion_m.pt())
    histos["HLTpixelTrack"].Fill(mass)
#    1/0
#    
#    
#    for pf in scoutingPfCandidates.product():
#        if pf.pt()<5: continue
#        print(pf.eta(), pf.phi(), pf.pt(), pf.trk_pt(), pf.pdgId())
#    
#    print("Scouting Track")
#    for track in scoutingTracks.product():
#        if track.tk_pt()<5: continue
#        print(track.tk_eta(), track.tk_phi(), track.tk_pt(), track.tk_charge())
#    
#    print("Scouting Photon")
#    for photon in photons.product():
#        if photon.pt()<5: continue
#        print(photon.eta(), photon.phi(), photon.pt())
#    
#    print("Full Track")
#    for track in tracks.product():
#        if track.pt()<5: continue
#        print(track.eta(), track.phi(), track.pt(), track.charge())
#    
#    print("HLT PF Candidates")
#    for pf in pfCandidates.product():
#        if pf.pt()<5: continue
#        print(pf.eta(), pf.phi(), pf.pt(), pf.charge(), pf.pdgId())
    
#    track_pt = [p.tk_pt () for p in scoutingTracks.product()]
#    pf_pt = [p.pt () for p in scoutingPfCandidates.product()]
#    pf_tkpt = [p.trk_pt () for p in scoutingPfCandidates.product()]
#    photons_pt = [p.pt () for p in photons.product()]
    
#    print()
#    print("photons_pt")
#    for pt in sorted(photons_pt): 
#        if pt>1: print(pt)
#    print()
#    print("pf_pt")
#    for pt in sorted(pf_pt): 
#        if pt>1: print(pt)
#    print()
#    print("pf_tkpt")
#    for pt in sorted(pf_tkpt): 
#        if pt>1: print(pt)
#    print()
#    print("track_pt")
#    for pt in sorted(track_pt): 
#        if pt>1: print(pt)
#    
#    momenta = []
#    for scoutingPfCandidate in scoutingPfCandidates.product():
#        if scoutingPfCandidate.momentum().pt()>2.5 and scoutingPfCandidate.charge()!=0:
#            pt = scoutingPfCandidate.momentum().pt()
#            eta = scoutingPfCandidate.momentum().eta()
#            phi = scoutingPfCandidate.momentum().phi()
#            mass = max(1E-9, scoutingPfCandidate.momentum().mass())
##            mass = 0.14
#            momenta.append((pt, eta, phi, mass))
#    masses = getInvariantMasses(momenta)
#    for mass in masses: histo.Fill(mass)
#    
#    momenta = []
#    for scoutingTrack in scoutingTracks.product():
#        if scoutingTrack.tk_pt()>2.5 and scoutingTrack.tk_vtxInd() == 0 :
#            pt = scoutingTrack.tk_pt()
#            eta = scoutingTrack.tk_eta()
#            phi = scoutingTrack.tk_phi()
#            mass = 0.14
#            momenta.append((pt, eta, phi, mass))
#    masses = getInvariantMasses(momenta)
#    for mass in masses: histoScouting.Fill(mass)
#    
##        if scoutingPfCandidate.momentum().pt()>2 and scoutingPfCandidate.charge()!=0:
##            print(scoutingPfCandidate.momentum().pt(), scoutingPfCandidate.type(), scoutingPfCandidate.trackId(), scoutingPfCandidate.genpartIndex())
##            for scoutingPfCandidate2 in scoutingPfCandidates.product():
##                if scoutingPfCandidate2.momentum().pt()>2 and scoutingPfCandidate2.charge()!=0 and scoutingPfCandidate2!=scoutingPfCandidate:
##                    for scoutingPfCandidate3 in scoutingPfCandidates.product():
##                        if scoutingPfCandidate3.momentum().pt()>2 and scoutingPfCandidate3.charge()!=0 and scoutingPfCandidate3!=scoutingPfCandidate and scoutingPfCandidate3!=scoutingPfCandidate2:
##                            for scoutingPfCandidate4 in scoutingPfCandidates.product():
##                                if scoutingPfCandidate4.momentum().pt()>2 and scoutingPfCandidate4.charge()!=0 and scoutingPfCandidate4!=scoutingPfCandidate and scoutingPfCandidate4!=scoutingPfCandidate2 and scoutingPfCandidate4!=scoutingPfCandidate3:
##                                    histo.Fill((scoutingPfCandidate.momentum()+scoutingPfCandidate2.momentum()+scoutingPfCandidate3.momentum()+scoutingPfCandidate4.momentum()).M())
##                    histo.Fill(invariant_mass(scoutingPfCandidate.momentum().pt(), scoutingPfCandidate2.momentum().pt(), scoutingPfCandidate.momentum().eta(), scoutingPfCandidate2.momentum().eta(), scoutingPfCandidate.momentum().phi(), scoutingPfCandidate2.momentum().phi(), max(1E-3, scoutingPfCandidate.momentum().mass()), max(1E-3, scoutingPfCandidate2.momentum().mass())))
##                for scoutingPfCandidate2 in scoutingPfCandidates.product():
##                    if scoutingPfCandidate2.momentum().pt()>2 and scoutingPfCandidate2.charge()!=0:
##                    histo.Fill(invariant_mass(scoutingPfCandidate.momentum().pt(), scoutingPfCandidate2.momentum().pt(), scoutingPfCandidate.momentum().eta(), scoutingPfCandidate2.momentum().eta(), scoutingPfCandidate.momentum().phi(), scoutingPfCandidate2.momentum().phi(), 0, 1E-3))
#    
##    for scoutingTrack in scoutingTracks.product():
##        if scoutingTrack.tk_pt()>2:
###            print(scoutingTrack.momentum().pt(), scoutingTrack.type(), scoutingTrack.trackId(), scoutingTrack.genpartIndex())
##            for scoutingTrack2 in scoutingTracks.product():
##                if scoutingTrack2.tk_pt()>2 and scoutingTrack2!=scoutingTrack:
##                    tk1 = scoutingTrack
##                    tk2 = scoutingTrack2
##                    histoScouting.Fill(invariant_mass(tk1.tk_pt(), tk2.tk_pt(), tk1.tk_eta(), tk2.tk_eta(), tk1.tk_phi(), tk2.tk_phi(), 0.14, 0.14))
#    
    if iev>10000:
        break


ROOT.gROOT.SetBatch(1)
c1 = ROOT.TCanvas("c1")


for i, histo in enumerate(histos.values()):
    if i==0:
        histo.Draw()
    else:
        histo.Draw("same")

c1.SaveAs("plot.png")
c1.SaveAs("plot.root")


