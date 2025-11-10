import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLT" )

process.load("HLTrigger.Configuration.HLT_GRun_cff")

print()
print(process.HLTL3muonrecoSequenceNoVtx.dumpPython())

print()
print(process.HLTL3muonrecoSequence.dumpPython())
print()

moduleNoVtx = {}
for module in list((process.HLTL3muonrecoSequenceNoVtx.expandAndClone()).moduleNames()):
 #   print(getattr(process, module).dumpPython())
    moduleNoVtx[module.replace("NoVtx","")] = getattr(process, module).dumpPython().replace("NoVtx","")

moduleVtx = {}
for module in list((process.HLTL3muonrecoSequence.expandAndClone()).moduleNames()):
#    print(getattr(process, module).dumpPython())
    moduleVtx[module] = getattr(process, module).dumpPython()

allModules = list(set(moduleNoVtx.keys()).union(set(moduleVtx.keys())))


for module in allModules:
    if module in moduleVtx:
        if module in moduleNoVtx:
            if moduleNoVtx[module] != moduleVtx[module]:
                print(f"Module {module} differs between NoVtx and Vtx versions.")
                ## Print only the line that differs
                import difflib
                diff_lines = difflib.unified_diff(
                    moduleNoVtx[module].splitlines(),
                    moduleVtx[module].splitlines(),
                    lineterm='',
                )
                for line in diff_lines:
                    print(line)
                # print("NoVtx version:")
                # print(moduleNoVtx[module])
                # print("Vtx version:")
                # print(moduleVtx[module])
            else:
                # print(f"Module {module} is identical in both versions.")
                pass
        else:
            print(f"Module {module} is only in Vtx version.")
            # print(moduleVtx[module])
    else:
        print(f"Module {module} is only in NoVtx version.")
        # print(moduleNoVtx[module])
