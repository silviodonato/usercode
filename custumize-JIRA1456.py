file_ = open("dump_muonSeq.py")
modules = []
for line in file_:
    if "HLTMuonL2FromL1TPreFilter" in line:
        module = line
        module = module.replace("\n","")
        module = module.replace("process.","")
        module = module.replace(' = cms.EDFilter("HLTMuonL2FromL1TPreFilter",',"")
        modules.append(module)

print modules

newTxt = ""

file_.seek(0)
for line in file_.readlines():
    if "cms.Sequence" in line or "cms.Path" in line:
        for module in modules:
            if module in line and not "cms.ignore(proces
            s.%s"%module in line:
                print module
                print line
                line = line.replace("process."+module,"cms.ignore(process.%s)"%module)
                print line
    newTxt += line

newFile = open("dump_muonSeq_new.py","w")
newFile.write(newTxt)
