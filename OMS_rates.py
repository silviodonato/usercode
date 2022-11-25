#!/usr/bin/env python

""" Get maximum rate of L1 trigger algo bits
Taken from https://gitlab.cern.ch/cmsoms/oms-api-client/-/blob/master/examples/06-get-max-rate-l1trigger-bit.py
"""

from __future__ import print_function
import sys
import os
import argparse
import re
import ROOT
from array import array

trigger = "L1_Mu18er2p1_Tau24er2p1"
doL1 = False
minLS = 0
maxLS = 5000
maxHLTPaths = 5000

if not os.path.exists( os.getcwd() + 'omsapi.py' ):
    sys.path.append('..')  # if you run the script in the more-examples sub-folder 
from omsapi import OMSAPI

parser = argparse.ArgumentParser( 
    description='python script using OMS API to get maximum rate of L1 trigger algos', 
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

parser.add_argument( 'run', type = int, help = 'run for which rates should be retrieved' )
#group = parser.add_mutually_exclusive_group(required=True)
#group.add_argument( '--pattern', help = 'regexp pattern for algos for which max rate will be retrieved, example: ".*EG.*"' )
#group.add_argument( '--algo', help = 'name of algorithm for which max rate will be retrieved' )
#group.add_argument( '--bits', nargs='+', help = 'list of algo bits for which max rate will be retrieved')

args = parser.parse_args()

#omsapi = OMSAPI('http://cmsoms.cms/agg/api/','v1', cert_verify=False)
omsapi = OMSAPI("https://cmsoms.cern.ch/agg/api", "v1")
#cern-get-sso-cookie -u https://cmsoms.cern.ch/cms/fills/summary -o ssocookies.txt
omsapi.auth_krb()


l1BitMap = {}
l1Bits = []

### Init root file
f = ROOT.TFile(str(args.run)+".root","recreate")
tree = ROOT.TTree("tree","tree")

triggerCounts = {}
### Define tree variables, option https://root.cern.ch/doc/master/classTTree.html 
def SetVariable(tree,name,option='F',lenght=1,maxLenght=100):
    if option is 'F': arraytype='f'
    elif option is 'O': arraytype='i'
    elif option is 'I': arraytype='i'
    else:
        print('option ',option,' not recognized.')
        return

    if not type(lenght) is str:
        maxLenght = lenght
        lenght = str(lenght)
    variable = array(arraytype,[0]*maxLenght)
    if maxLenght>1: name = name + '['+lenght+']'
    tree.Branch(name,variable,name+'/'+option)
    return variable

lumi = SetVariable(tree,"lumi",'I',1)
run = SetVariable(tree,"run",'I',1)

#print(l1BitMap)

###############################################


hltBitMap = {}
hltBits = []

query = omsapi.query("hltpathinfo")
query.per_page = 1000  # to get all names in one go

# Projection. Specify attributes you want to fetch
query.attrs(["path_name"])

# Filter run
query.filter("run_number", args.run )

# Execute query and fetch data
resp = query.data()
oms = resp.json()   # all the data returned by OMS
data = oms['data']
HLTPaths = []
for row in data[:maxHLTPaths]:
    HLTPaths.append(row['attributes']['path_name'])


HLTAccepted = {}
for path in reversed(HLTPaths):
    HLTAccepted[path] = SetVariable(tree, path.split("_v")[0]+"_v",'I',1)
###############

query = omsapi.query("hltpathrates")
query.per_page = 1000  # to get all names in one go


# Projection. Specify attributes you want to fetch

firstPath = True
HLT_Counters = {}
HLTlumis = []
query.attrs(["counter",'last_lumisection_number']) #
for HLT_path in reversed(HLTPaths):
#    print(HLT_path)
    HLT_Counters[HLT_path] = []
    query.clear_filter()

    # Filter run
    query.filter("run_number", args.run )

    query.filter("path_name", HLT_path)
    query.filter("first_lumisection_number", minLS, "GE")
    query.filter("last_lumisection_number", maxLS, "LE")

    # Execute query and fetch data
    resp = query.data()
    oms = resp.json()   # all the data returned by OMS
    data = oms['data']
    HLTCounters = {}
    for row in data:
#        run[0], aaa, new_lumi = [int(el) for el in row['id'].split("__")]
        HLT_Counters[HLT_path].append(row['attributes']['counter'])
    if 'last_lumisection_number' in row['attributes']:
        for row in data:
    #        run[0], aaa, new_lumi = [int(el) for el in row['id'].split("__")]
            HLTlumis.append(row['attributes']['last_lumisection_number'])
    query.attrs(["counter"]) #

#print(HLT_Counters[HLT_path])
#################################################################

query = omsapi.query("lumisections")
query.per_page = 1000  # to get all names in one go
query.filter("run_number",  args.run)
resp = query.data()
oms = resp.json()   # all the data returned by OMS
data = oms['data']

lumisections = {}
det_flags = ['bpix', 'fpix', 'tob', 'tecp', 'tecm', 'tibtid', 'esm', 'ebp', 'esp', 'eep', 'ebm', 'eem', 'ho', 'hbhea', 'hbhec', 'hbheb', 'hf', 'gemm', 'gemp', 'gem', 'dt0', 'dtm', 'dtp', 'rpc', 'cscm', 'cscp', 'rp_sect_45', 'rp_sect_56', 'rp_time']
lhc_flags = ['beams_stable','beam_present','beam2_stable','beam2_present','physics_flag']
lhc_int = ['run_number','fill_number','lumisection_number']
lhc_float = ['recorded_lumi_per_lumisection','delivered_lumi_per_lumisection','pileup']

lumisections_vars = {}
for var in det_flags+lhc_flags:
    lumisections_vars[var] = SetVariable(tree,var,'O',1)
    lumisections[var] = []

for var in lhc_int+["year","month","day","hour","minute","second","time"]:
    if not var in ['lumisection_number','run_number']:
        lumisections_vars[var] = SetVariable(tree,var,'I',1)
    lumisections[var] = []

for var in lhc_float:
    lumisections_vars[var] = SetVariable(tree,var,'F',1)
    lumisections[var] = []

from datetime import datetime
for row in data:
    for var in det_flags:
        lumisections[var].append(row['attributes'][var+"_ready"])
    for var in lhc_flags+lhc_int+lhc_float:
        lumisections[var].append(row['attributes'][var])
    dtime = row['attributes']['start_time'] #format: '2022-11-24T08:45:47Z'
    date, time = dtime.split('T')
    yy,mm,dd = date.split('-')
    HH,MM,SS = time[:-1].split(':')
    lumisections['year'].append(int(yy))
    lumisections['month'].append(int(mm))
    lumisections['day'].append(int(dd))
    lumisections['hour'].append(int(HH))
    lumisections['minute'].append(int(MM))
    lumisections['second'].append(int(SS))
    lumisections['time'].append(int(datetime(int(yy), int(mm), int(dd), int(HH), int(MM),int(SS)).timestamp()))
    
#q.filter("lumisection_number", minLS, operator="GE")
#q.filter("lumiseciton_number", maxLS, operator="LE")
#q.custom("include", "meta")

####################################################################


query = omsapi.query("l1algorithmtriggers")
query.per_page = 1000  # to get all names in one go

# Projection. Specify attributes you want to fetch
query.attrs(["name","bit"])

# Filter run
query.filter("run_number", args.run )

# Execute query and fetch data
resp = query.data()
oms = resp.json()   # all the data returned by OMS
data = oms['data']
for row in data:
    algo = row['attributes']
    l1BitMap[int(algo['bit'])] = algo['name']
for bit in l1BitMap:
    triggerCounts[bit] = SetVariable(tree,l1BitMap[bit],'I',1)
# Create a query.
query = omsapi.query("l1algorithmtriggers")
query.per_page = 10000  # to get all LS in one go

# Projection. Specify attributes you want to fetch
query.attrs(["pre_dt_counter"]) #"name","bit", see https://cmsoms.cern.ch/agg/api/v1/l1algorithmtriggers/362616__1__1

#print(l1Bits)
lumis = range(0,2)
#bit = l1Bits[0]
query.clear_filter()
query.filter("run_number", args.run )
#query.filter("lumisection_number", minLS, operator="GE")
#query.filter("lumiseciton_number", maxLS, operator="LE")

#query.filter("bit", bit)  # returns data per lumisection
#query.custom("group[granularity]", "lumisection")
data = query.data().json()['data']
query.verbose = False
max = 0.0
lumisection = 4

#362616__383__25

first_el = True
for ls in data:
    run[0], l1Bit, new_lumi = [int(el) for el in ls['id'].split("__")]
    if first_el: 
        first_el = False
        lumi[0] = new_lumi
    if lumi[0] != new_lumi:
        print (run[0], lumi[0], triggerCounts[336][0])
        tree.Fill()
        lumi[0] = new_lumi
    pre_dt_counter = ls['attributes']['pre_dt_counter']
    triggerCounts[l1Bit][0] =  int(pre_dt_counter)
    idx_lumi = HLTlumis.index(lumi[0])
    for path in reversed(HLTPaths):
        HLTAccepted[path][0] = HLT_Counters[path][idx_lumi]
    idx_lumi = lumisections['lumisection_number'].index(lumi[0])
    for var in lumisections_vars:
        lumisections_vars[var][0] = lumisections[var][idx_lumi] if lumisections[var][idx_lumi] else False


#row

f.Write()
f.Close()



def getSingleHLTRate(self, runNumber, name, minLS=-1, maxLS=9999999):

        q = omsapi.query("hltpathrates")
        q.filter("run_number", runNumber)
        q.filter("path_name", name)
        q.filter("first_lumisection_number", minLS, "GE")
        q.filter("last_lumisection_number", maxLS, "LE")
        q.custom("fields", "first_lumisection_number,rate")
        q.per_page = PAGE_LIMIT
        data = q.data().json()['data']
        trigger_rates = {}
        for item in data:
            LS = item['attributes']['first_lumisection_number']
            rate = item['attributes']['rate']
            hltps = 0 # HLT Prescale                                                                                                                                                                       

            # TODO: We can probably come up with a better solution then a try, except here                                                                                                                 
            try:
                psi = self.PSColumnByLS[LS] # Get the prescale index                                                                                                                                       
            except:
                psi = 0
            if psi is None:
                psi = 0
            try:
                hltps = self.HLTPrescales[name][psi]
            except:
                hltps = 1.
            hltps = float(hltps)
            try:
                if self.HLTSeed[name] in self.L1IndexNameMap:
                    l1ps = self.L1Prescales[self.L1IndexNameMap[self.HLTSeed[name]]][psi]
                else:
                    l1ps = self.UnwindORSeed(self.HLTSeed[name],self.L1Prescales,psi)
            except:
                l1ps = 1
            ps = l1ps*hltps
            trigger_rates[LS] = [ps*rate, ps]

        return trigger_rates


#def getHLTRates(runNumber):

#    HLTRates = {}
#    q = omsapi.query("hltpathinfo")
#    q.filter("run_number", runNumber)
#    q.custom("fields", "path_name,rate")
#    q.per_page = PAGE_LIMIT
#    try:
#        data = q.data().json()['data']
#    except:
#        print("Failed to get HLT rates")
#        return {}
#    for item in data:
#        HLTRates[stripVersion(item['attributes']['path_name'])] = item['attributes']['rate']
#    return HLTRates


#        if ls['attributes']['pre_dt_rate'] > max:
#            max = ls['attributes']['pre_dt_rate']
#    print('max rate: {rate:8.1f} Hz    bit {bit:3d} {algo}'.format( rate = round(max), 
#                                                                    bit = data[0]['attributes']['bit'],
#                                                                    algo = data[0]['attributes']['name'] ) )

## let's check the mean rates
#for bit in l1Bits:
#    query.clear_filter().filter("run_number", args.run ).filter("bit", bit).custom('group[granularity]','run')  # returns mean value over run or lumisection range
#    data = query.data().json()['data']
#    print('mean rate: {rate:8.1f} Hz    bit {bit:3d} {algo}'.format( rate = data[0]['attributes']['pre_dt_rate'],
#                                                                    bit = data[0]['attributes']['bit'],
#                                                                    algo = data[0]['attributes']['name'] ) )
