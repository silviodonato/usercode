import ROOT
import copy

def THNFtoTH1F(histo3D):
    nx = histo3D.GetNbinsX()
    ny = histo3D.GetNbinsY()
    nz = histo3D.GetNbinsZ()
    if histo3D.GetDimension() == 1:
        nbins = (nx+2) 
    elif histo3D.GetDimension() == 2:
        nbins = (nx+2)*(ny+2) 
    elif histo3D.GetDimension() == 3:
        nbins = (nx+2)*(ny+2)*(nz+2) 
    else:
        print("EROR dimension", histo3D.GetDimension())
    histo1D = ROOT.TH1F("histo1D","",nbins-2,0,nbins-2)
    histo1D.Sumw2()
    if histo3D.fN != histo1D.fN:
        print("histo3D.fN",histo3D.fN)
        print("histo1D.fN",histo1D.fN)
        print("must be identical!")
    for i in range(histo1D.fN):
        histo1D.GetSumw2()[i] = histo3D.GetSumw2()[i]
        histo1D.GetArray()[i] = histo3D.GetArray()[i]
        print(i,histo1D.GetSumw2()[i])
    return copy.copy(histo1D)

def TH1FtoTHNF(histo1D,histo3D):
    if histo3D.fN != histo1D.fN:
        print("histo3D.fN",histo3D.fN)
        print("histo1D.fN",histo1D.fN)
        print("must be identical!")
        return
    for i in range(histo1D.fN):
        histo3D.GetSumw2()[i] = histo1D.GetSumw2()[i]
        histo3D.GetArray()[i] = histo1D.GetArray()[i]
    return histo3D


def GetEfficiencyTHNF(num,den):
    ## Convert THNF num and den histo to TH1F
    num_1d = THNFtoTH1F(num)
    den_1d = THNFtoTH1F(den)
    
    ## Calculate the effienciency
    nbins = num_1d.GetNbinsX()
    eff = ROOT.TEfficiency(num_1d,den_1d);
    
    ## Convert TEffiency in TH1F
    eff_1d = num_1d.Clone("eff")
    eff_1d.Reset()
    for i in range(nbins+2):
        eff_1d.SetBinContent(i,eff.GetEfficiency(i))
        eff_1d.SetBinError(i,(eff.GetEfficiencyErrorUp(i)+eff.GetEfficiencyErrorLow(i))/2)
    print("Done")
    
    ## Convert TH1F in THNF
    eff = den.Clone("eff_data")
    eff.Reset()
    eff = TH1FtoTHNF(eff_1d, eff)
    
    return eff

## Generate num and den THNF histo
xmax = 10
ymax = 20
zmax = 30
num_data = ROOT.TH3F ("num_data","",xmax,0,xmax,ymax,0,ymax,zmax,0,zmax)
den_data = ROOT.TH3F ("den_data","",xmax,0,xmax,ymax,0,ymax,zmax,0,zmax)

k=1
for i in range(1,xmax+1):
    for j in range(1,ymax+1):
        for k in range(1,zmax+1):
            val = i * j * k
            num_data.SetBinContent(i,j,k,5*0.5132412*(val))
            den_data.SetBinContent(i,j,k,5*0.5132412*(val))

num_data.Sumw2()
den_data.Sumw2()

## Get Efficiency
eff_data = GetEfficiencyTHNF (num_data, den_data)

## Plot and checks
eff_data.Draw("LEGO")

print("num:",num_data.GetBinContent(5,5,5))
print("den:",den_data.GetBinContent(5,5,5))
print("eff:",eff_data.GetBinContent(5,5,5)," +/- ", eff_data.GetBinError(5,5,5))

print("num:",num_data.GetBinContent(9,9,9))
print("den:",den_data.GetBinContent(9,9,9))
print("eff:",eff_data.GetBinContent(9,9,9)," +/- ", eff_data.GetBinError(9,9,9))
