from math import sqrt, pi, log10, log, exp

def printLabelFilters(triggerEv):
    print "Filters:"
    for i in range(triggerEv.sizeFilters()):
        print "\t",triggerEv.filterLabel(i)
    print

def printLabelCollections(triggerEv):
    print "Collection:"
    for i in range(triggerEv.sizeCollections()):
        print "\t",triggerEv.collectionTagEncoded(i)
    print

def getSizeFilter(triggerEv,inputTag):
    filterIndex = triggerEv.filterIndex(inputTag)
    if filterIndex >= triggerEv.sizeFilters():
        return -1
    else:
        return len(triggerEv.filterKeys(filterIndex))

def goodEvent(run,lumi): #https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt
#    JSONlist={"254231": [[1, 24]], "254232": [[1, 81]], "254790": [[90, 90], [93, 630], [633, 697], [701, 715], [719, 784]], "254852": [[47, 94]], "254879": [[52, 52], [54, 140]], "254906": [[1, 75]], "254907": [[1, 52]], "254914": [[32, 32], [34, 78]], "256630": [[5, 26]], "256673": [[55, 56]], "256674": [[1, 2]], "256675": [[1, 106], [111, 164]], "256676": [[1, 160], [162, 208]], "256677": [[1, 291], [293, 390], [392, 397], [400, 455], [457, 482]], "256801": [[73, 263]], "256842": [[131, 132]], "256843": [[1, 204], [207, 284], [286, 378], [380, 461], [463, 587], [598, 627], [630, 661], [1001, 1034], [1036, 1081], [1083, 1191], [1193, 1193], [1195, 1329], [1331, 1332]], "256866": [[34, 47]], "256867": [[1, 16], [19, 94]], "256868": [[5, 33], [35, 200], [202, 492]], "256869": [[1, 34]], "256926": [[35, 50], [53, 62], [64, 65]], "256941": [[1, 17], [19, 29], [103, 105], [107, 126], [129, 129], [131, 168], [170, 170], [175, 290], [293, 294]], "257461": [[44, 95]], "257531": [[5, 45], [50, 143]], "257599": [[42, 118]], "257613": [[14, 1307]], "257614": [[1, 16]], "257645": [[37, 73], [75, 1096]], "257682": [[66, 366]], "257722": [[1, 19]], "257723": [[1, 1], [3, 108], [114, 148]], "257735": [[1, 15]], "257751": [[1, 463]], "257804": [[1, 17]], "257805": [[1, 249]], "257816": [[1, 385]], "257819": [[1, 248]], "257968": [[69, 326]], "257969": [[1, 634]], "258129": [[30, 124]], "258136": [[1, 60]], "258157": [[1, 56]], "258158": [[1, 1088], [1091, 1786]], "258159": [[1, 501]], "258177": [[1, 342], [347, 724], [755, 1939]], "258211": [[43, 129]], "258213": [[1, 165]], "258214": [[1, 217]], "258215": [[1, 6]], "258287": [[45, 144], [148, 227]], "258403": [[1, 251]], "258425": [[3, 136]], "258426": [[1, 10]], "258427": [[1, 107]], "258428": [[1, 159]], "258432": [[1, 4]], "258434": [[1, 453]], "258440": [[1, 442], [444, 732]], "258444": [[1, 37]], "258445": [[1, 302]], "258446": [[1, 142]], "258448": [[2, 100], [102, 731]], "258655": [[60, 68]], "258656": [[1, 334]], "258694": [[23, 199]], "258702": [[52, 402]], "258703": [[1, 389]], "258705": [[1, 100]], "258706": [[1, 733]], "258712": [[1, 524]], "258713": [[1, 161]], "258714": [[1, 67]], "258741": [[22, 72]], "258742": [[2, 693]], "258745": [[1, 260]], "258749": [[1, 204], [220, 604]], "258750": [[1, 197]], "259626": [[83, 106], [108, 111], [115, 166], [169, 215], [218, 437]], "259637": [[1, 72], [75, 221]], "259681": [[64, 98]], "259683": [[5, 19], [22, 23], [25, 94]], "259685": [[1, 209], [213, 240], [242, 290], [292, 445], [447, 538], [540, 544], [546, 630]], "259686": [[1, 43], [45, 47], [49, 100], [102, 108], [110, 163], [165, 245], [248, 341]], "259721": [[73, 99], [102, 408]], "259809": [[53, 222]], "259810": [[1, 113], [116, 116]], "259811": [[1, 47], [50, 91]], "259813": [[1, 10]], "259817": [[1, 5]], "259818": [[1, 160]], "259820": [[1, 32], [36, 161]], "259821": [[1, 75], [78, 212]], "259822": [[1, 14], [17, 464]], "259861": [[1, 34], [36, 38], [40, 66], [69, 77]], "259862": [[1, 13], [16, 532]], "259884": [[73, 143], [147, 155]], "259890": [[1, 34], [37, 109]], "259891": [[1, 108]], "260373": [[47, 370], [373, 408]], "260424": [[3, 12], [15, 266], [269, 672]], "260425": [[1, 18], [21, 55], [58, 256]], "260426": [[1, 52], [55, 296], [298, 307], [310, 504]], "260427": [[1, 198]], "260431": [[1, 447]], "260532": [[3, 8], [10, 456], [458, 746]], "260533": [[1, 14]], "260534": [[1, 375]], "260536": [[9, 37], [45, 60], [62, 193]], "260538": [[1, 284]], "260541": [[1, 24]], "260575": [[1, 24]], "260576": [[2, 88], [90, 150]], "260577": [[1, 76]], "260593": [[65, 401]], "260627": [[97, 611], [613, 757], [760, 788], [791, 1051], [1054, 1530], [1533, 1845]]}
# https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt
    JSONlist={"272007":[[1,6]], "272008":[[1,5],[10,35]], "272010":[[1,24]], "272011":[[1,30],[32,38],[42,90],[93,107],[110,116],[119,132],[135,147],[150,189],[191,202]], "272012":[[1,27],[30,41],[44,55],[57,68],[71,82],[85,96],[99,112],[116,148],[150,158],[160,168],[170,185],[187,193],[195,201],[204,214]], "272014":[[1,10],[12,19],[21,28],[32,39],[41,47],[50,56],[58,82],[84,91],[93,99],[101,108],[110,125]], "272016":[[1,9],[12,18],[21,27],[29,36],[38,48]], "272017":[[1,2]], "272019":[[1,22]], "272021":[[1,125]], "272022":[[1,69]], "272760":[[66,78],[79,79],[80,86]], "272761":[[1,51],[52,54],[55,85]], "272762":[[1,80],[81,81],[82,108]], "272774":[[99,112]], "272775":[[1,30],[31,32],[33,186],[187,187],[188,204]], "272776":[[1,105]], "272782":[[80,113]], "272783":[[1,151]], "272784":[[1,305]], "272785":[[1,149]], "272786":[[1,59]], "272798":[[91,223],[224,947],[948,948],[949,959],[960,960],[961,972],[973,973],[974,995],[996,996],[997,1022],[1023,1024],[1025,1036],[1037,1038],[1039,1051],[1052,1053],[1054,1060],[1061,1065],[1066,1066],[1067,1067],[1068,1360],[1361,1363],[1364,1370],[1371,1373],[1374,1718],[1719,1720],[1721,1800]], "272811":[[95,189]], "272812":[[1,380]], "272814":[[1,9]], "272815":[[1,22]], "272816":[[1,35]], "272818":[[1,65],[66,67],[68,245],[246,246],[247,279],[280,280],[281,451],[452,457],[458,620]], "272827":[[98,111]], "272828":[[1,59]], "272922":[[15,34]], "272923":[[1,32]], "272924":[[1,22]], "272925":[[1,9]], "272926":[[1,22]], "272927":[[1,73]], "272930":[[1,164]], "272936":[[25,379]], "273013":[[26,330]], "273017":[[1,928]], "273150":[[64,75]], "273158":[[1,1283]], "273290":[[10,22]], "273291":[[1,83]], "273292":[[1,21]], "273294":[[1,8]], "273295":[[1,11]], "273299":[[1,47]], "273301":[[1,614]], "273302":[[1,459]], "273402":[[100,292]], "273403":[[1,68]], "273404":[[1,22]], "273405":[[1,34]], "273406":[[1,125]], "273407":[[1,9]], "273408":[[1,9]], "273409":[[1,317]], "273410":[[1,99]], "273411":[[1,29]], "273425":[[62,352],[353,353],[354,742]], "273426":[[1,65]], "273445":[[7,9]], "273446":[[1,48]], "273447":[[1,113],[114,114],[115,420]], "273448":[[1,396]], "273449":[[1,216]], "273450":[[1,214],[215,218],[219,647]], "273492":[[71,282],[283,283],[284,325],[326,326],[327,343]], "273493":[[1,241]], "273494":[[1,192]], "273502":[[73,256],[257,257],[258,318],[319,319],[320,813],[814,814],[815,1077]], "273503":[[1,598]], "273522":[[79,121]], "273523":[[1,228]], "273526":[[1,34]], "273531":[[1,280]], "273537":[[1,779]], "273554":[[77,444],[445,446]], "273555":[[1,173]]}
    if str(run) in JSONlist.keys():
        for rg in JSONlist[str(run)]:
            if len(rg) ==2:
                if lumi>=rg[0] and lumi<=rg[1]:
                    return True
    
    return False

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

