import lhapdf
from data600 import data

trials = 101

pdfSet=lhapdf.getPDFSet("NNPDF23_lo_as_0130_qed")

sigma_mus = []
sqrtS = 13000.


pc = {}
for i in range(trials):
    pc[i] = pdfSet.mkPDF(i)

fx1_fx2_means = []
fx1_fx2_mean = 0.
fx1_fx2_mean2 = 0. 
for i in range(trials):
    fx1_fx2_sum = 0.
    for (p1, pdg1, p2, pdg2) in data[:]:
        x1 = p1/(sqrtS/2)
        x2 = p2/(sqrtS/2)
        Q2 = x1*x2*(sqrtS**2)
        fx1 = pc[i].xfxQ(pdg1, x1, Q2) / x1
        fx2 = pc[i].xfxQ(pdg2, x2, Q2) / x2
        fx1_fx2 = fx1 * fx2
        fx1_fx2_sum += fx1_fx2
        
    fx1_fx2_means.append(fx1_fx2_sum / len(data))

import numpy
arr = numpy.array(fx1_fx2_means)

print arr.std()/arr.mean()
