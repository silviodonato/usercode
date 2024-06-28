import ROOT, math
## python3 plotHLTSCOUTSparseHisto.py sparseHisto_all_2GeV.root
## python3 python3 plotHLTSCOUTSparseHistoDisplaced.py sparseHisto_all_displaced5.root  plotsDisplaced

# from defHLTSCOUTSparseHisto import axisDef
# python3 plotHLTSCOUTSparseHistoDisplaced.py sparseHisto_test_10k.root

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

# scaleSS = 1.35
scaleSS = 1.0
# fName = "sparseHisto_100k_0GeV.root"
# fName = "sparseHisto_all_1p5GeV.root"
# fName = "sparseHisto_test2_1p5GeV.root"
# fName = "sparseHisto_displaced_1p5GeV.root"
# fName = "sparseHisto_100k_1p5GeV.root"
# fName = "sparseHisto_test_10k.root"

## take fName as external parameter
import sys
fName = sys.argv[1]

if len(sys.argv) > 2:
    plotFolder = sys.argv[2]
else:
    plotFolder = "plots"
#Kpi resonance
#KK resonance: phi, prompt
#ppi resonance: Lambda, prompt
#pK resonance: Sigma, prompt
#ee resonance: Z, prompt
#pipi resonance: rho, prompt
#mumu resonance: Jpsi, prompt


f = ROOT.TFile.Open(fName)
sparseHisto = f.Get("sparseHisto")
variables = []
for i in range(sparseHisto.GetNdimensions()):
    variables.append(sparseHisto.GetAxis(i).GetTitle())
    axis = sparseHisto.GetAxis(i)
    print(axis.GetNbins(), "\t",axis.GetXmin(), "\t",axis.GetXmax(), "\t",axis.GetTitle())

print(variables)

massRange = [1.01, 1.025]
massRange = [0.98, 1.15]
massRange = [1.01, 10]
dzRange = [0, 0.07]
drRange = [0, 0.17]
ptRange = [0, 999]
dxyRange = [5, 999]

massRange = [0.5, 1.5]
massK = 0.493677
massPi = 0.139570
massMu = 0.105658
massProton = 0.938272

massPhi = 1.019461
massKstar = 0.89166
massD0 = 1.86483
massDstar = 2.01026
massDs = 1.96834
massB = 5.27963
massBs = 5.36677
massBd = 5.27963
massJpsi = 3.096916
massPsi2S = 3.686109
massUpsilon1S = 9.4603
massUpsilon2S = 10.02326
massUpsilon3S = 10.3552
massZ = 91.1876
massW = 80.385
massTop = 173.1
massH = 125.1
massKshort = 0.497614
massLambda = 1.115683
massEle = 0.000511

selectionPhotonConversionPeak = {
    "mass_ee" : [0.065,0.085], ## tight seletion (~1 sigma)
    "deltaEta" : [0.00,0.01],
    "dxySig" : [5, 999], 
   # "dxy" : [3, 999],
    # "dxy" : [3, 999],
}

selectionKshort = {
    "mass_pipi" : [massKshort-0.015, massKshort+0.015], ## tight seletion (~1 sigma)
    "deltaEta" : [0.01, 0.2], ## exclude photon conversion peak
    "deltaPhi" : [0.1, 999], ## exclude photon conversion peak
    "dxySig" : [5, 999], 
}

selectionD0 = {
    "mass_piK" : [massD0-0.02, massD0+0.02], ## tight seletion (~1 sigma) 
    "eta" : [-1.6, +1.6],
    "dz" : [0, 0.06],
    "dxy" : [0, 0.04],
    "dxySig" : [5, 999], 
}
selectionD0bar = dict(selectionD0)
selectionD0bar["mass_Kpi"] = selectionD0["mass_piK"]
del selectionD0bar["mass_piK"]

