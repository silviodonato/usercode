import sys
from ROOT import *
from DataFormats.FWLite import Handle, Events

#filesInput = "~/TTbar_GEN-SIM-RAW_PhaseI_81X_FlatPU28to62.root"
filesInput = "~/ttH_RAWMINIAODSIM.root"

print
print "Opening ",filesInput
print
events = Events (filesInput)
for iev,event in enumerate(events): break

#puSummaryInfos_source, puSummaryInfos_label = Handle("vector<PileupSummaryInfo>"), ("addPileupInfo")
puSummaryInfos_source, puSummaryInfos_label = Handle("vector<PileupSummaryInfo>"), ("slimmedAddPileupInfo")
event.getByLabel(puSummaryInfos_label, puSummaryInfos_source)

puSummaryInfos = puSummaryInfos_source.product()

for bx in range(puSummaryInfos.size()):
    print
    print "BX = ",bx
    puSummaryInfo = puSummaryInfos.at(bx)
    print "bunchCrossing=",puSummaryInfo.getBunchCrossing()
    print "trueNumInteractions=",puSummaryInfo.getTrueNumInteractions()
    print "pT_hats size=",puSummaryInfo.getPU_pT_hats().size()
    print "zpositions size=",puSummaryInfo.getPU_zpositions().size()
    print "EventID size=",puSummaryInfo.getPU_EventID().size()
    print "Int. ",puSummaryInfo.getPU_NumInteractions()
    print "pt-Hat ,\tzPosition ,\tEventID"
    for i in range(puSummaryInfo.getPU_pT_hats().size()):
        print puSummaryInfo.getPU_pT_hats()[i],",\t",
        print puSummaryInfo.getPU_zpositions()[i],
        print puSummaryInfo.getPU_EventID()[i].event()
        
        
    ## Empty collections ##
#    print puSummaryInfo.getPU_instLumi().size()
#    print puSummaryInfo.getPU_times().size()
#    print puSummaryInfo.getPU_ntrks_highpT().size(),puSummaryInfo.getPU_ntrks_highpT()[0]
#    print puSummaryInfo.getPU_ntrks_lowpT().size(),puSummaryInfo.getPU_ntrks_lowpT()[0]
#    print puSummaryInfo.getPU_sumpT_highpT().size(),puSummaryInfo.getPU_ntrks_lowpT()[0]
#    print puSummaryInfo.getPU_sumpT_lowpT().size(),puSummaryInfo.getPU_ntrks_lowpT()[0]

