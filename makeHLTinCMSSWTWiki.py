import os

CMSSW_base = "/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/"

def confDb(menu,release):
    confDbAdd = os.popen('head /cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/%s/python/HLTrigger/Configuration/HLT_%s_cff.py  | grep tableName '%(release,menu))
    confDbAdd = confDbAdd.readlines()[0].split("'")[1]
#    print(menu,confDbAdd)
    return confDbAdd

def getMenus(release):
    menus = os.popen('ls '+CMSSW_base+'%s/python/HLTrigger/Configuration/  | grep HLT_ | grep -v ".pyc" | grep _cff '%release)
    menus = menus.readlines()
    for i in range(len(menus)):
        menus[i] = menus[i].replace("HLT_","")
        menus[i] = menus[i].replace("_cff.py\n","")
#    print(menus)
    return menus

### This code is used to generate the TWiki such as https://twiki.cern.ch/twiki/bin/view/CMS/HLTinCMSSW80X

releases = [
    #"CMSSW_9_4_0_pre1",
    #"CMSSW_9_4_0_pre2",
    #"CMSSW_9_4_0_pre3",
    #"CMSSW_9_4_0",
    #"CMSSW_9_4_0_patch1",
    #"CMSSW_9_4_1",
    #"CMSSW_9_4_2",
    #"CMSSW_9_4_3",
    #"CMSSW_9_4_4",

    #"CMSSW_9_3_0_pre1",
    #"CMSSW_9_3_0_pre2",
    #"CMSSW_9_3_0_pre3",
    #"CMSSW_9_3_0_pre4",
    #"CMSSW_9_3_0_pre5",
    #"CMSSW_9_3_0",
    #"CMSSW_9_3_1",
    #"CMSSW_9_3_2",
    #"CMSSW_9_3_3",
    #"CMSSW_9_3_4",
    #"CMSSW_9_3_5",
    #"CMSSW_9_3_6",
    #"CMSSW_9_3_6_patch1",

    "CMSSW_10_0_0_pre1",
    "CMSSW_10_0_0_pre2",
    "CMSSW_10_0_0_pre3",
    "CMSSW_10_0_0_pre1",
    "CMSSW_10_0_0",
    "CMSSW_10_0_1",
    "CMSSW_10_0_2",
    "CMSSW_10_0_3",
    "CMSSW_10_0_4",
    "CMSSW_10_0_5",
    
    #"CMSSW_10_1_0_pre1",
    #"CMSSW_10_1_0_pre2",
    #"CMSSW_10_1_0_pre3",
    #"CMSSW_10_1_0_pre4",
    #"CMSSW_10_1_0_pre5",
    #"CMSSW_10_1_0",
]
releases.reverse()

### Define the HTML parser class. We use it to simply transform the html in a string without tags (MyHTMLParser.text)
import urllib2
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    HTMLParser.text = ""
    HTMLParser.currentTags = []
    def handle_starttag(self, tag, attrs):
        self.currentTags.append(tag)
#        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        el = self.currentTags.pop()
        if el!=tag:
            Exception("parsing error. El = %s, Tag = %s"%(el,tag))
#        print "Encountered an end tag :", tag

    def handle_data(self, data):
        if len(self.currentTags)>0 and self.currentTags[-1] == "code":
            self.text +="["+data+"]"
        else:
            self.text +=data
#        print data,
#        print "Encountered some data  :", data,self.currentTags

### Loop in releases
twiki = ""
for release in releases:
    ### download the html and parse it
    response = urllib2.urlopen('https://github.com/cms-sw/cmssw/releases/%s'%release)
    mfile = response.read()

    parser = MyHTMLParser()
    parser.feed(mfile)
    PRs = {}
    ### parse the text to get: 1) the old relase 2) the PR number 3) the PR description of the PR related to the trigger
    for line in parser.text.split("\n"):
        if "Changes since " in line:
            oldRelease = line.split("Changes since ")[1][:-1]
        if len(line)>0 and line[0] is "#":
            line_ = line.lower()
            if "hlt" in line or "trigger" in line or "l1" in line:
                line = line.replace("]  [",",")
                PRnum = int(line[1:6])
                PRtext = line[line.find(":")+2:]
                for i in range(len(PRtext)):
                    if PRtext[i].isupper() and (i==0 or PRtext[i-1]==" "):
                        PRtext = PRtext[:i]+"!"+PRtext[i:]
                PRs[PRnum] = PRtext
    
### print the text to be added to https://twiki.cern.ch/twiki/bin/view/CMS/HLTinCMSSW80X, using the Wiki text format
    twiki +="""
---+++ %s

---++++ CMSSW code changes potentially relevant to HLT in %s with respect to %s

[[https://github.com/cms-sw/cmssw/releases/%s][Release notes]] for !%s
"""%(release,release,oldRelease,release,release)
    for pr in sorted(PRs.keys(),reverse=True):
        twiki += "   * [[https://github.com/cms-sw/cmssw/pull/%s][#%s]]: %s\n"%(pr,pr,PRs[pr])
    twiki +="""

---++++ HLT menus in CMSSW_10_0_4

"""
    menus = getMenus(release)
    for menu in menus:
        if not "Fake" in menu:
            twiki += "   * [[https://github.com/cms-sw/cmssw/blob/CMSSW_10_0_4/HLTrigger/Configuration/python/HLT_%s_cff.py][%s]]: %s\n"%(menu,menu,confDb(menu,release))
   

print twiki