def getCollectionKeys(triggerEvent,inputTag):
    collectionKeys = []
    collectionIndex = triggerEvent.collectionIndex(inputTag)
    if collectionIndex<triggerEvent.sizeCollections():
        start = 0
        if collectionIndex>0: start = triggerEvent.collectionKey(collectionIndex-1)
        stop = triggerEvent.collectionKey(collectionIndex)
        collectionKeys = range(start, stop)
        del start
        del stop
    
    del collectionIndex
    return collectionKeys

def getMET(triggerEvent,inputTag):
    collectionKeys = getCollectionKeys(triggerEvent,inputTag)
    trigObjColl = triggerEvent.getObjects()
    if len(collectionKeys)>0:
        met = trigObjColl[collectionKeys[0]]
        return met.pt(), met.phi()
    else:
        return 0,0
    del trigObjColl
    del collectionKeys


def getFilterKeys(triggerEvent,inputTag):
    filterKeys = []
    filterIndex = triggerEvent.filterIndex(inputTag)
    if filterIndex<triggerEvent.sizeFilters():
        filterKeys = triggerEvent.filterKeys(filterIndex)
    
    del filterIndex
    return filterKeys


def launchNtupleFromAOD(fileOutput,filesInput,maxevents):
    print "fileOutput=",fileOutput
    print
    print "filesInput=",filesInput
    print
    print "maxevents=",maxevents
    print

    import ROOT
    import itertools
    import resource
    from array import array
    from math import sqrt, pi, log10, log, exp
    # load FWlite python libraries
    from DataFormats.FWLite import Handle, Events

    pt_min=20
    eta_max=2.4
    NHFmax=0.9
    NEMFmax=0.99
    CHFmin=0.
    MUFmax=0.8
    CEMFmax=0.99
    NumConstMin=1
    CHMmin=0

    f = ROOT.TFile(fileOutput,"recreate")
    tree = ROOT.TTree("tree","tree")
    
    maxJets = 50
    
    calobjets = [
    'hltBTagCaloCSVp014DoubleWithMatching',
    'hltBTagCaloCSVp022Single',
    'hltBTagCaloCSVp026DoubleWithMatching',
    'hltBTagCaloCSVp067Single',
    'hltBTagCaloCSVp087Double',
    'hltBTagCaloCSVp087Triple',
    'hltBTagCaloCSVp14Single',
    'hltBTagCaloCSVp20Single',
    'hltBTagCaloCSVp24Double',
    'hltBTagCaloCSVp24Single',
    'hltBTagCaloCSVp50Double',
    ]
    
#    calobjetsMC = [
#    'hltBLifetimeL3FilterCSVsusy',
#    'hltCSV0p7L3',
#    'hltCSVL30p6',
#    'hltTripleCSV0p5',
#    'hltDoubleCSV0p5',
#    'hltBLifetimeL3FilterCSVLoose0p41',
#    'hltCSV0p5L3',
#    ]
    
    pfbjets = [
    'hltBTagPFCSVp016SingleWithMatching',
    'hltBTagPFCSVp056Double',
    'hltBTagPFCSVp056Single',
    'hltBTagPFCSVp063Double',
    'hltBTagPFCSVp063DoubleMbb60200Ptb5030',
    'hltBTagPFCSVp063Single',
    'hltBTagPFCSVp063p20Mbb60200Ptb5030',
    'hltBTagPFCSVp11DoubleWithMatching',
    'hltBTagPFCSVp13Single',
    'hltBTagPFCSVp20Double'
    ]
    
