'''
 This script forces the normalization of each MC in VR+CR to be to be equal to systDown (QGL weight down) case.
 It has been made to avoid that QGL weight change the normalization of our MCs.
 Here we assume that QGL weight down corresponds to no QGL correction.
'''

import ROOT

fileNameSR = "merged_SR.root"
fileNameVR = "merged_VR.root"

fileNameCR = "merged_CR.root"
fileNameCR2 = "merged_CR2.root"

####################################################################################
####  IMPORTANT: replace CMS_ttH_CSVjesPileUpPtEC1 with QGL weight up & down!! #####
####################################################################################

systDown = "CMS_ttH_CSVjesPileUpPtEC1Down"
systUp = "CMS_ttH_CSVjesPileUpPtEC1Up"

def doFiles(fileNameSR, fileNameVR):
    print "File %s and %s"%(fileNameSR,fileNameVR)
    fileSR = ROOT.TFile(fileNameSR)
    fileVR = ROOT.TFile(fileNameVR)
    
    samples = set()
    categories = set()
    variables = set()
    scv = set() # set of (sample, category, variable)
    
    ## Get sample, category, and variable sets
    for histo in fileSR.GetListOfKeys():
        (sample,category,variable) = histo.GetTitle().split("__")[:3]
        if(sample!="data"):
            samples.add(sample)
            categories.add(category)
            variables.add(variable)
            scv.add((sample,category,variable))
    
    print
    print "I've found ..."
    print "Samples: ", samples
    print "Categories: ", categories
    print "Variables: ", variables
    print
    
    ## Compute the correction
    
    corrNominal = {}
    corrUp = {}
    for (sample,category,variable) in scv:
        histoName = "%s__%s__%s"%(sample,category,variable)
        yield_nominal = fileSR.Get(histoName).Integral() + fileVR.Get(histoName).Integral()
        yield_down = fileSR.Get(histoName+"__"+systDown).Integral() + fileVR.Get(histoName+"__"+systDown).Integral()
        yield_up = fileSR.Get(histoName+"__"+systUp).Integral() + fileVR.Get(histoName+"__"+systUp).Integral()
        
        corrNominal [(sample,category,variable)] = 1. * yield_down / yield_nominal
        corrUp [(sample,category,variable)]      = 1. * yield_down / yield_up
        
        if (sample,category,variable) == ("diboson","fh_j9_t4","mem_FH_4w2h2t_p"):
            print "yield_up=",yield_up
            print "yield_down=",yield_down
            print "yield_nominal=",yield_nominal
    
    print "corrNominal=",corrNominal [("diboson","fh_j9_t4","mem_FH_4w2h2t_p")]
    print "corrUp=",corrUp [("diboson","fh_j9_t4","mem_FH_4w2h2t_p")]
    ## Write the new file
    
    aaa = None
    sampleOld = ""
    for file_ in [fileSR,fileVR]:
        filePath = file_.GetName()
        newFile = ROOT.TFile(filePath.replace(".root","_new.root"),"recreate")
        for histo in file_.GetListOfKeys():
            histo = histo.ReadObj()
            syst = ""
            words = histo.GetTitle().split("__")
            if len(words)>=4:
                (sample,category,variable,syst) = words[0:4]
            else:
                (sample,category,variable) = words[0:3]
            if sampleOld != sample: 
                sampleOld = sample
                print sample 
            if (sample,category,variable) in corrNominal:
                if syst == systDown:
                    pass
                elif syst == systUp:
                    histo.Scale(corrUp[(sample,category,variable)])
                else:
                    histo.Scale(corrNominal[(sample,category,variable)])
            histo.Write()
        newFile.Close()
        file_.Close()
        print
        print "Done"
        print

doFiles(fileNameSR, fileNameVR)
doFiles(fileNameCR, fileNameCR2)

#CMS_ttH_CSVhfstats1Up
#CMS_ttH_CSVhfstats1Down


#diboson__fh_j9_t4__mem_FH_4w2h2t_p__CMS_ttH_CSVjesPileUpPtEC1Down

#set(['ttz', 'ttH_hbb', 'diboson', 'ttbarPlusB', 'ttw', 'ttH_nonhbb', 'stop', 'ttbarPlusCCbar', 'wjets', 'ttbarPlus2B', 'ttbarOther', 'qcd', 'ttbarPlusBBbar', 'zjets', 'data'])
#set(['fh_j7_t4', 'fh_j7_t3', 'fh_j8_t3', 'fh_j8_t4', 'fh_j9_t4', 'fh_j9_t3'])
#set(['mem_FH_3w2h2t_p', 'jetsByPt_0_pt', 'mem_FH_4w2h2t_p', 'ht', 'mem_FH_4w2h1t_p'])

