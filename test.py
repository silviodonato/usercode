xsec = {}
br_h_to_bb = 0.577
#https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt1314TeV#s_13_0_TeV
xsec["tth"] = 0.5085
xsec["tthbb"] = xsec["tth"] * br_h_to_bb
xsec["tthnobb"] = xsec["tth"] * (1.0 - br_h_to_bb)

xsec["tt"] = 831.76

xsec["qcd300"] = 366800.0
xsec["qcd500"] = 29370.0
xsec["qcd700"] = 6524.0
xsec["qcd1000"] = 1064.0
xsec["qcd1500"] = 121.5
xsec["qcd2000"] = 25.42

import TdrStyles
import string
import ROOT
import os
from math import *
from copy import *
from array import array
ROOT.gROOT.LoadMacro("CSVn.C")
#ROOT.gROOT.ProcessLine(".L CSVn.C++")

def getOverlayScale(signalPlot,stack):
    maxSig = signalPlot.GetMaximum()
    maxStack = stack.GetMaximum()
    scale = str(maxStack/maxSig).split(".")[0]
    scale = int(scale[0])*(10**len(scale))/10
    return int(scale)
    
class Dataset(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.loadTree()
    def loadTree(self):
        self.tfile = ROOT.TFile(self.fileName)
        self.tree = self.tfile.Get("tree")
        print "Getting tree from ",self.fileName," id=",id(self.tree)
        assert(type(self.tree)==ROOT.TTree)
    def closeFile(self):
        self.tfile.Close()

class DatasetMC(Dataset):
    def __init__(self, xsec, fileName):
        Dataset.__init__(self, fileName)
        self.xsec = xsec
        self.count = self.getCount()
    def getCount(self):
        return self.tfile.Get("CountWeighted").GetBinContent(1)
    def setSingleEventWeight(self,lumi):
        self.singleEventWeight = lumi * self.xsec / self.count
        

class DatasetData(Dataset):
    def __init__(self, lumi, fileName):
        Dataset.__init__(self, fileName)
        self.lumi = lumi #pb

class Group():
    def __init__(self, color, latexName, samples):
        self.color = color
        self.latexName = latexName
        self.samples = samples
        
datasetMC = {
#    "tt" : DatasetMC(
#        xsec = xsec["tt"],
#        fileName = "had_V24_4__TT_TuneCUETP8M1_13TeV-powheg-pythia8.root",
#    ),
#    "tth" : DatasetMC(
#        xsec = xsec["tth"],
#        fileName = "had_V24_4__ttHTobb_M125_13TeV_powheg_pythia8.root",
#    ),
    "tthnobb" : DatasetMC(
        xsec = xsec["tthnobb"],
        fileName = "had_V24_4__ttHTobb_M125_13TeV_powheg_pythia8.root",
    ),
#    "qcd300" : DatasetMC(
#        xsec = xsec["qcd300"],
#        fileName = "had_V24_4__QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root",
#    ),
#    "qcd500" : DatasetMC(
#        xsec = xsec["qcd500"],
#        fileName = "had_V24_4__QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root",
#    ),
#    "qcd700" : DatasetMC(
#        xsec = xsec["qcd700"],
#        fileName = "had_V24_4__QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root",
#    ),
#    "qcd1000" : DatasetMC(
#        xsec = xsec["qcd1000"],
#        fileName = "had_V24_4__QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root",
#    ),
#    "qcd1500" : DatasetMC(
#        xsec = xsec["qcd1500"],
#        fileName = "had_V24_4__QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root",
#    ),
#    "qcd2000" : DatasetMC(
#        xsec = xsec["qcd2000"],
#        fileName = "had_V24_3__QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root",
#    ),
}
datasetData = {
#    "JetHT" : DatasetData(
#        lumi = 19786,
#        fileName = "had_V24_4__JetHT.root"
#    ),
}

def testDraw(tree,nbins, xmin, xmax):
    tree.Draw("jets_pt[0] >> histo(%s,%s,%s)"%(nbins,xmin,xmax))
    histo = ROOT.gDirectory.Get("histo").Clone("histo")
    return histo
    
def test(tree,nbins, xmin, xmax):
    maxJets = 30

    tree.SetBranchStatus( '*', 0 )
    tree.SetBranchStatus( 'njets', 1 )
    tree.SetBranchStatus( 'jets_pt', 1 )

    histo = ROOT.TH1F("","",nbins, xmin, xmax)
    jets_pt = array( 'd', maxJets*[ 0 ] )
    tree.SetBranchAddress( 'jets_pt', jets_pt)

    for i  in range(tree.GetEntries()):
        tree.GetEntry(i)
        histo.Fill(jets_pt[0])
    return histo
    
    
nbins = 100
xmin  = 0
xmax  = 500
tree = datasetMC["tthnobb"].tree

histo = test(tree,nbins, xmin, xmax)
#histo = testDraw(tree,nbins, xmin, xmax)
