import lhapdf
from data import data

trials = 101

pdfSet=lhapdf.getPDFSet("NNPDF23_lo_as_0130_qed")

sigma_mus = []
sqrtS = 13000.


pc = {}
for i in range(trials):
    pc[i] = pdfSet.mkPDF(i)

for (p1, pdg1, p2, pdg2) in data:
    pass
    
    x1 = p1/(sqrtS/2)
    x2 = p2/(sqrtS/2)
    Q2 = x1*x2*(sqrtS**2)
    fx1_fx2_mean = 0.
    fx1_fx2_mean2 = 0. 
    for i in range(trials):
        fx1 = pc[i].xfxQ(pdg1, x1, Q2) / x1
        fx2 = pc[i].xfxQ(pdg2, x2, Q2) / x2
        fx1_fx2 = fx1 * fx2
        fx1_fx2_mean += fx1_fx2 / trials
        fx1_fx2_mean2 += fx1_fx2*fx1_fx2 / trials
        print(fx1_fx2)

    sigma_mu = ( fx1_fx2_mean2 / fx1_fx2_mean / fx1_fx2_mean - 1. )**0.5

    print(fx1_fx2_mean)
    print(fx1_fx2_mean2)
    print(fx1_fx2_mean2 / fx1_fx2_mean / fx1_fx2_mean)
    print(sigma_mu)
    if sigma_mu<1:
        sigma_mus.append(sigma_mu)


for sigma_mu in sigma_mus:
    print sigma_mu

print sum(sigma_mus)/len(sigma_mus)

