'''
HLT rates for first collision (October 2021)
hltGetConfiguration adg:/cdaq/test/elfontan/CRAFT_TB/Collisions >hlt.py
(drop hltOnlineBeamMonitorPB from process.DQMHistograms)
hltDumpStream --csv hlt.py  > hlt.txt
'''


fName = "hlt.csv"
outName = "hlt_withRates.csv"

prescale_column= "ZeroBias"

dump = open(fName, 'r')
out = open(outName, 'w')

L1_ZeroBias_rate = 22000
L1_Random_rate = 18000
L1_ETT35_rate = 2000
L1_Physics_rate = L1_ZeroBias_rate + L1_Random_rate

def getInputRate(line, L1_seed):
    if "L1_ZeroBias" in values[L1_seed_num]:
        return 1.*L1_ZeroBias_rate
    elif "L1_ETT35" in values[L1_seed_num]:
        return 1.*L1_ETT35_rate
    elif "(none)" in values[L1_seed_num]:
        if "random" in values[2].lower():
            return 1.*L1_Random_rate
        elif "physics" in values[2].lower():
            return 1.*L1_Physics_rate
        print("Problem with [Physics??]:",line, values[2].lower())
        return 1.*L1_Physics_rate
    else:
        print("Problem with [Other seeds??]:",line, values[2].lower())
        return 0


def hiddenPrescale(HLTPath):
    path = HLTPath.split("_v")[0]
    if path in ["HLT_HcalPhiSym","HLT_HcalNZS"]: return 4096 ## hidden prescale NZS
    elif path in ["HLT_Physics"]: return 107 # hidden prescale "L1 fat"
    else: return 1 ## no hidden prescale

first = True
for l in dump:
    l = l.replace("\n","")
    if first:
        first = False
        labels = l.split(",")
        try:
            L1_seed_num = labels.index(" L1 trigger")
            prescale_num = labels.index(" %s"%prescale_column)
        except:
            print(labels)
            L1_seed_num = labels.index(" L1 trigger")
            prescale_num = labels.index(" %s"%prescale_column)
        out.write(",".join(labels[:-1])+",L1Rate(Hz),HLTRate(Hz),%s\n"%(labels[-1]))
    else:
        values = l.split(",")
        HLTPath = l[2]
        inputRate = getInputRate(values, L1_seed_num)
        try:
            prescale = int(values[prescale_num]) * hiddenPrescale(HLTPath)
        except:
            print (values, prescale_num)
            prescale = int(values[prescale_num]) * hiddenPrescale(HLTPath)
        outRate = inputRate/prescale
        out.write(",".join(values[:-1])+",%d,%d,%s\n"%(inputRate,outRate,values[-1]))
    
