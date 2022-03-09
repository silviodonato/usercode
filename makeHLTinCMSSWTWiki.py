### This code is used to generate the TWiki such as https://twiki.cern.ch/twiki/bin/view/CMS/HLTinCMSSW80X

import os,sys

if len(sys.argv)<=1:
    print()
    print("python makeHLTinCMSSWTWiki.py CMSSW_12_3_X")
    print()
cycle = sys.argv[1]

def getReleases(cycle):
    cycle = cycle.replace("X","")
    releases = os.popen('scram list --all | grep %s | grep -v X'%(cycle))
    releases = releases.readlines()
    relPaths = []
    for i in range(len(releases)):
        cvmfs = "/cvmfs/"
        if cvmfs in releases[i]:
            releases[i] = releases[i].replace('\n',"")
            path = cvmfs + releases[i].split(cvmfs)[1]
            release = cycle + releases[i].split(cycle)[1]
            relPaths.append((release, path))
    return relPaths

def confDb(menu,path):
#    print('head %s/python/HLTrigger/Configuration/HLT_%s_cff.py -n20 | grep tableName '%(path,menu))
    confDbAdd = os.popen('head %s/python/HLTrigger/Configuration/HLT_%s_cff.py  -n20 | grep tableName '%(path,menu))
    try:
        confDbAdd = confDbAdd.readlines()[0].split("'")[1]
    except:
        confDbAdd = "none"
#    print(menu,confDbAdd)
    return confDbAdd

def getMenus(path):
    menus = os.popen('ls '+path+'/python/HLTrigger/Configuration/  | grep HLT_ | grep -v ".pyc" | grep _cff ')
    menus = menus.readlines()
    for i in range(len(menus)):
        menus[i] = menus[i].replace("HLT_","")
        menus[i] = menus[i].replace("_cff.py\n","")
#    print(menus)
    return menus

releases = getReleases(cycle)
rels = set()
for i in reversed(list(range(len(releases)))):
    if releases[i][0] in rels:
        releases.remove(releases[i])
    else:
        rels.add(releases[i][0])
        releases[i] = (releases[i][0].replace("_pre","_apre"), releases[i][1])
        releases[i] = (releases[i][0].replace("_patch","_zpatch"), releases[i][1])
        if releases[i][0][-2:] == "_0": 
            releases[i] = (releases[i][0] + "_final",releases[i][1])
        if len(releases[i][0].split("_")[3]) == 1: 
            nums = releases[i][0].split("_")
            nums[3] = "0"+nums[3]
            releases[i] = ('_'.join(nums) ,releases[i][1])

releases.sort()
releases.reverse()
#print(releases)

for i in reversed(list(range(len(releases)))):
    cycle_ = cycle.replace("X","")
    releases[i] = (releases[i][0].replace(cycle_+"0",cycle_), releases[i][1])
    releases[i] = (releases[i][0].replace("_0_final","_0"), releases[i][1])
    releases[i] = (releases[i][0].replace("final",""), releases[i][1])
    releases[i] = (releases[i][0].replace("_apre","_pre"), releases[i][1])
    releases[i] = (releases[i][0].replace("_zpatch","_patch"), releases[i][1])

#print(releases)

### Define the HTML parser class. We use it to simply transform the html in a string without tags (MyHTMLParser.text)
import urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser
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
twiki = """
---+ !HLT menus in the %s release serie

%%TOC%%

---++ !HLT Developments in !ConfDB

  (See https://twiki.cern.ch/twiki/bin/view/CMS/SoftToolsOnlRelMenus#HLT_menus_in_CMSSW_releases)

---++ !HLT developments in !CMSSW

---+++ !Schedule of %s (pre)-releases

A draft of the official !CMSSW schedule for %s is maintained in
[[%%SCRIPTURL{"view"}%%auth/CMS/%s][https://twiki.cern.ch/twiki/bin/viewauth/CMS/%s]]

"""%(cycle,cycle,cycle,cycle.replace("_X","_0"),cycle.replace("_X","_0"))


for release,path in releases[:]:
    ### download the html and parse it
    #print(release)
    response = urllib.request.urlopen('https://github.com/cms-sw/cmssw/releases/%s'%release)
    mfile = response.read()

    parser = MyHTMLParser()
    parser.feed(str(mfile))
    PRs = {}
    ### parse the text to get: 1) the old relase 2) the PR number 3) the PR description of the PR related to the trigger
    for line in parser.text.split("\\n"):
#        print("deb", line)
        if "Changes since " in line:
            oldRelease = line.split("Changes since ")[1][:-1].split(":")[0]
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
    for pr in sorted(list(PRs.keys()),reverse=True):
        twiki += "   * [[https://github.com/cms-sw/cmssw/pull/%s][#%s]]: %s\n"%(pr,pr,PRs[pr])
    twiki +="""

---++++ HLT menus in %s

"""%release
    menus = getMenus(path)
    for menu in menus:
        if not "Fake" in menu:
            twiki += "   * [[https://github.com/cms-sw/cmssw/blob/%s/HLTrigger/Configuration/python/HLT_%s_cff.py][%s]]: %s\n"%(release,menu,menu,confDb(menu,path))
   

print(twiki)
