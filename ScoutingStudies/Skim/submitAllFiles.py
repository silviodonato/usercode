## python3 -u submitAllFiles.py >& log &

nprocesses = 4
folder = "/eos/cms/tier0/store/data/Run2024F/ScoutingPFRun3/HLTSCOUT/v1/000/382/504/00000"

import os

## get the list of files in the directory
fileNames = [f"file:{folder}/{line.strip()}" for line in os.listdir(folder)]

## create logs directory
os.system("mkdir -p logs")

import ROOT
from multiprocessing import Pool
fileNames = fileNames[:6] ## test only 1 file

for fileName in fileNames[:]:
    print(f"Processing: {fileName}")


    ## If outputfile already exists and is good, skip
    runNumber = int(fileName.split("/")[-4]+fileName.split("/")[-3])
    fName = fileName.split("/")[-1]
    outputFile = f"Skim_{runNumber}_{fName}"
    # print("Checking if output file exists: ", outputFile)
    if os.path.exists(outputFile):
        # print(f"Output file {outputFile} already exists.")
        try:
            f_ = ROOT.TFile.Open(outputFile)
            Events = f_.Get("Events")
            assert(Events.GetEntries()>0)
            print(f"Output file {outputFile} is good. Skipping.")
            fileNames.remove(fileName)
        except:
            pass
    
def process_file(fileName):
    command = "cmsRun skim_hlt_bit.py file:%s"%(fileName)
    ## redirect stdout and stderr to a log file
    log_file = f"logs/{fileName.split('/')[-1].replace('.root', '.log')}"
    command = f"{command} > {log_file} 2>&1"
    
    ## submit the command to the terminal
    print(f"Running: {command}")
    os.system(command)

    ## wait for the job to finish
    ## os.system(f"tail -f {log_file}")


if __name__ == '__main__':
    pool = Pool(processes=nprocesses)  # create a pool of worker processes
    pool.map(process_file, fileNames)  # distribute the work among the worker processes
    pool.close()  # close the pool
    pool.join()  # wait for all the worker processes to finish
