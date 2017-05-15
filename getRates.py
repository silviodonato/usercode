import ROOT

lumi = 2.E34

puRange = "pu>50"

### QuadJet_80_70_50_40_HT300_TripleBTagCSV_p070
#l1 = "l1HT>280 && Alt$(l1Jets_pt[0],0)>=80 && Alt$(l1Jets_pt[1],0)>=70 && Alt$(l1Jets_pt[2],0)>=50 && Alt$(l1Jets_pt[3],0)>=40"
#calo = "Sum$(caloJets_pt)>280 && Alt$(caloJets_pt[0],0)>=80 && Alt$(caloJets_pt[1],0)>=70 && Alt$(caloJets_pt[2],0)>=50 && Alt$(caloJets_pt[3],0)>=40"
#btag = "Sum$(caloJets_csv>0.7)>=3"
#pf = "Sum$(caloJets_pt)>300 && Alt$(caloJets_pt[0],0)>=80 && Alt$(caloJets_pt[1],0)>=70 && Alt$(caloJets_pt[2],0)>=50 && Alt$(caloJets_pt[3],0)>=40"
###

### || (l1HT>380) || (Sum$(l1Jets_pt>50 && abs(l1Jets_eta)<2.5)>=4)
### SixJet30_TripleBTagCSV_p07_OptB
l1 = "(l1HT>280 && Alt$(l1Jets_pt[0],0)>=80 && Alt$(l1Jets_pt[1],0)>=70 && Alt$(l1Jets_pt[2],0)>=50 && Alt$(l1Jets_pt[3],0)>=40)"
calo = "Alt$(caloJets_pt[5],0)>25"
btag = "Sum$(caloJets_csv>0.7)>=3"
pf = "Alt$(pfJets_pt[5],0)>30"
###


selection = "(%s) && (%s) && (%s) && (%s) && (%s) && ptHat>maxPUptHat "%(l1,calo,btag,pf,puRange)

#QuadJet_80_70_50_40_HT300_TripleBTagCSV_p070

def getFraction(fileName, selection):
    file_ = ROOT.TFile(fileName)
    tree = file_.Get("tree")
    den = file_.Get("Count").GetBinContent(1)
    num = tree.Draw("",selection)
    fraction = num/den
    if num<=0: return (0.,0.)
    file_.Close()
    return (fraction , (fraction*(1-fraction)/den)**0.5)

def getRate(fileName, selection, xsection, lumi):
    sampleRate = 1.E-36*xsection*lumi
    (fraction, errFraction) = getFraction(fileName, selection)
    return (sampleRate * fraction , sampleRate * errFraction)

## https://github.com/cms-steam/RateEstimate/blob/master/datasetCrossSections/datasetCrossSectionsSummer16.py#L66
bkgCrossSection = [
    ("QCD15to30.root"   , 1837410000.),
    ("QCD30to50.root"   , 140932000.),
    ("QCD50to80.root"   , 19204300.),
    ("QCD80to120.root"  , 2762530.),
    ("QCD120to170.root" , 471100.),
    ("QCD170to300.root" , 117276.),
    ("QCD300to470.root" , 7823.),
    ("QCD470to600.root" , 648.2),
]

totalRate = 0
totalRateError = 0

for (fileName,xsection) in bkgCrossSection:
    rate , rateError = getRate(fileName, selection, xsection, lumi)
    print fileName,"\t",rate," +/- ",rateError
    totalRate += rate
    totalRateError += rateError

print "totalRate\t",totalRate," +/- ",totalRateError

#for signal in ["VBFHbb.root","ttHbb.root","ggHbb.root","ggHH4b.root"]:
#    (fraction, errFraction) = getFraction(signal, selection)
#    print signal,"\t",fraction," +/- ",errFraction

