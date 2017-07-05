import FWCore.ParameterSet.Config as cms
from HLTrigger.Configuration.common import *

def customize(process):
    if hasattr(process, "hltEgammaEleGsfTrackIso"):
        process.hltEgammaEleGsfTrackIso.egTrkIsoConeSize = cms.double(0.2)
        process.hltEgammaEleGsfTrackIso.egTrkIsoStripBarrel = cms.double(0.01)
        process.hltEgammaEleGsfTrackIso.egTrkIsoStripEndcap = cms.double(0.01)
        
    for filter_ in process._Process__filters.values():
        if filter_.label() == None: continue
        if "WPTightClusterShapeFilter" in filter_.label():
            filter_.thrRegularEB = cms.vdouble(0.011)
            filter_.thrRegularEE = cms.vdouble(0.0305)
        if "WPTightGsfDetaFilter" in filter_.label():
            filter_.thrRegularEE = cms.vdouble(999.005)
            filter_.useEt = cms.bool(False)
        if "WPTightGsfDphiFilter" in filter_.label():
            filter_.thrRegularEE = cms.vdouble(999.023)
            filter_.useEt = cms.bool(False)
        if "WPTightGsfMissingHitsFilter" in filter_.label():
            filter_.useEt = cms.bool(False)
            filter_.candTag = filter_.label().replace("WPTightGsfMissingHitsFilter","WPTightGsfOneOEMinusOneOPFilter")
        if "WPTightGsfOneOEMinusOneOPFilter" in filter_.label():
            filter_.thrRegularEB = cms.vdouble(0.012)
            filter_.thrRegularEE = cms.vdouble(0.011)
            filter_.useEt = cms.bool(False)
            filter_.candTag = filter_.label().replace("WPTightGsfOneOEMinusOneOPFilter","WPTightPMS2Filter")
        if "WPTightEcalIsoFilter" in filter_.label():
            newFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
                absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
                candTag = filter_.candTag,
                doRhoCorrection = cms.bool(True),
                effectiveAreas = cms.vdouble(0.325, 0.296, 0.283, 0.438),
                energyLowEdges = cms.vdouble(0.0),
                etaBoundaryEB12 = cms.double(1.0),
                etaBoundaryEE12 = cms.double(2.1),
                l1EGCand = cms.InputTag("hltEgammaCandidates"),
                lessThan = cms.bool(True),
                ncandcut = filter_.ncandcut,
                rhoMax = cms.double(99999999.0),
                rhoScale = cms.double(1.0),
                rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
                saveTags = cms.bool(True),
                thrOverE2EB1 = cms.vdouble(0.0),
                thrOverE2EB2 = cms.vdouble(0.0),
                thrOverE2EE1 = cms.vdouble(0.0),
                thrOverE2EE2 = cms.vdouble(0.0),
                thrOverEEB1 = cms.vdouble(0.03),
                thrOverEEB2 = cms.vdouble(0.03),
                thrOverEEE1 = cms.vdouble(0.025),
                thrOverEEE2 = cms.vdouble(0.025),
                thrRegularEB1 = cms.vdouble(-0.581),
                thrRegularEB2 = cms.vdouble(-0.698),
                thrRegularEE1 = cms.vdouble(-0.892),
                thrRegularEE2 = cms.vdouble(-0.885),
                useEt = cms.bool(True),
                varTag = cms.InputTag("hltEgammaEcalPFClusterIso")
            )
            replace_with(filter_,newFilter)
        if "WPTightGsfTrackIsoFilter" in filter_.label():
            newFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
                absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
                candTag = filter_.candTag,
                doRhoCorrection = cms.bool(True),
                effectiveAreas = cms.vdouble(0.029, 0.111, 0.114, 0.032),
                energyLowEdges = cms.vdouble(0.0),
                etaBoundaryEB12 = cms.double(1.0),
                etaBoundaryEE12 = cms.double(2.1),
                l1EGCand = cms.InputTag("hltEgammaCandidates"),
                lessThan = cms.bool(True),
                ncandcut = filter_.ncandcut,
                rhoMax = cms.double(99999999.0),
                rhoScale = cms.double(1.0),
                rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
                saveTags = cms.bool(True),
                thrOverE2EB1 = cms.vdouble(0.0),
                thrOverE2EB2 = cms.vdouble(0.0),
                thrOverE2EE1 = cms.vdouble(0.0),
                thrOverE2EE2 = cms.vdouble(0.0),
                thrOverEEB1 = cms.vdouble(0.03),
                thrOverEEB2 = cms.vdouble(0.03),
                thrOverEEE1 = cms.vdouble(0.025),
                thrOverEEE2 = cms.vdouble(0.025),
                thrRegularEB1 = cms.vdouble(0.838),
                thrRegularEB2 = cms.vdouble(-0.385),
                thrRegularEE1 = cms.vdouble(-0.363),
                thrRegularEE2 = cms.vdouble(0.702),
                useEt = cms.bool(True),
                varTag = cms.InputTag("hltEgammaEleGsfTrackIso")
            )
            replace_with(filter_,newFilter)
        if "WPTightHEFilter" in filter_.label():
            newFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
                absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
                candTag = filter_.candTag,
                doRhoCorrection = cms.bool(True),
                effectiveAreas = cms.vdouble(0.098, 0.159, 0.353, 0.423),
                energyLowEdges = cms.vdouble(0.0),
                etaBoundaryEB12 = cms.double(1.0),
                etaBoundaryEE12 = cms.double(2.1),
                l1EGCand = cms.InputTag("hltEgammaCandidates"),
                lessThan = cms.bool(True),
                ncandcut = filter_.ncandcut,
                rhoMax = cms.double(99999999.0),
                rhoScale = cms.double(1.0),
                rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
                saveTags = cms.bool(True),
                thrOverE2EB1 = cms.vdouble(0.0),
                thrOverE2EB2 = cms.vdouble(0.0),
                thrOverE2EE1 = cms.vdouble(0.0),
                thrOverE2EE2 = cms.vdouble(0.0),
                thrOverEEB1 = cms.vdouble(0.02),
                thrOverEEB2 = cms.vdouble(0.02),
                thrOverEEE1 = cms.vdouble(0.015),
                thrOverEEE2 = cms.vdouble(0.015),
                thrRegularEB1 = cms.vdouble(0.887),
                thrRegularEB2 = cms.vdouble(1.476),
                thrRegularEE1 = cms.vdouble(2.672),
                thrRegularEE2 = cms.vdouble(5.095),
                useEt = cms.bool(False),
                varTag = cms.InputTag("hltEgammaHoverE")
            )
            replace_with(filter_,newFilter)
        if "WPTightHcalIsoFilter" in filter_.label():
            newFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
                absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
                candTag = filter_.candTag,
                doRhoCorrection = cms.bool(True),
                effectiveAreas = cms.vdouble(0.259, 0.328, 0.414, 0.456),
                energyLowEdges = cms.vdouble(0.0),
                etaBoundaryEB12 = cms.double(1.0),
                etaBoundaryEE12 = cms.double(2.1),
                l1EGCand = cms.InputTag("hltEgammaCandidates"),
                lessThan = cms.bool(True),
                ncandcut = filter_.ncandcut,
                rhoMax = cms.double(99999999.0),
                rhoScale = cms.double(1.0),
                rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForMuons"),
                saveTags = cms.bool(True),
                thrOverE2EB1 = cms.vdouble(0.0),
                thrOverE2EB2 = cms.vdouble(0.0),
                thrOverE2EE1 = cms.vdouble(0.0),
                thrOverE2EE2 = cms.vdouble(0.0),
                thrOverEEB1 = cms.vdouble(0.03),
                thrOverEEB2 = cms.vdouble(0.03),
                thrOverEEE1 = cms.vdouble(0.025),
                thrOverEEE2 = cms.vdouble(0.025),
                thrRegularEB1 = cms.vdouble(0.786),
                thrRegularEB2 = cms.vdouble(0.298),
                thrRegularEE1 = cms.vdouble(0.402),
                thrRegularEE2 = cms.vdouble(-0.061),
                useEt = cms.bool(True),
                varTag = cms.InputTag("hltEgammaHcalPFClusterIso")
            )
            replace_with(filter_,newFilter)
        if "WPTightPixelMatchFilter" in filter_.label():
            label = filter_.label()
            newLabel = label.replace("WPTightPixelMatchFilter","WPTightPMS2Filter")
            newModule = cms.EDFilter("HLTEgammaGenericFilter",
                absEtaLowEdges = cms.vdouble(0.0, 1.479),
                candTag = cms.InputTag(label),
                doRhoCorrection = cms.bool(False),
                effectiveAreas = cms.vdouble(0.0, 0.0),
                energyLowEdges = cms.vdouble(0.0),
                l1EGCand = cms.InputTag("hltEgammaCandidates"),
                lessThan = cms.bool(True),
                ncandcut = filter_.ncandcut,
                rhoMax = cms.double(99999999.0),
                rhoScale = cms.double(1.0),
                rhoTag = cms.InputTag(""),
                saveTags = cms.bool(True),
                thrOverE2EB = cms.vdouble(-1.0),
                thrOverE2EE = cms.vdouble(-1.0),
                thrOverEEB = cms.vdouble(-1.0),
                thrOverEEE = cms.vdouble(-1.0),
                thrRegularEB = cms.vdouble(70.0),
                thrRegularEE = cms.vdouble(45.0),
                useEt = cms.bool(False),
                varTag = cms.InputTag("hltEgammaPixelMatchVars","s2")
            )
            setattr(process,newLabel,newModule)
    for sequence in process._Process__sequences.itervalues():
        if "WPTightGsf" in sequence.label():
            pixelMatchfilter_ = 0
            for mod in sequence.moduleNames():
                if "WPTightPixelMatchFilter" in mod:
                    pixelMatchfilter_ = getattr(process,mod)
                    newModule = cms.EDFilter("HLTEgammaGenericFilter",
                        absEtaLowEdges = cms.vdouble(0.0, 1.479),
                        candTag = cms.InputTag(mod),
                        doRhoCorrection = cms.bool(False),
                        effectiveAreas = cms.vdouble(0.0, 0.0),
                        energyLowEdges = cms.vdouble(0.0),
                        l1EGCand = cms.InputTag("hltEgammaCandidates"),
                        lessThan = cms.bool(True),
                        ncandcut = pixelMatchfilter_.ncandcut,
                        rhoMax = cms.double(99999999.0),
                        rhoScale = cms.double(1.0),
                        rhoTag = cms.InputTag(""),
                        saveTags = cms.bool(True),
                        thrOverE2EB = cms.vdouble(-1.0),
                        thrOverE2EE = cms.vdouble(-1.0),
                        thrOverEEB = cms.vdouble(-1.0),
                        thrOverEEE = cms.vdouble(-1.0),
                        thrRegularEB = cms.vdouble(70.0),
                        thrRegularEE = cms.vdouble(45.0),
                        useEt = cms.bool(False),
                        varTag = cms.InputTag("hltEgammaPixelMatchVars","s2")
                    )
                    setattr(process,mod.replace("WPTightPixelMatchFilter","WPTightPMS2Filter"),newModule)
                if "WPTightGsfChi2Filter" in mod:
                    sequence.remove(getattr(process,mod))
            if not pixelMatchfilter_ is 0:
                sequence.insert(sequence.index(pixelMatchfilter_)+1,newModule)
        
    for producer in producers_by_type(process, "EgammaHLTElectronTrackIsolationProducers"):
        producer.egTrkIsoStripEndcap = cms.double(0.01)
        producer.egTrkIsoStripBarrel = cms.double(0.01)
        producer.egTrkIsoConeSize = cms.double(0.2)
    
    return process