selectionPhi = {
    "mass_KK" : [massPhi-0.006, massPhi+0.004],
}
rebin = 4
selection = {
    # "mass_pipi" : [0,0.5],
    # "mass_KK" : [massPhi-0.01, massPhi+0.01],
    # "mass_KK" : [0, massPhi-0.01],
    "mass_KK" : [massPhi+0.02, 999 ],
    # "mass_pipi" : [massKshort-0.015, massKshort+0.015],
    # "mass_pipi" : [0, massKshort-0.025], ## below Kshort peak
    # "mass_pipi" : [massKshort+0.025, 999], ## above Kshort peak
    # "mass_Kpi" : [0, massD0-0.03], ## below D0 peak
    # "mass_piK" : [0, massD0-0.03], ## below D0bar peak
    # "mass_Kpi" : [massD0+0.03, 999], ## below D0 peak
    # "mass_piK" : [massD0+0.03, 999], ## below D0bar peak
    # "deltaEta" : [0.01, 999], ## exclude photon conversion peak
    # "eta" : [-1.6, +1.6],
    # "dz" : [0, 0.06],
    # "dxy" : [0.04,999],
    # "deltaPhi" : [0.1, 999], ## exclude photon conversion peak
    # "mass" : [massPhi+0.01, 999], ##Phi veto and above  
    # "mass_pipi" : [massKshort+0.03, 999], ##Kshort veto and above
    # "mass_pipi" : [0, massKshort-0.03], ##Kshort veto and below
    # "mass_ee" : [0.00,0.15], ## ee peak

    # "mass_ee" : [0.06,0.08],
    # "mass" : [0, massPhi-0.01], ##Phi veto and above
    # "mass_pipi" : [0.25, 0.4],
    # "mass_mumu" : [0.22, 0.24],
    # "mass_mumu" : [0.44, 0.48],
    #  "mass" : [0.98, 1.1],
    #  "mass_mumu" : [3.0, 1.1],
    #  "mass_Kpi" : [0.7, 1.1],
    #  "mass_piK" : [0.7, 1.1],
    #  "mass_pipi" : [0.25, 0.4],
    # "dxy" : [3, 999],
    #  "pt" : [0, 999],
}

selection = dict(selectionPhi)

# selection = dict(selectionD0bar)
# del selection["mass_Kpi"]

# selection = {
#             # "mass" : massRange,
#             # "charge" : [-0.7, -9999]
#             "deltaR" : drRange, 
#             "dz" : dzRange,
#             "pt" : ptRange,
#             "dxy" : dxyRange,  
#         }

# selectionSS = {
#             # "pt" : ptRange,
#             "mass" : massRange,
#             # "charge" : [-0.7, -9999]
#             "charge" : [1.5, 2.5],
#             "deltaR" : drRange,
#             "dz" : dzRange,
#         } 

# selectionOS = {
#             # "pt" : ptRange,
#             "mass" : massRange,
#             "charge" : [-0.5, 0.5],
#             "deltaR" : drRange,
#             "dz" : dzRange, 
#         }

rng = 3.0
plotDefs = { ## plot name: (variable , selection)
    "mass_KK_phiPeak_both" : ( "mass_KK" ,selectionPhi, 1, [massPhi-0.05, massPhi+0.05]),
    "mass_pipi_KshortPeak_both" : ( "mass_pipi" ,selectionKshort, rebin, [massPi*2, 0.8]),
    "mass_Kpi_D0bar_peak_both" : ( "mass_Kpi" ,selectionD0bar, rebin*5, [massD0-0.5, massD0+0.5]),
    "mass_piK_D0_peak_both" : ( "mass_piK" ,selectionD0, rebin*5, [massD0-0.5, massD0+0.5]),
    "mass_ee_photonConversionPeak_both" : ( "mass_ee" ,selectionPhotonConversionPeak, rebin, [massEle*2,0.15]),
    # # "mass_pipi_both" : ( "mass_pipi" ,{}, rebin, [massKshort+0.03, 999]),

    # "mass_KK_both" : ( "mass_KK" ,selectionPhi),
    # # "mass_pipi_both" : ( "mass_pipi" ,selection, rebin,[0.5,1.7]),  
    # # "mass_pipi_log_both" : ( "mass_pipi_log" ,selection, rebin, [math.log(massPi*2),1.8]),
    # # "mass_mumu_both" : ( "mass_mumu" ,selection, rebin, [massMu*2,2.0]), 
    # # "mass_ee_both" : ( "mass_ee" ,selection, rebin, [massEle*2,2.0]),
    # # "mass_pK_both" : ( "mass_ee" ,selection, rebin, [massProton+massK,3.0]),
    # # # "mass_Kpi_LambdaPeak_both" : ( "mass_Kpi" ,selection, rebin, [massLambda-0.2, massLambda+0.2]),
    # # "mass_piK_both" : ( "mass_piK" ,selection, rebin, [massPi+massK,massPi+massK+rng]),
    # # # "mass_Kpi_both" : ( "mass_Kpi" ,selection, rebin, [massPi+massK,massPi+massK+rng]),
    # # "mass_ppi_both" : ( "mass_ppi" ,selection, rebin, [massPi+massProton,massPi+massProton+rng]),
    # # "mass_pip_both" : ( "mass_pip" ,selection, rebin, [massPi+massProton,massPi+massProton+rng]),
    # # "mass_pK_both" : ( "mass_pK" ,selection, rebin, [massProton+massK,massProton+massK+rng]),
    # # "mass_Kp_both" : ( "mass_Kp" ,selection, rebin, [massProton+massK,massProton+massK+rng]),
    # # "mass_ee_both" : ( "mass_ee" ,selection, rebin, [0,rng]),
    # "deltaR_both" : ( "deltaR" ,selection,rebin, [0.00,0.4]),
    # "deltaPhi_both" : ( "deltaPhi" ,selection,1, [0.00,0.4]),
    # "deltaEta_both" : ( "deltaEta" ,selection,1, [0.00,0.4]),
    # "dz_both" : ( "dz" ,selection),
    "dxy_both" : ( "dxy" ,selectionPhotonConversionPeak,1, [-999, 9999]),
    "dxySig_both" : ( "dxySig" ,selectionPhotonConversionPeak,1 , [-999, 9999]),
    # "pt_both" : ( "pt" ,selection),
    # "eta_both" : ( "eta" ,selection, rebin),
    # "phi_both" : ( "phi" ,selection, rebin),


}

