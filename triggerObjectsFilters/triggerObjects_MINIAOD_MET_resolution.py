trigger="MC_PFMET_v17"
metCollection="hltPFMETOpenFilter"
from DataFormats.FWLite import Handle, Events
#offMETs, offMETLabel = Handle("vector<pat::MET>"), ("slimmedMETs")
offMETs, offMETLabel = Handle("vector<pat::MET>"), ("slimmedMETsPuppi")

#xrdcp root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18MiniAODv2/VBF_HToInvisible_M125_TuneCP5_withDipoleRecoil_13TeV_powheg_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/3ADE2E10-FD8F-B941-9C62-400308C99FB8.root .
#fileName='3ADE2E10-FD8F-B941-9C62-400308C99FB8.root'

fileName = "190C6D7C-FC26-A949-BE2C-551947B33215.root"
#fileName = ["/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/190C6D7C-FC26-A949-BE2C-551947B33215.root"]


import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()

c1 = ROOT.TCanvas("c1")

offMETvsGen = ROOT.TH2F("offMETvsGen","",100,0.,400.,100,-200.,200.)
offMETvsGen.GetYaxis().SetTitle("MET - genMET")
offMETvsGen.GetXaxis().SetTitle("gen MET")
offMETvsGen.SetLineWidth(2)
offMETvsGen.SetMarkerSize(2)

hltMETvsGen = offMETvsGen.Clone("hltMETvsGen")

test = offMETvsGen.Clone("hltMETvsGen")


offMETRes = ROOT.TH1F("offMETRes","",100,-100.,100)
offMETRes.GetXaxis().SetTitle("offline/hlt MET")
offMETRes.GetYaxis().SetTitle("Events")
offMETRes.SetLineWidth(2)
offMETRes.SetMarkerSize(2)

hltMETRes = offMETRes.Clone("hltMETRes")
hltoffMETRes = offMETRes.Clone("hltoffMETRes")
testMETRes = offMETRes.Clone("testMETRes")


# load FWlite python libraries

triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "slimmedPatTrigger"
triggerPrescales, triggerPrescaleLabel  = Handle("pat::PackedTriggerPrescales"), "patTrigger"

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
events = Events ([fileName])

for iev,event in enumerate(events):
    if iev%1000==0: print("iev=",iev)
    if iev>10000: break
    event.getByLabel(triggerBitLabel, triggerBits)
    event.getByLabel(triggerObjectLabel, triggerObjects)
    event.getByLabel(triggerPrescaleLabel, triggerPrescales)
    event.getByLabel(offMETLabel, offMETs)
    
    names = event.object().triggerNames(triggerBits.product())
    index = names.triggerIndex(trigger)
#    print(index, len(names))
    if index<len(names) and triggerBits.product().accept(index):
        offlineMET = offMETs.product().at(0).pt()
        genMET = offMETs.product().at(0).genMET().pt()
        triggerObjects.product().at(0).unpackPathNames(names)
        for j,to in enumerate(triggerObjects.product()):
            to.unpackFilterLabels(event.object(), triggerBits.product())
            if metCollection in to.filterLabels():
                hltMET = to.pt()
        if genMET>50:
            offMETRes.Fill( (offlineMET - genMET) )
            hltMETRes.Fill( (hltMET - genMET) )
            hltoffMETRes.Fill( (hltMET - offlineMET) )
            testMETRes.Fill( (hltMET + offlineMET)/2 - genMET )
        hltMETvsGen.Fill( genMET, hltMET - genMET )
        offMETvsGen.Fill( genMET, offlineMET - genMET )
        test.Fill( genMET, (hltMET + offlineMET)/2 - genMET )
    

c1 = ROOT.TCanvas("c1")

offMETRes.SetLineColor(ROOT.kRed)
hltMETRes.SetLineColor(ROOT.kBlue)
hltoffMETRes.SetLineColor(ROOT.kBlack)
testMETRes.SetLineColor(ROOT.kGreen)
offMETRes.Fit("gaus")
hltMETRes.Fit("gaus")
hltoffMETRes.Fit("gaus")
testMETRes.Fit("gaus")
offMETRes.Draw()
hltMETRes.Draw("same")
#hltoffMETRes.Draw("same")
testMETRes.Draw("same")

leg = ROOT.TLegend(0.1,0.7,0.28,0.9)
leg.AddEntry(offMETRes,"offline","lep")
leg.AddEntry(hltMETRes,"HLT","lep")
leg.AddEntry(testMETRes,"(HLT+offline)/2","lep")
leg.AddEntry(hltoffMETRes,"HLT vs offline","lep")
leg.Draw()

c1.SaveAs("resolution.root")
c1.SaveAs("resolution.png")


c2 = ROOT.TCanvas("c2")

offMETvsGenProf = offMETvsGen.ProfileX("_off",1,-1,"s")
hltMETvsGenProf = hltMETvsGen.ProfileX("_hlt",1,-1,"s")
testProf = test.ProfileX("_hltvsoff",1,-1,"s")
offMETvsGenProf.SetLineColor(ROOT.kRed)
hltMETvsGenProf.SetLineColor(ROOT.kBlue)
testProf.SetLineColor(ROOT.kGreen)

offMETvsGenProf.SetMaximum( 50)
offMETvsGenProf.SetMinimum(-50)
offMETvsGenProf.Draw()
c2.SaveAs("offline.png")
hltMETvsGenProf.SetMaximum( 50)
hltMETvsGenProf.SetMinimum(-50)
hltMETvsGenProf.Draw()
c2.SaveAs("HLT.png")
testProf.SetMaximum( 50)
testProf.SetMinimum(-50)
testProf.Draw()
c2.SaveAs("test.png")

offMETvsGenProf.Draw()
hltMETvsGenProf.Draw()
testProf.Draw()

offMETvsGenProf.Draw()
hltMETvsGenProf.Draw("same")
testProf.Draw("same")

leg2 = ROOT.TLegend(0.1,0.7,0.28,0.9)
leg2.AddEntry(offMETvsGenProf,"offline","lep")
leg2.AddEntry(hltMETvsGenProf,"HLT","lep")
leg2.AddEntry(testMETRes,"(HLT+offline)/2","lep")
leg2.Draw()


c2.SaveAs("2Dplot.root")
c2.SaveAs("2Dplot.png")

c3 = ROOT.TCanvas("c3")

testProf.Draw()

c3.SaveAs("hltVsOff.root")
c3.SaveAs("hltVsOff.png")

