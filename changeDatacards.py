class Datacard():
    def __init__(self):
        self.bins = []
        self.shapes = []
        self.templates = []
        self.nuisances = []



class Template():
    def __init__(self):
        self.bin = None
        self.processName = None
        self.processNumber = None
        self.rate = None

class Nuisance():
    def __init__(self):
        self.name = None
        self.type = None
        self.values = {}

class Shape():
    def __init__(self):
        self.boh = None
        self.bin = None
        self.fileName = None
        self.histoName = None
        self.histoNameSyst = None

class Bin():
    def __init__(self):
        self.name = None
        self.observation = None

def read_DC(fileName):
    fileDC = open(fileName)
    DC = Datacard()
    binsDone = False
    templatesDone = False
    for line in fileDC.readlines():
        line = line.replace("\t"," ")
        nline = line.replace("  "," ")
        while(nline!=line):
            line = nline
            nline = line.replace("  "," ")
        line = line.replace(" \n","")
        line = line.replace("\n","")
        words = line.split(" ")
        if words[0]=="#": continue
        ## Read "shapes" part
        elif words[0]=="shapes" and len(words)==6:
            shape = Shape()
            shape.boh, shape.bin, shape.fileName, shape.histoName, shape.histoNameSyst = words[1], words[2], words[3], words[4], words[5]
            DC.shapes.append(shape)
        ## Read "bins" part
        elif not binsDone:
            if words[0]=="bin":
                for i in range(1,len(words)):
                    DC.bins.append(Bin())
                    DC.bins[i-1].name = words[i]
            elif words[0]=="observation":
                for i in range(1,len(words)):
                    DC.bins[i-1].observation = words[i]
                binsDone = True
        ## Read "templates" part
        elif binsDone and not templatesDone:
            if words[0]=="bin":
                for i in range(1,len(words)):
                    DC.templates.append(Template())
                    DC.templates[i-1].bin = words[i]
            elif words[0]=="process":
                for i in range(1,len(words)):
                    if DC.templates[i-1].processName == None:
                        DC.templates[i-1].processName = words[i]
                    else:
                        DC.templates[i-1].processNumber = int(words[i])
            elif words[0]=="rate":
                for i in range(1,len(words)):
                    DC.templates[i-1].rate = float(words[i])
                templatesDone = True
        ## Read "nuisances" part
        elif templatesDone and len(words)>2:
            nuisance = Nuisance()
            nuisance.name = words[0]
            nuisance.type = words[1]
            for i in range(2,len(words)):
                if words[i]!="-":
                    nuisance.values[DC.templates[i-2]] = words[i]
                else:
                    nuisance.values[DC.templates[i-2]] = 0
            DC.nuisances.append(nuisance)
    fileDC.close()
    
    return DC

def printTemplatesWithNuisances(DC):
    for template in DC.templates:
        print
        print "#"*10
        print template.bin,template.processName,template.processNumber,template.rate
        print "#"*10
        for nuisance in DC.nuisances:
            print nuisance.name, nuisance.type,
            try:
                print nuisance.values[template]
            except:
                print "????"


def printDatacard(DC):
    output = ""
    bins = set()
    processNames = set()
    for template in DC.templates:
        bins.add(template.bin)
        processNames.add(template.processName)
    
    ## print common part
    output = """imax %d
jmax %d
kmax %d
---------------
"""%(len(bins), len(DC.templates)-1, len(DC.nuisances))
    ## print shapes part
    for shape in DC.shapes:
        output += "shapes %s %s %s %s %s\n"%(shape.boh, shape.bin, shape.fileName, shape.histoName, shape.histoNameSyst)
    output += "---------------\n"
    
    ## print bins part
    output += "bin"
    for bin_ in DC.bins:
        output += "\t%s"%(bin_.name)
    output += "\n"
    
    output += "observation"
    for bin_ in DC.bins:
        output += "\t%s"%(bin_.observation)
    output += "\n"
    output += "---------------\n"
    
    ## print templates part
    output += "bin"
    for template in DC.templates:
        output += "\t%s"%(template.bin)
    output += "\n"
    
    output += "process"
    for template in DC.templates:
        output += "\t%s"%(template.processName)
    output += "\n"
    
    output += "process"
    for template in DC.templates:
        output += "\t%s"%(template.processNumber)
    output += "\n"
    
    output += "rate"
    for template in DC.templates:
        output += "\t%s"%(template.rate)
    output += "\n"
    output += "---------------\n"
    
    ## print nuisances part
    for nuisance in DC.nuisances:
        output += "%s\t%s\t"%(nuisance.name, nuisance.type)
        for template in DC.templates:
            val = nuisance.values[template]
            if val == 0:
                output += "-\t"
            else:
                output += str(val)+"\t"
        output += "\n"
    return output


fileNames = [
    "shapes_fh_j7_t3__mem_FH_4w2h1t_p.txt",
    "shapes_fh_j7_t4__mem_FH_3w2h2t_p.txt",
    "shapes_fh_j8_t3__mem_FH_4w2h1t_p.txt",
    "shapes_fh_j8_t4__mem_FH_3w2h2t_p.txt",
    "shapes_fh_j9_t3__mem_FH_4w2h1t_p.txt",
    "shapes_fh_j9_t4__mem_FH_4w2h2t_p.txt"
]
for fileName in fileNames:
    fileNameNew = fileName.replace(".txt","_new.txt")

    DC = read_DC(fileName)
    #printTemplatesWithNuisances(DC)
    newDC = printDatacard(DC)

    newDC_file = open(fileNameNew,'w')
    newDC_file.write(newDC)
    newDC_file.close()













