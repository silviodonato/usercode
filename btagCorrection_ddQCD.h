
#include<algorithm>

float btagCorrection(float pt, float eta, float csv){
    if(csv<0.542600 || csv>0.848400) return 1;
    else return (2.80676-0.0317586*pow(eta,1)-0.410152*pow(eta,2)+0.00368126*pow(eta,3)-0.107052*pow(eta,4)-0.000799443*pow(eta,5)+0.058918*pow(eta,6)-9.85038e-06*pow(eta,7)-0.00659241*pow(eta,8))*((87.2275-0.000799443*pt)*erf((pt+293.834)*0.00666484)-86.6398);
}
