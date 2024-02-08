import ROOT

ROOT.gROOT.SetBatch()
ROOT.gStyle.SetOptStat(0)

def getPlot(fName, color):
    f = ROOT.TFile.Open(fName)
    c1 = f.Get("c1")
    plot = c1.GetListOfPrimitives().At(0)
    f.Close()
    plot.SetLineWidth(2)
    
    fit = ROOT.TF1(plot.GetName()+"fit", "gaus", -0.2, 0.2)
    fit.SetLineColor(color)
    plot.Fit(fit, "", "", -0.2, 0.2)
    
    plot.SetLineColor(color)
    
    return plot, fit

for fNameOld in [
    "plotScoutingPF_ZEE_longRun_ZEE_GRunV14Jet1bin50.root",
    "plotScoutingPF_ZEE_longRun_ZEE_GRunV14Jet1bin100.root",
    ]:
    fNameNew = fNameOld.replace("GRunV14","CommonPFSequence")
    #fNameNew = "plotScoutingPF_ZEE_longRun_ZEE_CommonPFSequenceJet1bin50.root"
    
    plotOld, fitOld = getPlot(fNameOld, ROOT.kRed)
    plotNew, fitNew = getPlot(fNameNew, ROOT.kBlue)
    
    c2 = ROOT.TCanvas("c2","", 1280, 1024)
    c2.Update()
    
#    plotNew.SetTitle("Events")
    plotNew.GetYaxis().SetTitle("Events")
    plotNew.GetXaxis().SetTitle("(Scouting - Offline)/Offline")
    plotNew.SetMaximum(1.2 * plotNew.GetMaximum())
    plotNew.Draw()
    plotOld.Draw("same")
    
    leg = ROOT.TLegend(0.1,0.8,0.48,0.9)
    leg.AddEntry(plotOld, "Current scouting #mu = %.3f #sigma = %.3f" %(fitOld.GetParameter(1), fitOld.GetParameter(2)), "l")
    leg.AddEntry(plotNew, "Proposed scouting #mu = %.3f #sigma = %.3f" %(fitNew.GetParameter(1), fitNew.GetParameter(2)), "l")
    leg.Draw()
    
    c2.Update()
    fNameOut = fNameOld.replace("GRunV14","Combination")
    c2.SaveAs(fNameOut)
    c2.SaveAs(fNameOut.replace(".root",".png"))


for fNameOld in [
    "plotScoutingPF_ZEE_longRun_ZEE_GRunV14MET70.root",
    "plotScoutingPF_ZEE_longRun_ZEE_GRunV14METFake.root",
    ]:
    fNameOff = fNameOld.replace("MET","offMET")
    fNameNew = fNameOld.replace("GRunV14","CommonPFSequence")
    #fNameNew = "plotScoutingPF_ZEE_longRun_ZEE_CommonPFSequenceJet1bin50.root"
    
    plotOld, fitOld = getPlot(fNameOld, ROOT.kRed)
    plotNew, fitNew = getPlot(fNameNew, ROOT.kBlue)
    plotOff, fitOff = getPlot(fNameOff, ROOT.kMagenta)

    m = fitNew.GetParameter(1)
    s = fitNew.GetParameter(2)
    plotNew.Fit(fitNew, "", "", m-1.0*s, m+1.0*s)
    m = fitNew.GetParameter(1)
    s = fitNew.GetParameter(2)
    plotNew.Fit(fitNew, "", "", m-1.0*s, m+1.0*s)

    m = fitOld.GetParameter(1)
    s = fitOld.GetParameter(2)
    plotOld.Fit(fitOld, "", "", m-1.0*s, m+1.0*s)
    m = fitOld.GetParameter(1)
    s = fitOld.GetParameter(2)
    plotOld.Fit(fitOld, "", "", m-1.0*s, m+1.0*s)
    
    m = fitOff.GetParameter(1)
    s = fitOff.GetParameter(2)
    plotOff.Fit(fitOff, "", "", m-1.0*s, m+1.0*s)
    m = fitOff.GetParameter(1)
    s = fitOff.GetParameter(2)
    plotOff.Fit(fitOff, "", "", m-1.0*s, m+1.0*s)
    
    c2 = ROOT.TCanvas("c2","", 1280, 1024)
    c2.SetGridx()
    c2.SetGridy()
    c2.Update()
    
