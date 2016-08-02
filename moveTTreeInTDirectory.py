from ROOT import TTree
from ROOT import TFile
file_ = TFile("VHBB.root")
tree = file_.Get("tree")
newfile_ = TFile("new.root","recreate")
dir = newfile_.mkdir("vhbb")
dir.cd()
newtree = tree.CloneTree()
newtree.Write()
newfile_.Close()
