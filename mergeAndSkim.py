from ROOT import *

fileout = TFile("merged.root","recreate")
chain = TChain("tree")
#chain.Add("tree_134.root")
#chain.Add("tree_699.root")
chain.Add("tree_*.root")

chain.SetBranchStatus("*",0)
chain.SetBranchStatus("HLT_PFHT800",1)
chain.SetBranchStatus("caloJet_*",1)
chain.SetBranchStatus("pfJet_*",1)
chain.SetBranchStatus("offJet_*",1)
chain.SetBranchStatus("hltQuadCentralJet45",1)
chain.SetBranchStatus("hltBTagCaloCSVp087Triple",1)
chain.SetBranchStatus("hltBTagPFCSVp016SingleWithMatching",1)
chain.SetBranchStatus("run",1)
chain.SetBranchStatus("lumi",1)
chain.SetBranchStatus("event",1)
chain.SetBranchStatus("bx",1)
chain.SetBranchStatus("JSON",1)
chain.SetBranchStatus("instLumi",1)
chain.SetBranchStatus("nVertices",1)


fileout.cd()
newTree = chain.CloneTree(0)
for entry in chain:
    if chain.HLT_PFHT800:
        newTree.Fill()

newTree.Write()
