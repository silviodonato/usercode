import FWCore.ParameterSet.Config as cms

def replaceTrackMerger(process):
    if not 'hltScoutingTracks' in process.__dict__:
        return process
    
    # replace TrackListMerger with TrackSimpleMerger
    process.hltScoutingTracks = cms.EDProducer('TrackSimpleMerger',
       src = process.hltScoutingTracks.TrackProducers
    )
    
    return process


#process.hltScoutingTracks = cms.EDProducer("TrackListMerger",
#    Epsilon = cms.double(-0.001),
#    FoundHitBonus = cms.double(5.0),
#    LostHitPenalty = cms.double(5.0),
#    MaxNormalizedChisq = cms.double(1000.0),
#    MinFound = cms.int32(3),
#    MinPT = cms.double(0.05),
#    ShareFrac = cms.double(0.19),
#    TrackProducers = cms.VInputTag("hltPixelTracksToNotBeExtended", "hltIter0PFlowTrackSelectionHighPurityForScouting"),
#    allowFirstHitShare = cms.bool(False),
#    copyExtras = cms.untracked.bool(False),
#    copyMVA = cms.bool(False),
#    hasSelector = cms.vint32(0, 0),
#    indivShareFrac = cms.vdouble(1.0, 1.0),
#    newQuality = cms.string(''),
#    selectedTrackQuals = cms.VInputTag("hltPixelTracksToNotBeExtended", "hltIter0PFlowTrackSelectionHighPurityForScouting"),
#    setsToMerge = cms.VPSet(cms.PSet(
#        pQual = cms.bool(False),
#        tLists = cms.vint32(0, 1)
#    )),
#    trackAlgoPriorityOrder = cms.string('hltESPTrackAlgoPriorityOrder'),
#    writeOnlyTrkQuals = cms.bool(False)
#)

#process.hltScoutingTracks = cms.EDProducer('TrackSimpleMerger',
#       src = cms.VInputTag(cms.InputTag('hltPixelTracksToNotBeExtended'), cms.InputTag('hltIter0PFlowTrackSelectionHighPurityForScouting'))
#)

