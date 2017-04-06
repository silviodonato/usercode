#!/usr/bin/env python
import os
#import PhysicsTools.HeppyCore.framework.config as cfg
#cfg.Analyzer.nosubdir=True

import PSet
import sys
import re

import shlex
from subprocess import Popen, PIPE
def launch(cmd):
    process = Popen(shlex.split(cmd), stdout=PIPE)
    output = process.communicate() #output
    exit_code = process.wait()
    return exit_code

print "ARGV:",sys.argv
JobNumber=sys.argv[1]
crabFiles=PSet.process.source.fileNames
maxEvents=int(PSet.process.maxEvents.input.value())
if maxEvents<0:
    maxEvents = 1000000000
if len(crabFiles)==0:
    crabFiles=[
         "root://eoscms.cern.ch//eos/cms/store/mc/PhaseIFall16DR/GluGluToRSGravitonToHHTo4B_M-450_narrow_13TeV-madgraph/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/80000/EAACC9D6-0F11-E711-A9B1-FA163EDAFEAB.root",
    ]
print "crabFiles before: ",crabFiles
print "--------------- using edmFileUtil to convert PFN to LFN -------------------------"
sequence = range(0,len(crabFiles))
sequence.reverse()
for i in sequence :
     if os.getenv("GLIDECLIENT_Group","") != "overflow" :
       print "Data is local"
       pfn=os.popen("edmFileUtil -d %s"%(crabFiles[i])).read() 
       pfn=re.sub("\n","",pfn)
       print crabFiles[i],"->",pfn
       crabFiles[i]=pfn
     else:
       print "Data is not local, using AAA/xrootd"
       crabFiles[i]="root://cms-xrd-global.cern.ch/"+crabFiles[i]
       print crabFiles[i],
       exit_code = launch("edmFileUtil "+crabFiles[i])
       if exit_code != 0:
            print "REMOVED"
            del crabFiles[i]
       
#for i in sequence :
#     pfn=os.popen("edmFileUtil -d %s"%(crabFiles[i])).read() 
#     pfn=re.sub("\n","",pfn)
#     print crabFiles[i],"->"
##     crabFiles[i]=pfn ##un-comment me!!
##     crabFiles[i]="root://xrootd-cms.infn.it/"+crabFiles[i] 
#     exit_code = launch("edmFileUtil "+pfn)
#     if exit_code == 0:
#        crabFiles[i] = pfn
#        print crabFiles[i],
#     else:
#        crabFiles[i]="root://cms-xrd-global.cern.ch//"+crabFiles[i] ##comment me!!
#        exit_code = launch("edmFileUtil "+crabFiles[i])
#        print crabFiles[i],
#     if exit_code != 0:
#        print "REMOVED"
#        del crabFiles[i]
#    
#     print
#     launch("edmEventSize -v A262C860-5626-E511-A401-02163E0134C6.root")

if len(crabFiles)>0:
    firstInput = crabFiles[0]
else:
    firstInput = "emptyFile"
print "crabFiles after: ",crabFiles

from fwlite_config import *
import imp
handle = open("fwlite_config.py", 'r')
cfo = imp.load_source("config", "fwlite_config.py", handle)
#config = cfo.config
handle.close()

##replace files with crab ones
#config.components[0].files=crabFiles

launchNtupleFromHLT("tree.root",crabFiles,maxEvents)

#from PhysicsTools.HeppyCore.framework.looper import Looper
#looper = Looper( 'Output', config, nPrint = 1)
#looper.loop()
#looper.write()

#print PSet.process.output.fileName
#os.system("ls -lR")
try:
    os.rename("Output/tree.root", "tree.root")
except:
    pass
#os.system("ls -lR")

import ROOT
try:
    f=ROOT.TFile.Open('tree.root')
    entries=f.Get('tree').GetEntries()
except:
    entries=0

fwkreport='''<FrameworkJobReport>
<ReadBranches>
</ReadBranches>
<PerformanceReport>
  <PerformanceSummary Metric="StorageStatistics">
    <Metric Name="Parameter-untracked-bool-enabled" Value="true"/>
    <Metric Name="Parameter-untracked-bool-stats" Value="true"/>
    <Metric Name="Parameter-untracked-string-cacheHint" Value="application-only"/>
    <Metric Name="Parameter-untracked-string-readHint" Value="auto-detect"/>
    <Metric Name="ROOT-tfile-read-totalMegabytes" Value="0"/>
    <Metric Name="ROOT-tfile-write-totalMegabytes" Value="0"/>
  </PerformanceSummary>
</PerformanceReport>
<GeneratorInfo>
</GeneratorInfo>
<InputFile>
<LFN>%s</LFN>
<PFN></PFN>
<Catalog></Catalog>
<InputType>primaryFiles</InputType>
<ModuleLabel>source</ModuleLabel>
<GUID></GUID>
<InputSourceClass>PoolSource</InputSourceClass>
<EventsRead>1</EventsRead>
</InputFile>
<File>
<LFN></LFN>
<PFN>tree.root</PFN>
<Catalog></Catalog>
<ModuleLabel>HEPPY</ModuleLabel>
<GUID></GUID>
<OutputModuleClass>PoolOutputModule</OutputModuleClass>
<TotalEvents>%s</TotalEvents>
<BranchHash>dc90308e392b2fa1e0eff46acbfa24bc</BranchHash>
</File>
</FrameworkJobReport>''' % (firstInput,entries)

f1=open('./FrameworkJobReport.xml', 'w+')
f1.write(fwkreport)
