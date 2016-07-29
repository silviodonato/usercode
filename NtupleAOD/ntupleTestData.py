from launchNtupleFromAOD import launchNtupleFromAOD

maxevents=1000
fileOutput = 'ntupleTestData.root'
filesInput=[
"~/scratch/JetHT_AOD_275375.root",
]
launchNtupleFromAOD(fileOutput,filesInput,maxevents)
