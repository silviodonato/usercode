#include"MyTree.C" //generated with MakeClass in /scratch/dsalerno/tth/80x_M17/V25_lepVetoLoose_systematics_v1/ttHTobb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8.root
#include <TCanvas.h>
#include <TH1F.h>
#include <TLorentzVector.h>
#include <TCanvas.h>
#include <iostream>


TCanvas canv("canv","",1280,720);
TH1F mass("Mass","",100,0,300);
auto part1 = TLorentzVector();
auto part2 = TLorentzVector();

/// common part
void loop(){
    MyTree t;
    t.fChain->SetBranchStatus("*",0);  // disable all branches
    t.fChain->SetBranchStatus("njets",1);  // activate branchname
    t.fChain->SetBranchStatus("jets_pt",1);  // activate branchname
    t.fChain->SetBranchStatus("jets_eta",1);  // activate branchname
    t.fChain->SetBranchStatus("jets_phi",1);  // activate branchname
    t.fChain->SetBranchStatus("jets_mass",1);  // activate branchname
    t.fChain->SetBranchStatus("jets_btagCSV",1);  // activate branchname
    t.fChain->SetBranchStatus("nBCSVM",1);  // activate branchname

    Long64_t nentries = t.fChain->GetEntriesFast();
    Long64_t nbytes = 0, nb = 0;
    for (Long64_t jentry=0; jentry<nentries;jentry++) {
      if(jentry%1000 == 0) std::cout << jentry << std::endl;
      if(jentry>100000) break;
      Long64_t ientry = t.LoadTree(jentry);
      if (ientry < 0) break;
      nb = t.fChain->GetEntry(jentry);   nbytes += nb;
/// end common part
      if(t.nBCSVM!=4) continue;
      for(int i=0; i<t.njets; i++){
          if(t.jets_btagCSV[i]<0.8) continue;
          part1.SetPtEtaPhiM(t.jets_pt[i],t.jets_eta[i],t.jets_phi[i],t.jets_mass[i]);
          for(int j=i+1; i<t.njets; i++){
              if(t.jets_btagCSV[j]<0.8) continue;
              part2.SetPtEtaPhiM(t.jets_pt[j],t.jets_eta[j],t.jets_phi[j],t.jets_mass[j]);
              mass.Fill((part1+part2).M());
          }
      }
    }
    mass.Draw();
    canv.SaveAs("canv.png");
}
