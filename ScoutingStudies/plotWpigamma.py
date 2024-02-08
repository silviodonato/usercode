import ROOT
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

def invariant_mass3(pt1, pt2, pt3, eta1, eta2, eta3, phi1, phi2, phi3, mass1, mass2, mass3):
    # Convert eta and phi to Cartesian coordinates
    px1 = pt1 * math.cos(phi1)
    py1 = pt1 * math.sin(phi1)
    pz1 = pt1 * math.sinh(eta1)
    E1 = math.sqrt(px1**2 + py1**2 + pz1**2 + mass1**2)
    
    px2 = pt2 * math.cos(phi2)
    py2 = pt2 * math.sin(phi2)
    pz2 = pt2 * math.sinh(eta2)
    E2 = math.sqrt(px2**2 + py2**2 + pz2**2 + mass2**2)
    
    px3 = pt3 * math.cos(phi3)
    py3 = pt3 * math.sin(phi3)
    pz3 = pt3 * math.sinh(eta3)
    E3 = math.sqrt(px3**2 + py3**2 + pz3**2 + mass3**2)
    
    # Calculate invariant mass
    invariant_mass = math.sqrt((E1 + E2 + E3)**2 - (px1 + px2 + px3)**2 - (py1 + py2 + py3)**2 - (pz1 + pz2 + pz3)**2)
    
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
    
options = VarParsing ('analysis')

options.maxEvents = 1000000
#options.inputFiles = ["outputScoutingPF__.root"]
#options.inputFiles = ["outputScoutingPF.root"]
#options.inputFiles = ["outputScoutingPF_noAddTracks.root"]

for inputFile in [
    "outputScoutingPF_Wpigamma_pt999.root",
    "outputScoutingPF_Wpigamma_pt0.root",
    "outputScoutingPF_Wpigamma_pt1.root",
    "outputScoutingPF_Wpigamma_pt5.root",
    "outputScoutingPF_Wpigamma_pt7.root",
    "outputScoutingPF_Wpigamma_pt10.root",
    "outputScoutingPF_Wpigamma_pt20.root",
]:
    options.inputFiles.clear()
    options.inputFiles = [inputFile]
    #options.inputFiles = ["outputScoutingPF_original.root"]

    #options.secondaryInputFiles = [
    #]

    print(options.maxEvents)
    print(options.inputFiles)
    print(options.secondaryInputFiles)

    #file_ = ROOT.TFile.Open("/eos/cms//store/mc/Run3Winter24Digi/BsToJpsiPhi_KMuFilter_SoftQCDnonD_TuneCP5_13p6TeV-pythia8-evtgen/GEN-SIM-RAW/133X_mcRun3_2024_realistic_v8-v2/80000/21a72136-634d-4377-9077-5d708302fc46.root")
    #events = file_.Get("Events")
    #events.SetBranchStatus("*", 0)
    #events.SetBranchStatus("*scoutingPfCandidate*g4SimHits*", 1)



    #def twoLeadingCandidates(collection):
    #    
    from DataFormats.FWLite import Handle, Events
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
        if iev%100==0: print(iev)
        event.getByLabel(pfCandidateLabel, pfCandidates)
        event.getByLabel(scoutingPfCandidateLabel, scoutingPfCandidates)
        event.getByLabel(photonLabel, photons)
        event.getByLabel(trackLabel, tracks)
        event.getByLabel(pixelTrackLabel, pixelTracks)
        if len(photons.product())==0: continue
#        if len([obj for obj in scoutingTracks.product() if obj.tk_charge()==-1])==0: continue
#        if len([obj for obj in scoutingTracks.product() if obj.tk_charge()==+1])==0: continue
#        if len([obj for obj in scoutingTracks.product()])<3: continue
    #    scoutingTracks = scoutingTracks.product()
    #    scoutingPfCandidates = scoutingPfCandidates.product()
    #    photons = photons.product()
        
#        print("ScoutingPF")
        pion = max([obj for obj in scoutingPfCandidates.product() if abs(obj.pdgId())==211], key=lambda obj: obj.pt())
        photon = max([obj for obj in photons.product()], key=lambda obj: obj.pt())
        mass = invariant_mass(pion.pt(), photon.pt(), pion.eta(), photon.eta(), pion.phi(), photon.phi(), pion_mass, 0)
        histos["ScoutingPF"].Fill(mass)
        
##        print("ScoutingPFtrk")
        pion = max([obj for obj in scoutingPfCandidates.product() if abs(obj.pdgId())==211], key=lambda obj: obj.pt() + obj.trk_pt())
#        photon = max([obj for obj in photons.product()], key=lambda obj: obj.tpt())
        mass = invariant_mass(pion.pt() + pion.trk_pt(), photon.pt(), pion.eta() + pion.trk_eta(), photon.eta(), pion.phi() + pion.trk_phi(), photon.phi(), pion_mass, 0)
        histos["ScoutingPFtrk"].Fill(mass)
#        
##        print("ScoutingTrack")
        pion = max([obj for obj in scoutingTracks.product()], key=lambda obj: obj.tk_pt())
#        photon = max([obj for obj in photons.product()], key=lambda obj: obj.tpt())
        mass = invariant_mass(pion.tk_pt(), photon.pt(), pion.tk_eta(), photon.eta(), pion.tk_phi(), photon.phi(), pion_mass, 0)
        histos["ScoutingTrack"].Fill(mass)
        
        if iev>10000:
            break
    
    del events
    ROOT.gROOT.SetBatch(1)
    c1 = ROOT.TCanvas("c1")
    
    first = "ScoutingPF"
    histos[first].SetMaximum(histos[first].GetMaximum()*2)
    histos[first].Draw()
    
    for i, histo in enumerate(histos.values()):
        if histo!=first:
            histo.Draw("same")
    
    leg = ROOT.TLegend(0.1,0.7,0.48,0.9)
    for name in histos:
        leg.AddEntry(histos[name], name, "l")
    
    leg.Draw()

    fName = inputFile
    fName = fName.replace("output","plot")
    c1.SaveAs(fName)
    c1.SaveAs(fName.replace(".root",".png"))


