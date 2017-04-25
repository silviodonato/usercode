import ROOT
from getHistoUsingDraw import getHistoUsingDraw

## create the THStack plot using tree.Draw function
def getStackWithDataOverlayAndLegend(leg, datasetMC, datasetData, groups, var, nbins, xmin, xmax, weightMC = "1", cutsData="1", cutsMC="1", yTitle="", xTitle="", opts="HIST goff",variableList=["*"]):
    dataPlot = None
    signalPlot = None
    stack = ROOT.THStack(var,'')
    for group in groups:
        print group.latexName
        if not group.latexName.lower() == "data":
            firstSample = True
            for sampleName in group.samples:
                sample = datasetMC[sampleName]
                histoOptions = (var, nbins, xmin, xmax, weightMC, cutsMC, opts,sampleName)
                tmp = getHistoUsingDraw(sample.tree, histoOptions)
                tmp.Scale(sample.singleEventWeight)
                print sampleName+":",round(tmp.Integral(),1)
                if firstSample:
                    print id(tmp)
                    print id(histo)
                    histo = tmp
                    print id(tmp)
                    print id(histo)
                    histo.SetFillColor(group.color)
                    histo.SetLineColor(ROOT.kBlack)
                    print id(tmp)
                    print id(histo)
                else:
                    histo.Add(tmp)
                firstSample = False
            stack.Add(histo)
            if group.latexName.lower() == "signal":
                print "copy signal for overlay"
                signalPlot = histo.Clone("Overlay")
            
            leg.AddEntry(histo,group.latexName+" (%s)"%str(round(histo.Integral(),1)),"f")
        else:
            firstSample = True
            for sampleName in group.samples:
                sample = datasetData[sampleName]
                histoOptions = (var, nbins, xmin, xmax, "1", cutsData, opts,sampleName)
                if firstSample:
                    histo = getHistoUsingDraw(sample.tree, histoOptions)
                    print sampleName+":",round(histo.Integral(),1)
                    histo.SetLineColor(ROOT.kBlack)
                else:
                    tmp = getHistoUsingDraw(sample.tree, histoOptions)
                    print sampleName+":",round(tmp.Integral(),1)
                    histo.Add(tmp)
                firstSample = False
            dataPlot=histo
    
    if xTitle == "": xTitle = var
    bin_size = 1.*(xmax-xmin)/nbins
    if yTitle == "": yTitle = "Events/"+str(bin_size)

    stack.Draw("goff")
            
    stack.GetYaxis().SetTitle(yTitle)
    stack.GetXaxis().SetTitle(xTitle)

    return stack,dataPlot,signalPlot

def createLegend():
    leg = ROOT.TLegend(0.75, 0.65,0.92,0.92)
    leg.SetLineWidth(2)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(4000)
    leg.SetTextFont(62)
    leg.SetTextSize(0.035)
    return leg
