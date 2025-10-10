#!/usr/bin/env python3
# dump_approx_clusters.py
import sys, ROOT
from DataFormats.FWLite import Events, Handle

# Enable FWLite in Python
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.gSystem.Load("libDataFormatsFWLite.so")
ROOT.FWLiteEnabler.enable()
ROOT.gROOT.SetBatch(True)

# Input file (default to the one you mentioned)
infile = sys.argv[1] if len(sys.argv) > 1 else "outputPhysicsHIPhysicsRawSecond.root"

# Event source
events = Events(infile)

# Prepare both possible handle strings (the first should work;
# the second is a fallback for older releases)
h_cl  = Handle("edmNew::DetSetVector<SiStripCluster>")
lable_cl = ("hltSiStripClusterizerForRawPrime", "", "HLTX")
h_clFromV1 = Handle("edmNew::DetSetVector<SiStripCluster>")
h_clFromV2 = Handle("edmNew::DetSetVector<SiStripCluster>")
h_coll  = Handle("SiStripApproximateClusterCollection")
h_collV2  = Handle("v1::SiStripApproximateClusterCollection")
#h_dsv   = Handle("edmNew::DetSetVector<SiStripApproximateCluster>")

# InputTag: module, instance, process
label = ("hltSiStripClusters2ApproxClusters", "", "HLTX")
labelV2 = ("hltSiStripClusters2ApproxClustersv1", "", "HLTX")

labelclFromV1 = ("hltSiStripClustersFromRawPrime", "", "HLTX")
labelclFromV2 = ("hltSiStripClustersFromRawPrimev1", "", "HLTX")


# Small factory for histogram pairs to reduce repetition
def make_hist_pair(name1, title1, name2, title2, nbins, xmin, xmax):
    h1 = ROOT.TH1F(name1, title1, nbins, xmin, xmax)
    h2 = h1.Clone(name2)
    h2.SetTitle(title2)
    return h1, h2

histos = {}
# Basic comparisons
# histos["avgCharge1"], histos["avgCharge2"] = make_hist_pair(
#     "avgCharge1", "avgCharge1", "avgCharge2", "avgCharge2", 100, -3, 3
# )
# histos["barycenter1"], histos["barycenter2"] = make_hist_pair(
#     "barycenter1", "barycenter1", "barycenter2", "barycenter2", 100, -2, 2
# )
# Method comparisons
histos["barycenter_data_v1"], histos["barycenter_data_v2"] = make_hist_pair(
    "barycenter_data_v1", "barycenter() method - version 1",
    "barycenter_data_v2", "barycenter() method - version 2", 100, -1, 1
)
histos["barycenter_get_v1"], histos["barycenter_get_v2"] = make_hist_pair(
    "barycenter_get_v1", "barycenter() method - version 1",
    "barycenter_get_v2", "barycenter() method - version 2", 100, -0.1, 0.1
)
histos["avgCharge_data_v1"], histos["avgCharge_data_v2"] = make_hist_pair(
    "avgCharge_data_v1", "avgCharge() method - version 1",
    "avgCharge_data_v2", "avgCharge() method - version 2", 100, -3, 3
)
histos["avgCharge_get_v1"], histos["avgCharge_get_v2"] = make_hist_pair(
    "avgCharge_get_v1", "getAvgCharge() method - version 1",
    "avgCharge_get_v2", "getAvgCharge() method - version 2", 100, -3, 3
)
histos["rawPrime_barycenter_diff_v1"], histos["rawPrime_barycenter_diff_v2"] = make_hist_pair(
    "rawPrime_barycenter_diff_v1", "RawPrime V1 - Clusterizer barycenter",
    "rawPrime_barycenter_diff_v2", "RawPrime V2 - Clusterizer barycenter", 100, -0.1, 0.1
)
histos["rawPrime_avgCharge_diff_v1"], histos["rawPrime_avgCharge_diff_v2"] = make_hist_pair(
    "rawPrime_avgCharge_diff_v1", "RawPrime V1 - Clusterizer avgCharge",
    "rawPrime_avgCharge_diff_v2", "RawPrime V2 - Clusterizer avgCharge", 100, -3, 3
)

# --- Helpers to reduce repetition -------------------------------------------------
def _style_hist_pair(h1, h2, color1=ROOT.kRed, color2=ROOT.kBlue, width=2):
    h1.SetLineColor(color1)
    h1.SetLineWidth(width)
    h2.SetLineColor(color2)
    h2.SetLineWidth(width)


