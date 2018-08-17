from math import sqrt, pi, log10, log, exp
from array import array

class EmptyClass():
    def size(self):
        return 0

class DummyClass():
    def size(self):
        return 0
    def product(self):
        return EmptyClass()

def deltaPhi(phi1, phi2):
  PHI = abs(phi1-phi2)
  if PHI<=pi:
      return PHI
  else:
      return 2*pi-PHI

def deltaR(eta1, phi1, eta2, phi2):
  deta = eta1-eta2
  dphi = deltaPhi(phi1,phi2)
  return sqrt(deta*deta + dphi*dphi)

def matching(eta,phi,offJet_eta,offJet_phi,offJet_num):
    dRMin = 99.
    index = -1
    for i in range(0,offJet_num):
        dR = deltaR(eta,phi,offJet_eta[i],offJet_phi[i])
        if dR < 0.5 and dR < dRMin:
            dRMin = dR
            index = i
    
    return index
    

def SetVariable(tree,name,option='F',lenght=1,maxLenght=100):
    if option is 'F': arraytype='f'
    elif option is 'O': arraytype='l'
    elif option is 'I': arraytype='l'
    else:
        print 'option ',option,' not recognized.'
        return

    if not type(lenght) is str:
        maxLenght = lenght
        lenght = str(lenght)
    variable = array(arraytype,[0]*maxLenght)
    if maxLenght>1: name = name + '['+lenght+']'
    tree.Branch(name,variable,name+'/'+option)
    return variable

class EmptyProduct(list):
    def size(self):
        return 0

def productWithCheck(self):
    try:
        return self.product()
    except:
        return EmptyProduct()

def Matching(eta, phi, collection):
    index = -1
    dRmax = 999
    for i in range(collection.num[0]):
        dR = deltaR(eta,phi,collection.eta[i],collection.phi[i])
        if dR<dRmax:
            index = i
            dRmax = dR
    return index,dRmax

#example:
#checkTriggerIndex(triggerName,triggerIndex,names.triggerNames())
def getHLTindexes(hltnames, triggernames):
    names = triggernames.triggerNames()
    hltIndexs = [-1]*len(hltnames)
    for i, hltname in enumerate(hltnames):
        for idx, triggername in enumerate(names):
            if hltname in triggername:
                if hltIndexs[i] == -1:
                    hltIndexs[i] = idx
                else:
                    hltIndexs[i] = -2
        if hltIndexs[i] == -1 or hltIndexs[i] == -2:
            for tr in names: print tr
            print
            print "Something wrong with ",hltname,hltIndexs[i]
            print
    return hltIndexs

#example:
#checkTriggerIndex(triggerName,triggerIndex,names.triggerNames())
def checkTriggerIndex(name,index, names):
    if not 'firstTriggerError' in globals():
        global firstTriggerError
        firstTriggerError = True
    if index>=names.size():
        if firstTriggerError:
            for tr in names: print tr
            print
            print name," not found!"
            print
            firstTriggerError = False
            return False
        else:
            return False
    else:
        return True

#example: 
#jets = BookVector(tree, "jets", ['pt','eta','phi','mass','btag'],maxJets)
def BookVector(tree,name="vector",listMembers=[],maxJets=100):
    obj = DummyClass()
    obj.num   = SetVariable(tree,name+'_num' ,'I')
    for member in listMembers:
        if "match" in name:
            setattr(obj,member,SetVariable(tree,name+'_'+member  ,'I',name+'_num',maxJets))
        else:
            setattr(obj,member,SetVariable(tree,name+'_'+member  ,'F',name+'_num',maxJets))
    return obj



#example: 
#filterFunction = lambda x: x.pt()>20
#FillVector(patJets_source,jets,filterFunction)
def FillVector(source,variables,filterFunction = lambda x: True):
    variables.num[0] = 0
    for obj in source.productWithCheck():
        if not filterFunction(obj): continue
        if variables.num[0]<len(variables.pt):
            for (name,var) in variables.__dict__.items():
                if name == "pt" :           var[variables.num[0]] = obj.pt()
                elif name == "eta" :        var[variables.num[0]] = obj.eta()
                elif name == "phi" :        var[variables.num[0]] = obj.phi()
                elif name == "mass" :       var[variables.num[0]] = obj.mass()
                elif name == "neHadEF" :    var[variables.num[0]] = obj.neutralHadronEnergyFraction()
                elif name == "neEmEF" :     var[variables.num[0]] = obj.neutralEmEnergyFraction()
                elif name == "chHadEF" :    var[variables.num[0]] = obj.chargedHadronEnergyFraction()
                elif name == "chEmEF" :     var[variables.num[0]] = obj.chargedEmEnergyFraction()
                elif name == "muEF" :       var[variables.num[0]] = obj.muonEnergyFraction()
                elif name == "mult" :       var[variables.num[0]] = obj.chargedMultiplicity()+obj.neutralMultiplicity();
                elif name == "neMult" :     var[variables.num[0]] = obj.neutralMultiplicity()
                elif name == "chMult" :     var[variables.num[0]] = obj.chargedMultiplicity()
                elif name == "btag2b" :       var[variables.num[0]] = obj.bDiscriminator("pfDeepCSVJetTags:probbb")
                elif name == "btag1b" :       var[variables.num[0]] = obj.bDiscriminator("pfDeepCSVJetTags:probb")
                elif name == "btagc" :       var[variables.num[0]] = obj.bDiscriminator("pfDeepCSVJetTags:probc")
                elif name == "btagudsg" :  var[variables.num[0]] = obj.bDiscriminator("pfDeepCSVJetTags:probudsg")
                elif name == "btag" :       var[variables.num[0]] = obj.bDiscriminator("pfDeepCSVJetTags:probb") + obj.bDiscriminator("pfDeepCSVJetTags:probbb")
                elif name == "btagCSV" :    var[variables.num[0]] = obj.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")
            variables.num[0] += 1