#    plotNew.SetTitle("Events")
    plotNew.GetYaxis().SetTitle("Events")
    plotNew.GetXaxis().SetTitle("(Scouting - Offline)/Offline")
    plotOff.SetMaximum(1.2 * plotOff.GetMaximum())
    if "Fake" in fNameOld:
        plotOff.SetMinimum(1)
    plotOff.SetMaximum(10 * plotOff.GetMaximum())
    c2.SetLogy(1)
    plotOff.Draw()
    plotNew.Draw("same")
    plotOld.Draw("same")
    
    if not "Fake" in fNameOld:
        leg = ROOT.TLegend(0.1,0.8,0.48,0.9)
        leg.AddEntry(plotOld, "Current scouting #mu = %.3f #sigma = %.3f" %(fitOld.GetParameter(1), fitOld.GetParameter(2)), "l")
        leg.AddEntry(plotNew, "Proposed scouting #mu = %.3f #sigma = %.3f" %(fitNew.GetParameter(1), fitNew.GetParameter(2)), "l")
        leg.AddEntry(plotOff, "Offline PUPPI MET #mu = %.3f #sigma = %.3f" %(fitOff.GetParameter(1), fitOff.GetParameter(2)), "l")
        leg.Draw()
        c2.SetLogy(0)
    else:
        leg = ROOT.TLegend(0.1,0.8,0.48,0.9)
        leg.AddEntry(plotOld, "Current scouting" , "l")
        leg.AddEntry(plotNew, "Proposed scouting" , "l")
        leg.AddEntry(plotOff, "Offline PUPPI MET" , "l")
        leg.Draw()
        c2.SetLogy(1)
    
    c2.Update()
    fNameOut = fNameOld.replace("GRunV14","Combination")
    c2.SaveAs(fNameOut)
    c2.SaveAs(fNameOut.replace(".root",".png"))


for fNameOld in [
    "plotScoutingPF_ZEE_longRun_ZEE_GRunV14offMETprofile.root",
    "plotScoutingPF_ZEE_longRun_ZEE_GRunV14METprofile.root",
    "plotScoutingPF_ZEE_longRun_ZEE_GRunV14JetProf.root",
    ]:
    fNameNew = fNameOld.replace("GRunV14","CommonPFSequence")
    #fNameNew = "plotScoutingPF_ZEE_longRun_ZEE_CommonPFSequenceJet1bin50.root"
    
    plotOld, fitOld = getPlot(fNameOld, ROOT.kRed)
    plotNew, fitNew = getPlot(fNameNew, ROOT.kBlue)
    
    c2 = ROOT.TCanvas("c2","", 1280, 1024)
    c2.SetGridx()
    c2.SetGridy()
    c2.Update()
    
#    plotNew.SetTitle("Events")
    plotNew.GetXaxis().SetTitle("Offline")
    plotNew.GetYaxis().SetTitle("(Scouting - Offline)/Offline")
    plotNew.SetMaximum(1.2 * plotNew.GetMaximum())
    plotNew.SetLineWidth(3)
    plotNew.Draw("E1")
#    ax = plotOld.GetXaxis()
#    shift = 0.001
#    ax.Set(ax.GetNbins(), ax.GetXmin()+shift, ax.GetXmax()+shift)
#    plotOld.RebinAxis(0, ax)
    plotOld.SetLineWidth(2)
    plotOld.Draw("E1,same")
    
    leg = ROOT.TLegend(0.1,0.8,0.48,0.9)
    leg.AddEntry(plotOld, "Current scouting ", "l")
    leg.AddEntry(plotNew, "Proposed scouting " , "l")
    leg.Draw()
    
    c2.Update()
    fNameOut = fNameOld.replace("GRunV14","Combination")
    c2.SaveAs(fNameOut)
    c2.SaveAs(fNameOut.replace(".root",".png"))
