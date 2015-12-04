#include "TPad.h"
#include "TCanvas.h"
#include "TLatex.h"
#include "TLine.h"
#include "TBox.h"
#include "TASImage.h"

//
// Global variables
//

TString cmsText     = "CMS";
float cmsTextFont   = 61;  // default is helvetic-bold

float scale = 1;
//scale = 1.5;
bool writeExtraText = true;
TString extraText   = "Preliminary";
float extraTextFont = 52;  // default is helvetica-italics

// text sizes and text offsets with respect to the top frame
// in unit of the top margin size
float lumiTextSize     = 0.6;
float lumiTextOffset   = 0.2;
float cmsTextSize      = 0.75 * scale;
float cmsTextOffset    = 0.1;  // only used in outOfFrame version

float relPosX    = 0.045;
float relPosY    = 0.035;
float relExtraDY = 1.2;

// ratio of "CMS" and extra text size
float extraOverCmsTextSize  = 0.76 * scale;

//TString lumi_13TeV = "40.0 pb^{-1}";
TString lumi_13TeV = "595 pb^{-1}";
TString lumi_8TeV  = "19.7 fb^{-1}";
//TString lumi_7TeV  = "5.1 fb^{-1}";

TString lumi_7TeV  = "40.0 pb^{-1}";

//TString lumi_8TeV  = "";

bool drawLogo      = false;

void CMS_lumi_canvas( TCanvas* pad2, int iPeriod=4, int iPosX=10 );


