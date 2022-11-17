hltGetConfiguration run:360991 \
   --globaltag 124X_dataRun3_HLT_Candidate_2022_11_16_12_59_42 \
   --data \
   --unprescale \
   --output minimal \
   --max-events -1 \
   --input root://eoscms.cern.ch//store/data/Run2022F/HLTPhysics/RAW/v1/000/360/991/00000/69592673-b357-4478-b6c8-fb4fb2bcb980.root \
   --path HLT_PFMETNoMu110_* \
   > hltReference.py

## instead of run:360991, you can specify directly the HLT menu (eg. adg:/cdaq/physics/Run2022/2e34/v1.3.6/HLT/V8)
## remove "--globaltag ..." to use the online globaltag
## remove "--path..." to run over all the HLT paths 

## fix necessary to avoid a crash
echo "process.schedule.remove(process.DQMHistograms)" >> hltReference.py

## if you want to increase the number of threads
echo "process.options.numberOfThreads = 16" >> hltReference.py

cp hltReference.py hltTarget.py

echo "process.GlobalTag.globaltag = '124X_dataRun3_HLT_Candidate_2022_11_16_09_10_32'" >> hltTarget.py
echo "process.hltOutputMinimal.fileName = 'outputTarget.root'" >> hltTarget.py

rm output.root outputTarget.root
cmsRun hltReference.py >& logRef &
sleep 5
cmsRun hltTarget.py >& logTar

hltDiff -o output.root -n outputTarget.root


