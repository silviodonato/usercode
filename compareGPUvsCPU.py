import ROOT

file_ = ROOT.TFile.Open("/afs/cern.ch/work/s/sdonato/public/GPU_fluctuation_study/output_HLT_GPU_CPU_GPU2.root")

from DataFormats.FWLite import Handle, Events

events = Events (file_)
for ievt,event in enumerate(events): 
    if ievt>=1:
        break

pixelTracksLabel_GPU = ("hltPixelTracks::HLTGPU")
pixelTracksLabel_CPU = ("hltPixelTracks::HLTCPU")

pixelTracks_CPU = Handle("vector<reco::Track>")
pixelTracks_GPU = Handle("vector<reco::Track>")

events.getByLabel(pixelTracksLabel_GPU, pixelTracks_GPU)
events.getByLabel(pixelTracksLabel_CPU, pixelTracks_CPU)

#pixelTrack_CPU = pixelTracks_CPU.product()
#pixelTrack_GPU = pixelTracks_GPU.product()


funcNames = [
("phi",[]),
("eta",[]),
("dz",[]),
("dxy",[]),
("pt",[]),
("chi2",[]),
#("beta",[]),
("charge",[]),
("missingInnerHits",[]),
#("dxyError",[]),
#("dzError",[]),
#("phiError",[]),
#("etaError",[]),
#("ptError",[]),
#("quality",[1]),
]

trackMissing = [-2000]*len(funcNames)

npar = 2 

def getVect(track, funcNames):
    vect = []
    for functionName,params in funcNames:
        vect.append(getattr(track, functionName)(*params))
    return vect

def readTracks(pixelTracks_handle, funcNames):
    out = []
    pixelTracks = pixelTracks_handle.product()
    for track in pixelTracks:
        out.append(getVect(track, funcNames))
#    out = sorted(out, key=lambda x:x[0])
    return out

def distance(track1, track2, npar):
    return sum((track1[p]-track2[p])**2 for p in range(npar))

def sortTracks(tracks1, tracks2, npar):
    dists = []
    for i in range(len(tracks1)):
        for j in range(len(tracks2)):
            dists.append((distance(tracks1[i], tracks2[j],npar), i, j))
    dists = sorted(dists) #,reverse=True
    i_matched = set()
    j_matched = set()
    tracks2_index = [-1]*max(len(tracks1),len(tracks2))
    for dist, i, j in dists:
        if not (i in i_matched) and not (j in tracks2_index):
            tracks2_index[i] = j
#            print(dist, i, j)
            i_matched.add(i)
    
    tracks2_sorted = [tracks2[j] if j>=0 and j<len(tracks2) else trackMissing for j in tracks2_index ]
    dist, i, j = dists[0]
#    print(dists[0])
#    print(tracks1[i])
#    print(tracks2[j])
#    print(tracks2_sorted[i])
    
#    for i in range(len(tracks2_sorted)):
#        print(distance(tracks2_sorted[i], tracks1[i],npar), i, tracks2_index[i])
    return tracks2_sorted

#print("##################### pixelTrack ######################")
#for funcName in funcNames:
#    compare(pixelTrack_GPU, pixelTrack_CPU, funcName)


tracks_CPU = readTracks(pixelTracks_CPU, funcNames)
for p in range(len(tracks_CPU[0])): print(p, funcNames[p], tracks_CPU[0][p])

#tracks_CPU = sorted(tracks_CPU, key=lambda x:x[4], reverse=True) #sort by pt
tracks_GPU = readTracks(pixelTracks_GPU, funcNames)

tracks_GPU = sortTracks (tracks_CPU,tracks_GPU, npar)

def roundVect(vect):
    return [round(el, 2) for el in vect]

def compare (tracks_CPU, tracks_GPU, funcNames):
    print("i", "distance", "diff", 'CPU', 'GPU')
    for i in range(max(len(tracks_CPU),len(tracks_GPU))):
        if i>=len(tracks_CPU): 
            print(i, "Missing CPU track")
            continue
        diff = [tracks_CPU[i][p]-tracks_GPU[i][p] for p in range(len(tracks_GPU[i]))]
        d = distance(tracks_CPU[i],tracks_GPU[i], len(funcNames))
        if d>0.01:
            print(i,'\t',round(d,2),'\t', roundVect(tracks_CPU[i]),'\t', roundVect(tracks_GPU[i]),'\t', roundVect(diff))
            
#            print(i,'\t',round(d,2))
#            print("cpu:", roundVect(tracks_CPU[i]))
#            print("gpu:", roundVect(tracks_GPU[i]))
#            print("dif:", roundVect(diff))

print([f[0] for f in funcNames])
compare(tracks_CPU,tracks_GPU, funcNames)

print("")

