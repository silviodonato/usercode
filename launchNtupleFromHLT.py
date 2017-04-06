import sys

if len(sys.argv)<=2:
    print
    print 'try "python /gpfs/ddn/srm/cms/store/user/sdonato/VBFHbb_trigger_v5/ launchNtupleFromHLT.py VBFHToBB_M-120_13TeV_powheg_pythia8"'
    print
    raise Exception()

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

#filesInput = ["/gpfs/ddn/srm/cms/store/user/sdonato/VBFHbb_trigger_v5/VBFHToBB_M-120_13TeV_powheg_pythia8/VBFHbbFlat/160221_162241/0000/outputFULL_2.root"]
#fileOutput = "test.root"

from os import walk

dir_    = sys.argv[1]
subdir  = sys.argv[2]
name    = dir_+"/"+subdir+"/"

filesInput = []
for (dirpath, dirnames, filenames) in walk(name):
    for filename in filenames:
        if filename.endswith(".root") and not 'failed' in dirpath:
            filesInput.extend([dirpath + "/"+ filename])
        
    if len(filesInput)>=256:    break

fileOutput = subdir+".root"

print
print "filesInput:",filesInput
print "fileOutput:",fileOutput
print
from ntuplizerHLT import launchNtupleFromHLT
launchNtupleFromHLT(filesInput,fileOutput)

