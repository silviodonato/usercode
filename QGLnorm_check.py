'''
 This script checks the good behaviour of "QGLnorm.py".
'''

import ROOT

fileNameSR = "merged_SR.root"
fileNameVR = "merged_VR.root"

fileNameCR = "merged_CR.root"
fileNameCR2 = "merged_CR2.root"

####################################################################################
####  IMPORTANT: replace CMS_ttH_CSVjesPileUpPtEC1 with QGL weight up & down!! #####
####################################################################################

systDown = "CMS_ttH_CSVjesPileUpPtEC1Down" ## I assume down = no QGL correction
systUp = "CMS_ttH_CSVjesPileUpPtEC1Up"

def doFiles(fileNameSR, fileNameVR):
    print 
    print fileNameSR,fileNameVR
    fileSR = ROOT.TFile(fileNameSR)
    fileVR = ROOT.TFile(fileNameVR)
    
    print "Nominal: ",fileSR.Get("diboson__fh_j9_t4__mem_FH_4w2h2t_p").Integral()+fileVR.Get("diboson__fh_j9_t4__mem_FH_4w2h2t_p").Integral()
    print "Down: ",fileSR.Get("diboson__fh_j9_t4__mem_FH_4w2h2t_p__CMS_ttH_CSVjesPileUpPtEC1Down").Integral()+fileVR.Get("diboson__fh_j9_t4__mem_FH_4w2h2t_p__CMS_ttH_CSVjesPileUpPtEC1Down").Integral()
    print "Up: ",fileSR.Get("diboson__fh_j9_t4__mem_FH_4w2h2t_p__CMS_ttH_CSVjesPileUpPtEC1Up").Integral()+fileVR.Get("diboson__fh_j9_t4__mem_FH_4w2h2t_p__CMS_ttH_CSVjesPileUpPtEC1Up").Integral()
    print "data: ",fileSR.Get("data__fh_j9_t4__mem_FH_4w2h2t_p").Integral()+fileVR.Get("data__fh_j9_t4__mem_FH_4w2h2t_p").Integral()


doFiles("merged_SR.root","merged_VR.root")
doFiles("merged_SR_new.root","merged_VR_new.root")

doFiles("merged_CR.root","merged_CR2.root")
doFiles("merged_CR_new.root","merged_CR2_new.root")
