import ROOT

file_ = ROOT.TFile.Open("/afs/cern.ch/work/s/sdonato/public/GPU_fluctuation_study/output_HLT_GPU_CPU_GPU2.root")

from DataFormats.FWLite import Handle, Events

events = Events (file_)
for ievt,event in enumerate(events): 
    if ievt>=1:
        break

vecPixelHitsLabel_GPU = ("hltSiPixelRecHits::HLTGPU")
vecPixelHitsLabel_CPU = ("hltSiPixelRecHits::HLTCPU")

vecPixelHits_CPU = Handle("edmNew::DetSetVector<SiPixelRecHit>")
vecPixelHits_GPU = Handle("edmNew::DetSetVector<SiPixelRecHit>")

events.getByLabel(vecPixelHitsLabel_GPU, vecPixelHits_GPU)
events.getByLabel(vecPixelHitsLabel_CPU, vecPixelHits_CPU)

#vecPixelHit_CPU = vecPixelHits_CPU.product()
#vecPixelHit_GPU = vecPixelHits_GPU.product()

#funcNames = []
#for i in range(1736):
#    funcNames.append("detsetSize",[i])

funcNames = [
("x",[]),
("y",[]),
("charge",[]),
("colSpan",[]),
("size",[]),
("sizeX",[]),
("sizeY",[]),
#("getSplitClusterErrorX",[]),
#("getSplitClusterErrorY",[]),
("minPixelCol",[]),
("maxPixelCol",[]),
("minPixelRow",[]),
("maxPixelRow",[]),
("overflow",[]),
("overflowCol",[]),
("overflowRow",[]),
("colSpan",[]),
("rowSpan",[]),
#("pixelADC",[]),
]

hitMissing = [-2000]*len(funcNames)

npar = 2

def getVect(hit, funcNames):
    vect = []
    for functionName,params in funcNames:
        vect.append(getattr(hit.cluster().get(), functionName)(*params))
    return vect

def readHits(pixelHits, funcNames):
    out = []
    for hit in pixelHits:
        out.append(getVect(hit, funcNames))
#    out = sorted(out, key=lambda x:x[0])
    return out

def distance(hit1, hit2, npar):
    return sum((hit1[p]-hit2[p])**2 for p in range(npar))

def sorthits(hits1, hits2, npar):
    dists = []
    for i in range(len(hits1)):
        for j in range(len(hits2)):
            dists.append((distance(hits1[i], hits2[j],npar), i, j))
    dists = sorted(dists) #,reverse=True
    i_matched = set()
    hits2_index = [-1]*min(len(hits1),len(hits2))
    for dist, i, j in dists:
        if not (i in i_matched) and not (j in hits2_index):
            hits2_index[i] = j
#            print(dist, i, j)
            i_matched.add(i)
    
    hits2_sorted = [hits2[j] for j in hits2_index ]
    if len(hits1)>len(hits2):
        for i in range(len(hits1)-len(hits2)):
            hits2_sorted.append([-2000]*len(hits2[0]))
    elif len(hits2)>len(hits1):
        for j in range(len(hits2)):
            if not (j in hits2_index):
                hits2_sorted.append(hits2[j])
    
    dist, i, j = dists[0]
#    print(dists[0])
#    print(hits1[i])
#    print(hits2[j])
#    print(hits2_sorted[i])
    
#    for i in range(len(hits2_sorted)):
#        print(distance(hits2_sorted[i], hits1[i],npar), i, hits2_index[i])
    return hits2_sorted

#print("##################### vecPixelHit ######################")
#for funcName in funcNames:
#    compare(vecPixelHit_GPU, vecPixelHit_CPU, funcName)


def compare (hits_CPU, hits_GPU, funcNames, detId):
#    print("i", "distance", "diff", 'CPU', 'GPU')
    for i in range(max(len(hits_CPU),len(hits_GPU))):
        if i>=len(hits_CPU): 
            print(i, "Missing CPU hit")
            continue
        diff = [hits_CPU[i][p]-hits_GPU[i][p] for p in range(len(hits_GPU[i]))]
        d = distance(hits_CPU[i],hits_GPU[i], len(funcNames))
        if d>2:
#            print(i,'\t',round(d,2),'\t', roundVect(hits_CPU[i]),'\t', roundVect(hits_GPU[i]),'\t', roundVect(diff))
            print("detId:",detId,'\t', "cluster:",i,'\t',"diff:",round(d,2))
            print("cpu:", roundVect(hits_CPU[i]))
            print("gpu:", roundVect(hits_GPU[i]))
            print("dif:", roundVect(diff))

def roundVect(vect):
    return [round(el, 2) for el in vect]

first = True
for pixelHits_CPU, pixelHits_GPU in zip(vecPixelHits_CPU.product(), vecPixelHits_GPU.product()):
#    print(pixelHits_CPU.detId(),pixelHits_CPU.size())
    if (pixelHits_CPU.detId()!=pixelHits_GPU.detId()):
        print(pixelHits_CPU.detId(),pixelHits_GPU.detId())
    if (pixelHits_CPU.size()!=pixelHits_GPU.size()):
        print(pixelHits_CPU.size(),pixelHits_GPU.size())

    hits_CPU = readHits(pixelHits_CPU, funcNames)

    #hits_CPU = sorted(hits_CPU, key=lambda x:x[4], reverse=True) #sort by pt
    hits_GPU = readHits(pixelHits_GPU, funcNames)

    hits_GPU = sorthits (hits_CPU,hits_GPU, npar)

    if first:
        print([f[0] for f in funcNames])
        for p in range(len(hits_CPU[0])): print(p, funcNames[p], hits_CPU[0][p])
        first = False
    
    compare(hits_CPU,hits_GPU, funcNames, pixelHits_CPU.detId())
### DEBUG ###

clusterDebug = { #DetId ClusterNumber
    303054852: [35, 39],
    303067152: [36],
}

for pixelHits_CPU, pixelHits_GPU in zip(vecPixelHits_CPU.product(), vecPixelHits_GPU.product()):
    if pixelHits_CPU.detId() in clusterDebug:
        for clNum in clusterDebug[pixelHits_CPU.detId()]:
            print()
            print("DetId:",pixelHits_CPU.detId()," clNum:",clNum)
            cluster_CPU = pixelHits_CPU[clNum].cluster().get()
            cluster_GPU = pixelHits_GPU[clNum].cluster().get()
            
            pixels_CPU = [[p.x,p.y,p.adc] for p in cluster_CPU.pixels()]
            pixels_GPU = [[p.x,p.y,p.adc] for p in cluster_GPU.pixels()]
            pixels_CPU = sorthits(pixels_GPU, pixels_CPU,2)
            
            print("    "," x"," y"," adc",)
            
            for i in range(max(len(pixels_CPU),len(pixels_GPU))):
                cpu = pixels_CPU[i] if i<len(pixels_CPU) else [-200]*3 
                gpu = pixels_GPU[i] if i<len(pixels_GPU) else [-300]*3 
                diff = [cpu[p] - gpu[p] for p in range(len(cpu))]
                print("diff: ",diff," cpu: ",cpu," gpu: ",gpu)

