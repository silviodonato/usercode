# https://cmsweb.cern.ch/das/request?input=dataset%3D%2FMET%2FRun2018D-UL2018_MiniAODv2_NanoAODv9-v1%2FNANOAOD&instance=prod/global
# 

# https://cmsweb.cern.ch/das/request?view=plain&limit=50&instance=prod%2Fglobal&input=file+dataset%3D%2FEGamma%2FRun2018D-UL2018_MiniAODv2_NanoAODv9-v3%2FNANOAOD
#"/store/data/Run2018D/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v3/230000/02C2D9F5-BC4F-4949-B173-B4820840EF37.root"

fName = "/store/data/Run2018D/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v3/230000/00D736B9-1F44-E244-AD50-FBCD58B72EF9.root"
prefix = "root://cms-xrd-global.cern.ch/"

fName = "/store/data/Run2018D/MET/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/130000/5F6D5A27-518E-7941-9758-B8062B4747A8.root"
prefix = "root://cms-xrd-global.cern.ch/"

#local file
fName = "met.root"
prefix = ""


import ROOT

fil = ROOT.TFile.Open(prefix+fName)
events = fil.Events

L1_triggers = ["L1_SingleMu22","L1_SingleMu25"]

histos = {}
histos["den"] = ROOT.TH1F("den","Efficiecy",50,0,50)
for L1_seed in L1_triggers:
    histos[L1_seed] = histos["den"].Clone(L1_seed)

histo = ROOT.TH1F("histo","Efficiecy",50,0,50)

#get first event
print("Loop")
for i, event in enumerate(events):
    if i%1000==0: print("Event %d"%i)
    if event.HLT_PFMETNoMu120_PFMHTNoMu120_IDTight:
        muonPt = -1
        for i in range(event.nMuon):
            if (event.HLT_IsoMu24 and event.Muon_mediumId[i]>0) and (abs(event.Muon_eta[i])<2.4) and (event.Muon_pfIsoId[i]==3):
                muonPt = max(muonPt, event.Muon_pt[i])
        if muonPt>0:
            histos["den"].Fill(muonPt)
            for L1_seed in L1_triggers:
                if getattr(event,L1_seed):
                    histos[L1_seed].Fill(muonPt)# https://cmsweb.cern.ch/das/request?input=dataset%3D%2FMET%2FRun2018D-UL2018_MiniAODv2_NanoAODv9-v1%2FNANOAOD&instance=prod/global
# 

# https://cmsweb.cern.ch/das/request?view=plain&limit=50&instance=prod%2Fglobal&input=file+dataset%3D%2FEGamma%2FRun2018D-UL2018_MiniAODv2_NanoAODv9-v3%2FNANOAOD
#"/store/data/Run2018D/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v3/230000/02C2D9F5-BC4F-4949-B173-B4820840EF37.root"

fName = "/store/data/Run2018D/EGamma/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v3/230000/00D736B9-1F44-E244-AD50-FBCD58B72EF9.root"
prefix = "root://cms-xrd-global.cern.ch/"

fName = "/store/data/Run2018D/MET/NANOAOD/UL2018_MiniAODv2_NanoAODv9-v1/130000/5F6D5A27-518E-7941-9758-B8062B4747A8.root"
prefix = "root://cms-xrd-global.cern.ch/"

#local file
fName = "met.root"
prefix = ""


import ROOT

fil = ROOT.TFile.Open(prefix+fName)
events = fil.Events

L1_triggers = ["L1_SingleMu22","L1_SingleMu25"]

histos = {}
histos["den"] = ROOT.TH1F("den","Efficiency",50,0,50)
for L1_seed in L1_triggers:
    histos[L1_seed] = histos["den"].Clone(L1_seed)

histo = ROOT.TH1F("histo","Efficiecy",50,0,50)

#get first event
print("Loop")
for i, event in enumerate(events):
    if i%1000==0: print("Event %d"%i)
    if event.HLT_PFMETNoMu120_PFMHTNoMu120_IDTight:
        muonPt = -1
        for i in range(event.nMuon):
            if (event.Muon_mediumId[i]>0) and (abs(event.Muon_eta[i])<2.4) and (event.Muon_pfIsoId[i]==3):
                muonPt = max(muonPt, event.Muon_pt[i])
        if muonPt>0:
            histos["den"].Fill(muonPt)
            if event.HLT_IsoMu24:
                for L1_seed in L1_triggers:
                    if getattr(event,L1_seed):
                        histos[L1_seed].Fill(muonPt)
#    if i>10000:
#        break


leg = ROOT.TLegend(0.1,0.7,0.48,0.9)
#leg.SetHeader("")

eff = {}
for L1_seed in L1_triggers:
    eff[L1_seed] = histos["den"].Clone("eff"+L1_seed)
    eff[L1_seed].Reset()
    eff[L1_seed].Divide(histos[L1_seed], histos["den"])
    eff[L1_seed].SetLineWidth(2)

eff["L1_SingleMu22"].SetLineColor(ROOT.kRed)
eff["L1_SingleMu25"].SetLineColor(ROOT.kBlue)

ROOT.gStyle.SetOptStat(0)
first = True
for L1_seed in L1_triggers:
    leg.AddEntry(eff[L1_seed],L1_seed)
    if first:
        eff[L1_seed].Draw("")
        first = False
    else:
        eff[L1_seed].Draw("same")

leg.Draw()

#    if i>10000:
#        break

eff = {}
for L1_seed in L1_triggers:
    eff[L1_seed] = histos["den"].Clone("eff"+L1_seed)
    eff[L1_seed].Reset()
    eff[L1_seed].Divide(histos[L1_seed], histos["den"])

first = True
for L1_seed in L1_triggers:
    if first:
        eff[L1_seed].Draw("")
        first = False
    else:
        eff[L1_seed].Draw("same")
