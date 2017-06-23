#include"TChain.h"
#include"TFile.h"
#include"TH1F.h"
#include"TTreeFormula.h"
#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include"TLorentzVector.h"
#include <future>
#include"btagCorrection_ddQCD.h"

bool sort_function (std::pair<float,int> csv1, std::pair<float,int> csv2) { return ((csv1.first) > (csv2.first)); }

void addCSV(string fileName){
    TFile* file               = TFile::Open(fileName.c_str());
//    auto file_withCSVsorted   = new TFile(fileName.replace(fileName.find("V25_systematics_nBCSVM_CR_v1")+28,0,"_withCSVsorted").c_str(),"recreate");
    cout << "\nI'm doing " << fileName ;

    TFile* file_withCSVsorted   = TFile::Open(fileName.replace(0,fileName.rfind("/"),"./").c_str(),"recreate");
    cout << " -> "<< fileName.replace(0,fileName.rfind("/"),"./").c_str() << endl;
    
    
    int njets = 0;
    double jets_btagCSV[20]={};
    double jets_pt[20]={};
    double jets_eta[20]={};
    double jets_phi[20]={};
    float jets_btagCorr[20]={};
    float jets_dRmax[20]={};
    float jets_dRmin[20]={};
    float jets_dRave[20]={};
    int jets_btagCSVsorted[20]={};
    int jets_btagCSVindex[20]={};
    double btagCorr = 0;
    float deta1,deta2,dphi1,dphi2,dR1,dR2;
    
    
    file->cd();
    auto tree = (TTree*) file->Get("tree");
    tree->SetBranchStatus("*",1);
//    tree->SetBranchStatus("*loose*",0);
    tree->SetBranchStatus("*othertop*",0);
    tree->SetBranchStatus("*Candidate*",0);
//    tree->SetBranchStatus("*gen*",0);
    tree->SetBranchStatus("*Time*",0);
    tree->SetBranchStatus("genWeight*",1);
    tree->SetBranchAddress("njets",&njets);
    tree->SetBranchAddress("jets_btagCSV",jets_btagCSV);
    tree->SetBranchAddress("jets_pt",jets_pt);
    tree->SetBranchAddress("jets_eta",jets_eta);
    tree->SetBranchAddress("jets_phi",jets_phi);
    auto Count = (TH1F*) file->Get("Count");
    
    file_withCSVsorted->cd();
    if(Count != NULL) Count->Write();
    auto tree_withCSVsorted = tree->CloneTree(0);
    
    tree_withCSVsorted->Branch("jets_dRmax",     jets_dRmax,    "jets_dRmax[njets]/F"); 
    tree_withCSVsorted->Branch("jets_dRmin",     jets_dRmin,    "jets_dRmin[njets]/F"); 
    tree_withCSVsorted->Branch("jets_dRave",     jets_dRave,    "jets_dRave[njets]/F"); 
    tree_withCSVsorted->Branch("jets_btagCSVsorted",     jets_btagCSVsorted,    "jets_btagCSVsorted[njets]/I"); 
    tree_withCSVsorted->Branch("jets_btagCSVindex",     jets_btagCSVindex,    "jets_btagCSVindex[njets]/I"); 
    tree_withCSVsorted->Branch("jets_btagCorr",     jets_btagCorr,    "jets_btagCorr[njets]/F"); 
    tree_withCSVsorted->Branch("btagCorr",     &btagCorr,    "btagCorr/F"); 

    int nentries = tree->GetEntries();
//    nentries = 1000000; //############
    int i=0;
    tree->GetEntry(i);
    
    vector<pair<float,int> > csv;
    csv.reserve(20);
    for(; i<nentries; i++, tree->GetEntry(i)){
        if(i%1000==0) cout << "Event "<<i<<endl;
        csv.clear();
        for(int i=0; i<njets;i++){
            csv.push_back(pair<float,int> (jets_btagCSV[i],i));
            jets_btagCorr[i] =  btagCorrection(jets_pt[i], jets_eta[i], jets_btagCSV[i]);
            }
        std::sort (csv.begin(), csv.end(), sort_function);
        for(int i=0; i<csv.size();i++) {
            jets_btagCSVsorted[csv[i].second] = i;
            jets_btagCSVindex[i] = csv[i].second;
        }
        btagCorr = 1.;
        for(int i=0; i<njets;i++){
            dphi1 = TVector2::Phi_mpi_pi( jets_phi[csv[0].second] - jets_phi[i]);
            dphi2 = TVector2::Phi_mpi_pi( jets_phi[csv[1].second] - jets_phi[i]);
            deta1 = jets_eta[csv[0].second] - jets_eta[i];
            deta2 = jets_eta[csv[1].second] - jets_eta[i];
            dR1 = sqrt(dphi1*dphi1+deta1*deta1);
            dR2 = sqrt(dphi2*dphi2+deta2*deta2);
            jets_dRmax[i] = std::max(dR1,dR2);
            jets_dRmin[i] = std::min(dR1,dR2);
            jets_dRave[i] = (dR1+dR2)/2;
            
            btagCorr *= jets_btagCorr[i];
        }
        tree_withCSVsorted->Fill();
    }
    file->Close();
    file_withCSVsorted->Write();
    file_withCSVsorted->Close();
}

void pippo(int i){
    cout << "pippo" << endl;
}
void addCSVsorted(string aaa){
    cout << aaa << endl;
//void addCSVsorted(){
    int i; 
    bool toBeFilled;

//    vector<string> fileNames;
//    
//    fileNames.push_back(string("/home/sdonato/CMS/tth/V25_systematics_nBCSVM_CR_v1/JetHT.root"));
//    fileNames.push_back(string("/home/sdonato/CMS/tth/V25_systematics_nBCSVM_CR_v1/JetHT.root"));
//    fileNames.push_back(fileName);
    
//    std::vector<std::future<void> > futures;
//    for(const auto& fileName_: fileNames){
        addCSV(aaa);
//        futures.push_back (std::async(addHMass2, fileName_));
//    }
    
//    for(auto &e : futures) {
//      std::cout << e.get() << std::endl;
//    }
}

