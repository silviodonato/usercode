### This code is used to generate the TWiki such as https://twiki.cern.ch/twiki/bin/view/CMS/ConfDB900

import sys

print("python makeConfDBXXXTWiki.py /dev/CMSSW_12_3_0/HLT")
run3=True
condDBbase = sys.argv[1]

from getConfDBdescr import getConfDBdescr
confDBdescr = getConfDBdescr(condDBbase, run3=run3)

### Loop in releases
twiki ="""
---+ !HLT menus in !ConfDB: pp menus for "Run2" in 2016


---++ !HLT Developments in !ConfDB %s
"""%(condDBbase)
for (configuration, description) in confDBdescr:
    ### download the html and parse it
        twiki += "   * =%s=: %s\n"%(configuration,description)

print(twiki)
