import ROOT

ROOT.gROOT.SetBatch()
#fileName = "had_V24_4__QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"
#fileName = "had_V24_4__QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"
#fileName = "Oct19-__QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_bis.root"
fileName = "Oct19-__QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"


file_ = ROOT.TFile(fileName)

tree = file_.Get("tree")

qgl_bins = 40
qgl_min  = 0.
qgl_max  = 1.

pt_bins = 20
pt_min  = 0.
pt_max  = 200.

eta_bins = 12
eta_min  = -2.4
eta_max  = +2.4

tree.Draw("jets_eta:min(jets_pt,200):max(0,jets_qgl) >> histo3D_quark(%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(qgl_bins,qgl_min,qgl_max,pt_bins,pt_min,pt_max,eta_bins,eta_min,eta_max),"abs(jets_mcFlavour)<5")
histo3D_quark = ROOT.gDirectory.Get("histo3D_quark")

tree.Draw("jets_eta:min(jets_pt,200):max(0,jets_qgl) >> histo3D_gluon(%s,%s,%s,%s,%s,%s,%s,%s,%s)"%(qgl_bins,qgl_min,qgl_max,pt_bins,pt_min,pt_max,eta_bins,eta_min,eta_max),"jets_mcFlavour==21")
histo3D_gluon = ROOT.gDirectory.Get("histo3D_gluon")

fileNew = ROOT.TFile("QGL_3dPlot.root","recreate")

histo3D_quark = histo3D_quark.Clone("histo3D_quark")
histo3D_gluon = histo3D_gluon.Clone("histo3D_gluon")

histo3D_quark.Sumw2()
histo3D_gluon.Sumw2()

histo3D_quark.Scale(1./histo3D_quark.Integral())
histo3D_gluon.Scale(1./histo3D_gluon.Integral())

fileNew.Write()

