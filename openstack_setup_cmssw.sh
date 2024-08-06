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
sudo scp -r sdonato@lxplus.cern.ch:/etc/grid-security/certificates/* /etc/grid-security/certificates

ln -s /afs/cern.ch/user/s/sdonato afs
ln -s /afs/cern.ch/user/s/sdonato/.globus .

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

pip install oauth2client gspread --proxy socks5://localhost:12345


#OR
#use_proxy=yes
#http_proxy=localhost:12345
#https_proxy=localhost:12345

# test
wget https://ubuntu.mirror.garr.it/releases/24.04/ubuntu-24.04-desktop-amd64.iso

# kinit
python3 /afs/cern.ch/user/s/sdonato/SilvioCronJob2/renewticket.py


#### To make a new disk partition
###### Remember to attach Volume to Instance from OpenStack! ################


###### CREATE PARTITION ################
```
[root@sdonato-openstack /]# lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
vda     252:0    0   40G  0 disk 
|-vda1  252:1    0 39.5G  0 part /
|-vda14 252:14   0    4M  0 part 
`-vda15 252:15   0  545M  0 part /boot/efi
vdb     252:16   0  240G  0 disk 
`-vdb1  252:17   0  240G  0 part 
```

```
fdisk /dev/vdb       
                                                                                                                                                                                                             
Welcome to fdisk (util-linux 2.32.1).            
Changes will remain in memory only, until you decide to write them.                                                                                                                                          
Be careful before using the write command.       
                                                                                                                                                                                                             
The old ext4 signature will be removed by a write command.
                                                                                                                                                                                                             
Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x4b129eef.                                                                                                                                                 
                                                 
Command (m for help): F                          
Unpartitioned space /dev/vdb: 240 GiB, 257696989184 bytes, 503314432 sectors                                                                                                                                 
Units: sectors of 1 * 512 = 512 bytes            
Sector size (logical/physical): 512 bytes / 4096 bytes                                                                                                                                                       
                                                 
Start       End   Sectors  Size                                                                                                                                                                              
 2048 503316479 503314432  240G                  
                                                                                                                                                                                                             
Command (m for help): n                          
Partition type                                                                                                                                                                                               
   p   primary (0 primary, 0 extended, 4 free)   
   e   extended (container for logical partitions)                                                                                                                                                           
Select (default p): p                            
Partition number (1-4, default 1):                                                                                                                                                                           
First sector (2048-503316479, default 2048):     
Last sector, +sectors or +size{K,M,G,T,P} (2048-503316479, default 503316479):                                                                                                                               
                                                 
Created a new partition 1 of type 'Linux' and of size 240 GiB.                                                                                                                                               
                                                 
Command (m for help): w                                                                                                                                                                                      
                                                 
The partition table has been altered.                                                                                                                                                                        
Calling ioctl() to re-read partition table.      
Syncing disks.                                                                                                                                                                                               
                      ```

### CREAT FILESYSTEM (XFS or EXT4)
mkfs.xfs -K /dev/vdb1

### MOUNT 
mkdir /scratch
mount /dev/vdb1 /scratch/