# for pt_min, pt_max in [
#         (0, 2),
#         (2, 2.5),
#         (2.5, 3),
#         (3, 3.5),
#         (3.5, 4),
#         (4, 5),
#         (5, 999),
#     ]:
#     sel = dict(selection)
#     sel["pt"] = [pt_min, pt_max]
#     plotDefs["mass_pt_%.1f_%.1f_both"%(pt_min, pt_max)] = ( "mass" ,sel)

# for dR_min, dR_max in [
#         (0.0, 0.05),
#         (0.05, 0.1),
#         (0.1, 0.15),
#         (0.15, 0.2),
#         (0.2, 0.25),
#         (0.25, 0.3),
#         (0.3, 999),
#     ]:
#     sel = dict(selection)
#     sel["deltaR"] = [dR_min, dR_max]
#     plotDefs["mass_dR_%.2f_%.2f_both"%(dR_min, dR_max)] = ( "mass" ,sel)


# for dZ_min, dZ_max in [
#         (0.0, 0.03),
#         (0.03, 0.07),
#         (0.07, 0.11),
#         (0.11, 0.15),
#         (0.15, 0.2),
#         (0.2, 0.3),
#     ]:
#     sel = dict(selection)
#     sel["dz"] = [dZ_min, dZ_max]
#     plotDefs["mass_dZ_%.2f_%.2f_both"%(dZ_min, dZ_max)] = ( "mass" ,sel)


# for dxy_min, dxy_max in [
#         (0.0, 0.05),
#         (0.05, 0.1),
#         (0.1, 0.13),
#         (0.13, 0.15),
#         (0.15, 0.17),
#         (0.17, 999),
#     ]:
#     sel = dict(selection)
#     sel["dxy"] = [dxy_min, dxy_max]
#     plotDefs["mass_dxy_%.2f_%.2f_both"%(dxy_min, dxy_max)] = ( "mass" ,sel)

# for eta_min, eta_max in [
#         (-2.4, -1.6),
#         (-1.6, 0),
#         (0, 1.6),
#         (1.6, 2.4),
#     ]:
#     sel = dict(selection) 
#     sel["eta"] = [eta_min, eta_max]
#     plotDefs["mass_eta_%.1f_%.1f_both"%(eta_min, eta_max)] = ( "mass" ,sel)


def makePlot(sparseHisto, plotDef):
    range_ = None
    if len(plotDef) == 2:
        varPlot, selection = plotDef
        rebin = 1
    elif len(plotDef) == 3:
        varPlot, selection, rebin = plotDef
    elif len(plotDef) == 4:
        varPlot, selection, rebin, range_ = plotDef
    print("makePlot", varPlot)
    print("selection:") 
    for varSel in selection:
        if range_ and varSel == varPlot:
            print("skip ", varSel, " (will use different range)")
            continue
        xmin, xmax = selection[varSel]
        print(varPlot, varSel, xmin, xmax)
        ax = sparseHisto.GetAxis(variables.index(varSel))
        ax.SetRange(ax.FindBin(xmin+1E-9), ax.FindBin(xmax-1E-9))
    histo = sparseHisto.Projection(variables.index(varPlot))
    ## revert changes   
    for varSel in selection:
        ax = sparseHisto.GetAxis(variables.index(varSel))
        ax.SetRange()
    histo.SetMarkerStyle(20)
    histo.SetMarkerSize(0.5) 
    print("rebin:", rebin)
    histo.Rebin(rebin)
    xmin, xmax = -1, -1
    for i in range(0, int(histo.GetNbinsX())+1):
        if histo.GetBinContent(i) > 0:
            histo.GetXaxis().SetRange(i, i)
            xmin = histo.GetBinLowEdge(i)+1E-9
            break
    for i in range(histo.GetNbinsX(), 0, -1):
        if histo.GetBinContent(i) > 0:
            histo.GetXaxis().SetRange(histo.GetXaxis().GetFirst(), i)
            xmax = histo.GetBinLowEdge(i+1)-1E-9
            break
    if range_:
        print("range: ", range_)
        if range_[0] > xmin:
            xmin = range_[0]
        if range_[1] < xmax:
            xmax = range_[1]
    histo.GetXaxis().SetRangeUser(xmin, xmax)
    return histo


