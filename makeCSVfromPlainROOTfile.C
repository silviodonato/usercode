#include"TString.h"
#include"TChain.h"
#include"TTree.h"
#include"TFile.h"
#include"TH1F.h"
#include"TTreeFormula.h"
#include <iostream>
#include <fstream>

void
doCSV (TString inputFile)
{
  TFile *filein = new TFile (inputFile);
  TTree *tree = (TTree*) filein->Get("rootTupleTree/tree");
  cout << "tree:" << tree << endl;

  Double_t L1_HTT240, run, lumi;
  tree->GetEntry(0);
  tree->SetBranchAddress ("L1_HTT240", &L1_HTT240);
  tree->SetBranchAddress ("run", &run);
  tree->SetBranchAddress ("lumi", &lumi);
  cout << "2" << endl;

  int entries = tree->GetEntries ();
  if (entries <= 0) {
    cout << "No entries in file " << inputFile << endl;
    throw 1;
  }
  TTree *newTree = tree->CloneTree (0);

  vector < pair < int, int >>goodRunLumi;
  int oldLumi = -1;
  for (int i = 0; i < tree->GetEntries (); i++) {
    tree->GetEntry (i);
    if (L1_HTT240 && lumi != oldLumi)
      goodRunLumi.push_back (pair < int, int >(run, lumi));
    oldLumi = lumi;
  }
  
  ofstream myfile;
  myfile.open ("lowLumi.csv");
  for(const auto & pair: goodRunLumi) myfile << pair.first<< ","<<pair.second<< endl;
  myfile.close();

}

void
makeCSV ()
{
  doCSV ("../ntupleTrigger/L1HTTSkim.root");
}
