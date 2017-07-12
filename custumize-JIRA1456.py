file_ = open("dump_muonSeq.py")
modules = []
for line in file_:
    if "HLTMuonL2FromL1TPreFilter" in line:
        module = line
        module = module.replace("\n","")
        module = module.replace(' = cms.EDFilter("HLTMuonL2FromL1TPreFilter",',"")
        modules.append(module)

print modules

newTxt = ""

file_.seek(0)
for line in file_.readlines():
    if "cms.Sequence" in line or "cms.Path" in line:
        for el in line.split("+"):
            if el in modules:
                print el
                print line
                line = line.replace(el,"cms.ignore(%s)"%el)
                print line
    newTxt += line

newFile = open("dump_muonSeq_new.py","w")
newFile.write(newTxt)