#    pfbjetsMC = [
#    'hltCSVFilterSingleTop',
#    'hltDoubleCSVPF0p4',
#    'hltCSVPF0p7',
#    'hltCSV0p5FilterSingleMu10',
#    'hltCSV0p5FilterSingleEle10',
#    'hltCSVFilterPF0p7',
#    'hlt2CSVFilterPF0p7',
#    ]
    
#    filtersMC = [
#    'hltL1sTripleVBF',
#    'hltPreQuadPFJetDoubleBTagCSVVBFMqq200',
#    'hltPreQuadPFJetSingleBTagCSVVBFMqq460',
#    'hltPreQuadPFJetDoubleBTagCSVVBFMqq240',
#    'hltPreQuadPFJetSingleBTagCSVVBFMqq500',
#    'hltQuadJet15',
#    'hltTripleJet50',
#    'hltDoubleJet65',
#    'hltSingleJet80',
#    'hltVBFCaloJetEtaSortedMqq150Deta1p5',
#    'hltCSVL30p6',
#    'hltPFQuadJetLooseID15',
#    'hltPFTripleJetLooseID64',
#    'hltPFDoubleJetLooseID76',
#    'hltPFSingleJetLooseID92',
#    'hltSelector6PFJets',
#    'hltDoubleCSVPF0p4',
#    'hltCSVPF0p7',
#    'hltVBFPFJetCSVSortedMqq200Detaqq1p2',
#    'hltVBFPFJetCSVSortedMqq460Detaqq4p1',
#    'hltVBFPFJetCSVSortedMqq240Detaqq2p0',
#    'hltVBFPFJetCSVSortedMqq500Detaqq4p6',
#    ]
    
    filters = [
    'hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet',
    'hltQuadJet15',
    'hltTripleJet50',
    'hltDoubleJet65',
    'hltSingleJet80',
    'hltVBFCaloJetEtaSortedMqq150Deta1p5',
    'hltBTagCaloCSVp022Single',
    'hltPFQuadJetLooseID15',
    'hltPFTripleJetLooseID64',
    'hltPFDoubleJetLooseID76',
    'hltPFSingleJetLooseID92',
    'hltBTagPFCSVp016SingleWithMatching',
    'hltBTagPFCSVp11DoubleWithMatching',
    'hltVBFPFJetCSVSortedMqq200Detaqq1p5',
    'hltVBFPFJetCSVSortedMqq240Detaqq2p3',
    'hltVBFPFJetCSVSortedMqq460Detaqq3p5',
    'hltVBFPFJetCSVSortedMqq500Detaqq4p1',

    'hltL1sQuadJetCIorTripleJetVBFIorHTT',
    'hltQuadCentralJet45',
    'hltQuadPFCentralJetLooseID45',

    'hltL1sTripleJetVBFIorHTTIorDoubleJetCIorSingleJet',
    'hltQuadCentralJet30',
    'hltDoubleCentralJet90',
    'hltQuadPFCentralJetLooseID30',
    'hltDoublePFCentralJetLooseID90',

    'hltBTagCaloCSVp087Double',
    'hltBTagCaloCSVp087Triple',

    'hltL1sSingleEG40IorSingleIsoEG22erIorSingleIsoEG24erIorSingleIsoEG24IorSingleIsoEG26',
    'hltJetFilterEle27WPLoose',
    'hltHCand80NoEle27WPLoose',
    'hltWCand80NoEle27WPLooseMET',
    'hltWCand70NoEle27WPLooseMHTIDTight',
#    'hltL1sL1SingleIsoEG22erOrSingleEG25',

#    'hltEGL1SingleIsoEG22erOrSingleEG25Filter',
#    'hltEG27EtL1IsoEG22erOrSingleEG25Filter',
#    'hltEle27WPLooseClusterShapeFilter',
#    'hltEle27WPLooseHEFilter',
#    'hltEle27WPLooseEcalIsoFilter',
#    'hltEle27WPLooseHcalIsoFilter',
#    'hltEle27WPLoosePixelMatchFilter',
#    'hltEle27WPLooseGsfOneOEMinusOneOPFilter',
#    'hltEle27WPLooseGsfChi2Filter',
#    'hltEle27WPLooseGsfMissingHitsFilter',
#    'hltEle27WPLooseGsfDetaFilter',
#    'hltEle27WPLooseGsfDphiFilter',
#    'hltEle27noerWPLooseGsfTrackIsoFilter',

#    'hltEGL1EG25erHTT125ORL1SingleIsoEG30erORL1SingleEG40',
#    'hltEG27EtL1EG25erHTT125ORL1SingleIsoEG30erORL1SingleEG40',
#    'hltEle27noerWPLooseClusterShapeFilter',
#    'hltEle27noerWPLooseHEFilter',
#    'hltEle27erWPLooseEcalIsoFilter',
#    'hltEle272erWPLooseHcalIsoFilter',
#    'hltEle27noerWPLoosePixelMatchFilter',
#    'hltEle27noerWPLooseGsfOneOEMinusOneOPFilter',
#    'hltEle27noerWPLooseGsfChi2Filter',
#    'hltEle27noerWPLooseGsfMissingHitsFilter',
#    'hltEle27noerWPLooseGsfDetaFilter',
#    'hltEle27noerWPLooseGsfDphiFilter',
    'hltEle27noerWPLooseGsfTrackIsoFilter',

	'hltL1sETM50IorETM60IorETM70lorETM80lorETM90lorETM100',
	'hltMET70',
	'hltMHT70',
	'hltPFMHTTightID90',
	'hltPFMET90',

	'hltMET80',
	'hltMHT80',
	'hltPFMHTTightID100',
	'hltPFMET100',

	'hltPFMHTTightID110',
	'hltPFMET110',

	'hltMET90',
	'hltMHT90',

	'hltPFMHTTightID120',
	'hltPFMET120',

	'hltMHTNoPU90',
	'hltBTagCaloCSVp067Single',

    ]

    MC = False
    if len(filesInput)>0 and ('AODSIM' in filesInput[0]):
        MC = True
    print "MC=",MC
    
    btags, btagLabel = Handle("edm::AssociationVector<edm::RefToBaseProd<reco::Jet>,vector<float>,edm::RefToBase<reco::Jet>,unsigned int,edm::helper::AssociationIdenticalKeyReference>"), ("pfCombinedInclusiveSecondaryVertexV2BJetTags") #("pfCombinedSecondaryVertexBJetTags")
    
    if MC:
        btagLabel = ("combinedInclusiveSecondaryVertexV2BJetTags")
        calobjets = calobjetsMC
        pfbjets = pfbjetsMC
    
    ncalobjets = len(calobjets)
    npfbjets = len(pfbjets)

    ##python array types: http://docs.python.it/html/lib/module-array.html
    ##ROOT branch types: https://root.cern.ch/doc/master/classTTree.html
    nVertices = array( 'i', [ 0 ] )
    tree.Branch( 'nVertices', nVertices, 'nVertices/I' )
    run = array( 'L', [ 0 ] )
    tree.Branch( 'run', run, 'run/i' )
    lumi = array( 'L', [ 0 ] )
    tree.Branch( 'lumi', lumi, 'lumi/i' )
    eventNumber = array( 'L', [ 0 ] )
    tree.Branch( 'event', eventNumber, 'event/i' )
    JSON = array( 'i', [ 0 ] )
    tree.Branch( 'JSON', JSON, 'JSON/I' )
    
    caloMet = array( 'f', [ 0 ] )
    tree.Branch( 'caloMet', caloMet, 'caloMet/F' )
    caloMet_phi = array( 'f', [ 0 ] )
    tree.Branch( 'caloMet_phi', caloMet_phi, 'caloMet_phi/F' )
    
    pfMet = array( 'f', [ 0 ] )
    tree.Branch( 'pfMet', pfMet, 'pfMet/F' )
    pfMet_phi = array( 'f', [ 0 ] )
    tree.Branch( 'pfMet_phi', pfMet_phi, 'pfMet_phi/F' )
    
    caloMht = array( 'f', [ 0 ] )
    tree.Branch( 'caloMht', caloMht, 'caloMht/F' )
    caloMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'caloMht_phi', caloMht_phi, 'caloMht_phi/F' )
    
    pfMht = array( 'f', [ 0 ] )
    tree.Branch( 'pfMht', pfMht, 'pfMht/F' )
    pfMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'pfMht_phi', pfMht_phi, 'pfMht_phi/F' )
    
    caloNoPuMht = array( 'f', [ 0 ] )
    tree.Branch( 'caloNoPuMht', caloNoPuMht, 'caloNoPuMht/F' )
    caloNoPuMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'caloNoPuMht_phi', caloNoPuMht_phi, 'caloNoPuMht_phi/F' )
    
    l1Met = array( 'f', [ 0 ] )
    tree.Branch( 'l1Met', l1Met, 'l1Met/F' )
    l1Met_phi = array( 'f', [ 0 ] )
    tree.Branch( 'l1Met_phi', l1Met_phi, 'l1Met_phi/F' )
    l1Met_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'l1Met_sumet', l1Met_sumet, 'l1Met_sumet/F' )
    
    l1Mht = array( 'f', [ 0 ] )
    tree.Branch( 'l1Mht', l1Mht, 'l1Mht/F' )
    l1Mht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'l1Mht_phi', l1Mht_phi, 'l1Mht_phi/F' )
    l1Mht_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'l1Mht_sumet', l1Mht_sumet, 'l1Mht_sumet/F' )
    
    l1Jet_num = array( 'i', [ 0 ] )
    tree.Branch( 'l1Jet_num', l1Jet_num, 'l1Jet_num/I' )
    l1Jet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_pt', l1Jet_pt, 'l1Jet_pt[l1Jet_num]/F' )
    l1Jet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_eta', l1Jet_eta, 'l1Jet_eta[l1Jet_num]/F' )
    l1Jet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_phi', l1Jet_phi, 'l1Jet_phi[l1Jet_num]/F' )
    l1Jet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_mass', l1Jet_mass, 'l1Jet_mass[l1Jet_num]/F' )
    l1Jet_tau = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_tau', l1Jet_tau, 'l1Jet_tau[l1Jet_num]/I' )
    l1Jet_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'l1Jet_offmatch', l1Jet_offmatch, 'l1Jet_offmatch[l1Jet_num]/I' )
    
    l1EG_num = array( 'i', [ 0 ] )
    tree.Branch( 'l1EG_num', l1EG_num, 'l1EG_num/I' )
    l1EG_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1EG_pt', l1EG_pt, 'l1EG_pt[l1EG_num]/F' )
    l1EG_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1EG_eta', l1EG_eta, 'l1EG_eta[l1EG_num]/F' )
    l1EG_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1EG_phi', l1EG_phi, 'l1EG_phi[l1EG_num]/F' )
    l1EG_iso = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'l1EG_iso', l1EG_iso, 'l1EG_iso[l1EG_num]/I' )
    l1EG_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'l1EG_offmatch', l1EG_offmatch, 'l1EG_offmatch[l1EG_num]/I' )
    
    l1Muon_num = array( 'i', [ 0 ] )
    tree.Branch( 'l1Muon_num', l1Muon_num, 'l1Muon_num/I' )
    l1Muon_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Muon_pt', l1Muon_pt, 'l1Muon_pt[l1Muon_num]/F' )
    l1Muon_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Muon_eta', l1Muon_eta, 'l1Muon_eta[l1Muon_num]/F' )
    l1Muon_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'l1Muon_phi', l1Muon_phi, 'l1Muon_phi[l1Muon_num]/F' )
    l1Muon_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'l1Muon_offmatch', l1Muon_offmatch, 'l1Muon_offmatch[l1Muon_num]/I' )
    
    offMet = array( 'f', [ 0 ] )
    tree.Branch( 'offMet', offMet, 'offMet/F' )
    offMet_phi = array( 'f', [ 0 ] )
    tree.Branch( 'offMet_phi', offMet_phi, 'offMet_phi/F' )
    offMet_sig = array( 'f', [ 0 ] )
    tree.Branch( 'offMet_sig', offMet_sig, 'offMet_sig/F' )
    offMet_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'offMet_sumet', offMet_sumet, 'offMet_sumet/F' )
    
    offMht = array( 'f', [ 0 ] )
    tree.Branch( 'offMht', offMht, 'offMht/F' )
    offMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'offMht_phi', offMht_phi, 'offMht_phi/F' )
    offMht_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'offMht_sumet', offMht_sumet, 'offMht_sumet/F' )
    
    offPUPPIMht = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMht', offPUPPIMht, 'offPUPPIMht/F' )
    offPUPPIMht_phi = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMht_phi', offPUPPIMht_phi, 'offPUPPIMht_phi/F' )
    offPUPPIMht_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMht_sumet', offPUPPIMht_sumet, 'offPUPPIMht_sumet/F' )
    
    caloJet_num = array( 'i', [ 0 ] )
    tree.Branch( 'caloJet_num', caloJet_num, 'caloJet_num/I' )
    caloJet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_pt', caloJet_pt, 'caloJet_pt[caloJet_num]/F' )
    caloJet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_eta', caloJet_eta, 'caloJet_eta[caloJet_num]/F' )
    caloJet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_phi', caloJet_phi, 'caloJet_phi[caloJet_num]/F' )
    caloJet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_mass', caloJet_mass, 'caloJet_mass[caloJet_num]/F' )
    caloJet_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'caloJet_offmatch', caloJet_offmatch, 'caloJet_offmatch[caloJet_num]/I' )
    caloJet_btagged ={}
    for calobjet in calobjets:
        caloJet_btagged[calobjet] = array( 'f', maxJets*[ 0 ] )
        tree.Branch( 'caloJet_'+calobjet, caloJet_btagged[calobjet], 'caloJet_'+calobjet+'[caloJet_num]/F' )
    
    pfJet_num = array( 'i', [ 0 ] )
    tree.Branch( 'pfJet_num', pfJet_num, 'pfJet_num/I' )
    pfJet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_pt', pfJet_pt, 'pfJet_pt[pfJet_num]/F' )
    pfJet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_eta', pfJet_eta, 'pfJet_eta[pfJet_num]/F' )
    pfJet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_phi', pfJet_phi, 'pfJet_phi[pfJet_num]/F' )
    pfJet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_mass', pfJet_mass, 'pfJet_mass[pfJet_num]/F' )
    pfJet_offmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'pfJet_offmatch', pfJet_offmatch, 'pfJet_offmatch[pfJet_num]/I' )
    pfJet_btagged ={}
    for pfbjet in pfbjets:
        pfJet_btagged[pfbjet] = array( 'f', maxJets*[ 0 ] )
        tree.Branch( 'pfJet_'+pfbjet, pfJet_btagged[pfbjet], 'pfJet_'+pfbjet+'[pfJet_num]/F' )
    
    offJet_num = array( 'i', [ 0 ] )
    tree.Branch( 'offJet_num', offJet_num, 'offJet_num/I' )
    offJet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_pt', offJet_pt, 'offJet_pt[offJet_num]/F' )
    offJet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_eta', offJet_eta, 'offJet_eta[offJet_num]/F' )
    offJet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_phi', offJet_phi, 'offJet_phi[offJet_num]/F' )
    offJet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_mass', offJet_mass, 'offJet_mass[offJet_num]/F' )
    offJet_csv = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offJet_csv', offJet_csv, 'offJet_csv[offJet_num]/F' )
    offJet_pfmatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'offJet_pfmatch', offJet_pfmatch, 'offJet_pfmatch[offJet_num]/I' )
    offJet_calomatch = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'offJet_calomatch', offJet_calomatch, 'offJet_calomatch[offJet_num]/I' )
    offJet_l1match = array( 'i', maxJets*[ 0 ] )
    tree.Branch( 'offJet_l1match', offJet_l1match, 'offJet_l1match[offJet_num]/I' )

    
    offElectron_num = array( 'i', [ 0 ] )
    tree.Branch( 'offElectron_num', offElectron_num, 'offElectron_num/I' )
    offElectron_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offElectron_pt', offElectron_pt, 'offElectron_pt[offElectron_num]/F' )
    offElectron_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offElectron_eta', offElectron_eta, 'offElectron_eta[offElectron_num]/F' )
    offElectron_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offElectron_phi', offElectron_phi, 'offElectron_phi[offElectron_num]/F' )
    offElectron_iso = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offElectron_iso', offElectron_iso, 'offElectron_iso[offElectron_num]/F' )
    
    offMuon_num = array( 'i', [ 0 ] )
    tree.Branch( 'offMuon_num', offMuon_num, 'offMuon_num/I' )
    offMuon_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offMuon_pt', offMuon_pt, 'offMuon_pt[offMuon_num]/F' )
    offMuon_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offMuon_eta', offMuon_eta, 'offMuon_eta[offMuon_num]/F' )
    offMuon_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offMuon_phi', offMuon_phi, 'offMuon_phi[offMuon_num]/F' )
    offMuon_iso = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offMuon_iso', offMuon_iso, 'offMuon_iso[offMuon_num]/F' )
    
    offPhoton_num = array( 'i', [ 0 ] )
    tree.Branch( 'offPhoton_num', offPhoton_num, 'offPhoton_num/I' )
    offPhoton_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPhoton_pt', offPhoton_pt, 'offPhoton_pt[offPhoton_num]/F' )
    offPhoton_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPhoton_eta', offPhoton_eta, 'offPhoton_eta[offPhoton_num]/F' )
    offPhoton_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPhoton_phi', offPhoton_phi, 'offPhoton_phi[offPhoton_num]/F' )
    offPhoton_iso = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPhoton_iso', offPhoton_iso, 'offPhoton_iso[offPhoton_num]/F' )
    
    
    offPUPPIMet = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMet', offPUPPIMet, 'offPUPPIMet/F' )
    offPUPPIMet_phi = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMet_phi', offPUPPIMet_phi, 'offPUPPIMet_phi/F' )
    offPUPPIMet_sig = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMet_sig', offPUPPIMet_sig, 'offPUPPIMet_sig/F' )
    offPUPPIMet_sumet = array( 'f', [ 0 ] )
    tree.Branch( 'offPUPPIMet_sumet', offPUPPIMet_sumet, 'offPUPPIMet_sumet/F' )
    
    offPUPPIJet_num = array( 'i', [ 0 ] )
    tree.Branch( 'offPUPPIJet_num', offPUPPIJet_num, 'offPUPPIJet_num/I' )
    offPUPPIJet_pt = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_pt', offPUPPIJet_pt, 'offPUPPIJet_pt[offPUPPIJet_num]/F' )
    offPUPPIJet_eta = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_eta', offPUPPIJet_eta, 'offPUPPIJet_eta[offPUPPIJet_num]/F' )
    offPUPPIJet_phi = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_phi', offPUPPIJet_phi, 'offPUPPIJet_phi[offPUPPIJet_num]/F' )
    offPUPPIJet_mass = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_mass', offPUPPIJet_mass, 'offPUPPIJet_mass[offPUPPIJet_num]/F' )
    offPUPPIJet_csv = array( 'f', maxJets*[ 0 ] )
    tree.Branch( 'offPUPPIJet_csv', offPUPPIJet_csv, 'offPUPPIJet_csv[offPUPPIJet_num]/F' )
    
    triggerBits, triggerBitLabel = Handle("edm::TriggerResults"), ("TriggerResults::HLT")
    triggerObjects, triggerObjectLabel  = Handle("std::vector<pat::TriggerObjectStandAlone>"), "selectedPatTrigger"
    triggerPrescales, triggerPrescaleLabel  = Handle("pat::PackedTriggerPrescales"), "patTrigger"
    
    patJets, patJetLabel = Handle("vector<reco::PFJet>"), ("ak4PFJets") #AOD

    l1JetCentrals, l1JetCentralLabel = Handle("vector<l1extra::L1JetParticle>"), ("l1extraParticles:Central") #AOD
    l1JetForwards, l1JetForwardLabel = Handle("vector<l1extra::L1JetParticle>"), ("l1extraParticles:Forward") #AOD
    l1JetTaus, l1JetTauLabel = Handle("vector<l1extra::L1JetParticle>"), ("l1extraParticles:Tau") #AOD
    l1JetIsoTaus, l1JetIsoTauLabel = Handle("vector<l1extra::L1JetParticle>"), ("l1extraParticles:IsoTau") #AOD

    l1EGNonIsos, l1EGNonIsoLabel = Handle("vector<l1extra::L1EmParticle>"), ("l1extraParticles:NonIsolated") #AOD
    l1EGIsos, l1EGIsoLabel = Handle("vector<l1extra::L1EmParticle>"), ("l1extraParticles:Isolated") #AOD

    l1METs, l1METLabel = Handle("vector<l1extra::L1EtMissParticle>"), ("l1extraParticles:MET") #AOD
    l1MHTs, l1MHTLabel = Handle("vector<l1extra::L1EtMissParticle>"), ("l1extraParticles:MHT") #AOD

    l1Muons, l1MuonLabel = Handle("vector<l1extra::L1MuonParticle>"), ("l1extraParticles") #AOD

    patMets, patMetLabel = Handle("vector<reco::PFMET>"), ("pfMet") #AOD
    recoVertexs, recoVertexLabel = Handle("vector<reco::Vertex>"), ("offlinePrimaryVertices") #AOD
    patElectrons, patElectronLabel = Handle("vector<reco::GsfElectron>"), ("gedGsfElectrons") #AOD
    patMuons, patMuonLabel = Handle("vector<reco::Muon>"), ("muons") #AOD
    patPhotons, patPhotonLabel = Handle("vector<reco::Photon>"), ("photons") #AOD
    
    ##load file
    if len(filesInput)==0: return
    events = Events (filesInput)

    ##get triggerNames from the first event
    events.to(0)
    for event in events: break
    event.getByLabel(triggerBitLabel, triggerBits)
    names = event.object().triggerNames(triggerBits.product())
    triggerNames = names.triggerNames()
    for name in triggerNames: name = name.split("_v")[0]
    nTriggers = len(triggerNames)

    triggerEvent, triggerEventLabel = Handle("trigger::TriggerEvent"), ("hltTriggerSummaryAOD::HLT")
