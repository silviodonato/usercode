# https://root.cern.ch/download/doc/RooFit_Users_Manual_2.91-33.pdf

import ROOT

c1 = ROOT.TCanvas("c1")

file_ = ROOT.TFile.Open("cards_qq_trijet_06_06/dijet_combine_qq_450_lumi-35.900_CaloTrijet2016.root")
w = file_.Get("wCaloTrijet2016")
print("\nWorkSpace:")
w.Print()
print()

data = w.data("data_obs")
bkg = w.data("CaloTrijet2016_qq_mjj")
sig = w.data("CaloTrijet2016_qq")
sig_JES_up = w.data("CaloTrijet2016_qq_jesUp")
sig_JES_down = w.data("CaloTrijet2016_qq_jesDown")
sig_JER_up = w.data("CaloTrijet2016_qq_jerUp")
sig_JER_down = w.data("CaloTrijet2016_qq_jerDown")


mjj = w.var("mjj")
th1x = w.var("th1x")

print("\ndata_obs:")
data.Print()
print()

frame = th1x.frame()


#data.plotOn(frame)
sig.plotOn(frame)

#sig_JES_up.plotOn(    frame,ROOT.RooFit.LineColor(ROOT.kRed) , ROOT.RooFit.DataError(ROOT.RooAbsData.None))
#sig_JES_down.plotOn(  frame,ROOT.RooFit.LineColor(ROOT.kBlue) , ROOT.RooFit.DataError(ROOT.RooAbsData.None))

sig_JER_up.plotOn(    frame,ROOT.RooFit.LineColor(ROOT.kRed), ROOT.RooFit.DataError(ROOT.RooAbsData.None))
sig_JER_down.plotOn(  frame,ROOT.RooFit.LineColor(ROOT.kBlue), ROOT.RooFit.DataError(ROOT.RooAbsData.None))

#sig.plotOn(frame)
frame.Draw("")
