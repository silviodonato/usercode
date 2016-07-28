import sys
from ROOT import *
from DataFormats.FWLite import Handle, Events

ImpPar_source, ImpPar_label = Handle("vector<reco::IPTagInfo<edm::RefVector< vector<reco::Track>,reco::Track,edm::refhelper::FindUsingAdvance< vector<reco::Track>,reco::Track> >,reco::JTATagInfo> >"), ("hltImpactParameterTagInfos")

filesInput = [sys.argv[1]]
events = Events (filesInput)

for iev,event in enumerate(events):
    event.getByLabel(ImpPar_label, ImpPar_source)
    print "event: ",iev
    ImpParJets = ImpPar_source.product()
    for ImpParJet in ImpParJets:
        ImpParTracks = ImpParJet.impactParameterData()
        for ImpParTrack in ImpParTracks:
            print ImpParTrack.ip3d.value()/ImpParTrack.ip3d.error()

