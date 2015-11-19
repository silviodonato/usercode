import ROOT

#samples = "TTbar"
#trigger = "HLT_IsoMu24_eta2p1_"
#rel1 = "760pre2"
#rel2 = "760pre1"

#samples = "TTbar"
#trigger = "HLT_Ele32_eta2p1_"
#rel1 = "760"
#rel2 = "760pre7"

#samples = "TTbar"
#trigger = "HLT_QuadPFJet_VBF"
#rel1 = "760"
#rel2 = "760pre7"

#samples = "TTbar"
#trigger = "HLT_QuadPFJet_VBF"
#rel1 = "760pre1"
#rel2 = "760pre2"

#samples = "QCD"
#trigger = "HLT_QuadPFJet_VBF"
#rel1 = "760pre1"
#rel2 = "760pre2"

#samples = "QCD"
#trigger = "HLT_QuadPFJet_VBF"
#rel1 = "760"
#rel2 = "760pre7"

#samples = "SMS"
#trigger = "HLT_Ele32_eta2p1_"
#rel1 = "760"
#rel2 = "760pre7"

#samples = "SMS"
#trigger = "HLT_QuadPFJet_VBF"
#rel1 = "760"
#rel2 = "760pre7"

#samples = "SMS"
#trigger = "HLT_QuadPFJet_VBF"
#rel1 = "760pre1"
#rel2 = "760pre2"

#samples = "TTbarNew"
#trigger = "HLT_QuadPFJet_VBF"
#rel1 = "760"
#rel2 = "760pre7"

#samples = "TTbarNew"
#trigger = "HLT_PFHT450_SixJet40_"
#rel1 = "760"
#rel2 = "760pre7"

#samples = "SMS"
#trigger = "HLT_QuadPFJet_VBF"
#rel1 = "760"
#rel2 = "760pre7"

#samples = "SMS"
#trigger = "HLT_PFHT450_SixJet40_"
#rel1 = "760"
#rel2 = "760pre7"

#samples = "QCDNew"
#trigger = "HLT_PFHT450_SixJet40_"
#rel1 = "760"
#rel2 = "760pre7"
#WPs = [0.40,0.54,0.58,0.70,0.72,0.78]

samples = "QCDNew"
trigger = "HLT_QuadPFJet_VBF"
rel1 = "760"
rel2 = "760pre7"
WPs = [0.20,0.40,0.45,0.55,0.67,0.72,0.74,0.85,0.90]

btag = "hltCombinedSecondaryVertexBJetTagsCalo__light_efficiency_vs_disc"
if trigger=="HLT_Ele32_eta2p1_" or trigger=="HLT_IsoMu24_eta2p1_" or trigger=="HLT_PFHT450_SixJet40_":
    btag = "hltCombinedSecondaryVertexBJetTagsPF__light_efficiency_vs_disc"
    


c1 = ROOT.TCanvas("c1","",1280,720)
npoints = 10
#WPs = [x*1./npoints for x in range(1,npoints)]

colors = [
ROOT.kBlack,

ROOT.kYellow+1,
ROOT.kRed,
ROOT.kMagenta,
ROOT.kBlue,
ROOT.kCyan+1,
ROOT.kGreen+1,

ROOT.kOrange,
ROOT.kPink,
ROOT.kViolet,
ROOT.kAzure,
ROOT.kTeal,
ROOT.kSpring,

ROOT.kGray,
] 

def sign(x):
    if x==0: return 1
    return x/abs(x)


#initdiff = -1.
initstep = 0.1
initwp2 = 1
def findNewWP(graph1,graph2,wp):
    val = graph1.Eval(wp)
    wp2 = initwp2
    val2 = graph2.Eval(wp2)
    diff = val2 - val
    step = initstep
    while step>0.0001:
        val2 = graph2.Eval(wp2)
        newdiff = val2 - val
#        print wp,wp2, newdiff
        if sign(newdiff)*sign(diff)<=0: step = step/2
        diff = newdiff
        wp2 = wp2 + step*sign(newdiff)
        if wp2<0-2*initstep or wp2>1+2*initstep:
            break
    
    return wp2

def getgraph(fileName,releasename,triggerName = "HLT_QuadPFJet_VBF",btag = "hltCombinedSecondaryVertexBJetTagsCalo__light_efficiency_vs_disc"):
    import copy
    graphName = "DQMData/Run 1/HLT/Run summary/BTag/Discriminator/%s/efficiency/%s" %(triggerName,btag)
    myfile = ROOT.TFile(fileName)
    graph = myfile.Get(graphName).Clone(releasename)
    graphs[releasename] = copy.copy(graph)
#    graphs[releasename] = copy.copy(ROOT.TGraph(graph))
    return

