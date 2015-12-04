#include"efficiencies_offMet.C"

void DrawHisto(){

  gROOT->LoadMacro("tdrstyleTrigger.C");
  setTDRStyle();

  gROOT->LoadMacro("CMS_lumi.C");
  gStyle->SetFitFormat("2.3f");
//  gROOT->LoadMacro("efficiencies_offMet.C");

   Double_t xAxis1[12] = {0, 63.2, 82.1, 94.05, 104.4, 113.95, 124.8, 137.2, 156.35, 187.9, 349.85, 500}; 

   TH1F *histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff = new TH1F("histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff","",11, xAxis1);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(1,3.169035e-05);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(2,0.002085921);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(3,0.01419126);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(4,0.03651452);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(5,0.08198052);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(6,0.1298851);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(7,0.1577236);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(8,0.2100193);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(9,0.2447059);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(10,0.3133515);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinContent(11,0.2307692);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(1,3.457646e-06);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(2,0.0002208765);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(3,0.001502021);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(4,0.003820735);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(5,0.007815845);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(6,0.01139747);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(7,0.01469732);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(8,0.01787945);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(9,0.02085383);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(10,0.02421308);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetBinError(11,0.1168545);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetMaximum(1.1);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetEntries(2705972);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetStats(0);

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#0000ff");
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetLineColor(ci);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->SetLineWidth(2);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetXaxis()->SetTitle("offMet");
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetXaxis()->SetLabelFont(42);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetXaxis()->SetLabelSize(0.035);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetXaxis()->SetTitleSize(0.035);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetXaxis()->SetTitleFont(42);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetYaxis()->SetTitle("Events");
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetYaxis()->SetLabelFont(42);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetYaxis()->SetLabelSize(0.035);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetYaxis()->SetTitleSize(0.035);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetYaxis()->SetTitleFont(42);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetZaxis()->SetLabelFont(42);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetZaxis()->SetLabelSize(0.035);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetZaxis()->SetTitleSize(0.035);
   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->GetZaxis()->SetTitleFont(42);
//   histo_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v1_eff->Draw("");
   Double_t xAxis2[12] = {0, 63.2, 82.1, 94.05, 104.4, 113.95, 124.8, 137.2, 156.35, 187.9, 349.85, 500}; 
   
   TH1F *histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff = new TH1F("histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff","",11, xAxis2);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(1,2.980402e-05);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(2,0.000445309);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(3,0.004515401);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(4,0.02074689);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(5,0.06412338);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(6,0.1252874);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(7,0.2585366);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(8,0.4412331);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(9,0.6611764);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(10,0.8446866);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(11,0.7692308);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinContent(12,1);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(1,3.353164e-06);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(2,0.0001021381);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(3,0.0008514018);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(4,0.002903457);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(5,0.006979304);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(6,0.01122346);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(7,0.01765502);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(8,0.02179544);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(9,0.0229589);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(10,0.01890685);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetBinError(11,0.1168545);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetMaximum(1.1);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetEntries(2705972);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetStats(0);

   ci = TColor::GetColor("#ff00ff");
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetLineColor(ci);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->SetLineWidth(2);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetXaxis()->SetTitle("offMet");
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetXaxis()->SetLabelFont(42);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetXaxis()->SetLabelSize(0.035);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetXaxis()->SetTitleSize(0.035);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetXaxis()->SetTitleFont(42);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetYaxis()->SetTitle("Events");
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetYaxis()->SetLabelFont(42);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetYaxis()->SetLabelSize(0.035);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetYaxis()->SetTitleSize(0.035);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetYaxis()->SetTitleFont(42);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetZaxis()->SetLabelFont(42);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetZaxis()->SetLabelSize(0.035);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetZaxis()->SetTitleSize(0.035);
   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->GetZaxis()->SetTitleFont(42);
//   histo_HLT_PFMET120_PFMHT120_IDTight_v1_eff->Draw("same");
   Double_t xAxis3[12] = {0, 63.2, 82.1, 94.05, 104.4, 113.95, 124.8, 137.2, 156.35, 187.9, 349.85, 500}; 
   
   TH1F *histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff = new TH1F("histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff","",11, xAxis3);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(1,0.0001211024);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(2,0.007406192);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(3,0.05289469);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(4,0.1352697);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(5,0.2662338);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(6,0.3758621);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(7,0.5382114);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(8,0.6319846);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(9,0.7647059);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(10,0.8555858);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(11,0.8461539);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinContent(12,1);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(1,6.758868e-06);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(2,0.0004150852);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(3,0.002842329);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(4,0.00696678);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(5,0.0125923);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(6,0.01642082);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(7,0.02010298);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(8,0.02116911);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(9,0.02057587);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(10,0.01834863);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetBinError(11,0.1000683);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetMaximum(1.1);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetEntries(2705972);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetStats(0);

   ci = TColor::GetColor("#ff0000");
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetLineColor(ci);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetLineWidth(2);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetXaxis()->SetTitle("offMet");
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetXaxis()->SetLabelFont(42);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetXaxis()->SetLabelSize(0.035);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetXaxis()->SetTitleSize(0.035);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetXaxis()->SetTitleFont(42);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetYaxis()->SetTitle("Events");
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetYaxis()->SetLabelFont(42);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetYaxis()->SetLabelSize(0.035);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetYaxis()->SetTitleSize(0.035);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetYaxis()->SetTitleFont(42);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetZaxis()->SetLabelFont(42);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetZaxis()->SetLabelSize(0.035);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetZaxis()->SetTitleSize(0.035);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetZaxis()->SetTitleFont(42);
//   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->Draw("same");
   Double_t xAxis4[12] = {0, 63.2, 82.1, 94.05, 104.4, 113.95, 124.8, 137.2, 156.35, 187.9, 349.85, 500}; 
   
   TH1F *histo_HLT_PFMET170_NoiseCleaned_v2_eff = new TH1F("histo_HLT_PFMET170_NoiseCleaned_v2_eff","",11, xAxis4);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(1,7.922588e-06);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(2,4.687463e-05);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(3,0.0001612643);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(4,0.0008298755);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(5,0.00487013);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(6,0.009195402);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(7,0.02439024);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(8,0.09826589);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(9,0.3623529);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(10,0.8283378);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(11,0.9230769);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinContent(12,1);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(1,1.728844e-06);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(2,3.314459e-05);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(3,0.0001612513);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(4,0.0005865671);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(5,0.001983375);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(6,0.003236084);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(7,0.006220261);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(8,0.01306643);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(9,0.02331641);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(10,0.01968376);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetBinError(11,0.0739053);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetMaximum(1.1);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetEntries(2705972);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetStats(0);

   ci = TColor::GetColor("#cccc00");
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetLineColor(ci);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetLineWidth(2);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetXaxis()->SetTitle("offMet");
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetXaxis()->SetLabelFont(42);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetXaxis()->SetLabelSize(0.035);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetXaxis()->SetTitleSize(0.035);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetXaxis()->SetTitleFont(42);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetYaxis()->SetTitle("Events");
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetYaxis()->SetLabelFont(42);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetYaxis()->SetLabelSize(0.035);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetYaxis()->SetTitleSize(0.035);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetYaxis()->SetTitleFont(42);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetZaxis()->SetLabelFont(42);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetZaxis()->SetLabelSize(0.035);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetZaxis()->SetTitleSize(0.035);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetZaxis()->SetTitleFont(42);
//   histo_HLT_PFMET170_NoiseCleaned_v2_eff->Draw("same");
   Double_t xAxis5[12] = {0, 63.2, 82.1, 94.05, 104.4, 113.95, 124.8, 137.2, 156.35, 187.9, 349.85, 500}; 
   
   TH1F *histo_All_eff = new TH1F("histo_All_eff","",11, xAxis5);
   histo_All_eff->SetBinContent(1,0.0001260069);
   histo_All_eff->SetBinContent(2,0.007828064);
   histo_All_eff->SetBinContent(3,0.05386228);
   histo_All_eff->SetBinContent(4,0.1377593);
   histo_All_eff->SetBinContent(5,0.2711039);
   histo_All_eff->SetBinContent(6,0.3816092);
   histo_All_eff->SetBinContent(7,0.5430894);
   histo_All_eff->SetBinContent(8,0.6416185);
   histo_All_eff->SetBinContent(9,0.7858824);
   histo_All_eff->SetBinContent(10,0.9100817);
   histo_All_eff->SetBinContent(11,0.9230769);
   histo_All_eff->SetBinContent(12,1);
   histo_All_eff->SetBinError(1,6.894355e-06);
   histo_All_eff->SetBinError(2,0.0004266528);
   histo_All_eff->SetBinError(3,0.002866742);
   histo_All_eff->SetBinError(4,0.007020471);
   histo_All_eff->SetBinError(5,0.01266471);
   histo_All_eff->SetBinError(6,0.01646953);
   histo_All_eff->SetBinError(7,0.02008694);
   histo_All_eff->SetBinError(8,0.02104881);
   histo_All_eff->SetBinError(9,0.01989805);
   histo_All_eff->SetBinError(10,0.01493245);
   histo_All_eff->SetBinError(11,0.0739053);
   histo_All_eff->SetMaximum(1.1);
   histo_All_eff->SetEntries(2705972);
   histo_All_eff->SetStats(0);
   histo_All_eff->SetLineWidth(2);
   histo_All_eff->GetXaxis()->SetTitle("offMet");
   histo_All_eff->GetXaxis()->SetLabelFont(42);
   histo_All_eff->GetXaxis()->SetLabelSize(0.035);
   histo_All_eff->GetXaxis()->SetTitleSize(0.035);
   histo_All_eff->GetXaxis()->SetTitleFont(42);
   histo_All_eff->GetYaxis()->SetTitle("Events");
   histo_All_eff->GetYaxis()->SetLabelFont(42);
   histo_All_eff->GetYaxis()->SetLabelSize(0.035);
   histo_All_eff->GetYaxis()->SetTitleSize(0.035);
   histo_All_eff->GetYaxis()->SetTitleFont(42);
   histo_All_eff->GetZaxis()->SetLabelFont(42);
   histo_All_eff->GetZaxis()->SetLabelSize(0.035);
   histo_All_eff->GetZaxis()->SetTitleSize(0.035);
   histo_All_eff->GetZaxis()->SetTitleFont(42);
//   histo_All_eff->Draw("same");


  int W = 1280;
  int H = 720;
 
  int W_ref = W*1.2;
  int H_ref = H*1.2;

  float T = 0.08*H_ref;
  float B = 0.12*H_ref; 
  float L = 0.12*W_ref;
  float R = 0.04*W_ref;

  TString canvName = "FigExample_";
  canvName += W;
  canvName += "-";
  canvName += H;
  canvName += "_";  
  int iPos=0;
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

//  TH1F *histo_HLT_PFMET170_NoiseCleaned_v2_eff = gDirectory->Get("histo_HLT_PFMET170_NoiseCleaned_v2_eff");
//  TH1F *histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff = gDirectory->Get("histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff");

   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetLineColor(2);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->SetLineWidth(2);
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetXaxis()->SetTitle("MHT(reco)-MHT(gen)/MHT(gen)");
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->GetYaxis()->SetTitle("Events/0.02"); ///2.3
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->Draw("");

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#000099");
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetLineColor(ci);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->SetLineWidth(2);
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->GetXaxis()->SetTitle("(calomht-((Sum$(genjetPt * (genjetPt>20)  * sin(genjetPhi))**2 +Sum$(genjetPt * (genjetPt>20)  * cos(genjetPhi))**2)**0.5))/((Sum$(genjetPt * (genjetPt>20)  * sin(genjetPhi))**2 +Sum$(genjetPt * (genjetPt>20)  * cos(genjetPhi))**2)**0.5)");
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->Draw("same");

   TF1 *fit1 = new TF1("fit1"," 1/(1+exp(-[0]*(x-[1]))) ",120,500);
   fit1->SetLineColor(2);
   fit1->SetLineWidth(2);

   TF1 *fit2 = new TF1("fit2"," 1/(1+exp(-[0]*(x-[1]))) ",120,500);
   fit2->SetLineColor(ci);
   fit2->SetLineWidth(2);

   gStyle->SetOptFit(0110);
  histo_HLT_PFMET170_NoiseCleaned_v2_eff->Fit(fit1,"","",120,500);
  gPad->Update();
  TPaveStats *st1 = ((TPaveStats*)histo_HLT_PFMET170_NoiseCleaned_v2_eff->FindObject("stats"))->Clone("st1");
  st1->GetListOfLines()->RemoveAt(0);
  histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->Fit(fit2,"","",120,500);
  gPad->Update();
  TPaveStats *st2 = ((TPaveStats*)histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->FindObject("stats"))->Clone("st2");
  st2->GetListOfLines()->RemoveAt(0);

  gStyle->SetOptFit(0);

  st1->SetFillStyle(0);
  st1->SetLineColor(2);
  st1->SetTextColor(2);

  st2->SetFillStyle(0);
  st2->SetLineColor(ci);
  st2->SetTextColor(ci);
 
   histo_HLT_PFMET170_NoiseCleaned_v2_eff->Draw("");
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->Draw("same");
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

   histo_HLT_PFMET170_NoiseCleaned_v2_eff->Draw("");
   histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff->Draw("same");
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
    legend->AddEntry(histo_HLT_PFMET170_NoiseCleaned_v2_eff,"cal. MHT online with PU rejection","l");
    legend->AddEntry(histo_HLT_PFMET90_PFMHT90_IDTight_v1_eff,"cal. MHT online","l");
    legend->Draw();
    
    TLatex* preselection = new TLatex(0.3,0.3,"preselection: MHT(gen)>20 GeV");
    preselection->SetTextSize(0.03);
//    preselection->Draw();

    canv->SaveAs("MHTres2.pdf");
    canv->SaveAs("MHTres2.png");
}