def draw_pair(h1, h2, out_base, logy=True,
              color1=ROOT.kRed, color2=ROOT.kBlue,
              legend_labels=None, legend_pos=(0.60, 0.72, 0.88, 0.88)):
    """
    Draw two histograms on the same canvas and save PNG/ROOT.
    - out_base: base filename (without extension), e.g. 'plot' or 'barycenter_plot'
    """
    c = ROOT.TCanvas(out_base, out_base, 800, 600)
    if logy:
        c.SetLogy()

    _style_hist_pair(h1, h2, color1, color2)
    h2.SetMaximum(1.2 * max(h1.GetMaximum(), h2.GetMaximum()))
    h2.SetMinimum(h2.GetMaximum()/1e4 )
    h2.Draw()
    h1.Draw("same")

    # Legend
    if legend_labels is None:
        legend_labels = (h1.GetTitle(), h2.GetTitle())
    leg = ROOT.TLegend(*legend_pos)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.AddEntry(h1, legend_labels[0], "l")
    leg.AddEntry(h2, legend_labels[1], "l")
    leg.Draw()
    # Keep a Python reference so legend isn't GC'd
    c._legend = leg
    c.SaveAs(f"{out_base}.png")
    c.SaveAs(f"{out_base}.root")



for iev, ev in enumerate(events):
    got = ev.getByLabel(label, h_coll)
    gotV2 = ev.getByLabel(labelV2, h_collV2)
    gotcl = ev.getByLabel(lable_cl, h_cl)
    gotclFromV1 = ev.getByLabel(labelclFromV1, h_clFromV1)
    gotclFromV2 = ev.getByLabel(labelclFromV2, h_clFromV2)
    coll = None
    collV2 = None
    collCl = None
    collClFromV1 = None
    collClFromV2 = None
    if got and h_coll.isValid():
        coll = h_coll.product()
    if gotV2 and h_collV2.isValid():
        collV2 = h_collV2.product()
    if gotcl and h_cl.isValid():
        collCl = h_cl.product()
    if gotclFromV1 and h_clFromV1.isValid():
        collClFromV1 = h_clFromV1.product()
    if gotclFromV2 and h_clFromV2.isValid():
        collClFromV2 = h_clFromV2.product()
    # else:
    #     # Fallback to edmNew::DetSetVector<SiStripApproximateCluster>
    #     got2 = ev.getByLabel(label, h_dsv)
    #     if got2 and h_dsv.isValid():
    #         coll = h_dsv.product()
    #     else:
    #         # No product in this event
    #         print("No SiStripApproximateClusterCollection or edmNew::DetSetVector<SiStripApproximateCluster> in this event")
    #         continue

    print(f"=== Event {iev} ===")

    if any(obj is None for obj in (coll, collV2, collCl, collClFromV1, collClFromV2)):
        print("Missing one or more cluster collections in this event, skipping comparisons.")
        for nm, obj in (("SiStripApproximateClusterCollection V1", coll),
                        ("SiStripApproximateClusterCollection V2", collV2),
                        ("SiStripCluster V1", collCl),
                        ("SiStripCluster FromRawPrime V1", collClFromV1),
                        ("SiStripCluster FromRawPrime V2", collClFromV2)):
            if obj is None:
                print(f"  Missing: {nm}")
        continue

    print("collCl size:", collCl.size())
    print("collClFromV1 size:", collClFromV1.size())
    print("collClFromV2 size:", collClFromV2.size())
    # print("collCl size:", sum([1 for x in collCl]))
    # print("coll size:", sum([1 for x in coll]))
    # print("collV2 size:", sum([1 for x in collV2]))
    # collClFromV1 = collCl  # Temporary: V1 not filled in this test yet
    # collClFromV2 = collClFromV1  # Temporary: V2 not filled in this test yet
    # The collection iterates as det-sets; each det-set holds clusters for one detId
    cl2_getbc = 0
    clo_bc = 0 
    offset_change_module = 0
    clo_w = 0
    cl2_getbc = 0.5
    collV2 = coll
    # coll = collV2
    for detset, detsetV2, detsetCl, detsetClFromV1, detsetClFromV2 in zip(coll, collV2, collCl, collClFromV1, collClFromV2):
        print(f"detsetCl.size()= {detsetCl.size()}")
        print(f"detsetClFromV1.size()= {detsetClFromV1.size()}")
        print(f"detsetClFromV2.size()= {detsetClFromV2.size()}")
        print(f"detset.end()-detset.begin()= {detset.end()-detset.begin()}")
        print(f"detsetV2.end()-detsetV2.begin()= {detsetV2.end()-detsetV2.begin()}")
        
        assert(detset.id() == detsetV2.id())
        assert(detset.end()-detset.begin() == detsetV2.end()-detsetV2.begin())
        assert(detset.end()-detset.begin() == detsetCl.size())
        assert(detsetCl.size() == detsetClFromV1.size())
        assert(detsetCl.size() == detsetClFromV2.size())
        assert(detset.id() == detsetCl.detId())
        assert(detset.id() == detsetClFromV1.detId())
        assert(detset.id() == detsetClFromV2.detId())
        # Try common detId accessors across CMSSW versions/bindings
        detid = None
        for nm in ("detId", "id", "rawId"):
            if hasattr(detset, nm):
                assert(getattr(detset, nm)() == getattr(detsetV2, nm)())
                # print(nm + " ok.")

        # print(f"DetId: {detid}", detsetCl.size(), "clusters")

        ## The length of module should be taken from the conditions, here a workaround
        if cl2_getbc>(512+10): offset_change_module = 768
        elif cl2_getbc>10: offset_change_module = 512
        else: offset_change_module = 0 # first cluster in module
        # Loop over clusters and print all data members (via getters)
        for i,x  in enumerate(detset):
            cl  = (detset.begin()  +i).base()
            cl2 = (detsetV2.begin()+i).base()
            cl_original = detsetCl[i]
            cl_rawprime_v1 = detsetClFromV1[i]
            cl_rawprime_v2 = detsetClFromV2[i]

            previous_cl2_getbc = float(cl2_getbc)
            previous_clo_w = int(clo_w)

            clo_bc  = cl_original.barycenter()     # stored *10 internally
            clo_w   = detsetCl[i].endStrip()-detsetCl[i].firstStrip()
            clo_q   = cl_original.charge()/clo_w
            clo_flt = bool(cl_original.filter())
            print(f"  [{i}] original barycenter={clo_bc}  width={clo_w}  avgCharge={clo_q}  "
                    f"filter={clo_flt}")

            ## if the position is completely different, update the previous barycenter from orginal (cheating)
            if abs(clo_bc - cl2.barycenter()) > 128:
                print("AAA clo_bc =", clo_bc, " previous_cl2_getbc =", previous_cl2_getbc, " cl2.barycenter =", cl2.barycenter(), " offset_change_module =", offset_change_module)
                previous_cl2_getbc = float(cl2_getbc - 256)
                print("AAA new previous_cl2_getbc =", previous_cl2_getbc)
                # previous_cl2_getbc = float(clo_bc) 
            # previous_cl2_getbc = 55.55
            # offset_change_module = int(100)
            print(" Old cl2_getbc =", previous_cl2_getbc, " offset_change_module=", offset_change_module)

            cl2_v2  = -1 #cl2.version()
