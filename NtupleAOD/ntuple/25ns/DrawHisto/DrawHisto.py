def MakeNicePlot(fileName="efficiencies_offMet.root"):
    import sys
    arg=sys.argv[1:]
    if len(arg)>=1:
        fileName=arg[0]
    print 'fileName=',fileName

    import ROOT

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

    ROOT.gROOT.SetBatch()

    inputFile = ROOT.TFile(fileName)
    plots = inputFile.Get("c1").GetListOfPrimitives()
    plots = plots[1:-1]

    ROOT.gROOT.LoadMacro("tdrstyleTrigger.C")
    ROOT.setTDRStyle()

    ROOT.gROOT.LoadMacro("CMS_lumi_canvas.C")

    ROOT.gStyle.SetFitFormat("2.3")
    ROOT.gStyle.SetOptFit(1111)



    W = 1280
    H = 720
     
    W_ref = W*1.2
    H_ref = H*1.2

    T = 0.08*H_ref
    B = 0.12*H_ref 
    L = 0.12*W_ref
    R = 0.04*W_ref

    canvName = "FigExample_"
    canvName += str(W)
    canvName += "-"
    canvName += str(H)
    canvName += "_"  
    iPos=0

    if( iPos%10==0 ): canvName += "-out"
    elif( iPos%10==1 ): canvName += "-left"
    elif( iPos%10==2 ):  canvName += "-center"
    elif( iPos%10==3 ):  canvName += "-right"

    canv = ROOT.TCanvas(canvName,canvName,50,50,W,H)
    canv.SetFillColor(0)
    canv.SetBorderMode(0)
    canv.SetFrameFillStyle(0)
    canv.SetFrameBorderMode(0)
    canv.SetLeftMargin( L/W )
    canv.SetRightMargin( R/W )
    canv.SetTopMargin( T/H )
    canv.SetBottomMargin( B/H )
    canv.SetTickx(0)
    canv.SetTicky(0)

    ROOT.CMS_lumi_canvas(canv)
    ROOT.setTDRStyle()

    for (i,plot) in enumerate(plots):
        name = plot.GetName()
        if name=="histo_All_eff":
            name = "All"
        else:
            name = "HLT_"+name.split("HLT_")[1]
            name = (name.split("_v"))[0]
        plots[i] = plot.Clone(name)
        plot.UseCurrentStyle()
        plot.SetLineColor(colors[len(plots)-1-i])
        plot.SetMarkerColor(colors[len(plots)-1-i])
#        plot.GetXaxis().SetRangeUser(0,plot.GetXaxis().GetXmax())
        if i==0:
            plot.Draw("AP")
        else:
            plot.Draw("P")

    ROOT.CMS_lumi_canvas(canv)

    legend = ROOT.TLegend(0.52,0.15,0.96,0.5)
    legend.SetFillStyle(0)
    legend.SetLineStyle(0)
    legend.SetLineWidth(0)
    legend.SetBorderSize(0)
    for plot in plots:
        legend.AddEntry(plot,plot.GetName(),"l")
    legend.Draw()

    canv.SaveAs(fileName.replace(".root","Plot.pdf"))
    canv.SaveAs(fileName.replace(".root","Plot.png"))
    canv.SaveAs(fileName.replace(".root","Plot.root"))

#import sys
#arg=sys.argv[1:]
#print arg
MakeNicePlot()
