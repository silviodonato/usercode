trigger="HLT_Ele27_eta2p1_WPLoose_Gsf_v1"
fileName='Run2015B_SingleElectron_MINIAOD_PromptReco-v1_251_244.root'
jetCollection="hltPFJetForBtagSelector"
bJetCollection="hltCSVFilterSingleTop"
deltaRMatching=0.4
pt_max=30
eta_max=2.4

NHFmax=0.99
NEMFmax=0.99
CHFmin=0.
MUFmax=0.8
CEMFmax=0.99
NumConstMin=1
CHMmin=0
                
from math import sqrt, pi, log10, log, exp
from array import array
def deltaPhi(phi1, phi2):
  PHI = abs(phi1-phi2)
  if PHI<=pi:
      return PHI
  else:
      return 2*pi-PHI

def deltaR(eta1, phi1, eta2, phi2):
  deta = eta1-eta2
  dphi = deltaPhi(phi1,phi2)
  return sqrt(deta*deta + dphi*dphi)
  
def function(x):
    x = min(x,0.999999999999999)
    x = max(x,0.000000000000001)
#    y=x
    y=-log10(1.-x)
#    y=x/exp(x)*exp(1)
    return y

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.AutoLibraryLoader.enable()

c1 = ROOT.TCanvas("c1")

dRplot = ROOT.TH1F("dRplot","",4000,0,3.5)

num = ROOT.TH1F("num","",100,0.,1.)
num.GetXaxis().SetTitle("offline CSVv2IVF")
num.GetYaxis().SetTitle("Events")
num.SetLineWidth(2)
num.SetMarkerSize(2)
den = num.Clone("den")
efficiency = num.Clone("efficiency")
efficiency.GetYaxis().SetTitle("Efficiency")

points = [0.0, 0.032, 0.036000000000000004, 0.04, 0.044, 0.048, 0.052000000000000005, 0.056, 0.06, 0.064, 0.068, 0.07200000000000001, 0.076, 0.08, 0.084, 0.088, 0.092, 0.096, 0.1, 0.10400000000000001, 0.108, 0.112, 0.116, 0.12, 0.124, 0.128, 0.132, 0.136, 0.14, 0.14400000000000002, 0.148, 0.152, 0.156, 0.16, 0.164, 0.168, 0.17200000000000001, 0.176, 0.18, 0.184, 0.188, 0.192, 0.196, 0.2, 0.20400000000000001, 0.20800000000000002, 0.212, 0.216, 0.22, 0.224, 0.228, 0.232, 0.23600000000000002, 0.24, 0.244, 0.248, 0.252, 0.256, 0.26, 0.264, 0.268, 0.272, 0.276, 0.28, 0.28400000000000003, 0.28800000000000003, 0.292, 0.296, 0.3, 0.304, 0.308, 0.312, 0.316, 0.32, 0.324, 0.328, 0.332, 0.336, 0.34, 0.34400000000000003, 0.34800000000000003, 0.352, 0.356, 0.36, 0.364, 0.368, 0.372, 0.376, 0.38, 0.384, 0.388, 0.392, 0.396, 0.4, 0.404, 0.40800000000000003, 0.41200000000000003, 0.42, 0.424, 0.428, 0.432, 0.436, 0.44, 0.444, 0.452, 0.456, 0.46, 0.464, 0.47200000000000003, 0.48, 0.488, 0.496, 0.5, 0.508, 0.512, 0.516, 0.52, 0.524, 0.528, 0.532, 0.536, 0.54, 0.544, 0.548, 0.552, 0.556, 0.56, 0.5640000000000001, 0.5680000000000001, 0.5720000000000001, 0.5760000000000001, 0.58, 0.584, 0.588, 0.592, 0.596, 0.6, 0.604, 0.608, 0.612, 0.616, 0.62, 0.624, 0.628, 0.632, 0.636, 0.64, 0.644, 0.648, 0.652, 0.656, 0.66, 0.664, 0.668, 0.672, 0.676, 0.68, 0.684, 0.6880000000000001, 0.6920000000000001, 0.6960000000000001, 0.7000000000000001, 0.704, 0.708, 0.712, 0.716, 0.72, 0.724, 0.732, 0.736, 0.74, 0.744, 0.748, 0.752, 0.756, 0.76, 0.764, 0.768, 0.772, 0.776, 0.78, 0.784, 0.788, 0.792, 0.796, 0.8, 0.808, 0.812, 0.8160000000000001, 0.8200000000000001, 0.8240000000000001, 0.8280000000000001, 0.8320000000000001, 0.84, 0.844, 0.848, 0.852, 0.856, 0.86, 0.864, 0.868, 0.876, 0.88, 0.884, 0.892, 0.896, 0.9, 0.904, 0.908, 0.912, 0.92, 0.928, 0.932, 0.936, 0.9400000000000001, 0.9440000000000001, 0.9480000000000001, 0.9520000000000001, 0.96, 0.964, 0.968, 0.976, 0.984, 0.988, 0.996, 1.0, 1.004, 1.008, 1.012, 1.016, 1.024, 1.028, 1.032, 1.036, 1.04, 1.044, 1.052, 1.06, 1.064, 1.068, 1.076, 1.084, 1.092, 1.096, 1.104, 1.112, 1.116, 1.124, 1.1320000000000001, 1.1360000000000001, 1.1400000000000001, 1.1480000000000001, 1.156, 1.16, 1.164, 1.172, 1.176, 1.18, 1.184, 1.188, 1.196, 1.204, 1.212, 1.228, 1.24, 1.256, 1.268, 1.276, 1.284, 1.296, 1.304, 1.324, 1.344, 1.36, 1.368, 1.3760000000000001, 1.3880000000000001, 1.4040000000000001, 1.42, 1.432, 1.444, 1.46, 1.48, 1.492, 1.508, 1.52, 1.532, 1.544, 1.568, 1.584, 1.608, 1.624, 1.6440000000000001, 1.668, 1.688, 1.708, 1.728, 1.76, 1.8, 1.824, 1.836, 1.848, 1.8760000000000001, 1.9000000000000001, 1.928, 1.964, 2.008, 2.044, 2.076, 2.12, 2.18, 2.236, 2.2720000000000002, 2.308, 2.38, 2.416, 2.456, 2.492, 2.532, 2.58, 2.628, 2.724, 2.7760000000000002, 2.7920000000000003, 2.856, 2.932, 2.968, 3.064, 3.104, 3.2, 3.2760000000000002, 3.368, 3.512, 3.648, 4.0440000000000005, 5]


