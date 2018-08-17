datasets =[
    "/JetHT/Run2018A-22May2018-v1/MINIAOD",
    "/JetHT/Run2018A-PromptReco-v1/MINIAOD",
    "/JetHT/Run2018A-PromptReco-v2/MINIAOD",
    "/JetHT/Run2018A-PromptReco-v3/MINIAOD",
    "/JetHT/Run2018B-PromptReco-v1/MINIAOD",
    "/JetHT/Run2018B-PromptReco-v2/MINIAOD",
    "/JetHT/Run2018C-PromptReco-v1/MINIAOD",
    "/JetHT/Run2018C-PromptReco-v2/MINIAOD",
    "/JetHT/Run2018C-PromptReco-v3/MINIAOD",
    "/JetHT/Run2018D-PromptReco-v1/MINIAOD",
    "/JetHT/Run2018D-PromptReco-v2/MINIAOD",
]

import os
from optparse import OptionParser

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
#    from CRABClient.UserUtilities import config
#    config = config()
    from WMCore.Configuration import Configuration
    config = Configuration()
    
    for dataset in datasets:
        name = 'HLT_Ntuple_BParking_v1p4_skim'
        config.section_("General")
        config.General.workArea = 'crab_'+name
        config.General.transferLogs=True
#        config.General.requestName = name+"_"+dataset.replace('/',"_")
        config.General.requestName = name + dataset[1:].replace("/","_")

        config.section_("JobType")
#        config.JobType.numCores = 4
        config.JobType.numCores = 1
#        config.JobType.maxMemoryMB = 16000
        config.JobType.pluginName = 'Analysis'
        config.JobType.psetName = 'crab_fake_pset.py'
        config.JobType.scriptExe = 'crab_script.sh'
        import os
        os.system("tar czf python.tar.gz --dereference --directory $CMSSW_BASE python")
        os.system("voms-proxy-info -path | xargs -i  cp {}  .")
        config.JobType.inputFiles = [
#                                     'hltDump2.py',
                                     'fwlite_config.py',
                                     'script.py',
                                     'utils.py',
                                     'python.tar.gz',
        ]
        
        config.section_("Data")
        config.Data.inputDBS = 'global'
#        config.Data.splitting = 'Automatic'
        config.Data.splitting = 'FileBased'
        config.Data.unitsPerJob = 25

        config.Data.totalUnits = -1
#        config.Data.totalUnits = 10*config.Data.unitsPerJob
#        config.Data.totalUnits = 1*config.Data.unitsPerJob

#        config.Data.totalUnits = 100*config.Data.unitsPerJob ##FIXME: use -1
#        config.Data.unitsPerJob = 1 #FIXME: use 20
        config.Data.totalUnits = -1 #10*config.Data.unitsPerJob #FIXME: use -1
#        config.Data.outLFNDirBase = '/store/user/sdonato/' + name
        config.Data.outLFNDirBase = '/store/user/sdonato/' + name
        config.Data.publication = True
#        config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt'
#        config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt' 
#'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt'
        config.Data.inputDataset = dataset
#        if "AODSIM" in dataset:
#            config.Data.secondaryInputDataset = dataset.replace("AODSIM","GEN-SIM-RAW")
#            print "using secondaryInputDataset: ",config.Data.secondaryInputDataset
#        config.Data.publishDataName = config.General.requestName
        config.Data.outputDatasetTag = name
        config.Data.allowNonValidInputDataset = True
        config.section_("Site")
        config.Site.blacklist = ['T0_*']
        
#        config.Site.storageSite = "T2_CH_CSCS"
        config.Site.storageSite = "T3_CH_PSI"
        print "submitting ",dataset
        crabCommand('submit',config = config)
        print "DONE ",dataset
    
