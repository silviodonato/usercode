from ROOT import *

fileout = TFile("merged.root","recreate")
chain = TChain("tree")
#chain.Add("tree_134.root")
#chain.Add("tree_699.root")
chain.Add("tree_*.root")

chain.SetBranchStatus("HLT*",0)
chain.SetBranchStatus("HLT_PFHT800",1)
chain.SetBranchStatus("caloJet_*",1)
chain.SetBranchStatus("pfJet_*",1)
chain.SetBranchStatus("offJet_*",1)
chain.SetBranchStatus("hltQuadCentralJet45",1)
chain.SetBranchStatus("hltBTagCaloCSVp087Triple",1)
chain.SetBranchStatus("hltBTagPFCSVp016SingleWithMatching",1)


fileout.cd()
newTree = chain.CloneTree(0)
for entry in chain:
    if chain.HLT_PFHT800:
        newTree.Fill()

newTree.Write()
