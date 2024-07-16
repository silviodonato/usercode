import ROOT
from DataFormats.FWLite import Handle, Events

maxEvents = 10
input_file = "/eos/cms/store/data/Run2024E/ScoutingPFMonitor/RAW/v1/000/381/380/00000/8c3e80f5-30b6-4105-b28c-ff5acd9285f6.root"
output_file = "test.root" 

treeNames = [
    # "Events"
    # "MetaData", "Events"
    # "MetaData", "ParameterSets", "Parentage", "Events", "LuminosityBlocks", "Runs"
    "ParameterSets", "Parentage", "Events", "LuminosityBlocks", "Runs"
]


input_file = ROOT.TFile(input_file)
trees = [input_file.Get(tree) for tree in treeNames]
input_tree = input_file.Get("Events")

output = ROOT.TFile(output_file, "RECREATE")
outTrees = []
for t in trees:
    outTrees.append(t.CloneTree(0))
# output_tree = input_tree.CloneTree(0)  # Clone the structure but not the entries

for i in range(maxEvents):
    for t in trees:
        t.GetEntry(i)
        # tree.GetEntry(i)
    for t in outTrees:
        t.Fill()

# Write and close the output file
output.cd()
for t in outTrees:
    t.Write()
output.Write()
output.Close()
