#!/usr/bin/python3.6
## This code creates .sh files to update the energy from 13 TeV to 14 TeV in the gridpacks, given their prep_id (eg. HIG-RunIIFall18wmLHEGS-00593). It works only on lxplus.
output_folder = '/afs/cern.ch/user/s/sdonato/AFSwork/public/Snowmass'
prep_ids = [## See https://docs.google.com/spreadsheets/d/1GhxNbPxHhI5V_xeLYJU7g5mOv4Poq0DP1JjMlS27EmM/edit#gid=0
    'HIG-RunIIFall18wmLHEGS-00603',
    'HIG-RunIIFall18wmLHEGS-00604',
    'HIG-RunIIFall18wmLHEGS-00601',
    'HIG-RunIIFall18wmLHEGS-00602',
    'SUS-RunIIFall18wmLHEGS-00029',
    'SUS-RunIIFall18wmLHEGS-00013',
    'SUS-RunIIFall18wmLHEGS-00014',
    'SUS-RunIIFall18wmLHEGS-00015',
    'SUS-RunIIFall18wmLHEGS-00016',
    'SUS-RunIIFall18wmLHEGS-00017',
    'SUS-RunIIFall18wmLHEGS-00018',
    'SUS-RunIIFall18wmLHEGS-00019',

    'HIG-RunIIFall18wmLHEGS-00597',
    'HIG-RunIIFall18wmLHEGS-00598',
    'HIG-RunIIFall18wmLHEGS-00599',
    'HIG-RunIIFall18wmLHEGS-00600',

    'HIG-RunIIFall18wmLHEGS-00593',
    'HIG-RunIIFall18wmLHEGS-00594',
    'HIG-RunIIFall18wmLHEGS-00595',
    'HIG-RunIIFall18wmLHEGS-00596',

    'HIG-RunIIFall18wmLHEGS-00419',

    'HIG-RunIIFall18wmLHEGS-03437',
    'HIG-RunIIFall18wmLHEGS-03366',

    'HIG-RunIIFall18wmLHEGS-00367',
    'HIG-RunIIFall18wmLHEGS-00364',
    'HIG-RunIIFall18wmLHEGS-00370',
    'HIG-RunIIFall18wmLHEGS-00361',
]
#prep_ids = ['HIG-RunIIFall18wmLHEGS-03366']


import subprocess, os

