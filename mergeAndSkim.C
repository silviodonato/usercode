#include"TString.h"
#include"TChain.h"
#include"TTree.h"
#include"TFile.h"
#include <iostream>

void skimAndMergeFile(TString inputFiles, TString outputFile){
    TFile* fileout = new TFile(outputFile,"recreate");
    TChain* tree = new TChain("tree");
    tree->Add(inputFiles);

    fileout->cd();
    if(tree->GetEntries()<=0) {
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
}

void mergeAndSkim(){
    TString inputFiles = TString("root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v3_noAODSIM/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/HLT_Ntuple_Hbb_Signal_v3_noAODSIM/170408_101635/0000/tree_11*.root");
    TString outputFile = TString("QCD30to50.root");
    skimAndMergeFile(inputFiles, outputFile);
}

