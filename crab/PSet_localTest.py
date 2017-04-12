import FWCore.ParameterSet.Config as cms

process = cms.Process("FAKE")

#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('root://dc2-grid-64.brunel.ac.uk//dpm/brunel.ac.uk/home/cms/store/mc/PhaseIFall16DR/GluGluToRSGravitonToHHTo4B_M-900_narrow_13TeV-madgraph/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/80000/9812F6D5-C511-E711-9D5D-001E67E6F7C4.root'),
#    secondaryFileNames = cms.untracked.vstring('root://dc2-grid-64.brunel.ac.uk//dpm/brunel.ac.uk/home/cms/store/mc/PhaseIFall16DR/GluGluToRSGravitonToHHTo4B_M-900_narrow_13TeV-madgraph/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/80000/A8F990B6-B810-E711-B530-001E677926A8.root')
#)

#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('file:///mnt/t3nfs01/data01/shome/sdonato/tth/Trigger2017/HLT/CMSSW_9_0_0/src/ntuples/crab/ZH2_AODSIM.root'),
#    secondaryFileNames = cms.untracked.vstring('file:////mnt/t3nfs01/data01/shome/sdonato/tth/Trigger2017/HLT/CMSSW_9_0_0/src/ntuples/crab/ZH2_RAW.root')
#)


#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('/store/mc/PhaseIFall16DR/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG087_90X_upgrade2017_realistic_v6_C1-v1/120000/009CCEA5-7815-E711-BA6C-0CC47A7C346E.root.root'),
#    secondaryFileNames = cms.untracked.vstring('/store/mc/PhaseIFall16DR/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG087_90X_upgrade2017_realistic_v6_C1-v1/120001/ACC1E2DB-6615-E711-9AD6-0025905A60AA.root')
#)



