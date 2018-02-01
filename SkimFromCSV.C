#include"TString.h"
#include"TChain.h"
#include"TTree.h"
#include"TFile.h"
#include"TH1F.h"
#include"TTreeFormula.h"
#include <iostream>
#include <fstream>
#include <sstream>


void
skim (TString inputFile, TString outputFile)
{
  cout << "I'm doing " << outputFile << endl;
  TFile *fileout = new TFile (outputFile, "recreate");
  TFile *filein = new TFile (inputFile);
  TTree *tree = (TTree *) filein->Get ("rootTupleTree/tree");
  cout << "tree:" << tree << endl;

  Double_t run, lumi;
  tree->GetEntry (0);
  tree->SetBranchAddress ("run", &run);
  tree->SetBranchAddress ("lumi", &lumi);
  cout << "2" << endl;

  fileout->cd ();
  int entries = tree->GetEntries ();
  if (entries <= 0) {
    cout << "No entries in file " << inputFile << endl;
    throw 1;
  }
  TTree *newTree = tree->CloneTree (0);
  cout << "3" << endl;
  
  ifstream file ("lowLumi.csv");        // declare file stream: http://www.cplusplus.com/reference/iostream/ifstream/
  int idx = 0;
  int goodRun = -1;
  int goodLumi = -1; 
  std::string s;
  for (int i = 0; i < tree->GetEntries (); i++) {
    tree->GetEntry (i);
    while (file.good () && (run > goodRun || (run == goodRun && lumi > goodLumi))) {
      getline (file, s);
      if(s.size()>5){
      int comma = s.find(",");
      goodRun = std::stoi(s.substr(0,comma));
      goodLumi = std::stoi(s.substr(comma+1,s.size()));
      }
    }
    if (run == goodRun
        && lumi == goodLumi) {
      newTree->Fill ();
    }
  }
  newTree->Write ();


  // Add histogram with Count ///
  TH1F *Count = new TH1F ("Count", "Count", 1, 0, 1);
  Count->SetBinContent (1, entries);
  Count->Write ();
  fileout->Close ();
}

void
skimFromCSV ()
{
  skim ("../ntupleTrigger/CaloJet40Skim.root",
                    "../ntupleTrigger/CaloJet40Skim_lowLumi.root");
}
