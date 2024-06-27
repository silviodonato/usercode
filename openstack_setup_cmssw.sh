#!/bin/bash
# Script used in https://openstack.cern.ch/ to setup a machine based on Alma8 to use CMSSW

printf "\033c" #clear screen
printf "TEST SILVIO" #clear screen

mkdir ~/testSilvio

yum -y install git puppet-agent locmap-release locmap rpm-build voms-clients-java krb5-devel perl python3-devel rpm-build pip git make cmake gcc-c++ gcc binutils libX11-devel libXpm-devel libXft-devel libXext-devel python39 openssl-devel perl screen wget  x2goserver xterm mesa-libGLU mesa-libGLU-devel ant javaws
### yum install xfdesktop

locmap --enable all
locmap --list
locmap --configure all

echo "export CMS_LOCAL_SITE=T2_CH_CERN" > /etc/cvmfs/config.d/cms.cern.ch.local
echo "CVMFS_HTTP_PROXY='http://cmsmeyproxy.cern.ch:3128;http://ca-proxy.cern.ch:3128'" >> /etc/cvmfs/config.d/cms.cern.ch.local

cvmfs_config reload

#locmap --enable all
#locmap --configure all
 
printf "DONE" #clear screen

exit 0

### Login as user (!!!), copy missing files
sudo scp -r sdonato@lxplus.cern.ch:/etc/grid-security /etc/grid-security
sudo scp -r sdonato@lxplus.cern.ch:/etc/vomses /etc/vomses

ln -s /afs/cern.ch/user/s/sdonato afs
ln -s /afs/cern.ch/user/s/sdonato/.globus .

pip install oauth2client gspread
pip install omsapi --index-url https://gitlab.cern.ch/api/v4/projects/45046/packages/pypi/simple

voms-proxy-init

### Test CMSSW
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_13_0_0_pre4
cd CMSSW_13_0_0_pre4
cmsenv

voms-proxy-init

runTheMatrix.py --show | grep HLTPhysics202
runTheMatrix.py -l 141.111 --ibeos

### PROXY all


ssh -f -N -D 12345 lxtunnel.cern.ch 
export ALL_PROXY=socks5://localhost:12345
#OR
#use_proxy=yes
#http_proxy=localhost:12345
#https_proxy=localhost:12345

# test
wget https://ubuntu.mirror.garr.it/releases/24.04/ubuntu-24.04-desktop-amd64.iso

# kinit
python3 /afs/cern.ch/user/s/sdonato/SilvioCronJob2/renewticket.py


