#include"TString.h"
#include"TChain.h"
#include"TTree.h"
#include"TFile.h"
#include"TH1F.h"
#include"TTreeFormula.h"
#include <iostream>

void skimAndMergeFile(TString inputFiles, TString outputFile){
    cout << "I'm doing "<< outputFile << endl;
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
    
    TTreeFormula* cut = new TTreeFormula("cut","Sum$(caloJets_csv>0.7)>=1 && Sum$(caloJets_pt>30 && abs(caloJets_eta)<2.4)>=2",tree);
    TTreeFormula* puFilter = new TTreeFormula("puFilter","ptHat>maxPUptHat",tree);
    
   for(int i=0; i<tree->GetEntries(); i++){
        tree->GetEntry(i);
        cut->UpdateFormulaLeaves();
        puFilter->UpdateFormulaLeaves();
        if(puFilter->EvalInstance() && cut->EvalInstance()){
            newTree->Fill();
        }
    }
    newTree->Write();

    /// Add histogram with Count ///
    TH1F* Count = new TH1F("Count","Count",1,0,1);
    Count->SetBinContent(1,entries);
    Count->Write();
    fileout->Close();
}

void mergeAndSkim(){
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMQCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/170411_120207/0000/tree_*.root", 
        "QCD15to30.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMQCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/170411_120216/0000/tree_*.root", 
        "QCD30to50.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMQCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/170411_120223/0000/tree_*.root",
        "QCD50to80.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMQCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/170411_120232/0000/tree_*.root",
        "QCD80to120.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMQCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/170411_120240/0000/tree_*.root",
        "QCD120to170.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMQCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/170411_120247/0000/tree_*.root",
        "QCD170to300.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMQCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/170411_120259/0000/tree_*.root",
        "QCD300to470.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMQCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/170411_120307/0000/tree_*.root",
        "QCD470to600.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/GluGluToHHTo4B_node_SM_13TeV-madgraph/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMGluGluToHHTo4B_node_SM_13TeV-madgraph/170411_120500/0000/tree_*.root", 
        "ggHH4b.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/ttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMttHTobb_M125_TuneCUETP8M2_13TeV-powheg-pythia8/170411_101616/0000/tree_*.root",
        "ttHbb.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/VBFHToBB_M-125_13TeV_powheg_pythia8_weightfix/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMVBFHToBB_M-125_13TeV_powheg_pythia8_weightfix/170411_120419/0000/tree_*.root",
        "VBFHbb.root"
        );
    skimAndMergeFile(
        "root://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/sdonato/HLT_Ntuple_Hbb_Signal_v5_noAODSIM/GluGluHToBB_M125_13TeV_powheg_pythia8/crab_HLT_Ntuple_Hbb_Signal_v5_noAODSIMGluGluHToBB_M125_13TeV_powheg_pythia8/170411_120440/0000/tree_*.root",
        "ggHbb.root"
        );
}

