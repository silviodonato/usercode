import ROOT

#fileName = "QGL_3dPlot.root"
fileName = "/tmp/QGL_3dPlot.root"
#fileName = "QGL_3dPlot_orig.root"

file_ = ROOT.TFile(fileName)

histo3D_gluon = file_.Get("histo3D_gluon")
histo3D_quark = file_.Get("histo3D_quark")


def qgl_ratio(qgl,pt,eta):
    bin_ = histo3D_gluon.FindBin(qgl,pt,eta)
    gl = histo3D_gluon.GetBinContent(bin_)
    q = histo3D_quark.GetBinContent(bin_)
    return q/gl

for i in range(10):
    qgl = i/10.
    pt = 100.
    eta = 1.2
    ratio = qgl_ratio(qgl,pt,eta)
    print "qgl:%s\tratio:%s"%(qgl,ratio)

ax = histo3D_gluon.GetXaxis()
print ax.GetNbins(), ax.GetXmin(), ax.GetXmax(), ax.GetBinWidth(1)



values = ROOT.TH1F("values","",200,0,2)
errors = ROOT.TH1F("errors","",200,0+1e-300,1)
xax = histo3D_quark.GetXaxis()
yax = histo3D_quark.GetYaxis()
zax = histo3D_quark.GetZaxis()
print "---------- xaxis ------------"
for i in range(xax.GetNbins()+5): print xax.GetBinLowEdge(i)
print "---------- yaxis ------------"
for i in range(yax.GetNbins()+5): print yax.GetBinLowEdge(i)
print "---------- zaxis ------------"
for i in range(zax.GetNbins()+5): print zax.GetBinLowEdge(i)
print "-----------------------------"
xax.Print()
for i in range(xax.GetNbins()):
    x = xax.GetBinCenter(i)
    for j in range(yax.GetNbins()):
        y = yax.GetBinCenter(j)
        for k in range(zax.GetNbins()):
            z = zax.GetBinCenter(k)
            
            bin_ = histo3D_quark.FindBin(x,y,z)
            quark_value = histo3D_quark.GetBinContent(bin_)
            quark_err = histo3D_quark.GetBinError(bin_)
            gluon_value = histo3D_quark.GetBinContent(bin_)
            gluon_err = histo3D_quark.GetBinError(bin_)
            
            ratio = quark_err/(quark_value+1e-300)
            pdf_ratio = quark_value/(gluon_value+1e-300)
            if (quark_value==0 or gluon_value==0) and y>25.0 and abs(z)<2.5:
                print quark_value,gluon_value,i, x, y, z
            values.Fill(min(pdf_ratio,1.99))
            errors.Fill(ratio)
            if ratio>0.1:
                print ratio, i, x, y, z


#projection_gluon = histo3D_gluon.Project3D("x")
#projection_quark = histo3D_quark.Project3D("x")
#projection_gluon.Draw()
#projection_quark.Draw("same")


errors.Draw()
c2 = ROOT.TCanvas("c2")
values.Draw()
