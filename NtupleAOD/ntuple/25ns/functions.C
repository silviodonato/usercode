#include"TVector2.h"

float SumPt(float pt1, float phi1, float pt2, float phi2){
    if(pt1==pt2 && phi1==phi2)
    {
        return 0;
    }
    else
    {
        return pow(pow(pt1*sin(phi1)+pt2*sin(phi2),2) + pow(pt1*cos(phi1)+pt2*cos(phi2),2),0.5);
//        TVector2 v1,v2;
//        v1.SetMagPhi(pt1,phi1);
//        v2.SetMagPhi(pt2,phi2);
//        return (v1+v2).Mod();
    }
}
