#!/bin/bash
# Script used in https://openstack.cern.ch/ to setup a machine based on Alma8 to use CMSSW

printf "\033c" #clear screen
printf "TEST SILVIO" #clear screen

mkdir ~/testSilvio

yum -y install git
yum -y install puppet-agent
yum -y install locmap-release
yum -y install locmap
#yum -y install rpm-build

locmap --enable all
locmap --list
locmap --configure all

yum -y install voms-clients-java

yum -y install git make cmake gcc-c++ gcc binutils libX11-devel libXpm-devel libXft-devel libXext-devel python39 openssl-devel

echo "export CMS_LOCAL_SITE=T2_CH_CERN" > /etc/cvmfs/config.d/cms.cern.ch.local
echo "CVMFS_HTTP_PROXY='http://cmsmeyproxy.cern.ch:3128;http://ca-proxy.cern.ch:3128'" >> /etc/cvmfs/config.d/cms.cern.ch.local

cvmfs_config reload

#locmap --enable all
#locmap --configure all
 
printf "DONE" #clear screen

exit 0

### Login as user, copy missing files
sudo scp -r sdonato@lxplus.cern.ch:/etc/grid-security /etc/grid-security
sudo scp -r sdonato@lxplus.cern.ch:/etc/vomses /etc/vomses

ln -s /afs/cern.ch/user/s/sdonato afs
ln -s /afs/cern.ch/user/s/sdonato/.globus .

voms-proxy-init

### Test CMSSW
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_13_0_0_pre4
cd CMSSW_13_0_0_pre4
cmsenv

runTheMatrix.py -l 140.115
