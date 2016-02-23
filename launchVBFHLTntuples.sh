 mkdir log
 
 setenv BASE /gpfs/ddn/srm/cms/store/user/sdonato/VBFHbb_trigger_v5/
 
 python launchNtupleFromHLT.py $BASE  VBFHToBB_M-120_13TeV_powheg_pythia8>& log/logVBF & 

 setenv BASE /gpfs/ddn/srm/cms/store/user/sdonato/VBFHbb_trigger_v5c/

 python launchNtupleFromHLT.py $BASE  QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8>&       log/logQCD15 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8>&       log/logQCD30 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8>&       log/logQCD50 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8>&      log/logQCD80 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8>&     log/logQCD120 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8>&     log/logQCD170 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8>&     log/logQCD300 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8>&     log/logQCD470 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8>&     log/logQCD600 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8>&    log/logQCD800 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8>&   log/logQCD1000 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8>&   log/logQCD1400 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8>&   log/logQCD2400 & 
 python launchNtupleFromHLT.py $BASE  QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8>&    log/logQCD3200 & 