#            cl2_bc  = cl2.barycenter(previous_cl2_getbc, offset_change_module)     # stored *10 internally
            cl2_bc  = 0     # stored *10 internally
            cl2_getbc  = cl2.barycenter()    
            # 1/0
            cl2_w   = ord(cl2.width())
            cl2_q   = 0
            # cl2_q   = ord(cl2.avgCharge())
            cl2_getq   = cl2.avgCharge()
            cl2_flt = bool(cl2.filter())
            cl2_sat = bool(cl2.isSaturated())
            cl2_pkf = bool(cl2.peakFilter())
            print(f"  [{i}] v2={cl2_v2} barycenter={cl2_bc}  getBarycenter={cl2_getbc}  getBarwidth={cl2_w}  avgCharge={cl2_q}  "
                     f"filter={cl2_flt}  isSaturated={cl2_sat}  peakFilter={cl2_pkf}")

            cl_v2  =  -1 #cl.version()
            cl_bc  = cl.barycenter()     # stored *10 internally
            cl_getbc  = cl.barycenter()   
            cl_w   = ord(cl.width())
            cl_q   = ord(cl.avgCharge())
            cl_getq   = cl.barycenter()
            cl_flt = bool(cl.filter())
            cl_sat = bool(cl.isSaturated())
            cl_pkf = bool(cl.peakFilter())
            print(f"  [{i}] v2={cl_v2} barycenter={cl_bc}  width={cl_w}  avgCharge={cl_q}  "
                    f"filter={cl_flt}  isSaturated={cl_sat}  peakFilter={cl_pkf}")

            # histos["avgCharge1"].Fill(cl_q-clo_q)
            # histos["avgCharge2"].Fill(cl2_q-clo_q)
            # histos["barycenter1"].Fill(cl_bc-clo_bc*10)
            # histos["barycenter2"].Fill(cl2_bc-clo_bc*10)

            offset_change_module = 0

            print(" previous_clo_w =", previous_clo_w, " clo_w =", clo_w)
            if  not((previous_clo_w==1) or (clo_w==1)):
                # Fill separate histograms for barycenter() vs barycenter() comparison
                histos["barycenter_data_v1"].Fill(cl_bc-clo_bc*10)
                histos["barycenter_data_v2"].Fill(cl2_bc-clo_bc*10)
                histos["barycenter_get_v1"].Fill(cl_getbc-clo_bc)
                histos["barycenter_get_v2"].Fill(cl2_getbc-clo_bc)
                histos["rawPrime_barycenter_diff_v1"].Fill(cl_rawprime_v1.barycenter() - cl_original.barycenter())
                histos["rawPrime_barycenter_diff_v2"].Fill(cl_rawprime_v2.barycenter() - cl_original.barycenter())
                print("Diff: cluster 1 vs 2:", cl_rawprime_v1.barycenter() - cl_original.barycenter())
                print("Diff: cluster 1 vs 2:", cl_rawprime_v2.barycenter() - cl_original.barycenter())
                print("Barycenter cluster 1 vs 2:", cl_rawprime_v1.barycenter(), cl_rawprime_v2.barycenter())
                print("Barycenter Approx cluster 1 vs 2:", cl_bc, cl2_bc)
            
            # Fill separate histograms for avgCharge() vs getAvgCharge() comparison
            cl_q_old = ord(cl.avgCharge())      # avgCharge() method
            cl2_q_old = 0      # avgCharge() method
            # cl2_q_old = ord(cl2.avgCharge())    # avgCharge() method
            cl_q_new = ord(cl.avgCharge())        # getAvgCharge() method
            cl2_q_new = ord(cl2.avgCharge())      # getAvgCharge() method
            histos["avgCharge_data_v1"].Fill(cl_q_old-clo_q)
            histos["avgCharge_data_v2"].Fill(cl2_q_old-clo_q)
            histos["avgCharge_get_v1"].Fill(cl_q_new-clo_q)
            histos["avgCharge_get_v2"].Fill(cl2_q_new-clo_q)

            rp1_width = cl_rawprime_v1.endStrip() - cl_rawprime_v1.firstStrip()
            rp2_width = cl_rawprime_v2.endStrip() - cl_rawprime_v2.firstStrip()
            rp1_avg_charge = cl_rawprime_v1.charge() / rp1_width if rp1_width else 0.0
            rp2_avg_charge = cl_rawprime_v2.charge() / rp2_width if rp2_width else 0.0
            print ("AvgCharge cluster 1 vs 2:", rp1_avg_charge, rp2_avg_charge, clo_q)
            # 1/0
            histos["rawPrime_avgCharge_diff_v1"].Fill(rp1_avg_charge - clo_q)
            histos["rawPrime_avgCharge_diff_v2"].Fill(rp2_avg_charge - clo_q)
            if True:
                if(abs(cl_bc - cl2_bc) > -1):
                    print(f"  [{i}] MISMATCH barycenter: {cl_bc} != {cl2_bc} orginal {clo_bc*10}")
                    print(f"  [{i}] MISMATCH barycenter: {cl_getbc} != {cl2_getbc} orginal {clo_bc}")
                if(abs(cl_w - cl2_w) > 0):
                    print(f"  [{i}] MISMATCH width: {cl_w} != {cl2_w} orginal {clo_w}")
                if(abs(cl_q_old - cl2_q_old) > 3):
                    print(f"  [{i}] MISMATCH avgCharge: {cl_q_old} != {cl2_q_old} orginal {clo_q}")
                    print(f"  [{i}] MISMATCH avgCharge: {cl_q_new} != {cl2_q_new} orginal {clo_q}")
                if(cl_flt != cl2_flt):
                    print(f"  [{i}] MISMATCH filter: {cl_flt} != {cl2_flt}")
                if(cl_sat != cl2_sat):
                    print(f"  [{i}] MISMATCH isSaturated: {cl_sat} != {cl2_sat}")
                if(cl_pkf != cl2_pkf):
                    print(f"  [{i}] MISMATCH peakFilter: {cl_pkf} != {cl2_pkf}")

# Draw histograms without fitting
draw_pair(
    histos["barycenter_data_v1"], histos["barycenter_data_v2"],
    out_base="barycenter_data", logy=True
)
draw_pair(
    histos["barycenter_get_v1"], histos["barycenter_get_v2"],
    out_base="barycenter_get", logy=True
)

draw_pair(
    histos["avgCharge_data_v1"], histos["avgCharge_data_v2"],
    out_base="avgCharge_data", logy=True
)
draw_pair(
    histos["avgCharge_get_v1"], histos["avgCharge_get_v2"],
    out_base="AvgCharge_get", logy=True
)

draw_pair(
    histos["rawPrime_barycenter_diff_v1"], histos["rawPrime_barycenter_diff_v2"],
    out_base="rawPrime_barycenter_diff", logy=True,
    legend_labels=("RawPrime V1 - Clusterizer", "RawPrime V2 - Clusterizer")
)

draw_pair(
    histos["rawPrime_avgCharge_diff_v1"], histos["rawPrime_avgCharge_diff_v2"],
    out_base="rawPrime_avgCharge_diff", logy=True,
    legend_labels=("RawPrime V1 - Clusterizer", "RawPrime V2 - Clusterizer")
)
