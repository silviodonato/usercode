##python3

import subprocess

def submit(command):
    return subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)

def getDependecies (package):
    process = submit("git grep %s"%package.replace("/",".")) ##works both for A/B and A.B
    print("git grep %s"%package.replace("/","."))
    modules = process.stdout.split("\n")
    modules = modules[:-1]
    return modules

packages = [
    "DiffractiveForwardAnalysis/Configuration",
    "DiffractiveForwardAnalysis/Skimming",
    "ElectroWeakAnalysis/Configuration",
    "ElectroWeakAnalysis/Skimming",
    "ElectroWeakAnalysis/Utilities",
    "ElectroWeakAnalysis/WENu",
    "ElectroWeakAnalysis/WMuNu",
    "ElectroWeakAnalysis/ZEE",
    "ElectroWeakAnalysis/ZMuMu",
    "QCDAnalysis/ChargedHadronSpectra",
    "QCDAnalysis/Configuration",
    "QCDAnalysis/Skimming",
    "QCDAnalysis/UEAnalysis",
    "HeavyFlavorAnalysis/Configuration",
    "HeavyFlavorAnalysis/Skimming",
    "HiggsAnalysis/HiggsToGammaGamma",
    "HiggsAnalysis/Configuration",
    "HiggsAnalysis/Skimming",
    "TopQuarkAnalysis/Examples",
    "TopQuarkAnalysis/TopPairBSM",
#    "TopQuarkAnalysis/TopSkimming",
    "SUSYBSMAnalysis/HSCP",
    "MuonAnalysis/Configuration",
]

depsMap = {}
for package in packages:
    depsMap[package] = getDependecies(package)
    for dep in depsMap[package][:]:
        for package2 in packages:
#            print("Check %s == %s ?"%(dep[0:len(package)+1], package+"/"))
            if dep[0:len(package2)+1]==(package2+"/") or dep[0:len("Utilities/ReleaseScripts/scripts/git-publish:")]=="Utilities/ReleaseScripts/scripts/git-publish:":
#                print("removing %s"%dep)
                if dep in depsMap[package]:
                    depsMap[package].remove(dep)
    print("Unresolved dependencies:")
    print()
    print("######"+package+"######")
    print()
    for dep in depsMap[package]:
        print(dep)

print("-----------------------------------------------------------------------")
print("Unresolved dependencies:")
for package in packages:
    if len(depsMap[package])>0:
        print()
        print("######"+package+"######")
        print()
        for dep in depsMap[package]:
            print(dep)