#    ##get filters from the first event
#    event.getByLabel(triggerEventLabel, triggerEvent) ## AOD
#    for i in range(triggerEvent.product().sizeFilters()): filters.append(triggerEvent.product().filterLabel(i))
    
    ##
    triggerVars = {}
    for trigger in triggerNames:
        triggerVars[trigger]=array( 'i', [ 0 ] )
        tree.Branch( trigger, triggerVars[trigger], trigger+'/O' )

    filterVars = {}
    for filter_ in filters:
        filterVars[filter_]=array( 'i', [ 0 ] )
        tree.Branch( filter_, filterVars[filter_], filter_+'/I' )
    
    memOld = 0
    ##event loop
    for iev,event in enumerate(events):
        if iev%1000==0:
            print "iev=",iev
            memNew = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            print 'Memory usage: %s (MB)'% (memNew/1000)
            print 'Diff', (memNew-memOld)/1000
            memOld = memNew
        if iev>maxevents: break
        event.getByLabel(triggerBitLabel, triggerBits)
#        event.getByLabel(triggerObjectLabel, triggerObjects)
#        event.getByLabel(triggerPrescaleLabel, triggerPrescales)
        event.getByLabel(triggerEventLabel, triggerEvent) ## AOD
        event.getByLabel(patJetLabel, patJets)
        event.getByLabel(patMetLabel, patMets)
        event.getByLabel(recoVertexLabel, recoVertexs)
        event.getByLabel(patElectronLabel, patElectrons)
        event.getByLabel(patMuonLabel, patMuons)
        event.getByLabel(patPhotonLabel, patPhotons)
        
        ## AOD
        event.getByLabel(btagLabel, btags)

        nVertices[0] = recoVertexs.product().size()
        run[0] = event.eventAuxiliary().run()
        lumi[0] = event.eventAuxiliary().luminosityBlock()
        eventNumber[0] = event.eventAuxiliary().event()
        JSON[0] = goodEvent(event.eventAuxiliary().run(),event.eventAuxiliary().luminosityBlock())
        
        i=0
        offJet_num[0] = 0
        for jet in patJets.product():
            if jet.pt()<20: continue
            if i<maxJets:                
                offJet_pt[i] = jet.pt()
                offJet_eta[i] = jet.eta()
                offJet_phi[i] = jet.phi()
                offJet_mass[i] = jet.mass()
                ## AOD
                offlineCSV = -1.
                for j in range(0,btags.product().size()):
                    jetB = btags.product().key(j).get()
                    dR = deltaR(jetB.eta(),jetB.phi(),jet.eta(),jet.phi())
                    if dR<0.3:
                        offlineCSV = max(0.,btags.product().value(j))
                        break
                
                offJet_csv[i] = offlineCSV
                offJet_num[0] = i + 1
                i+=1
        
        i=0
        offMuon_num[0] = 0
        for muon in patMuons.product():
            if muon.pt()<10: continue
            if i<maxJets:
                offMuon_pt[i] = muon.pt()
                offMuon_eta[i] = muon.eta()
                offMuon_phi[i] = muon.phi()
                offMuon_iso[i] = 0
                offMuon_num[0] = i + 1
                i+=1
        
        i=0
        offElectron_num[0] = 0
        for electron in patElectrons.product():
            if electron.pt()<10: continue
            if i<maxJets:
                offElectron_pt[i] = electron.pt()
                offElectron_eta[i] = electron.eta()
                offElectron_phi[i] = electron.phi()
                offElectron_iso[i] = 0
                offElectron_num[0] = i + 1
                i+=1

        i=0
        offPhoton_num[0] = 0
        for photon in patPhotons.product():
            if photon.pt()<10: continue
            if i<maxJets:
                offPhoton_pt[i] = photon.pt()
                offPhoton_eta[i] = photon.eta()
                offPhoton_phi[i] = photon.phi()
                offPhoton_iso[i] = 0
                offPhoton_num[0] = i + 1
                i+=1
                
        offMet[0] = patMets.product().begin().pt()
        offMet_phi[0] = patMets.product().begin().phi()
        offMet_sumet[0] = patMets.product().begin().sumEt()
        offMet_sig[0] = patMets.product().begin().significance()
        
        MHT2D = ROOT.TVector2()
        jet2D = ROOT.TVector2()
        offMht_sumet[0]=0
        for jet in patJets.product():
            if jet.pt()>pt_min and abs(jet.eta())<eta_max \
            and jet.neutralHadronEnergyFraction()<NHFmax \
            and jet.neutralEmEnergyFraction()<NEMFmax \
            and jet.chargedHadronEnergyFraction()>CHFmin \
            and jet.muonEnergyFraction()<MUFmax \
            and jet.chargedEmEnergyFraction()<CEMFmax \
            and jet.chargedMultiplicity()+jet.neutralMultiplicity()>NumConstMin \
            and jet.chargedMultiplicity()>CHMmin :
                jet2D.SetMagPhi(jet.pt(),jet.phi())
                MHT2D = MHT2D - jet2D
                offMht_sumet[0]+=jet.pt()
        
        offMht[0] = MHT2D.Mod()
        offMht_phi[0] = MHT2D.Phi()
        
        calojetCollection = "hltAK4CaloJetsCorrectedIDPassed"
        calojetCollectionForBtag = "hltSelector8CentralJetsL1FastJet"
        trigObjColl = triggerEvent.product().getObjects()
        collectionKeys = getCollectionKeys(triggerEvent.product(),ROOT.edm.InputTag(calojetCollection,"","HLT"))
        collectionKeysForBtag = getCollectionKeys(triggerEvent.product(),ROOT.edm.InputTag(calojetCollectionForBtag,"","HLT"))
        i=0
        caloJet_num[0] = 0
        for key in collectionKeys:
            caloJet = trigObjColl[key]
            if caloJet.pt()<20: continue
            if i<maxJets:
                caloJet_pt[i] = caloJet.pt()
                caloJet_eta[i] = caloJet.eta()
                caloJet_phi[i] = caloJet.phi()
                caloJet_mass[i] = caloJet.mass()
                caloJet_offmatch[i] = matching(caloJet.eta(),caloJet.phi(),offJet_eta,offJet_phi,offJet_num[0])
                caloJet_num[0] = i+1 
                for calobjet in calobjets:
                    caloJet_btagged[calobjet][i] = -1
                    filterIndex = triggerEvent.product().filterIndex(ROOT.edm.InputTag(calobjet,"","HLT"))
                    if filterIndex < triggerEvent.product().sizeFilters():
                        for key3 in collectionKeysForBtag:
                            jetForBtag = trigObjColl[key3];
                            dR = deltaR(jetForBtag.eta(),jetForBtag.phi(),caloJet.eta(),caloJet.phi())
                            if dR<0.3:
                                caloJet_btagged[calobjet][i] = 0
                                break
                        filterKeys = triggerEvent.product().filterKeys(filterIndex)
                        for key2 in filterKeys:
                            bjet = trigObjColl[key2];
                            dR = deltaR(bjet.eta(),bjet.phi(),caloJet.eta(),caloJet.phi())
                            if dR<0.3:
                                caloJet_btagged[calobjet][i] = 1
                                break
            i+=1
        pfjetCollection = "hltAK4PFJetsCorrected"
        pfjetCollectionForBtag = "hltPFJetForBtag"
        trigObjColl = triggerEvent.product().getObjects()
        collectionKeys = getCollectionKeys(triggerEvent.product(),ROOT.edm.InputTag(pfjetCollection,"","HLT"))
        collectionKeysForBtag = getCollectionKeys(triggerEvent.product(),ROOT.edm.InputTag(pfjetCollectionForBtag,"","HLT"))
        i=0
        pfJet_num[0] = 0
        for key in collectionKeys:
            pfJet = trigObjColl[key]
            if pfJet.pt()<20: continue
            if i<maxJets:
                pfJet_pt[i] = pfJet.pt()
                pfJet_eta[i] = pfJet.eta()
                pfJet_phi[i] = pfJet.phi()
                pfJet_mass[i] = pfJet.mass()
                pfJet_offmatch[i] = matching(pfJet.eta(),pfJet.phi(),offJet_eta,offJet_phi,offJet_num[0])
                pfJet_num[0] = i+1
                for pfbjet in pfbjets:
                    pfJet_btagged[pfbjet][i] = -1
                    filterIndex = triggerEvent.product().filterIndex(ROOT.edm.InputTag(pfbjet,"","HLT"))
                    if filterIndex < triggerEvent.product().sizeFilters():
                        for key3 in collectionKeysForBtag:
                            jetForBtag = trigObjColl[key3];
                            dR = deltaR(jetForBtag.eta(),jetForBtag.phi(),pfJet.eta(),pfJet.phi())
                            if dR<0.3:
                                pfJet_btagged[pfbjet][i] = 0
                                break
                        filterKeys = triggerEvent.product().filterKeys(filterIndex)
                        for key2 in filterKeys:
                            bjet = trigObjColl[key2];
                            dR = deltaR(bjet.eta(),bjet.phi(),pfJet.eta(),pfJet.phi())
                            if dR<0.3:
                                pfJet_btagged[pfbjet][i] = 1
                                break
            i+=1
        
        for i in range(offJet_num[0]):
            offJet_pfmatch[i] = matching(offJet_eta[i],offJet_phi[i],pfJet_eta,pfJet_phi,pfJet_num[0])
            offJet_calomatch[i] = matching(offJet_eta[i],offJet_phi[i],caloJet_eta,caloJet_phi,caloJet_num[0])
        
        caloMETCollection = "hltMet"
        caloMet[0],caloMet_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(caloMETCollection,"","HLT"))
        
        caloMHTCollection = "hltHtMht"
        caloMht[0],caloMht_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(caloMHTCollection,"","HLT"))

        caloNoPuMHTCollection = "hltMHTNoPU"
        caloNoPuMht[0],caloNoPuMht_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(caloNoPuMHTCollection,"","HLT"))

        pfMETCollection = "hltPFMETProducer"
        pfMet[0],pfMet_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(pfMETCollection,"","HLT"))
        
        pfMHTCollection = "hltPFMHTTightID"
        pfMht[0],pfMht_phi[0] = getMET(triggerEvent.product(),ROOT.edm.InputTag(pfMHTCollection,"","HLT"))

        event.getByLabel(l1JetCentralLabel, l1JetCentrals)
        event.getByLabel(l1JetForwardLabel, l1JetForwards)
        event.getByLabel(l1JetTauLabel, l1JetTaus)
        if not MC:
            event.getByLabel(l1JetIsoTauLabel, l1JetIsoTaus)
            l1JetIsoTaus_=l1JetIsoTaus.product()
        else:
            l1JetIsoTaus_=[]
        i=0
        l1Jet_num[0] = 0
        for l1Jet in itertools.chain(l1JetCentrals.product(),l1JetForwards.product(),l1JetTaus.product(),l1JetIsoTaus_):
            l1Jet_pt[i] = l1Jet.pt()
            l1Jet_eta[i] = l1Jet.eta()
            l1Jet_phi[i] = l1Jet.phi()
            l1Jet_mass[i] = l1Jet.mass()
            l1Jet_offmatch[i] = matching(l1Jet.eta(),l1Jet.phi(),offJet_eta,offJet_phi,offJet_num[0])
            l1Jet_tau[i] = 0
            if l1Jet in l1JetTaus.product():
                l1Jet_tau[i] = 1
            if l1Jet in l1JetIsoTaus_:
                l1Jet_tau[i] = 2
            l1Jet_num[0] = i+1
            i+=1

        event.getByLabel(l1MuonLabel, l1Muons)
        i=0
        l1Muon_num[0] = 0
        for l1Muon in itertools.chain(l1Muons.product()):
            l1Muon_pt[i] = l1Muon.pt()
            l1Muon_eta[i] = l1Muon.eta()
            l1Muon_phi[i] = l1Muon.phi()
            l1Muon_offmatch[i] = matching(l1Muon.eta(),l1Muon.phi(),offMuon_eta,offMuon_phi,offMuon_num[0])
            l1Muon_num[0] = i+1
            i+=1

        event.getByLabel(l1EGIsoLabel, l1EGIsos)
        event.getByLabel(l1EGNonIsoLabel, l1EGNonIsos)
        i=0
        l1EG_num[0] = 0
        for l1EG in itertools.chain(l1EGIsos.product(),l1EGNonIsos.product()):
            l1EG_pt[i] = l1EG.pt()
            l1EG_eta[i] = l1EG.eta()
            l1EG_phi[i] = l1EG.phi()
            l1EG_offmatch[i] = matching(l1EG.eta(),l1EG.phi(),offElectron_eta,offElectron_phi,offElectron_num[0]) #ignoring offline photons
            l1EG_iso[i] = 0
            if l1EG in l1EGIsos.product():
                l1EG_iso[i] = 1
            l1EG_num[0] = i+1
            i+=1

        ##[CHECKME] : .At(2) ???
        event.getByLabel(l1METLabel, l1METs)
        l1Met[0] = l1METs.product().at(0).pt()
        l1Met_phi[0] = l1METs.product().at(0).phi()
        l1Met_sumet[0] = l1METs.product().at(0).etTotal()

        event.getByLabel(l1MHTLabel, l1MHTs)
        l1Mht[0] = l1MHTs.product().begin().pt()
        l1Mht_phi[0] = l1MHTs.product().begin().phi()
        l1Mht_sumet[0] = l1MHTs.product().begin().etTotal()

        names = event.object().triggerNames(triggerBits.product())
        for i,triggerName in enumerate(triggerNames):
            index = names.triggerIndex(triggerName)
            if checkTriggerIndex(triggerName,index,names.triggerNames()):
                triggerVars[triggerName][0] = triggerBits.product().accept(index)
            else:
                triggerVars[triggerName][0] = 0
        
        for filter_ in filters:
            filterVars[filter_][0] = getSizeFilter(triggerEvent.product(),ROOT.edm.InputTag(filter_,"","HLT"))
        
#        if triggerVars["HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDLoose_v1"][0]:
#        if triggerVars['HLT_QuadPFJet_SingleBTagCSV_VBF_Mqq500_v2'][0]:
#            printLabelCollections(triggerEvent.product())
#            printLabelFilters(triggerEvent.product())

        tree.Fill()
    
    
    f.Write()
    f.Close()

maxevents=200
fileOutput = 'tree.root'
filesInput=[
"4C7B9F57-6F81-E511-95E4-02163E014438.root",
#"TT_Spring15_AODSIM.root",
]
#launchNtupleFromAOD(fileOutput,filesInput,maxevents)
