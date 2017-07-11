source /cvmfs/cms.cern.ch/cmsset_default.sh
export LOCAL_PATH=$PWD
export CMSSW_FOLDER=/mnt/t3nfs01/data01/shome/sdonato/CMSSW_9_2_5_patch2/src
cd $CMSSW_FOLDER
eval `scramv1 runtime -sh`
which python

echo $PWD
ls


export example=file:/scratch/sdonato/Run2017B_MuonEG_297469_RAW.root
## if you are run it locally, use example
if [$inputFile = '']; then export inputFile=$example;  echo "I'm using "$example" as test"  ; fi
if [$MAX_EVENTS = '']; then export MAX_EVENTS='10' ; fi
if [$index = '']; then export index='1' ; fi
if [$GC_SCRATCH = '']; then export GC_SCRATCH='/mnt/t3nfs01/data01/shome/sdonato/triggerRates/GC_TEST'; fi


echo "###### job parameters #######"
echo "inputFile:"$inputFile
echo "MAX_EVENTS:"$MAX_EVENTS
echo "GC_SCRATCH:"$GC_SCRATCH

echo "#############################"

cd $GC_SCRATCH
cp $CMSSW_FOLDER/hltData.py hltData.py
cp /mnt/t3nfs01/data01/shome/sdonato/.x509up_u636 $HOME
echo 

export MAX_EVENTS=100

echo '''
process.hltOutput = cms.OutputModule( "PoolOutputModule",
    fileName = cms.untracked.string( "trigRes_1.root" ),
    outputCommands = cms.untracked.vstring(
    "drop *",
    "keep *TriggerResults_*_*_*",
)
)
process.Output = cms.EndPath( process.hltOutput )
''' >> hltData.py

echo "process.source.fileNames = cms.untracked.vstring( '$inputFile')" >> hltData.py
echo "process.maxEvents.input = cms.untracked.int32($MAX_EVENTS)" >> hltData.py
#echo "process.hltOutput.fileName = cms.untracked.string( 'trigRes_$index.root' )" >> hltGrid.py
echo "process.hltOutput.fileName = cms.untracked.string( 'trigRes_"$index".root' )" >> hltData.py

cmsRun hltData.py

mv 'trigRes_'$index'.root' $CMSSW_FOLDER
