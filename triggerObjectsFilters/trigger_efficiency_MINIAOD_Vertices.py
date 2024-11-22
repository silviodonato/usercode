from DataFormats.FWLite import Handle, Events

json = {
    353689:[[9,194],]
}

def checkJSON(event):
    run = event.eventAuxiliary().run()
    if run in json:
        ranges = json[run]
        lumi = event.eventAuxiliary().luminosityBlock()
#        print(run, lumi)
        for (min_,max_) in json[run]:
            if lumi>=min_ and lumi<=max_: return True
    return False


triggers=["HLT_MinimumBiasHF_split_v1" , "HLT_PixelClusters_WP2_split_v1", "Dataset_DQMGPUvsCPU", "AlCa_LumiPixelsCounts_Random_v2"]

offVertexs, offVertexLabel = Handle("vector<reco::Vertex>"), ("offlineSlimmedPrimaryVertices")
fileName = "65565e24-a049-4c94-83fd-3538049c11fc.root"
#fileName = "/eos/cms/tier0/store/data/Run2022A/ZeroBias1/MINIAOD/PromptReco-v1/000/353/689/00000/65565e24-a049-4c94-83fd-3538049c11fc.root"

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()

c1 = ROOT.TCanvas("c1")

nverticesHisto_den = ROOT.TH1F("nverticesHisto_den","",10,0,10)
nverticesHisto_den.GetYaxis().SetTitle("Events")
nverticesHisto_den.GetXaxis().SetTitle("nvertices")
nverticesHisto_den.SetLineWidth(2)
nverticesHisto_den.SetMarkerSize(2)
nverticesHisto_num = {}
nverticesHisto_eff = {}
for trigger in triggers:
    nverticesHisto_num[trigger] = nverticesHisto_den.Clone(trigger+"nverticesHisto_num")
    nverticesHisto_eff[trigger] = nverticesHisto_den.Clone(trigger+"nverticesHisto_num")

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
    nverticesHisto_num[trigger].SetLineColor(color)
    nverticesHisto_eff[trigger].SetLineColor(color)

# load FWlite python libraries

triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "slimmedPatTrigger"
triggerPrescales, triggerPrescaleLabel  = Handle("pat::PackedTriggerPrescales"), "patTrigger"

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
events = Events ([fileName])

for iev,event in enumerate(events):
    if iev%1000==0: print("iev=",iev)
    if iev>1000000: break
#    print(checkJSON(event))
    if checkJSON(event): 
        event.getByLabel(triggerBitLabel, triggerBits)
        event.getByLabel(triggerObjectLabel, triggerObjects)
        event.getByLabel(triggerPrescaleLabel, triggerPrescales)
        event.getByLabel(offVertexLabel, offVertexs)
        
        names = event.object().triggerNames(triggerBits.product())
        nvertices = sum(not v.isFake() for v in offVertexs.product())
        nverticesHisto_den.Fill( nvertices )
        for trigger in triggers:
            index = names.triggerIndex(trigger)
        #    print(index, len(names))
            if index<len(names) and triggerBits.product().accept(index):
                nverticesHisto_num[trigger].Fill( nvertices )

for trigger in triggers:
    nverticesHisto_eff[trigger].Divide(nverticesHisto_num[trigger],nverticesHisto_den,1,1,"cl=0.683 b(1,1) mode")

c1 = ROOT.TCanvas("c1","",1600,1200)

max_ = max(histo.GetMaximum() for histo in nverticesHisto_eff.values())*1.2
min_ = min(histo.GetMinimum() for histo in nverticesHisto_eff.values())*0.8
for i,trigger in enumerate(triggers):
    nverticesHisto_eff[trigger].SetMaximum(max_)
    nverticesHisto_eff[trigger].SetMinimum(min_)
    if i==0:
        nverticesHisto_eff[trigger].Draw()
    else:
        nverticesHisto_eff[trigger].Draw("same")

leg = ROOT.TLegend(0.75,0.5,0.9,0.9)
for trigger in triggers:
    leg.AddEntry(nverticesHisto_eff[trigger],trigger,"lep")
leg.Draw()

c1.SaveAs("efficiency.root")
c1.SaveAs("efficiency.png")




c2 = ROOT.TCanvas("c2","",1600,1200)

nverticesHisto_den.Draw()
for i,trigger in enumerate(triggers):
    nverticesHisto_num[trigger].Draw("same")

leg = ROOT.TLegend(0.75,0.5,0.9,0.9)
leg.AddEntry(nverticesHisto_den,"den","lep")
for trigger in triggers:
    leg.AddEntry(nverticesHisto_num[trigger],trigger,"lep")
leg.Draw()

c2.SetLogy()
c2.SaveAs("tot.root")
c2.SaveAs("tot.png")