#process.source = cms.Source("PoolSource",
#    fileNames = cms.untracked.vstring('/store/mc/PhaseIFall16DR/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/130000/0450D6E6-2A12-E711-B81F-001E67E6F49F.root'),
#    secondaryFileNames = cms.untracked.vstring('/store/mc/PhaseIFall16DR/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/130002/0835344C-5C11-E711-9B59-001E6779267A.root',
#     '/store/mc/PhaseIFall16DR/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/130002/10905906-5B11-E711-888A-001E67C8050C.root',
#     '/store/mc/PhaseIFall16DR/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/130002/D4EB1D03-6611-E711-970F-001E67E71A56.root')
#)


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/1E1BBA64-121B-E711-B699-70106F4A95F8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/36C8DCC0-141B-E711-B0AD-E41D2D08E0C0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/406B9D8A-191B-E711-96CE-E41D2D08E080.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/44CE7F66-1C1B-E711-8229-70106F49CDF4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/6861C407-201B-E711-BA47-70106F48BA1E.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/6C7DA373-231B-E711-BFB8-0CC47A7E6A8A.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/74F51254-261B-E711-A888-70106F4A92A0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/8CB34731-111B-E711-AAE4-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/9CBCBB38-1D1B-E711-A7CE-0CC47A7FC7B8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/A257E44E-291B-E711-A4C9-0CC47A7E004C.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/A8F8FB62-101B-E711-91BF-70106F48BA1E.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/C4AE4AFA-2E1C-E711-A9BD-70106F4A4308.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/CCBE1788-0D1B-E711-88A6-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/CE61F9BA-171B-E711-8A7A-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/CEE64609-3D1B-E711-B2CD-0CC47A7E6A2C.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/D494AF11-5E1B-E711-8E5B-70106F4D68C4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/D897133D-2C1B-E711-B2F2-E41D2D08E0C0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/DA40EC1F-1B1B-E711-B5D7-0CC47A7FC7B8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/E2A86F55-151B-E711-A8E3-70106F4A44E0.root'),
    secondaryFileNames = cms.untracked.vstring(
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/5AEAD0FF-091B-E711-8447-E41D2D08DDB0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/60E67FC0-011B-E711-8D95-70106F4A95F8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/BE81DB49-0A1B-E711-BC76-E41D2D08E100.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/A00E8D11-041B-E711-A9FC-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/FA3198B1-081B-E711-AAA4-0CC47A7FC750.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/F0D0930E-0C1B-E711-AC4F-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/12340C3E-021B-E711-9CCB-70106F4A95F8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/C0600498-0C1B-E711-B232-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/6897FB3B-0B1B-E711-BA09-0CC47A7E6AAA.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/24B06C9F-021B-E711-84FD-70106F4A469C.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/06809E3C-091B-E711-AF26-0242AC110005.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/DAA5818A-0B1B-E711-986B-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/FC228540-121B-E711-97EA-70106F48B8DA.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/FEC0BBF3-0F1B-E711-9BD6-70106F4A95F8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/9CA4D415-081B-E711-BC19-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/42D0F936-0E1B-E711-AEAC-0CC47A7FC750.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/7CBB8290-101B-E711-9C79-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/8AB5220A-121B-E711-A229-0CC47A7FC750.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/CA35238E-131B-E711-861B-0242AC110002.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/70DF7E42-131B-E711-8B7B-0CC47A7FC750.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/C4C73E84-111B-E711-BFEE-70106F4D6898.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/7CBB8290-101B-E711-9C79-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/E65B27F5-151B-E711-9786-70106F44C438.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/7014F090-141B-E711-AF02-0025904B1372.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/E2660146-161B-E711-B6D0-70106F4D24D8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/EC9B8D0F-131B-E711-B893-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/9446B5FD-131B-E711-8A00-70106F44C438.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/B42CED14-191B-E711-9B9E-0CC47A7FC7B8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/AA82082C-181B-E711-8873-70106F44C438.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/7014F090-141B-E711-AF02-0025904B1372.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/F0347718-151B-E711-A77D-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/F029E2F1-1C1B-E711-B27D-0242AC110002.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/387F7D21-191B-E711-841C-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/28F5574D-1B1B-E711-AB6B-E41D2D08E0C0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/EC3D384B-1C1B-E711-9512-0CC47A7FC7B8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/48E19980-031B-E711-881A-70106F4A469C.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/445B275A-081B-E711-87B1-0CC47A7FC7C8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/E6A8F3D9-081B-E711-BFA3-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/BE81DB49-0A1B-E711-BC76-E41D2D08E100.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/34E1C177-071B-E711-931A-0CC47A7E69CE.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/9CA4D415-081B-E711-BC19-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/44F60C9B-141B-E711-94B0-002590DB923E.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/CA35238E-131B-E711-861B-0242AC110002.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/A44D28D1-061B-E711-B97C-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/E2660146-161B-E711-B6D0-70106F4D24D8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/EC9B8D0F-131B-E711-B893-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/C4C73E84-111B-E711-BFEE-70106F4D6898.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/F0347718-151B-E711-A77D-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/B8D1CFA5-1F1B-E711-9E94-70106F4A9680.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/5E1FAFB1-1D1B-E711-AF0B-0242AC110002.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/84B249EE-1E1B-E711-8DA3-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/EC3D384B-1C1B-E711-9512-0CC47A7FC7B8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/F06F090E-071B-E711-B77B-0242AC110005.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/48E19980-031B-E711-881A-70106F4A469C.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/A44D28D1-061B-E711-B97C-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/24B06C9F-021B-E711-84FD-70106F4A469C.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/34D7A4C3-001B-E711-B55D-70106F4A9284.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/A00E8D11-041B-E711-A9FC-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/644D2181-5C1B-E711-B638-E41D2D08DD30.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/12340C3E-021B-E711-9CCB-70106F4A95F8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/BA030E50-FE1A-E711-8434-E41D2D08DD60.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/A80DEBB2-FD1A-E711-9D9A-70106F4A9284.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/E072EF40-051B-E711-A1AD-70106F4D6898.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/60E67FC0-011B-E711-8D95-70106F4A95F8.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/6EA061E0-051B-E711-B5ED-E41D2D08DDB0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/A80DEBB2-FD1A-E711-9D9A-70106F4A9284.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/C0600498-0C1B-E711-B232-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/A65D09B4-0D1B-E711-B24F-70106F4D68C4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/60E38C12-0F1B-E711-8C0C-0242AC110004.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/42D0F936-0E1B-E711-AEAC-0CC47A7FC750.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/DA0D8173-241B-E711-B2EB-0CC47A7FC72A.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/ACDA0460-331B-E711-9A8E-0CC47A7E6A8A.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/B28956FD-2A1B-E711-A3C7-0CC47A7E6A8A.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/56454445-4A1B-E711-98FC-E41D2D08DEB0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/F288134C-441B-E711-9CFA-70106F4A469C.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/D0A62E3B-521B-E711-AE6E-002590DB918C.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/D2981305-231B-E711-9B39-70106F4A9680.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/28F5574D-1B1B-E711-AB6B-E41D2D08E0C0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/84B249EE-1E1B-E711-8DA3-0242AC110003.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/869B6A30-211B-E711-BD66-0CC47A7FC46A.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/44F60C9B-141B-E711-94B0-002590DB923E.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/FC228540-121B-E711-97EA-70106F48B8DA.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/70DF7E42-131B-E711-8B7B-0CC47A7FC750.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/60E38C12-0F1B-E711-8C0C-0242AC110004.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/CC97EF9E-131B-E711-B642-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/F0D0930E-0C1B-E711-AC4F-047D7BD6DEC4.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/F06F090E-071B-E711-B77B-0242AC110005.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/5AEAD0FF-091B-E711-8447-E41D2D08DDB0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/34E1C177-071B-E711-931A-0CC47A7E69CE.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/6EA061E0-051B-E711-B5ED-E41D2D08DDB0.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/FA3198B1-081B-E711-AAA4-0CC47A7FC750.root',
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/BA030E50-FE1A-E711-8434-E41D2D08DD60.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/E072EF40-051B-E711-A1AD-70106F4D6898.root', 
        '/store/mc/PhaseIFall16DR/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_HIG081_90X_upgrade2017_realistic_v6_C1-v1/60000/445B275A-081B-E711-87B1-0CC47A7FC7C8.root', 
        )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.options = cms.PSet(
    numberOfThreads = cms.untracked.uint32(4)
)

process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('tree.root')
)


process.out = cms.EndPath(process.output)

