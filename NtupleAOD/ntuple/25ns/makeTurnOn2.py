triggersDefault=[
'All',
'HLT_PFMET170_NoiseCleaned_v2',
'HLT_PFMET90_PFMHT90_IDTight_v1',
#'HLT_PFMET100_PFMHT100_IDTight_v1',
#'HLT_PFMET110_PFMHT110_IDTight_v1',
'HLT_PFMET120_PFMHT120_IDTight_v1',
'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1',
#'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v1',
]

variableDict={
"offMet":"offline PFMET (GeV)",
"min(offMet,offMht)":"offline min(PFMET,PFMHT) (GeV)",
}
def copyStyle(plot1,plot2):
      plot1.SetFillColor(plot2.GetFillColor())
      plot1.SetFillStyle(plot2.GetFillStyle())
      plot1.SetLineColor(plot2.GetLineColor())
      plot1.SetLineStyle(plot2.GetLineStyle())
      plot1.SetLineWidth(plot2.GetLineWidth())
      plot1.SetMarkerColor(plot2.GetMarkerColor())
      plot1.SetMarkerStyle(plot2.GetMarkerStyle())
      plot1.SetMarkerSize(plot2.GetMarkerSize())
      plot1.GetXaxis().SetTitle(plot2.GetXaxis().GetTitle())
      plot1.GetYaxis().SetTitle(plot2.GetYaxis().GetTitle())

def makeTurnOn(fileName , preselection="1", variable="offMet", triggers=triggersDefault, xMin=0, xMax=495.,eventsPerBin=30,minwidth=5):
    import ROOT
    from array import array
    ROOT.gROOT.SetBatch()
    ROOT.gStyle.SetOptStat(0)
#    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/s/sdonato/AFSwork/website/VHbb/50ns/functions.C")
    ROOT.gROOT.LoadMacro("/afs/cern.ch/user/s/sdonato/AFSwork/website/VHbb/25ns/functions_C.so")
    c1 = ROOT.TCanvas("c1","",1280,720)
