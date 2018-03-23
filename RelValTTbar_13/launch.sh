
#/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export LOCAL_PATH=/mnt/t3nfs01/data01/shome/sdonato/PVsort/CMSSW_10_1_0_pre3/src/PVsort/RelValTTbar_13
export CMSSW_FOLDER=/mnt/t3nfs01/data01/shome/sdonato/PVsort/CMSSW_10_1_0_pre3
cd $CMSSW_FOLDER
eval `scramv1 runtime -sh`
cd $LOCAL_PATH
echo $CMSSW_FOLDER
echo $LOCAL_PATH
echo $CMSSW_BASE
echo "cmsRun launch.py"
cmsRun launch.py
    