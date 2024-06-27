import ROOT, math
from defHLTSCOUTSparseHisto import axisDef

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

# scaleSS = 1.35
scaleSS = 1.0
# fName = "sparseHisto_100k_0GeV.root"
# fName = "sparseHisto_all_1p5GeV.root"
# fName = "sparseHisto_test2_1p5GeV.root"
# fName = "sparseHisto_displaced_1p5GeV.root"
# fName = "sparseHisto_100k_1p5GeV.root"
fName = "sparseHisto_MC.root"

#Kpi resonance
#KK resonance: phi, prompt
#ppi resonance: Lambda, prompt
#pK resonance: Sigma, prompt
#ee resonance: Z, prompt
#pipi resonance: rho, prompt
#mumu resonance: Jpsi, prompt


f = ROOT.TFile.Open(fName)
sparseHisto = f.Get("sparseHisto")
assert(sparseHisto.GetNdimensions() == len(axisDef))

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

rebin = 20
selection = {
    # "mass" : [massPhi-0.2, massPhi+0.2], ##Phi veto and above
    # "mass_gen": [1.0, 1.1],
    # "mass" : [massPhi+0.01, 999], ##Phi veto and above
    # "mass_pipi" : [massKshort+0.03, 999], ##Kshort veto and above
    # "mass_pipi" : [0, massKshort-0.03], ##Kshort veto and below
    #  "mass_ee" : [0.05,0.10], ## ee peak
    # "mass_gen" : [0.01,9], ## ee peak
    # "mass_gen" : [-999,0.0001], ##  no mass_ee limit
    # "mass_gen" : [9,999], ## no matching tracks
    # "mass_gen" : [0.001,9], ## ee peak

    "mass_ee" : [0.0,1],
    "mass_ST" : [0.01,9999],
    # "mass" : [0, massPhi-0.01], ##Phi veto and above
    # "mass_pipi" : [0.25, 0.4],
    # "mass_mumu" : [0.22, 0.24],
    # "mass_mumu" : [0.44, 0.48],
    #  "mass" : [0.98, 1.1],
    #  "mass_mumu" : [3.0, 1.1],
    #  "mass_Kpi" : [0.7, 1.1],
    #  "mass_piK" : [0.7, 1.1],
    #  "mass_pipi" : [0.25, 0.4],
    # "dxy" : [0, 3],
    #  "pt" : [0, 999],
    #  "phi" : [-1, 0],
    #  "phi" : [0, 1],
}

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