#    bins=10
#    eventsPerBin=100
#    minwidth=5
    initialBinning=10000
    _file0 = ROOT.TFile(fileName)
    tree = ROOT.gDirectory.Get("tree")

    colors = [
    ROOT.kBlack,

    ROOT.kRed,
    ROOT.kBlue,
    ROOT.kMagenta,
    ROOT.kGreen+1,
    ROOT.kYellow+1,
    ROOT.kCyan+1,

    ROOT.kOrange,
    ROOT.kPink,
    ROOT.kViolet,
    ROOT.kAzure,
    ROOT.kTeal,
    ROOT.kSpring,

    ROOT.kGray,
    ]

    triggerNames = [
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_BTagCSV0p7_v1',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_v1',
    'HLT_PFMET120_PFMHT120_IDLoose_v1',
    'HLT_PFMET110_PFMHT110_IDLoose_v1',
    'HLT_PFMET100_PFMHT100_IDLoose_v1',
    'HLT_PFMET90_PFMHT90_IDLoose_v1',
    'HLT_PFMET170_NoiseCleaned_v1',
    'HLT_PFMET120_NoiseCleaned_BTagCSV07_v1',
    'HLT_DiCentralPFJet70_PFMET120_NoiseCleaned_v1',
    'HLT_PFHT350_PFMET120_NoiseCleaned_v1',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v1',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v1',
    'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v1',
    'HLT_DoubleEle24_22_eta2p1_WP75_Gsf_v1',
    'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v1',
    'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v1',
    'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v1',
    'HLT_Ele32_eta2p1_WP75_Gsf_v1',
    'HLT_Ele32_eta2p1_WP75_Gsf_CentralPFJet30_BTagCSV07_v1',
    'HLT_Ele27_eta2p1_WP85_Gsf_HT200_v1',
    'HLT_Ele27_WP85_Gsf_v1',
    'HLT_Ele27_eta2p1_WP75_Gsf_v1',
    'HLT_Ele27_eta2p1_WP75_Gsf_CentralPFJet30_BTagCSV07_v1',
    'HLT_Ele105_CaloIdVT_GsfTrkIdT_v1',
    'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1',
    'HLT_IsoMu24_eta2p1_v1',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v1',
    'HLT_Mu24_eta2p1_v1',
    'HLT_TkMu24_eta2p1_v1',
    'HLT_Mu24_v1',
    'HLT_IsoMu27_v1',
    'HLT_IsoTkMu27_v1',
    'HLT_TkMu27_v1',
    'HLT_Mu27_v1',
    'HLT_IsoMu20_v1',
    'HLT_IsoTkMu20_v1',
    'HLT_IsoMu20_eta2p1_v1',
    'HLT_IsoMu20_eta2p1_CentralPFJet30_BTagCSV07_v1',
    'HLT_Mu20_v1',
    'HLT_TkMu20_v1',
    'HLT_Mu40_eta2p1_PFJet200_PFJet50_v1',
    'HLT_IsoMu16_eta2p1_CaloMET30_v1',
    'HLT_Mu16_eta2p1_CaloMET30_v1',
    'HLT_PFMET120_NoiseCleaned_Mu5_v1',
    'HLT_MonoCentralPFJet80_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v1',
    'HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v1',
    'HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v1',
    'HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v1',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v1',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v1',
    'HLT_Mu17_TkMu8_DZ_v1',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1',
    'HLT_DoubleIsoMu17_eta2p1_v1',
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v1',
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80_v1',
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_v1',
    'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq240_v1',
    'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq200_v1',
    'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq500_v1',
    'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq460_v1',
    'HLT_QuadPFJet_VBF_v1',
    'HLT_L1_TripleJet_VBF_v1',
    'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v1',
    'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v1',
    'HLT_QuadJet45_TripleCSV0p5_v1',
    'HLT_QuadJet45_DoubleCSV0p5_v1',
    'HLT_DoubleJet90_Double30_TripleCSV0p5_v1',
    'HLT_DoubleJet90_Double30_DoubleCSV0p5_v1',
    'HLT_PFHT450_SixJet40_PFBTagCSV_v1',
    'HLT_PFHT450_SixJet40_v1',
    'HLT_PFHT400_SixJet30_BTagCSV0p5_2PFBTagCSV_v1',
    'HLT_PFHT400_SixJet30_v1',
    'HLT_PFHT750_4Jet_v1',
    'HLT_PFHT900_v1'

    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1',
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v1',
    'HLT_PFMET120_PFMHT120_IDTight_v1',
    'HLT_PFMET110_PFMHT110_IDTight_v1',
    'HLT_PFMET100_PFMHT100_IDTight_v1',
    'HLT_PFMET90_PFMHT90_IDTight_v1',
    'HLT_PFMET170_NoiseCleaned_v2',
    'HLT_PFMET120_NoiseCleaned_BTagCSV0p72_v2',
    'HLT_DiCentralPFJet55_PFMET110_NoiseCleaned_v1',
    'HLT_PFHT350_PFMET100_NoiseCleaned_v1',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v2',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v1',
    'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v2',
    'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
    'HLT_Ele32_eta2p1_WPLoose_Gsf_v1',
    'HLT_Ele32_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v1',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v1',
    'HLT_Ele27_WPLoose_Gsf_WHbbBoost_v1',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_v1',
    'HLT_Ele27_eta2p1_WPTight_Gsf_v1',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v1',
    'HLT_Ele105_CaloIdVT_GsfTrkIdT_v2',
#    'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v2',
    'HLT_IsoMu24_eta2p1_v2',
    'HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v2',
    'HLT_Mu24_eta2p1_v1',
    'HLT_TkMu24_eta2p1_v2',
    'HLT_Mu24_v1',
    'HLT_IsoMu27_v2',
    'HLT_IsoTkMu27_v2',
    'HLT_TkMu27_v2',
    'HLT_Mu27_v1',
    'HLT_IsoMu20_v2',
    'HLT_IsoTkMu20_v2',
    'HLT_IsoMu20_eta2p1_v2',
    'HLT_IsoMu20_eta2p1_CentralPFJet30_BTagCSV07_v2',
    'HLT_Mu20_v1',
    'HLT_TkMu20_v2',
#    'HLT_Mu40_eta2p1_PFJet200_PFJet50_v2',
    'HLT_IsoMu16_eta2p1_CaloMET30_v2',
    'HLT_Mu16_eta2p1_CaloMET30_v2',
    'HLT_PFMET120_NoiseCleaned_Mu5_v2',
    'HLT_MonoCentralPFJet80_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v2',
    'HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v2',
    'HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v2',
    'HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v2',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v2',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v2',
    'HLT_Mu17_TkMu8_DZ_v2',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v2',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v2',
    'HLT_DoubleIsoMu17_eta2p1_v2',
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET120_v2',
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_MET80_v2',
    'HLT_LooseIsoPFTau50_Trk30_eta2p1_v2',
    'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq240_v2',
    'HLT_QuadPFJet_DoubleBTagCSV_VBF_Mqq200_v2',
    'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq500_v2',
    'HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq460_v2',
    'HLT_QuadPFJet_VBF_v2',
    'HLT_L1_TripleJet_VBF_v1',
    'HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v2',
    'HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v2',
    'HLT_QuadJet45_TripleBTagCSV0p67_v2',
    'HLT_QuadJet45_DoubleBTagCSV0p67_v2',
    'HLT_DoubleJet90_Double30_TripleBTagCSV0p67_v2',
    'HLT_DoubleJet90_Double30_DoubleBTagCSV0p67_v2',
    'HLT_PFHT450_SixJet40_PFBTagCSV0p72_v2',
    'HLT_PFHT450_SixJet40_v2',
    'HLT_PFHT400_SixJet30_BTagCSV0p55_2PFBTagCSV0p72_v2',
    'HLT_PFHT400_SixJet30_v2',
    'HLT_PFHT750_4JetPt50_v1',
    'HLT_PFHT800_v1',
    ]

    prescales = {
    'HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v1':25
    }

    ## get binning
    histo = ROOT.TH1F("histo","",initialBinning,xMin,xMax)
    selection = ""
    for trigger2 in triggers:
        if "HLT_" in trigger2:
            selection += trigger2 +" || "
    selection = selection[:-3]
