from ROOT import TFile
_file = TFile("ntuple.root")
#_file = TFile("ntuplePU_73.root")
tree = _file.Get("minBiasNtuple/tree");
leadingGenJets = {}
for event in tree:
    leadingGenJets[event.nevent] = event.leadingGenJet

nfile = 0
prevfile = -1
file_ = 0
for nevent in leadingGenJets:
    nfile = event.nevent/1000000
    if(nfile != prevfile):
        file_=file(nfile+".txt","w+")
        print "Creating "+nfile+".txt"
    file_.write(str(nevent)+"\t"+str(leadingGenJet[nevent])+"\n")

