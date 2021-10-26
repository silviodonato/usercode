'''
hltGetConfiguration adg:/cdaq/special/PilotBeamTest2021/Collisions/V25 >hlt.py
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
L1_FirstCollisionInOrbit_rate = 10
L1_Physics_rate = L1_ZeroBias_rate + L1_Random_rate + L1_FirstCollisionInOrbit_rate

def getInputRate(line, L1_seed):
    if "(L1_ZeroBias OR L1_AlwaysTrue) AND (L1_ETT20 OR L1_ETT35 OR L1_ETT50 OR L1_ETT70)" in values[L1_seed_num]:
        return 1.*L1_ETT35_rate
    elif "L1_ZeroBias" in values[L1_seed_num]:
        return 1.*L1_ZeroBias_rate
    elif "L1_ETT35" in values[L1_seed_num]:
        return 1.*L1_ETT35_rate
    elif "L1_FirstCollisionInOrbit" in values[L1_seed_num]:
        return 1.*L1_FirstCollisionInOrbit_rate
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
    hiddenPs=0
    path = HLTPath.split("_v")[0][1:]
    if path in ["HLT_HcalPhiSym","HLT_HcalNZS"]: hiddenPs=4096 ## hidden prescale NZS
    elif path in ["HLT_Physics"]: hiddenPs=107 # hidden prescale "L1 fat"
    elif path in ["HLT_PixelClusters_WP1_ZeroBias"]: hiddenPs=11 ## we expect a rate of 2kHz (equivalen to ~10 prescale)
    else: hiddenPs=1 ## no hidden prescale
    if hiddenPs!=1:
        print(path+" applying hidden prescale = "+str(hiddenPs))
    return hiddenPs

first = True
for l in dump:
    if "corresponding EndPath not found" in l:
        print(l)
        continue
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
        print(labels)
        print("L1_seed_num=%d"%L1_seed_num)
        print("prescale_num=%d"%prescale_num)
    else:
        values = l.split(",")
        HLTPath = values[2]
        try:
            inputRate = getInputRate(values, L1_seed_num)
        except:
            print("L1_seed_num=%d"%L1_seed_num)
            print(values)
            inputRate = getInputRate(values, L1_seed_num)
        try:
            prescale = int(values[prescale_num]) * hiddenPrescale(HLTPath)
        except:
            print (values, prescale_num)
            prescale = int(values[prescale_num]) * hiddenPrescale(HLTPath)
        if prescale>0:
            outRate = inputRate/prescale  
        else:
            outRate=0
        out.write(",".join(values[:-1])+",%d,%.1f,%s\n"%(inputRate,outRate,values[-1]))
    
