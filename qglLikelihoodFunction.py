from ROOT import TH3F,TFile

fileName = "QGL_3dPlot.root"
file_ = TFile(fileName)
histo3D_gluon = file_.Get("histo3D_gluon")
histo3D_quark = file_.Get("histo3D_quark")
assert type(histo3D_gluon)==TH3F
assert type(histo3D_quark)==TH3F

def qgl_likelihoods(qgl,pt,eta):
    bin_ = histo3D_gluon.FindBin(qgl,pt,eta)
    gl = histo3D_gluon.GetBinContent(bin_)
    q = histo3D_quark.GetBinContent(bin_)
    gl = max(gl,1e-13)
    q = max(q,1e-13)
    return q,gl


