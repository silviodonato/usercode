#! /usr/bin/env python

import ROOT
import sys
from DataFormats.FWLite import Events, Handle
from math import *

def deltaPhi(a,b) :
 r = a-b
 while r>2*pi : r-=2*pi 
 while r<-2*pi : r+=2*pi 
 return r

def deltaR(a,b) :
  dphi=deltaPhi(a.phi(),b.phi())
  return sqrt(dphi*dphi+(a.eta()-b.eta())**2)  

#events = Events (['/afs/cern.ch/work/g/gpetrucc/micro/70x/CMSSW_7_0_4/src/miniProd/ZH_HToBB_ZToLL_M-125_13TeV_powheg-herwigpp_PAT.root'])
events = Events (['/afs/cern.ch/work/g/gpetrucc/micro/70x/CMSSW_7_0_4/src/miniProd/ZH_HToBB_ZToLL_M-125_13TeV_powheg-herwigpp_PAT.root'])

handleGP  = Handle ("std::vector<reco::GenParticle>")
labelGP = ("prunedGenParticles")

#handleJet = Handle ("std::vector<pat::Jet>")
#labelJet = ("slimmedJets") 

ROOT.gROOT.SetBatch()        # don't pop up canvases
ROOT.gROOT.SetStyle('Plain') # white background
zptHist = ROOT.TH1F ("zpt", "Z Pt Gen", 50, 0, 500)

# loop over events
count= 0
for event in events:
    count+=1 
    if count % 1000 == 0 :
	print count
#    print "#######################################################################"
#    event.getByLabel (labelJet, handleJet)
#    jets = handleJet.product()
#    for j in jets:
#	print j.pt()
    event.getByLabel (labelGP, handleGP)
    genparts = handleGP.product()
    for g in genparts:
#      if  abs(g.pdgId()) == 23 : 
#	if g.numberOfMothers() > 0 :
#		print g.pdgId(), g.pt(), g.mother().pdgId(), g.mass(),  g.daughter(0).pdgId()
#	else:
#		print g.pdgId(), g.pt(), " no mom" , g.mass(), g.daughter(0).pdgId()
	if abs(g.pdgId()) == 23 and abs(g.daughter(0).pdgId() ) < 20 : 
		zptHist.Fill( g.pt())

f =ROOT.TFile("out.root","RECREATE")
zptHist.Write()
f.Write() 

