import ROOT

file_ = ROOT.TFile.Open("/afs/cern.ch/work/s/sdonato/public/GPU_fluctuation_study/output_HLT_GPU_CPU_GPU2.root")

from DataFormats.FWLite import Handle, Events

events = Events (file_)
for ievt,event in enumerate(events): 
#    if ievt>=1:
#        break
    
    vecPixelHitsLabel_GPU = ("hltSiPixelClusters::HLTGPU")
    vecPixelHitsLabel_CPU = ("hltSiPixelClusters::HLTCPU")

    vecPixelHits_CPU = Handle("edmNew::DetSetVector<SiPixelCluster>")
    vecPixelHits_GPU = Handle("edmNew::DetSetVector<SiPixelCluster>")

    events.getByLabel(vecPixelHitsLabel_GPU, vecPixelHits_GPU)
    events.getByLabel(vecPixelHitsLabel_CPU, vecPixelHits_CPU)

    cluster = 0
    pixels = 0
    cluster_dup = 0
    pixels_dup = 0

    for pixelHits_CPU, pixelHits_GPU in zip(vecPixelHits_CPU.product(), vecPixelHits_GPU.product()):
        if (pixelHits_CPU.detId()!=pixelHits_GPU.detId()):
            print(pixelHits_CPU.detId(),pixelHits_GPU.detId())
        detId = pixelHits_CPU.detId()
        
        for pixelHits in [pixelHits_CPU, pixelHits_GPU]:
            arch = "gpu" if pixelHits==pixelHits_GPU else "cpu"
            for pixelHit in pixelHits:
                buff = set()
                if arch == "gpu": cluster += 1
                for i, pix in enumerate(pixelHit.pixels()):
                    first = True
                    if arch == "gpu": pixels += 1
                    xy = (pix.x,pix.y)
                    if not (xy in buff):
                        buff.add(xy)
                    else:
                        if arch == "gpu": 
                            pixels_dup += 1
                            if first: cluster_dup += 1
#                        print("Duplicate %s in detId=%d cl=%d x=%d y=%d"%(arch, detId,i,xy[0],xy[1]))
    #            print(arch,detId,i)
    
    print("event =",event.eventAuxiliary().event(), " duplicates =",pixels_dup)
#    print(cluster,pixels)
#    print(cluster_dup,pixels_dup)
#    print(cluster_dup/cluster,pixels_dup/pixels)

