from DataFormats.FWLite import Handle, Events

json = {
    353689:[[14,14],]
}

def checkJSON(run, lumi):
    if run in json:
        ranges = json[run]
#        print(run, lumi)
        for (min_,max_) in json[run]:
            if lumi>=min_ and lumi<=max_: return True
    return False


triggers=["HLT_MinimumBiasHF_split_v1" , "HLT_PixelClusters_WP2_split_v1", "Dataset_DQMGPUvsCPU", "AlCa_LumiPixelsCounts_Random_v2"]

offVertexs, offVertexLabel = Handle("vector<reco::Vertex>"), ("offlineSlimmedPrimaryVertices")
#offTracks, offTrackLabel = Handle("vector<reco::Track>"), ("offlineSlimmedPrimaryVertices")
packedPFCandidates, packedPFCandidatesLabel = Handle("vector<pat::PackedCandidate>"), ("packedPFCandidates")

fileNames = ["65565e24-a049-4c94-83fd-3538049c11fc.root",
#fileName = "/eos/cms/tier0/store/data/Run2022A/ZeroBias1/MINIAOD/PromptReco-v1/000/353/689/00000/65565e24-a049-4c94-83fd-3538049c11fc.root"
#"/eos/cms/tier0/store/data/Run2022A/ZeroBias1/MINIAOD/PromptReco-v1/000/353/689/00000/430a749b-7d02-4ecb-8ee9-541ccbd8204a.root",
#"/eos/cms/tier0/store/data/Run2022A/ZeroBias1/MINIAOD/PromptReco-v1/000/353/689/00000/53d8f256-4e7e-4c39-87a6-cbea1ab60f7a.root",
#"/eos/cms/tier0/store/data/Run2022A/ZeroBias1/MINIAOD/PromptReco-v1/000/353/689/00000/5e0f7cd4-4f0f-453f-96e0-d85f1ccb45ff.root",
#"/eos/cms/tier0/store/data/Run2022A/ZeroBias1/MINIAOD/PromptReco-v1/000/353/689/00000/77206f68-bfc6-4877-ad69-d91cda6af12a.root"
]

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()

c1 = ROOT.TCanvas("c1")

histo_den = ROOT.TH1F("histo_den","",30,0,30)
histo_den.GetYaxis().SetTitle("Events")
#histo_den.GetXaxis().SetTitle("# offline primary vertex")
histo_den.GetXaxis().SetTitle("# PF cand with >=4 hits")
histo_den.SetLineWidth(2)
histo_den.SetMarkerSize(2)
histo_num = {}
histo_eff = {}
for trigger in triggers:
    histo_num[trigger] = histo_den.Clone(trigger+"histo_num")
    histo_eff[trigger] = histo_den.Clone(trigger+"histo_num")

for i,trigger in enumerate(triggers):
    if i ==0: color = ROOT.kBlue
    elif i ==1: color = ROOT.kRed
    elif i ==2: color = ROOT.kGreen
    elif i ==3: color = ROOT.kOrange
    elif i ==4: color = ROOT.kBlue+2
    elif i ==5: color = ROOT.kRed+2
    elif i ==6: color = ROOT.kGreen+2
    elif i ==7: color = ROOT.kOrange+2
    else: color = ROOT.kBlack
    histo_num[trigger].SetLineColor(color)
    histo_eff[trigger].SetLineColor(color)

# load FWlite python libraries

triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "slimmedPatTrigger"
triggerPrescales, triggerPrescaleLabel  = Handle("pat::PackedTriggerPrescales"), "patTrigger"

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
events = Events (fileNames)

for iev,event in enumerate(events):
    run = event.eventAuxiliary().run()
    lumi = event.eventAuxiliary().luminosityBlock()
    if iev%1000==0: print("iev=",iev," run=",run," lumi=",lumi)
    if iev>100000: break
#    print(checkJSON(event))
    if checkJSON(run,lumi): 
        event.getByLabel(triggerBitLabel, triggerBits)
        event.getByLabel(triggerObjectLabel, triggerObjects)
        event.getByLabel(triggerPrescaleLabel, triggerPrescales)
        event.getByLabel(offVertexLabel, offVertexs)
        event.getByLabel(packedPFCandidatesLabel, packedPFCandidates)
        
        names = event.object().triggerNames(triggerBits.product())
        nvertices = sum(not v.isFake() for v in offVertexs.product())
        ntracks = sum(cand.numberOfHits()>=4 for cand in packedPFCandidates.product())
#        ntracks = sum(v.dimension/3 for v in offVertexs.product())
        if nvertices>0:
            pass
#            print(nvertices,ntracks,ndim)
#            1/0
        var = ntracks
        histo_den.Fill( var )
        for trigger in triggers:
            index = names.triggerIndex(trigger)
        #    print(index, len(names))
            if index<len(names) and triggerBits.product().accept(index):
                histo_num[trigger].Fill( var )

for trigger in triggers:
    histo_eff[trigger].Divide(histo_num[trigger],histo_den,1,1,"cl=0.683 b(1,1) mode")

c1 = ROOT.TCanvas("c1","",1600,1200)

max_ = max(histo.GetMaximum() for histo in histo_eff.values())*1.2
min_ = min(histo.GetMinimum() for histo in histo_eff.values())*0.8
for i,trigger in enumerate(triggers):
    histo_eff[trigger].GetYaxis().SetTitle("Efficiency")
    histo_eff[trigger].SetMaximum(max_)
    histo_eff[trigger].SetMinimum(min_)
    if i==0:
        histo_eff[trigger].Draw()
    else:
        histo_eff[trigger].Draw("same")

leg = ROOT.TLegend(0.75,0.5,0.95,0.95)
for trigger in triggers:
    leg.AddEntry(histo_eff[trigger],trigger,"lep")
leg.Draw()

c1.SaveAs("efficiency.root")
c1.SaveAs("efficiency.png")




c2 = ROOT.TCanvas("c2","",1600,1200)

histo_den.Draw()
for i,trigger in enumerate(triggers):
    histo_num[trigger].Draw("same")

leg = ROOT.TLegend(0.75,0.5,0.9,0.9)
leg.AddEntry(histo_den,"den","lep")
for trigger in triggers:
    leg.AddEntry(histo_num[trigger],trigger,"lep")
leg.Draw()

c2.SetLogy()
c2.SaveAs("tot.root")
c2.SaveAs("tot.png")

