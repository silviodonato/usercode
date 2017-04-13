#include"TString.h"
#include"TChain.h"
#include"TTree.h"
#include"TFile.h"
#include"TH1F.h"
#include <iostream>

void skimAndMergeFile(TString inputFiles, TString outputFile){
    TFile* fileout = new TFile(outputFile,"recreate");
    TChain* tree = new TChain("tree");
    tree->Add(inputFiles);

    fileout->cd();
    int entries = tree->GetEntries();
    if(entries<=0) {
        cout<<"No entries in file "<<inputFiles<<endl;
        throw 1;
    }
    TTree* newTree = tree->CloneTree(0);
    for(int i=0; i<tree->GetEntries(); i++){
        if(true){
            newTree->Fill();
        }
    }
    newTree->Write();

    /// Add histogram with Count ///
    TH1F* Count = new TH1F("Count","Count",1,0,1);
    Count->SetBinContent(1,entries);
    Count->Write();
}

void mergeAndSkim(){
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v3_noAODSIM/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/HLT_Ntuple_Hbb_Signal_v3_noAODSIM/170408_101635/0000/tree_11*.root", 
        "QCD30to50.root"
        );
}

