#! /bin/bash

echo $PWD
export SCRATCH_FOLDER=$PWD 
source /cvmfs/cms.cern.ch/cmsset_default.sh
export LOCAL_PATH=$PWD
export CMSSW_FOLDER=/mnt/t3nfs01/data01/shome/sdonato/CMSSW_9_2_3_patch1/src
cd $CMSSW_FOLDER
eval `scramv1 runtime -sh`
which python

echo $PWD
ls

export example=root://t3se01.psi.ch//store/user/sdonato/tth_skim_June4/ZZ_TuneCUETP8M1_13TeV-pythia8.root
## if you are run it locally, use example
if [$inputFile = '']; then export inputFile=$example;  echo "I'm using "$example" as test"  ; fi

echo "###### job parameters #######"
echo "inputFile: " $inputFile
echo "#############################"

#cd /mnt/t3nfs01/data01/shome/sdonato/addCSVtth
cd $SCRATCH_FOLDER

cp /mnt/t3nfs01/data01/shome/sdonato/addCSVtth/addCSVsorted.C .
cp /mnt/t3nfs01/data01/shome/sdonato/addCSVtth/btagCorrection_ddQCD.h .

ls

echo root -l -q -b addCSVsorted.C+\(\"$inputFile\"\)

root -l -q -b addCSVsorted.C+\(\"$inputFile\"\)

mv *root /mnt/t3nfs01/data01/shome/sdonato/addCSVtth


