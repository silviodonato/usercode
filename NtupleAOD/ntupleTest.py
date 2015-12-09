from launchNtupleFromAOD import launchNtupleFromAOD

maxevents=1000
fileOutput = 'ntupleTest.root'
filesInput=[
"4C7B9F57-6F81-E511-95E4-02163E014438.root",

]
launchNtupleFromAOD(fileOutput,filesInput,maxevents)
