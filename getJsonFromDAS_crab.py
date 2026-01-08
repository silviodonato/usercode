import json
from FWCore.PythonUtilities.LumiList import LumiList

## run_lumi_das.json created with: dasgoclient -query="run,lumi dataset=/HIPhysicsRawSecond/snandan-HIPhysicsRawSecond_Lumibased-19b87fa2487685de0f955b0ba59ab561/USER instance=prod/phys03" -json > run_lumi_das.json


with open("run_lumi_das.json") as f:
    data = json.load(f)

lumis = []
for entry in data:
    # DAS returns a list of runs and a list of lumis for each record
    run_list = [r['run_number'] for r in entry.get('run', [])]
    lumi_list = [l['number'] for l in entry.get('lumi', [])]
    
    for run in run_list:
        for ls in lumi_list:
            lumis.append((run, ls))

LumiList(lumis=lumis).writeJSON("final_dataset.json")
