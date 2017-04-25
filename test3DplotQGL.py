import ROOT
from math import log

fileName = "QGL_3dPlot.root"
file_ = ROOT.TFile(fileName)
histo3D_gluon = file_.Get("histo3D_gluon")
histo3D_quark = file_.Get("histo3D_quark")


def qgl_likelihoods(qgl,pt,eta):
    bin_ = histo3D_gluon.FindBin(qgl,pt,eta)
    gl = histo3D_gluon.GetBinContent(bin_)
    q = histo3D_quark.GetBinContent(bin_)
    gl = max(gl,1e-13)
    q = max(q,1e-13)
    return q,gl


def getPlots(tree):
    histo_all_q_vs_all_gl  = ROOT.TH1F("histo_all_q_vs_all_gl" ,"histo_all_q_vs_all_gl" ,100,-10,10)
    for i in range(min(tree.GetEntries(),10000)):
        tree.GetEntry(i)
#        nBjets = 0
#        for j in range(tree.njets):
#            if tree.jets_btagCSV[j]>0.8:
#                nBjets += 1
#        if nBjets is not 2: continue
        all_q  = 1.
        all_gl  = 1.
        for j in range(tree.njets):
            if tree.jets_btagCSV[j]<0.8:
                (q,gl) = qgl_likelihoods(tree.jets_qgl[j],tree.jets_pt[j],tree.jets_eta[j])
                all_q *= q
                all_gl *= gl
        
        histo_all_q_vs_all_gl.Fill(log(all_q/all_gl))
    return histo_all_q_vs_all_gl.Clone("histo2")

#def getPlots(tree):
#    histo_gr1g  = ROOT.TH1F("histo_gr1g" ,"histo_gr1g" ,100,-10,10)
#    for i in range(min(tree.GetEntries(),10000)):
#        tree.GetEntry(i)
##        ratio = 0+1E-300
#        ratio = 1E300
#        for j in range(min(2,tree.njets)):
#            (q,gl) = qgl_likelihoods(tree.jets_qgl[j],tree.jets_pt[j],tree.jets_eta[j])
#            ratio = min(ratio, q/gl)
#        
#        histo_gr1g.Fill(log(ratio))
#    return histo_gr1g.Clone("histo2")


#fileNameBkg = "had_V24_4__QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"
fileNameBkg = "had_V24_4__QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root"
fileBkg = ROOT.TFile(fileNameBkg)
treeBkg = fileBkg.Get("tree")

histoBkg = getPlots(treeBkg)
histoBkg  = histoBkg.Clone("histoBkg")

fileNameSig = "had_V24_4__ttHTobb_M125_13TeV_powheg_pythia8.root"
fileSig = ROOT.TFile(fileNameSig)
treeSig = fileSig.Get("tree")

histoSig = getPlots(treeSig)
histoSig  = histoSig.Clone("histoSig")

c2 = ROOT.TCanvas("c2","")

histoSig.SetLineColor(ROOT.kRed)
histoSig.Draw("")
histoBkg.Draw("same")

#ax = histo3D_gluon.GetXaxis()
#print ax.GetNbins(), ax.GetXmin(), ax.GetXmax(), ax.GetBinWidth(1)



#errors = ROOT.TH1F("","",200,0+1e-300,1)
#xax = histo3D_quark.GetXaxis()
#yax = histo3D_quark.GetYaxis()
#zax = histo3D_quark.GetZaxis()
#for i in range(xax.GetNbins()):
#    x = xax.GetBinCenter(i)
#    for j in range(yax.GetNbins()):
#        y = yax.GetBinCenter(j)
#        for k in range(zax.GetNbins()):
#            z = zax.GetBinCenter(k)
#            
#            bin_ = histo3D_quark.FindBin(x,y,z)
#            ratio = histo3D_quark.GetBinError(bin_)/(histo3D_quark.GetBinContent(bin_)+1e-300)
#            errors.Fill(ratio)
#            if ratio>0.1:
#                print ratio, i, x, y, z


##projection_gluon = histo3D_gluon.Project3D("x")
##projection_quark = histo3D_quark.Project3D("x")
##projection_gluon.Draw()
##projection_quark.Draw("same")

#errors.Draw()
