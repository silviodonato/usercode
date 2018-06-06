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
sig_JESup = w.data("CaloTrijet2016_qq_jesUp")


mjj = w.var("mjj")
th1x = w.var("th1x")

print("\ndata_obs:")
data.Print()
print()

frame = th1x.frame()


#data.plotOn(frame)
sig_JESup.plotOn(frame)
#sig.plotOn(frame)
frame.Draw()