rng = 1.0
plotDefs = { ## plot name: (variable , selection)
    # "mass_KK_phiPeak_both" : ( "mass" ,{"mass_gen" : [0.01,9.9]}, rebin, [massPhi-0.02, massPhi+0.02]),
    # "mass_KK_phiPeak_both" : ( "mass" ,{"mass_gen" : [-999,0.1]}, rebin, [massPhi-0.02, massPhi+0.02]),
    "mass_KK_phiPeak_both" : ( "mass" ,selection, rebin, [massPhi-0.02, massPhi+0.02]),
    # "mass_KK_phiPeak_both" : ( "mass" ,{}, rebin, [massPhi-0.04, massPhi+0.04]),
    "mass_pipi_KshortPeak_both" : ( "mass_pipi" ,{}, rebin, [massKshort-0.03, massKshort+0.03]),
    # "mass_pipi_both" : ( "mass_pipi" ,{}, rebin, [massKshort+0.03, 999]),

    "mass_KK_both" : ( "mass" ,selection, rebin, [0, massLambda+0.2]),
    "mass_pipi_both" : ( "mass_pipi" ,selection, rebin,  [massPi*2, massPi*2+rng]),
    "mass_pipi_log_both" : ( "mass_pipi_log" ,selection, rebin, [math.log(massPi*2),2]),
    # "mass_mumu_both" : ( "mass_mumu" ,selection, rebin, [massMu*2,1.0]),
    "mass_Kpi_LambdaPeak_both" : ( "mass_Kpi" ,selection, rebin, [massLambda-0.2, massLambda+0.2]),
    "mass_Kpi_both" : ( "mass_Kpi" ,selection, rebin, [massPi+massK,massPi+massK+rng]),
    "mass_ppi_both" : ( "mass_ppi" ,selection, rebin, [massPi+massProton,massPi+massProton+rng]),
    "mass_pK_both" : ( "mass_pK" ,selection, rebin, [massProton+massK,massProton+massK+rng]),
    "mass_ee_both" : ( "mass_ee" ,selection, rebin, [0,rng]),
    "mass_gen_both" : ( "mass_gen" ,selection, rebin,  [0, massLambda+0.2]),
    "mass_gen_ee_both" : ( "mass_gen_ee" ,selection, rebin, [0, 0.3]),
    # "mass_gen_KK_both" : ( "mass_gen_KK" ,selection, rebin,  [massLambda-0.2, massLambda+0.2]),
    "mass_ST_both" : ( "mass_ST" ,selection, 1,  [0.0001, 0.05]),
    "mass_ST_KK_both" : ( "mass_ST_KK" ,selection, rebin,  [massLambda-0.2, massLambda+0.2]),
    "mass_ee_peak_both" : ( "mass_ee" ,selection, rebin, [0.00,0.15]),
    "deltaR_both" : ( "deltaR" ,selection,rebin, [0.00,0.15]),
    "deltaPhi_both" : ( "deltaPhi" ,selection,rebin, [0.00,0.05]),
    "deltaEta_both" : ( "deltaEta" ,selection,rebin, [0.00,0.15]),
    "eta_both" : ( "eta" ,selection, rebin),
    "phi_both" : ( "phi" ,selection, rebin),
    "dz_both" : ( "dz" ,selection),
    "dxy_both" : ( "dxy" ,selection),
    "pt_both" : ( "pt" ,selection),
    "dxyAbs_both" : ( "dxyAbs" ,selection,1, [0.00,0.15]),
    "dxyError_both" : ( "dxyError" ,selection,1, [0.00,0.03]),


    # "mass_os" : ( "mass" ,selectionOS),
    # "mass_ss" : ( "mass" ,selectionSS),
    # "deltaR_os" : ( "deltaR" ,selectionOS),
    # "deltaR_ss" : ( "deltaR" ,selectionSS),
    # "deltaEta" : ( "deltaEta" ,selectionSS),
    # "deltaPhi" : ( "deltaPhi" ,selectionSS),
    # "dz_ss" : ( "dz" ,selectionSS),
    # "dz_os" : ( "dz" ,selectionOS),
    # "charge1" : ( "charge" ,selectionOS),
    # "charge2" : ( "charge" ,selectionSS),
    # "pt_ss" : ( "pt" ,selectionSS),
    # "dxy_os" : ( "dxy" ,selectionOS),
    # "dxy_ss" : ( "dxy" ,selectionSS),
    # "dz_os" : ( "dz" ,selectionOS),
    # "dz_ss" : ( "dz" ,selectionSS),
    # "eta_os" : ( "eta" ,selectionOS),
    # "eta_ss" : ( "eta" ,selectionSS),
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
    range = None
    if len(plotDef) == 2:
        varPlot, selection = plotDef
        rebin = 1
    elif len(plotDef) == 3:
        varPlot, selection, rebin = plotDef
    elif len(plotDef) == 4:
        varPlot, selection, rebin, range = plotDef
    print("makePlot", varPlot)
    for varSel in selection:
        xmin, xmax = selection[varSel]
        print(varPlot, varSel, xmin, xmax)
        ax = sparseHisto.GetAxis(list(axisDef.keys()).index(varSel))
        ax.SetRange(ax.FindBin(xmin+1E-9), ax.FindBin(xmax-1E-9))
    histo = sparseHisto.Projection(list(axisDef.keys()).index(varPlot))
    ## revert changes
    for varSel in selection:
        ax = sparseHisto.GetAxis(list(axisDef.keys()).index(varSel))
        ax.SetRange()
    histo.SetMarkerStyle(20)
    histo.SetMarkerSize(0.5)
    print("rebin", rebin)
    histo.Rebin(rebin)
    if range:
        histo.GetXaxis().SetRangeUser(*range)
        print("range", range)
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
                plotDef[1]["charge"]=[-999,-1.1]              
                plot.Add(makePlot(sparseHisto, plotDef)) ## add charge --
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
        plotSS = plots[plotName.replace("_both", "_ss")]
        plotOS.SetMaximum(max(plotOS.GetMaximum(),plotSS.GetMaximum())*1.2)
        plotOS.Draw("E1")
        plotSS.Draw("same")
        leg = ROOT.TLegend(0.8, 0.9, 0.97, 0.97)
        leg.AddEntry(plotOS, "opposite sign", "ep")
        label = "same sign"
        if scaleSS != 1.0:
            label = label+ " x %.1f"%scaleSS
        leg.AddEntry(plotSS, label, "l")
        leg.Draw()
    
    canvas.SaveAs("plots/%s.png"%plotName)

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

