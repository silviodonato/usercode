### This code is used to generate the TWiki such as https://twiki.cern.ch/twiki/bin/view/CMS/HLTinCMSSW80X
releases = [
    "CMSSW_8_0_23",
    "CMSSW_8_0_23_patch1",
    "CMSSW_8_0_23_patch2",
    "CMSSW_8_0_24",
    "CMSSW_8_0_24_patch1",
    "CMSSW_8_0_25",
    "CMSSW_8_0_26",
    "CMSSW_8_0_26_patch1",
    "CMSSW_8_0_26_patch2",
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

print twiki
