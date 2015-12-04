{
// -.25 , .4
// -.3 , .45


  gROOT->LoadMacro("tdrstyleTrigger.C");
  setTDRStyle();

  gROOT->LoadMacro("CMS_lumi.C");
//  gStyle->SetOptStat(0);
//  gStyle->SetStatFormat("6.1g");
//  gStyle->SetOptFit(0);
  gStyle->SetFitFormat("2.3f");
  
//  int W = 800;
//  int H = 600;

  int W = 1280;
  int H = 720;

  // 
  // Simple example of macro: plot with CMS name and lumi text
  //  (this script does not pretend to work in all configurations)
  // iPeriod = 1*(0/1 7 TeV) + 2*(0/1 8 TeV)  + 4*(0/1 13 TeV) 
  // For instance: 
  //               iPeriod = 3 means: 7 TeV + 8 TeV
  //               iPeriod = 7 means: 7 TeV + 8 TeV + 13 TeV 
  // Initiated by: Gautier Hamel de Monchenault (Saclay)
  //
//  int H_ref = 600; 
//  int W_ref = 800; 
 
  int W_ref = W*1.2;
  int H_ref = H*1.2;

  // references for T, B, L, R
  float T = 0.08*H_ref;
  float B = 0.12*H_ref; 
  float L = 0.12*W_ref;
  float R = 0.04*W_ref;

  TString canvName = "FigExample_";
  canvName += W;
  canvName += "-";
  canvName += H;
  canvName += "_";  
//  canvName += iPeriod;
  int iPos=0;
//  if( writeExtraText ) canvName += "-prelim";
  if( iPos%10==0 ) canvName += "-out";
  else if( iPos%10==1 ) canvName += "-left";
  else if( iPos%10==2 )  canvName += "-center";
  else if( iPos%10==3 )  canvName += "-right";

  TCanvas* canv = new TCanvas(canvName,canvName,50,50,W,H);
  canv->SetFillColor(0);
  canv->SetBorderMode(0);
  canv->SetFrameFillStyle(0);
  canv->SetFrameBorderMode(0);
  canv->SetLeftMargin( L/W );
  canv->SetRightMargin( R/W );
  canv->SetTopMargin( T/H );
  canv->SetBottomMargin( B/H );
  canv->SetTickx(0);
  canv->SetTicky(0);
   
//    TFile *_file0 = TFile::Open("/home/sdonato/CMS/NtupleHLT/MET_PU40BX25/ntuplaZnnHbb.root");
    TFile *_file0 = TFile::Open("/home/sdonato/CMS/NtupleHLT/V3_MET/ntuple3_ZnnHbb_L1METSkim.root");
    s->cd();
//    tree->Draw("(Sum$(caloNoPUjetPt * (caloNoPUjetPt>20) * (abs(caloNoPUjetEta)<2.4) ) -Sum$(genjetPt * (genjetPt>20) * (abs(genjetEta)<2.4) ))/Sum$(caloNoPUjetPt * (caloNoPUjetPt>20) * (abs(caloNoPUjetEta)<2.4) ) >> htemp__1(100,-1,1)","Sum$(caloNoPUjetPt * (caloNoPUjetPt>20) * (abs(caloNoPUjetEta)<2.4) )>0");
//    tree->Draw("(Sum$(calojetPt * (calojetPt>20) * (abs(calojetEta)<2.4) ) -Sum$(genjetPt * (genjetPt>20) * (abs(genjetEta)<2.4) ))/Sum$(calojetPt * (calojetPt>20) * (abs(calojetEta)<2.4) ) >> htemp__2(100,-1,1)","Sum$(caloNoPUjetPt * (caloNoPUjetPt>20) * (abs(caloNoPUjetEta)<2.4) )>0");

    tree->Draw("(caloNoPUmht-((Sum$(genjetPt * (genjetPt>20)  * sin(genjetPhi))**2 +Sum$(genjetPt * (genjetPt>20)  * cos(genjetPhi))**2)**0.5))/caloNoPUmht >> htemp__1(100,-1,1)","caloNoPUmht!=0 && ((Sum$(genjetPt * (genjetPt>20)  * sin(genjetPhi))**2 +Sum$(genjetPt * (genjetPt>20)  * cos(genjetPhi))**2)**0.5)>20");
    tree->Draw("(calomht-((Sum$(genjetPt * (genjetPt>20)  * sin(genjetPhi))**2 +Sum$(genjetPt * (genjetPt>20)  * cos(genjetPhi))**2)**0.5))/calomht >> htemp__2(100,-1,1)","caloNoPUmht!=0 && ((Sum$(genjetPt * (genjetPt>20)  * sin(genjetPhi))**2 +Sum$(genjetPt * (genjetPt>20)  * cos(genjetPhi))**2)**0.5)>20");
    
    TH1F *htemp__1 = gDirectory->Get("htemp__1");
    TH1F *htemp__2 = gDirectory->Get("htemp__2");

   htemp__1->SetLineColor(2);
   htemp__1->SetLineWidth(2);
   htemp__1->GetXaxis()->SetTitle("MHT(reco)-MHT(gen)/MHT(gen)");
   htemp__1->GetYaxis()->SetTitle("Events/0.02"); ///2.3
   htemp__1->Draw("");

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#000099");
   htemp__2->SetLineColor(ci);
   htemp__2->SetLineWidth(2);
   htemp__2->GetXaxis()->SetTitle("(calomht-((Sum$(genjetPt * (genjetPt>20)  * sin(genjetPhi))**2 +Sum$(genjetPt * (genjetPt>20)  * cos(genjetPhi))**2)**0.5))/((Sum$(genjetPt * (genjetPt>20)  * sin(genjetPhi))**2 +Sum$(genjetPt * (genjetPt>20)  * cos(genjetPhi))**2)**0.5)");
   htemp__2->Draw("same");

   TF1 *fit1 = new TF1("fit1","gaus",-0.25,0.45);
   fit1->SetLineColor(2);
   fit1->SetLineWidth(2);

   TF1 *fit2 = new TF1("fit2","gaus",-0.2,0.6);
   fit2->SetLineColor(ci);
   fit2->SetLineWidth(2);

   gStyle->SetOptFit(0110);
  htemp__1->Fit(fit1,"","",-.25,.45);
  gPad->Update();
  TPaveStats *st1 = ((TPaveStats*)htemp__1->FindObject("stats"))->Clone("st1");
  st1->GetListOfLines()->RemoveAt(0);
  htemp__2->Fit(fit2,"","",-.2,.6);
  gPad->Update();
  TPaveStats *st2 = ((TPaveStats*)htemp__2->FindObject("stats"))->Clone("st2");
  st2->GetListOfLines()->RemoveAt(0);

  gStyle->SetOptFit(0);

  st1->SetFillStyle(0);
  st1->SetLineColor(2);
  st1->SetTextColor(2);

  st2->SetFillStyle(0);
  st2->SetLineColor(ci);
  st2->SetTextColor(ci);
 
   htemp__1->Draw("");
   htemp__2->Draw("same");
   fit1->Draw("same");
   fit2->Draw("same");

  float delta_x = 0;
  float delta_y = 0;
  delta_x = 0.17 - st1->GetX1NDC();
  delta_y = 0.62 - st1->GetY1NDC();
  float width_x = 0.2;
  float width_y = 0.1;
  st1->SetX1NDC(st1->GetX1NDC()+delta_x);
  st1->SetX2NDC(st1->GetX1NDC()+width_x);
  st1->SetY1NDC(st1->GetY1NDC()+delta_y);
  st1->SetY2NDC(st1->GetY1NDC()+width_y);

  delta_x = 0.17 - st2->GetX1NDC();
  delta_y = 0.51 - st2->GetY1NDC();
  st2->SetX1NDC(st2->GetX1NDC()+delta_x);
  st2->SetX2NDC(st2->GetX1NDC()+width_x);
  st2->SetY1NDC(st2->GetY1NDC()+delta_y);
  st2->SetY2NDC(st2->GetY1NDC()+width_y);

  st1->Draw("same");
  st2->Draw("same");


  st1->Draw("same");
  st2->Draw("same");

   htemp__1->Draw("");
   htemp__2->Draw("same");
   fit1->Draw("same");
   fit2->Draw("same");

  st1->Draw("same");
  st2->Draw("same");

  TString lumi_7TeV  = "Z(vv)H(bb), MHT(gen)>20GeV, 13 TeV, PU40, 25 ns ";
  CMS_lumi(gPad);
  
    TLegend* legend = new TLegend(0.62,0.72,0.96,0.9);
    legend->SetFillStyle(0);
    legend->SetLineStyle(0);
    legend->SetLineWidth(0);
    legend->SetBorderSize(0);
    legend->AddEntry(htemp__1,"cal. MHT online with PU rejection","l");
    legend->AddEntry(htemp__2,"cal. MHT online","l");
    legend->Draw();
    
    TLatex* preselection = new TLatex(0.3,0.3,"preselection: MHT(gen)>20 GeV");
    preselection->SetTextSize(0.03);
//    preselection->Draw();

    canv->SaveAs("MHTres2.pdf");
    canv->SaveAs("MHTres2.png");
}
