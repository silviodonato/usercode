from ROOT import TH3F,TFile

fileName = "btagCSV_3dPlot.root"
file_ = TFile(fileName)
histo3D_l = file_.Get("histo3D_lights")
histo3D_b = file_.Get("histo3D_b")
assert type(histo3D_l)==TH3F
assert type(histo3D_b)==TH3F


def btag_likelihoods(csv,pt,eta):
    bin_ = histo3D_l.FindBin(csv,pt,eta)
    gl = histo3D_l.GetBinContent(bin_)
    q = histo3D_b.GetBinContent(bin_)
    l = max(gl,1e-13)
    q = max(q,1e-13)
    return q,l

