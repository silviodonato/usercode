#! /usr/bin/env python

import cx_Oracle
import sys

def getConfDBdescr(configBase, addLink=True, fixCapital=True):
    ## Connect to confDB
    connstr = 'cms_hlt_gdr_r/convertMe!@cmsr'
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    curs.arraysize=50

    confDBdescr = []
    ## Loop on HLT versions
    for version in range(1,1000):
        configuration = configBase + "/V"+str(version)
        query="select a.description from u_confversions a where a.name='"+configuration+"'"
        curs.execute(query)
        curs_copy=curs
        ## get first row (curs_copy contains only one element here)
        for rows in curs_copy:
            ## get description, if it is not empty
            try:
                description = rows[0].read()
            except:
                description =""
            
            ## add link to JIRA tickets
            if addLink:
                posInit = description.find("CMSHLT-")
                if posInit>=0:
                    posFinal = posInit+7
                    while (posFinal<len(description) and description[posFinal].isdigit()): posFinal+=1
                    cmshlt = description[posInit:posFinal]
                    description = description.replace(cmshlt,"[[https://its.cern.ch/jira/browse/%s][%s]]"%(cmshlt,cmshlt))
             
            ## add '!' in front of capital letters
            if fixCapital:
                for i in range(len(description)):
                    if description[i].isupper() and (i==0 or description[i-1]==" "):
                        description = description[:i]+"!"+description[i:]
            
            ## fill confDBdescr
            confDBdescr.append((configuration,description))
    
    confDBdescr.reverse()
    return confDBdescr

if __name__ == "__main__":
    confDBdescr = getConfDBdescr(sys.argv[1])
    print confDBdescr
