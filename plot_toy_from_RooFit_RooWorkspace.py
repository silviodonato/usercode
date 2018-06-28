# https://root.cern.ch/download/doc/RooFit_Users_Manual_2.91-33.pdf

import ROOT

c1 = ROOT.TCanvas("c1")


#file_ = ROOT.TFile.Open("/mnt/t3nfs01/data01/shome/dbrzhech/DijetScouting/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/signal_bias_test/higgsCombineqq_300_lumi-35.900_r-1.000_CaloTrijet2016_fiveparam_fiveparam.MaxLikelihoodFit.mH120.123456.root")

fileFit = ROOT.TFile.Open("/mnt/t3nfs01/data01/shome/dbrzhech/DijetScouting/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/signal_bias_test/dijet_combine_qq_300_lumi-35.900_CaloTrijet2016.root")
fileToys = ROOT.TFile.Open("/mnt/t3nfs01/data01/shome/dbrzhech/DijetScouting/CMSSW_7_4_14/src/CMSDIJET/DijetRootTreeAnalyzer/signal_bias_test/higgsCombineqq_300_lumi-35.900_r-1.000_CaloTrijet2016_fiveparam_fiveparam.GenerateOnly.mH120.123456.root")
toys = fileToys.Get("toys")
toy1 = toys.Get("toy_984")
w = fileFit.Get("wCaloTrijet2016")

print("\nWorkSpace:")
w.Print()
print()

print("\toy1:")
toy1.Print()
print()


mjj = w.var("mjj")
th1x = w.var("th1x")

frame = th1x.frame()


#data.plotOn(frame)
toy1.plotOn(frame)

frame.Draw("")