plots = {}
canvas = ROOT.TCanvas("canvas", "canvas", 800, 800)
for plotName in plotDefs:
    plotDef = plotDefs[plotName]
    if not "_both" in plotName: ## default
        plots[plotName] = makePlot(sparseHisto, plotDef)
        plots[plotName].SetName(plotName)
        plots[plotName].SetTitle(plotName)     
        plots[plotName].GetXaxis().SetTitle(plotName)
        plots[plotName].GetYaxis().SetTitle("Events")     
        plots[plotName].Draw()
    else: ## plot opposite sign vs same sign
        for ssos in ["os", "ss"]:
            name = plotName.replace("_both", "_%s"%ssos)
            if ssos == "os":
                plotDef[1]["charge"]=[-0.1,0.1]
                plot = makePlot(sparseHisto, plotDef)
                color = ROOT.kBlack
            elif ssos == "ss":
                plotDef[1]["charge"]=[1.1,999]
                plot = makePlot(sparseHisto, plotDef) ## charge ++
                plot.SetName(name)
                plotDef[1]["charge"]=[-999,-1.1] 
                tmp = makePlot(sparseHisto, plotDef)       
                plot.Add(tmp) ## add charge --
                plot.Scale(scaleSS)
                color = ROOT.kBlue
            elif ssos == "pp":
                plotDef[1]["charge"]=[1.1,999]
                plot = makePlot(sparseHisto, plotDef)
                color = ROOT.kRed
            elif ssos == "nn":
                plotDef[1]["charge"]=[-999,-1.1]
                plot = makePlot(sparseHisto, plotDef)
                color = ROOT.kBlue
            else:
                raise Exception("ERROR", ssos)
            plot.SetName(name)
            plot.SetLineColor(color)
            plot.SetMarkerColor(color)
            plots[name] = plot
        plotOS = plots[plotName.replace("_both", "_os")]
        plotOS.SetTitle(plotName.replace("_both", ""))
        plotOS.GetXaxis().SetTitle(plotDef[0])
        plotOS.GetYaxis().SetTitle("Events")     
        plotOS.SetMinimum(0)
        plotOS.Draw("E1")
        plotSS = plots[plotName.replace("_both", "_ss")]
        plotSS.Draw("same")
        leg = ROOT.TLegend(0.8, 0.9, 0.97, 0.97)
        leg.AddEntry(plotOS, "opposite sign", "ep")
        label = "same sign"
        if scaleSS != 1.0:
            label = label+ " x %.1f"%scaleSS
        leg.AddEntry(plotSS, label, "l")
        leg.Draw()
    
    canvas.SaveAs("%s/%s.png"%(plotFolder,plotName))

for plotName in plotDefs:
    if "_os" in plotName:
        osName = plotName
        ssName = plotName.replace("_os", "_ss")
        if not ssName in plots: continue
        os = plots[osName]
        ss = plots[ssName]
        os.SetLineColor(ROOT.kRed)
        ss.SetLineColor(ROOT.kBlue)
        ## ratio
        ratio = os.Clone("ratio")
        os.Sumw2()
        ss.Sumw2()
        ratio.Divide(os, ss, 1., 2., "")
        ratio.SetLineColor(ROOT.kBlack)
        ratio.SetMarkerStyle(20)
        ratio.SetMarkerSize(0.5)
        ratio.SetMinimum(0.)
        ratio.SetMaximum(2.0)
        ratio.GetYaxis().SetTitle("OS/SS")
        ratio.SetTitle(plotName)
        ratio.Draw("E1")
        canvas.SaveAs("plots/%s.png"%plotName.replace("_os", "_ratio"))
        ## ss subtracted
        ssSubtracted = os.Clone("ssSubtracted")
        ssSubtracted.Add(ss, -2.0)
        ssSubtracted.SetLineColor(ROOT.kBlack)
        ssSubtracted.SetMarkerStyle(20)
        ssSubtracted.SetMarkerSize(0.5)
        # ssSubtracted.SetMinimum(-0.5)
        ssSubtracted.SetTitle(plotName)
        ssSubtracted.Draw("E1")
        canvas.SaveAs("plots/%s.png"%plotName.replace("_os", "_ssSubtracted"))

