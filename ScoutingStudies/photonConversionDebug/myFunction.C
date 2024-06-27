//using namespace std;

//template <typename aClass>
#include <iostream>    // std::sort
#include <algorithm>    // std::sort
#include <vector>       // std::vector

//aClass myFunction(const aClass& x) {
//   return x;
//}


//float computeMass(float pt, float eta, float phi, float mass, int iteration, int length){
//    using namespace std;
//    float value = 0;
//    if(iteration==0){
//        parts.clear();
//    }
//    TLorentzVector part;
//    part.SetPtEtaPhiM(pt, eta, phi, mass);
//    parts.push_back(part);
//    if(iteration==length-1){
//        if(parts.size()<2) return -1;
//        float maxMass = -1;
//        // Loop over all combinations of pairs of particles
//        for (size_t i = 0; i < parts.size(); ++i) {
//            for (size_t j = i + 1; j < parts.size(); ++j) {
//                // Compute invariant mass using TLorentzVector's method
//                double mass = (parts[i] + parts[j]).M();
//                if (mass > maxMass) {
//                    maxMass = mass;
//                }
//            }
//        }        
//        return maxMass;
//    }
//    else return 0;
//}
 
// Get the Nth object of x, after applying selection and sorting 
std::vector<float> myvect;
float selectNobject(const float x, const bool selection, const unsigned N, const unsigned int iteration, const unsigned int length){
    float value = 0;
    if(iteration==0){
        myvect.clear();
    }
    if (selection){
        myvect.push_back(x);
    }
    // std::cout << "myvect.size() = " << myvect.size() << std::endl;
    if(iteration==length-1){
        if(myvect.size()<=N) 
        {
            return 0;
        }
        sort (myvect.begin(), myvect.end(), std::greater<>());
        return myvect.at(N);
    }
    else return 0; //return Sum$ neutral object (to be used in Draw("Sum$(selectNobject(...))"))
} 

