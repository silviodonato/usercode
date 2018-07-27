def TH3FtoTH1F(histo3D):
    nx = histo3D.GetNbinsX()
    ny = histo3D.GetNbinsY()
    nz = histo3D.GetNbinsZ()
    nbins = (nx+2)*(ny+2)*(nz+2) - 2
    histo1D = ROOT.TH1F("histo1D","",nbins,0,nbins)
    histo1D.Sumw2()
    if histo3D.fN != histo1D.fN:
        print("histo3D.fN",histo3D.fN)
        print("histo1D.fN",histo1D.fN)
        print("must be identical!")
    for i in range(histo1D.fN):
        histo1D.GetSumw2()[i] = histo3D.GetSumw2()[i]
        histo1D.GetArray()[i] = histo3D.GetArray()[i]
    
    histo1D.Modify()
    histo3D.Modify()
    return copy.copy(histo1D)

def TH1FtoTH3F(histo1D,histo3D):
    if histo3D.fN != histo1D.fN:
        print("histo3D.fN",histo3D.fN)
        print("histo1D.fN",histo1D.fN)
        print("must be identical!")
        return
    for i in range(histo1D.fN):
        histo3D.GetSumw2()[i] = histo1D.GetSumw2()[i]
        histo3D.GetArray()[i] = histo1D.GetArray()[i]
    histo1D.Modify()
    histo3D.Modify()
    return histo3D