#    selection = selection+"&& l1Met>70"
#    events = tree.Draw(variable+" >> histo","("+selection+")" + "&&" + preselection)
    events = tree.Draw(variable+" >> histo", "(event%10==0)&&"+preselection)
    events = tree.Draw(variable+" >>+ histo","("+selection+")" + "&&" + preselection)
    events = histo.Integral()
#    events = tree.Draw(variable+" >>+ histo","(event%100==0)&&"preselection)
#    eventsPerBin = events/bins
    points = [xMin]
    start = 0
    stop = 0
    initialwidth=(xMax-xMin)/(initialBinning)
    while stop<initialBinning: 
        if histo.Integral(start,stop) >=eventsPerBin:
            start=stop
            points.append(histo.GetBinLowEdge(stop))
            stop=stop+int(minwidth/initialwidth) -1
        stop += 1

    points.append(histo.GetBinLowEdge(initialBinning+1))
    histo.Delete()

    standardBinning=False
    
    ## get inclusive plots
    varBinLog = array('f',points)
    inclusive = ROOT.TH1F("inclusive","",len(varBinLog)-1,varBinLog)
    if standardBinning:
        inclusive = ROOT.TH1F("inclusive","",30,0,400)
    inclusive.SetLineWidth(2)
    inclusive.SetLineColor(ROOT.kBlack)
    inclusive.GetXaxis().SetTitle(variable)
    inclusive.GetYaxis().SetTitle("Events")
    tree.Draw(variable + " >> inclusive",preselection)

    ## get triggers plots
    histos = []
    for i,trigger in enumerate(triggers):
        histo = inclusive.Clone("histo_"+trigger)
        histo.SetLineColor(colors[i])
        selection = ""
        if trigger == 'All':
            for trigger2 in triggers:
                if "HLT_" in trigger2:
                    selection += trigger2+"|| "
            selection = selection[:-3]
        else:
            selection = trigger
        print "("+selection+")" + "&&" + preselection, tree.Draw(variable+" >> "+"histo_"+trigger, "("+selection+")" + "&&" + preselection)
        histos.append(histo)


    efficiencies = []
    leg = ROOT.TLegend(0.1,0.75,0.4,0.9);
    inclusive.Sumw2()
    inclusive.Draw()
    for histo in histos:
        histo.Draw("same")
        histo.Sumw2()
        histo.GetYaxis().SetTitle("Events")
        xlabel = histo.GetXaxis().GetTitle()
        if xlabel in variableDict.keys():
            xlabel = variableDict[variable]
            histo.GetXaxis().SetTitle(xlabel)
        triggerName = histo.GetName()
        efficiency = ROOT.TGraphAsymmErrors()
        efficiency.SetName(triggerName+"_eff")
#        efficiency = histo.Clone(triggerName+"_eff")
        leg.AddEntry(efficiency,triggerName,"l");
#        efficiency.Divide(histo,inclusive,1.,1.,"B")
#        efficiency.Divide(histo,inclusive,1.,1.,"cl=0.683 b(1,1) mode")
        efficiency.Divide(histo,inclusive,"cl=0.683 b(1,1) mode")
        copyStyle(efficiency,histo)
        if triggerName in prescales.keys():
            efficiency.Scale(prescales[triggerName])
        efficiencies.append(efficiency)

    efficiencies.reverse()
    for i,efficiency in enumerate(efficiencies):
        print "Efficiency plot:",efficiency
        efficiency.GetYaxis().SetTitle("Efficiency")    
        if i==0:  efficiency.Draw("AP")
        else:   efficiency.Draw("P")
        efficiency.SetMaximum(1.1)
        efficiency.GetXaxis().SetRangeUser(xMin,xMax)

    leg.Draw()
    c1.SetGridx()
    c1.SetGridy()
    fileout = "efficiencies_"+variable
    fileout=fileout.replace("(","")
    fileout=fileout.replace(")","")
    fileout=fileout.replace(",","")
    fileout=fileout.replace("[","")
    fileout=fileout.replace("]","")
    fileout=fileout.replace("$","")
    fileout=fileout.replace("/","")
    c1.SaveAs(fileout+".png")
    import os
    try:
        os.popen("mkdir files")
    except:
        pass
    c1.SaveAs("files/"+fileout+".C")
    c1.SaveAs("files/"+fileout+".root")

    c1.Delete()
    ROOT.gROOT.SetBatch(0)


