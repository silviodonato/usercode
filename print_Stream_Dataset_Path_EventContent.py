# hltGetConfiguration run:367902 > hlt.py 

from hlt import process

printPath = True
printDataset = True
printEventContent = True

if printPath: printDataset = True

oms = list(process.outputModules_())[:]
for om in oms:
    print()
    print("OutputModule: %s"%om)
    m = getattr(process,om)
    print(" "*4+"Dataset:")
    if printDataset and hasattr(m, 'SelectEvents'):
        if hasattr(m.SelectEvents, 'SelectEvents'):
            for dataset in m.SelectEvents.SelectEvents:
                print(" "*8+dataset)
                if printPath and hasattr(process, dataset):
                    print(" "*8+"Paths:")
                    ## Dataset_ParkingDoubleMuonLowMass11 --> hltParkingDoubleMuonLowMass
                    datasetPathModuleName = "hltDataset%s"%dataset.split("Dataset_")[1] 
                    while not hasattr(process, datasetPathModuleName) and datasetPathModuleName[-1].isdigit(): datasetPathModuleName = datasetPathModuleName[:-1]
                    datasetPathModule = getattr(process, datasetPathModuleName)
                    for path in datasetPathModule.triggerConditions:
                        print(" "*12+path)
    
    print(" "*4+"Event Content:")
    if printEventContent and hasattr(m, 'outputCommands'):
        for out in m.outputCommands:
            print(" "*8+out)