varBinLog = array('f',points)

numLog = ROOT.TH1F("numLog","",len(varBinLog)-1,varBinLog)
#numLog = ROOT.TH1F("numLog","",10000,0,10)
numLog.Rebin(4)
numLog.GetXaxis().SetTitle("-Log(1-CSV)")
numLog.GetYaxis().SetTitle("Events")
numLog.SetLineWidth(2)
numLog.SetMarkerSize(2)
denLog = numLog.Clone("denLog")
efficiencyLog = numLog.Clone("efficiencyLog")
efficiencyLog.GetYaxis().SetTitle("Efficiency")

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults","","HLT")
triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "selectedPatTrigger"
triggerPrescales, triggerPrescaleLabel  = Handle("pat::PackedTriggerPrescales"), "patTrigger"
patJets, patJetLabel = Handle("vector<pat::Jet>"), ("slimmedJets")

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
events = Events ([fileName])

for iev,event in enumerate(events):
    if iev%1000==0: print "iev=",iev
    event.getByLabel(triggerBitLabel, triggerBits)
    event.getByLabel(triggerObjectLabel, triggerObjects)
    event.getByLabel(triggerPrescaleLabel, triggerPrescales)
    event.getByLabel(patJetLabel, patJets)

    names = event.object().triggerNames(triggerBits.product())
    index = names.triggerIndex(trigger)
    if triggerBits.product().accept(index):
        for jet in patJets.product():
                offlineCSV = jet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")
                if jet.pt()>pt_max and abs(jet.eta())<eta_max and offlineCSV>0 \
                and jet.neutralHadronEnergyFraction()<NHFmax \
                and jet.neutralEmEnergyFraction()<NEMFmax \
                and jet.chargedHadronEnergyFraction()>CHFmin \
                and jet.muonEnergyFraction()<MUFmax \
                and jet.chargedEmEnergyFraction()<CEMFmax \
                and jet.chargedMultiplicity()+jet.neutralMultiplicity()>NumConstMin \
                and jet.chargedMultiplicity()>CHMmin :
                    mindRJet = 999
                    mindRCSV = 999
                    for j,to in enumerate(triggerObjects.product()):
                        to.unpackPathNames(names)
                        if jetCollection in to.filterLabels():
                            dR = deltaR(to.eta(),to.phi(),jet.eta(),jet.phi())
                            mindRJet = min(mindRJet,dR)
                        dRplot.Fill(mindRJet)
                        if mindRJet>deltaRMatching: continue ## ignore jets that don't pass HLT jets selection 
                        if bJetCollection in to.filterLabels():
                            dR = deltaR(to.eta(),to.phi(),jet.eta(),jet.phi())
                            mindRCSV = min(mindRCSV,dR)
                    if mindRJet<deltaRMatching:
                        if mindRCSV<deltaRMatching:
                            num.Fill((offlineCSV))
                            den.Fill((offlineCSV))
                            numLog.Fill(function(offlineCSV))
                            denLog.Fill(function(offlineCSV))
                        else:
                            den.Fill((offlineCSV))
                            denLog.Fill(function(offlineCSV))

dRplot.Draw()
c1.SetLogy(1)
c1.SaveAs("dRplot.C")
c1.SaveAs("dRplot.png")
c1.SetLogy(0)

num.Sumw2()
den.Sumw2()
efficiency.Divide(num, den,1.,1.,"b");
efficiency.Draw()
efficiency.SetLineColor(ROOT.kBlue)
c1.SaveAs("turnonCSV.C")
c1.SaveAs("turnonCSV.png")

den.Draw()
num.Draw("same")
den.SetLineColor(ROOT.kBlue)
num.SetLineColor(ROOT.kRed)
c1.SetLogy(1)
c1.SaveAs("distro.C")
c1.SaveAs("distro.png")
c1.SetLogy(0)

numLog.Sumw2()
denLog.Sumw2()
efficiencyLog.Divide(numLog, denLog,1.,1.,"b");
efficiencyLog.Draw()
efficiencyLog.SetLineColor(ROOT.kBlue)
c1.SaveAs("turnonCSVLog.C")
c1.SaveAs("turnonCSVLog.png")

denLog.Draw()
numLog.Draw("same")
denLog.SetLineColor(ROOT.kBlue)
numLog.SetLineColor(ROOT.kRed)
c1.SetLogy(1)
c1.SaveAs("distroLog.C")
c1.SaveAs("distroLog.png")
c1.SetLogy(0)
