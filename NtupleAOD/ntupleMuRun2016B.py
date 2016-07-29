from launchNtupleFromAOD import launchNtupleFromAOD

maxevents=1000
#maxevents=1000
fileOutput = 'ntupleTest.root'
filesInput=[
    "file:2C852455-E232-E611-8DE1-02163E0124CA.root",
]
launchNtupleFromAOD(fileOutput,filesInput,maxevents)
