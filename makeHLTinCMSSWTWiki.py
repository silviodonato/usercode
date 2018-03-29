### This code is used to generate the TWiki such as https://twiki.cern.ch/twiki/bin/view/CMS/HLTinCMSSW80X

import os

cycle = "CMSSW_9_4_X"
CMSSW_base = "/cvmfs/cms.cern.ch/slc6_amd64_gcc630/cms/cmssw/"
#CMSSW_base = "/cvmfs/cms.cern.ch/slc6_amd64_gcc700/cms/cmssw/"

def getReleases(cycle):
    cycle = cycle.replace("X","")
    releases = os.popen('scram list | grep %s | grep -v X'%(cycle))
    releases = releases.readlines()
    for i in range(len(releases)):
        releases[i] = cycle + releases[i].split(cycle)[1]
        releases[i] = releases[i].split(" ")[0]
        releases[i] = releases[i].split("\n")[0]
    return releases

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

releases = getReleases(cycle)
print(releases)
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

---++++ HLT menus in %s

"""%release
    menus = getMenus(release)
    for menu in menus:
        if not "Fake" in menu:
            twiki += "   * [[https://github.com/cms-sw/cmssw/blob/%s/HLTrigger/Configuration/python/HLT_%s_cff.py][%s]]: %s\n"%(release,menu,menu,confDb(menu,release))
   

print twiki