filenames={}
if samples == "QCD":
    filenames["760"]="DQM_V0001_R000000001__RelValQCD_FlatPt_15_3000HS_13__CMSSW_7_6_0-76X_mcRun2_asymptotic_v11-v1__DQMIO.root"
    filenames["760pre1"]="DQM_V0001_R000000001__RelValQCD_FlatPt_15_3000HS_13__CMSSW_7_6_0_pre1-75X_mcRun2_asymptotic_v1-v1__DQMIO.root"
    filenames["760pre2"]="DQM_V0001_R000000001__RelValQCD_FlatPt_15_3000HS_13__CMSSW_7_6_0_pre2-75X_mcRun2_asymptotic_v2-v1__DQMIO.root"
    filenames["760pre7"]="DQM_V0001_R000000001__RelValQCD_FlatPt_15_3000HS_13__CMSSW_7_6_0_pre7-76X_mcRun2_asymptotic_v5-v1__DQMIO.root"
elif samples == "TTbar":
    filenames["760"]="DQM_V0001_R000000001__RelValTTbar_13__CMSSW_7_6_0-PU25ns_76X_mcRun2_asymptotic_v11-v1__DQMIO.root"
    filenames["760pre1"]="DQM_V0001_R000000001__RelValTTbar_13__CMSSW_7_6_0_pre1-PU25ns_75X_mcRun2_asymptotic_v1-v1__DQMIO.root"
    filenames["760pre2"]="DQM_V0001_R000000001__RelValTTbar_13__CMSSW_7_6_0_pre2-PU25ns_75X_mcRun2_asymptotic_v2-v1__DQMIO.root"
    filenames["760pre7"]="DQM_V0001_R000000001__RelValTTbar_13__CMSSW_7_6_0_pre7-PU25ns_76X_mcRun2_asymptotic_v5-v1__DQMIO.root"
elif samples == "TTbarNew":
    filenames["760"]="DQM_TTbar_760.root"
    filenames["760pre7"]="DQM_TTbar_760pre7.root"
elif samples == "QCDNew":
    filenames["760"]="DQM_V0001_R000000001__CMSSW_7_6_0__RelVal__TrigVal.root"
    filenames["760pre7"]="DQM_V0001_R000000001__CMSSW_7_6_0_pre7__RelVal__TrigVal.root"
elif samples == "SMS":
    filenames["760"]="DQM_V0001_R000000001__RelValSMS-T1tttt_mGl-1500_mLSP-100_13__CMSSW_7_6_0-PU25ns_76X_mcRun2_asymptotic_v11-v1__DQMIO.root"
    filenames["760pre1"]="DQM_V0001_R000000001__RelValSMS-T1tttt_mGl-1500_mLSP-100_13__CMSSW_7_6_0_pre1-PU25ns_75X_mcRun2_asymptotic_v1-v1__DQMIO.root"
    filenames["760pre2"]="DQM_V0001_R000000001__RelValSMS-T1tttt_mGl-1500_mLSP-100_13__CMSSW_7_6_0_pre2-PU25ns_75X_mcRun2_asymptotic_v2-v1__DQMIO.root"
    filenames["760pre7"]="DQM_V0001_R000000001__RelValSMS-T1tttt_mGl-1500_mLSP-100_13__CMSSW_7_6_0_pre7-PU25ns_76X_mcRun2_asymptotic_v5-v1__DQMIO.root"

releases = (filenames.keys())
releases.sort()

fits = {}
graphs = {}
leg = ROOT.TLegend(0.7,0.7,0.9,0.9)
for i,release in enumerate(releases):
    print filenames[release],release,trigger,btag
    getgraph(filenames[release],release,trigger,btag)
    graph = graphs[release]
    graph.SetLineColor(colors[i])
    graph.SetMarkerColor(colors[i])
    fits[release]=ROOT.TF1(release,"pol8",0,1)
    fits[release].SetLineColor(colors[i])
    graph.Fit(fits[release],"","",0.2,0.92)
    leg.AddEntry(graph,release,"ml")

for i,release in enumerate(releases):
    graphs[release].SetMaximum(0.5)
    graphs[release].SetMinimum(0.01)
    graphs[release].GetXaxis().SetRangeUser(0.1,0.9)
    graphs[release].GetXaxis().SetTitle("online CSV")
    graphs[release].GetYaxis().SetTitle("fake rate")
    graphs[release].SetTitle("online b-tagging fake rate vs discriminant")
#    if i==0: graphs[release].Draw("ALP")
#    else: graphs[release].Draw("LP")
    if i==0: graphs[release].Draw("")
    else: graphs[release].Draw("same")

leg.Draw("")
c1.SetGridx()
c1.SetGridy()
c1.SetLogy()
name = trigger+"_"+samples
c1.SaveAs(name+".png")
c1.Close()

#graph1 = graphs[rel1]
#graph2 = graphs[rel2]
graph1 = fits[rel1]
graph2 = fits[rel2]

name = name + rel1+"_"+rel2
out_file = open(name+".txt","w")

newWPs = [findNewWP(graph1,graph2,wp) for wp in WPs]
for (wp1,wp2) in zip(WPs,newWPs):
    print "%1.3f\t%1.3f" %(wp1,wp2)
    out_file.write("%1.3f\t%1.3f\n" %(wp1,wp2))
    
out_file.close()