## Download request_fragment_check.py (it works only on lxplus)
if not os.path.isfile('request_fragment_check.py'):
    process = subprocess.run('wget https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/utils/request_fragment_check.py', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

## Get the fragment
print("Calling python request_fragment_check.py for %s"%prep_ids)
for prep_id in prep_ids:
    print(prep_id)
    process = subprocess.run('python request_fragment_check.py --bypass_status --prepid %s'%prep_id, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
print("...done.\n")

## Look for the gridpack
print("Creating .sh file for %s"%prep_ids)
gridpack_filename = {}
for prep_id in prep_ids[:]:
    print(prep_id)
    if not os.path.isfile(prep_id):
        print("############ ERROR in %s ####################################"%prep_id)
        print("%s prep_id file not found (likely prep_id '%s' is wrong)"%(prep_id,prep_id))
        prep_ids.remove(prep_id)
        continue
    process = subprocess.run('grep  "/cvmfs/cms.cern.ch/phys_generator/gridpacks" %s'%prep_id, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    gridpack_original = process.stdout.split("'")[1]
    gridpack_extracted = '%s_extracted'%prep_id
    gridpack_filename[prep_id] = gridpack_original.split('/')[-1]
    if "14" in gridpack_filename[prep_id]:
        print("############ ERROR in %s ####################################"%prep_id)
        print("'14' found in %s"%gridpack_filename[prep_id])
        prep_ids.remove(prep_id)
        continue
    gridpack_filename[prep_id] = gridpack_filename[prep_id].replace("13TeV","14TeV")
    if "/powheg/" in gridpack_original:
        try:
            print('rm -rf powheg.input && (tar -xvf %s ./powheg.input || tar -xvf %s powheg.input) && grep 6500 powheg.input | wc -l'%(gridpack_original,gridpack_original))
            process = subprocess.run('rm -rf powheg.input && (tar -xvf %s ./powheg.input || tar -xvf %s powheg.input) && grep 6500 powheg.input | wc -l'%(gridpack_original,gridpack_original), shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        except:
            print("############ ERROR in %s ####################################"%prep_id)
            print("I cannot find in 'powheg.input' in %s."%gridpack_original)
            prep_ids.remove(prep_id)
            continue
        if not (int(process.stdout.split('\n')[1])==2):
            print("############ ERROR in %s ####################################"%prep_id)
            print(int(process.stdout.split('\n')[1]))
            print("I cannot find exactly two '6500' in 'powheg.input' in %s."%gridpack_original)
            prep_ids.remove(prep_id)
            continue
    elif "/madgraph/":
        try:
            print('rm -rf InputCards && (tar -xvf %s ./InputCards/*_run_card.dat || tar -xvf %s InputCards/*_run_card.dat) && grep 6500 ./InputCards/*_run_card.dat | wc -l'%(gridpack_original,gridpack_original))
            process = subprocess.run('rm -rf InputCards && (tar -xvf %s ./InputCards/*_run_card.dat || tar -xvf %s InputCards/*_run_card.dat) && grep 6500 InputCards/*_run_card.dat | wc -l'%(gridpack_original,gridpack_original), shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
        except:
            print("############ ERROR in %s ####################################"%prep_id)
            print("I cannot find in './InputCards/*_run_card.dat' in %s."%gridpack_original)
            prep_ids.remove(prep_id)
            continue
        if not (int(process.stdout.split('\n')[1])==2):
            print("############ ERROR in %s ####################################"%prep_id)
            print(int(process.stdout.split('\n')[1]))
            print("I cannot find exactly two '6500' in 'InputCards/*_run_card.dat' in %s."%gridpack_original)
            prep_ids.remove(prep_id)
            continue
    else:
        print("############ ERROR in %s ####################################"%prep_id)
        print("Not powheg nor madgraph found in %s."%gridpack_original)
        prep_ids.remove(prep_id)
        continue
    
    ## Create a script to update the gridpack
    script = open('updateEnergy_%s.sh'%prep_id,'w')
    script.write('#!/usr/bin/sh\n')
    script.write('mkdir %s\n'%gridpack_extracted)
    script.write('tar -xvf %s -C %s\n'%(gridpack_original, gridpack_extracted))
    script.write('echo "tar -xvf -C DONE"\n')
    script.write("sed -i 's/6500/7000/' %s/InputCards/*_run_card.dat\n"%gridpack_extracted)
    script.write("sed -i 's/6500/7000/' %s/powheg.input\n"%gridpack_extracted)
    script.write("cd %s\n"%(gridpack_extracted))
    if "tar.xz" in gridpack_filename[prep_id]:
        script.write("tar -cvJf ../%s *\n"%(gridpack_filename[prep_id]))
    else:
        script.write("tar -cvf ../%s *\n"%(gridpack_filename[prep_id]))
    script.write("cd ..\n")
    script.write('echo "tar -cvJf DONE"\n')
    script.write('pwd \n')
    script.write('ls -lrth \n')
    script.write("cp %s %s\n"%(gridpack_filename[prep_id], output_folder))
    script.close()
    
    ## Make the file executable
    from pathlib import Path
    import stat 
    f = Path('updateEnergy_%s.sh'%prep_id)
    f.chmod(f.stat().st_mode | stat.S_IEXEC)

print("Files created for %s"%prep_ids)
print("------------------------"%prep_ids)

## Check the output ##
for prep_id in prep_ids:
    script = open('updateEnergy_%s.sh'%prep_id,'r')
    print('\n\ncat updateEnergy_%s.sh:'%prep_id)
    print(script.read())

## HTCondor scripts ##
os.makedirs('HTCondorLog/',exist_ok=True)
for prep_id in prep_ids:
    HTCondor_script = open('HTCondorScript_%s.sub'%prep_id,'w')
    HTCondor_script.write('''
executable            = updateEnergy_%s.sh
arguments             = $(ClusterId) $(ProcId)
output                = HTCondorLog/%s.$(ClusterId).$(ProcId).out
error                 = HTCondorLog/%s.$(ClusterId).$(ProcId).err
log                   = HTCondorLog/%s.$(ClusterId).log
+JobFlavour           = "espresso"
should_transfer_files = YES
transfer_output_files = %s
queue
'''%(prep_id,prep_id,prep_id,prep_id,gridpack_filename[prep_id]))
HTCondor_script.close()

## HTCondor scripts ##
HTCondor_script = open('submitAll.sh','w')
for prep_id in prep_ids:
    HTCondor_script.write('condor_submit HTCondorScript_%s.sub\n'%prep_id)
HTCondor_script.write('\necho "condor_q"\n')
HTCondor_script.write('\necho "condor_wait -status HTCondorLog/%s.*.log"\n'%prep_id)
HTCondor_script.close()
print("submitAll.sh is READY.")
