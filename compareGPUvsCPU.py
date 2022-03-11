import ROOT

file_ = ROOT.TFile.Open("/afs/cern.ch/work/s/sdonato/public/GPU_fluctuation_study/output_HLT_GPU_CPU_GPU2.root")

from DataFormats.FWLite import Handle, Events

events = Events (file_)
for ievt,event in enumerate(events): 
    if ievt==2:
        break

pixelTracksLabel_GPU = ("hltPixelTracks::HLTGPU")
pixelTracksLabel_CPU = ("hltPixelTracks::HLTCPU")

pixelTracks_CPU = Handle("vector<reco::Track>")
pixelTracks_GPU = Handle("vector<reco::Track>")

events.getByLabel(pixelTracksLabel_GPU, pixelTracks_GPU)
events.getByLabel(pixelTracksLabel_CPU, pixelTracks_CPU)

pixelTrack_CPU = pixelTracks_CPU.product()
pixelTrack_GPU = pixelTracks_GPU.product()


funcNames = [
("phi",[]),
("eta",[]),
("dz",[]),
("dxy",[]),
("pt",[]),
("charge",[]),
("quality",[1]),
#"quality",
#"size",
]

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
    
    tracks2_sorted = [tracks2[j] for j in tracks2_index if j>=0 and j<len(tracks2)]
    dist, i, j = dists[0]
#    print(dists[0])
#    print(tracks1[i])
#    print(tracks2[j])
#    print(tracks2_sorted[i])
    return tracks2_sorted

#print("##################### pixelTrack ######################")
#for funcName in funcNames:
#    compare(pixelTrack_GPU, pixelTrack_CPU, funcName)

tracks_CPU = readTracks(pixelTracks_CPU, funcNames)
tracks_GPU = readTracks(pixelTracks_GPU, funcNames)

tracks_GPU = sortTracks (tracks_CPU,tracks_GPU, npar)

def roundVect(vect):
    return [round(el, 2) for el in vect]

def compare (tracks_CPU, tracks_GPU, funcNames):
    for i in range(min(len(tracks_CPU),len(tracks_GPU))):
        diff = [tracks_CPU[i][p]-tracks_GPU[i][p] for p in range(len(tracks_GPU[i]))]
        d = distance(tracks_CPU[i],tracks_GPU[i], npar)
#        if vcpu!=vgpu:
        print(i, round(d,5), roundVect(diff), roundVect(tracks_CPU[i]), roundVect(tracks_GPU[i]))

print(funcNames)
compare(tracks_CPU,tracks_GPU, funcNames)

print("")

