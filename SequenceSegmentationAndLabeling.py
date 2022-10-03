import io
import csv
import editdistance


class Parser():
    def __init__(self):
        self.sorcesId = 0
        self.sorces = ""
        self.masechet = ""
        self.chapter = ""
        self.subSequenceTokens = []
        self.subSequenceTags= []
        self.SequenceTagsWithSagesID = []
        self.subSequenceType = 0
        self.subSequencePatternID=0
        self.startIndex=0
        self.endIndex=0

class Corpus():
    def __init__(self):
        self.sorces = ""
        self.SequenceTokens = []
        self.SequenceTags= []
        self.SequenceTagsWithSagesID = []

class predicateDependencies():
    def __init__(self):
        self.predicateName=""
        self.dependencies=[]
        self.featureADJ=""
        self.featureVERB=""
        self.mustDependencyForPredicate=""


class TypeOFRelationship():
    def __init__(self):
        self.pairOFSequences=[]
        self.pairOFSequencesType=[]
        self.pairOFSequencesFeature=[]


class Sorces():
    def __init__(self):
        self.sederID = 0
        self.sederHeb = ""
        self.sederEng = ""
        self.masechetID = 0
        self.masechetHeb = ""
        self.masechetEng = ""


class Couple():
    def __init__(self):
        self.sorces = ""
        self.masechet = ""
        self.chapter = ""
        self.id1 = ""
        self.id1 = ""
        self.id2 = ""
        self.name1=""
        self.name2 = ""
        self.relationType = ""

class clsTanaim():
    def __init__(self):
        self.id = 0
        self.preffix = ""
        self.firstName = ""
        self.lastName = ""
        self.genaration = 0
        self.nickname = ""
        self.isTana = 0
        self.References = []


#=================================================================== reader

def reader():

    # read Tanaim Lexicon
    f_lex = pathReferenceFiles + "\\TanaimLex.csv"
    with open(f_lex,encoding="utf-8-sig", newline='') as csvfile:
        Lex = csv.DictReader(csvfile)
        for row in Lex:
            colToken.append(row['token'])
            colTags.append(row['pos'])
            colFeatures.append(row['features'])
            colLemmas.append(row['lemma'])
    #=====================================================================ToseftaTokensTags
    f_corpusT = pathfindings + "\\ToseftaTokensTags.csv"
    colCorpusT = []
    with open(f_corpusT,encoding="utf-8-sig", newline='') as csvfile:
        corpusT = csv.DictReader(csvfile)

        for row in corpusT:
            co = Corpus()
            co.sorces = row['sorces']
            for i, word in enumerate(row['SequenceTokens'].split(" ")):
                co.SequenceTokens.append(word)
            for i, word in enumerate(row['SequenceTags'].split(" ")):
                co.SequenceTags.append(word)

            for i, word in enumerate(row['SequenceTagsWithSagesID'].split(",")):
                co.SequenceTagsWithSagesID.append(word)
            colCorpusT.append(co)

    #====================================================================MishnaTokensTags
    # read MishnaTokensTags
    f_corpusM = pathfindings + "\\MishnaTokensTags.csv"
    colCorpusM = []
    with open(f_corpusM,encoding="utf-8-sig", newline='') as csvfile:
        corpusM = csv.DictReader(csvfile)

        for row in corpusM:
            co = Corpus()
            co.sorces = row['sorces']
            for i, word in enumerate(row['SequenceTokens'].split(" ")):
                co.SequenceTokens.append(word)
            for i, word in enumerate(row['SequenceTags'].split(" ")):
                co.SequenceTags.append(word)

            for i, word in enumerate(row['SequenceTagsWithSagesID'].split(",")):
                co.SequenceTagsWithSagesID.append(word)
            colCorpusM.append(co)

    #=============================================================
    f_TanaimList = pathReferenceFiles + "\\TanaimList.csv"
    colTanaimList = []
    with open(f_TanaimList,encoding="utf-8-sig", newline='') as csvfile:
        TanaimListSa = csv.DictReader(csvfile)

        for row in TanaimListSa:
            ro = clsTanaim()
            if int(row['id']) > 0:
                ro.id = row['id']
                ro.preffix = row['preffix']
                ro.firstName = row['firstName']
                ro.lastName = row['lastName']
                ro.nickname = row['nickname']
                ro.isTana = row['isTana']
                ro.genaration = row['genaration']

                colTanaimList.append(ro)
     #========================================================
    f_SederMasechetTab = pathReferenceFiles + "\\SederMasechetTab.csv"
    colSorces = []
    with open(f_SederMasechetTab,encoding="utf-8-sig", newline='') as csvfile:
        SederMasechetTab = csv.DictReader(csvfile)

        for row in SederMasechetTab:
            re = Sorces()
            re.sederID = row['sederID']
            re.sederHeb = row['sederHeb']
            re.sederEng = row['sederEng']
            re.masechetID = row['masechetID']
            re.masechetHeb = row['masechetHeb']
            re.masechetEng = row['masechetEng']
            colSorces.append(re)


    #=====================================find Dependencies of predicate for sequence segmantion
    #pd.featureVERB = "imp"
    pd=predicateDependencies()
    pd.predicateName="NNT"
    pd.dependencies=["ADJ","PROPN"]
    pd.featureADJ="preffix"
    colPDSS.append(pd)
    #===================================
    pd = predicateDependencies()
    pd.predicateName = "ADJ"
    pd.dependencies = ["PROPN"]
    pd.featureADJ = "preffix"
    colPDSS.append(pd)
    # ===================================
    pd = predicateDependencies()
    pd.predicateName = "ADJ"
    pd.dependencies = ["VERB"]
    pd.featureADJ = "suffix"
    colPDSS.append(pd)
    # ===================================
    pd = predicateDependencies()
    pd.predicateName = "PROPN"
    pd.dependencies = ["NN", "ADJ","VERB","CC"]
    pd.featureADJ = "suffix"
    #pd.mustDependencyForPredicate ="VERB"
    colPDSS.append(pd)
    # ===================================
    pd = predicateDependencies()
    pd.predicateName = "NP"
    pd.dependencies = ["ADJ", "VERB"]
    pd.featureADJ = "suffix"
    colPDSS.append(pd)
    # ===================================
    pd = predicateDependencies()
    pd.predicateName = "NN"
    pd.dependencies = ["NP", "ADJ"]
    pd.featureADJ = "preffix"
    colPDSS.append(pd)
    # ===================================
    pd = predicateDependencies()
    pd.predicateName = "VERB"
    pd.dependencies = ["ADJ", "PROPN","PRON"]
    pd.featureADJ = "preffix"
    pd.mustDependencyForPredicate="PROPN"
    colPDSS.append(pd)
    #====================================
    pd = predicateDependencies()
    pd.predicateName = "PRON"
    pd.dependencies = ["ADJ", "PROPN"]
    pd.featureADJ = "preffix"
    colPDSS.append(pd)

    #============================================== find Dependencies of predicate for sequence labeling
    pd = predicateDependencies()
    pd.predicateName = "NNT"
    pd.dependencies = ["ADJ", "PROPN"]
    pd.featureADJ = "preffix"
    colPDSL.append(pd)

    # ===================================
    pd = predicateDependencies()
    pd.predicateName = "PROPN"
    pd.dependencies = ["CCONJ","ADJ","NN","CC","NP","VERB"]
    pd.featureADJ = "suffix"
    colPDSL.append(pd)
    # ===================================
    pd = predicateDependencies()
    pd.predicateName = "PROPN"
    pd.dependencies = ["STORY", "ADJ", "NN", "CC","NP"]
    pd.featureADJ = "preffix"
    colPDSL.append(pd)

    #=====================================
    pd = predicateDependencies()
    pd.predicateName = "VERB"
    pd.dependencies = ["PROPN", "ADJ","PRON"]
    pd.featureADJ = "preffix"
    colPDSL.append(pd)


    # ====================================
    pd = predicateDependencies()
    pd.predicateName = "VERB"
    pd.dependencies = ["STORY"]
    colPDSL.append(pd)

    #=====================================================================TypeOFRelationship()
    #1= disagree
    #2= cited
    #3= agree
    #4= indirectly disagree with tana kama
    #9=DependingFeature

    tr.pairOFSequences=    ["1-3","1-4","3-3","5-3","7-3","6-66","4-3","8-2","4-4","3-6"]
    tr.pairOFSequencesType=["1"   ,"1" ,"9"  ,"1"   ,"3",   "2",  "1","4","1","1"]
    tr.pairOFSequencesFeature=["","","lemma","","","",""]
    # NO INSERT  3-4   ,  3-1  ,

    return colCorpusT,colCorpusM,colFeatures,colLemmas,colToken,colTags,colPDSS,colPDSL,tr,colTanaimList,colSorces

#=================================================================== isIncolLemma
def isIncolLemma(token):
    col=""
    if token in colToken:
        col=colLemmas[colToken.index(token)]
    else:
        #token= cleanApostrophes(token)
        if token in colToken:
            col = colLemmas[colToken.index(token)]
    return col
#====================================================================
def fillInData(ps,word,tag,tagSage,sorce,sourceId):
 ps.subSequenceTokens.append(word)
 ps.subSequenceTags.append(tag)
 ps.SequenceTagsWithSagesID.append(tagSage)
 ps.sorces = sorce
 ps.sorcesId = sourceId
#==================================================================]
def isEmptyList(lst,i):
    try:
        if len(lst)<2:
            return ""
        if i >len(lst):
          return "" # lst[i-1]
        return lst[i]
    except Exception as e:
        print(e)


#===================================================================doSequenceSegmantation
def doSequenceSegmantation(colParser,colCorpus):
    sourceId = 0
    for co in colCorpus:
        sorce = ""
        sourceId=sourceId+1
        idx = 0
        ps = Parser()
        ps.startIndex = idx
        while idx < len(co.SequenceTokens)-1 :
            if "8:5" in sorce and "Arak" in sorce:
               print(idx)
            word = co.SequenceTokens[idx]
            tag = co.SequenceTags[idx]

            tagSage = isEmptyList(co.SequenceTagsWithSagesID,idx)
            ps.sorcesId=sourceId
            if idx < 2:
                sorce = sorce + word
                idx = idx + 1
            else:
                ps.masechet,ps.chapter=getSource(co)

                #Ber 2:3
                if (tag == "SVO" and co.SequenceTags[idx + 1] not in ["SVO1"]) and (
                        (co.SequenceTags[idx + 1] in ["VERB", "PROPN", "ADJ"]) or ("PROPN" in ps.subSequenceTags)):# and co.SequenceTags[idx+1] not in ["SVO1"]):

                    fillInData(ps, word, tag, tagSage, sorce,sourceId)
                    ps.sorces = sorce
                    ps.endIndex = idx
                    colParser.append(ps)
                    ps = Parser()
                    ps.startIndex = idx + 1
                elif tag == "CC" and ("PROPN" in ps.subSequenceTags)and co.SequenceTags[idx+1] in ["ADJ","PROPN"]:
                    fillInData(ps, word, tag, tagSage, sorce,sourceId)
                    ps.sorces = sorce
                    ps.endIndex = idx
                    colParser.append(ps)
                    ps = Parser()
                    ps.startIndex = idx + 1
                #while the tag equal this list of tags it hars to cut the previous sequence
                elif (tag in ["NNT", "PROPN","ADJ"])\
                    or (tag=="VERB" and not(isIncolFeatures("imp=yes",word))):

                    if chkDependencies2(co, idx)==True:


                        if tag in ["VERB","PROPN", "ADJ"]and len(ps.subSequenceTags)>1:

                            ps.endIndex =idx
                            colParser.append(ps)
                            ps = Parser()
                            ps.startIndex = idx + 1

                        res, i = addDependencies(co, idx, ps, sourceId)

                        if len(colParser) - 1 > 0:
                            if "PROPN"  in colParser[len(colParser) - 1].subSequenceTags and "PROPN"  in ps.subSequenceTags and \
                                    "VERB" in colParser[len(colParser) - 1].subSequenceTags and "VERB" in ps.subSequenceTags:
                                ind1=(colParser[len(colParser) - 1]).subSequenceTags.index("PROPN")
                                ind2= ps.subSequenceTags.index("PROPN")
                                if  editdistance.eval( (colParser[len(colParser) - 1]).subSequenceTokens[ind1] , ps.subSequenceTokens[ind2])==0:

                                    ps1, ps2 = splitSubSequence(colParser[len(colParser) - 1], sourceId)
                                    colParser.pop(len(colParser) - 1)
                                    colParser.append(ps1)
                                    colParser.append(ps2)
                                    idx = i

                        nSages = "".join(ps.subSequenceTags).count('PROPN')
                        if nSages > 1:
                            ps1, ps2 = splitSubSequence(ps,sourceId)
                            colParser.append(ps1)
                            ps=ps2
                            colParser.append(ps)
                            idx = i

                        elif res ==2:  #end ps
                            ps.endIndex = i
                            ps.sorces = sorce
                            colParser.append(ps)
                            idx=i
                        elif res==3: #"SVO"
                            ps.endIndex = i
                            colParser.append(ps)
                            ps = Parser()
                            ps.startIndex = i + 1
                            idx = i
                        elif res == 4:
                            if tag == "NNT":
                                ps.endIndex = i
                                colParser.append(ps)
                                ps = Parser()
                                ps.startIndex = i + 1
                            idx = i

                    else:
                        fillInData(ps, word, tag, tagSage, sorce,sourceId)
                else:
                    fillInData(ps, word, tag, tagSage,sorce,sourceId)


                idx = idx + 1


        if idx == len(co.SequenceTokens)-1 and ps.endIndex ==0:
            fillInData(ps, co.SequenceTokens[idx], co.SequenceTags[idx], isEmptyList(co.SequenceTagsWithSagesID,idx), sorce,sourceId)

            ps.endIndex = idx
            colParser.append(ps)
    return  colParser

#======================================================================splitSubSequence(ps)
def splitSubSequence(ps,sourceId):
   ps1 = Parser()
   ps2 = Parser()
   ind=0
   ps1.startIndex=ps.startIndex
   for idx in range(len(ps.subSequenceTags)):
       if ps.subSequenceTags[idx]!="NONE" and ind <2:
           fillInData(ps1, ps.subSequenceTokens[idx], ps.subSequenceTags[idx],isEmptyList(ps.SequenceTagsWithSagesID, idx), ps.sorces, sourceId)
       elif ind <2:
           ind = ind + 1
           fillInData(ps1, ps.subSequenceTokens[idx], ps.subSequenceTags[idx], isEmptyList(ps.SequenceTagsWithSagesID, idx),ps.sorces, sourceId)
       else:
           ps1.endIndex=ps1.startIndex + len(ps1.subSequenceTags)
           ps2.startIndex=ps1.endIndex+1
           fillInData(ps2, ps.subSequenceTokens[idx], ps.subSequenceTags[idx], isEmptyList(ps.SequenceTagsWithSagesID,idx),ps.sorces,sourceId)

   ps2.endIndex=idx
   return ps1,ps2
#======================================================================chkDependencies2
def chkDependencies2(co, idx):
    i=idx
    predicateTag = co.SequenceTags[idx]
    predicateToken = co.SequenceTokens[idx]
    colDependenciesOfSubsequenceTags=[]
    for id, pd in enumerate(colPDSS):
        flag = 0
        idx=i
        try:
            j, res = isFitPredicate(predicateTag, predicateToken,pd,id)

            if res:
                idx = idx + 1
                while flag==0 and idx < len(co.SequenceTags):

                    dependencyTag = co.SequenceTags[idx]
                    dependencyToken = co.SequenceTokens[idx]

                    if dependencyTag in colPDSS[j].dependencies  and isFitDependencies(predicateTag,
                                                                                       predicateToken,
                                                                                       dependencyTag,
                                                                                       dependencyToken):
                        colDependenciesOfSubsequenceTags.append(dependencyTag)
                        try:
                            if (colPDSS[j].mustDependencyForPredicate in colDependenciesOfSubsequenceTags) or (colPDSS[j].mustDependencyForPredicate == ""):
                                return True

                        except Exception as e:
                            print(e)
                    else:
                        flag=1
                    idx = idx + 1
        except Exception as e:
            print(e)
    return False
#======================================================================
def addDependencies(co, idx, ps, sourceId):
    i = idx
    flag = 0
    id = 0
    fillInData(ps, co.SequenceTokens[idx], co.SequenceTags[idx],
               isEmptyList(co.SequenceTagsWithSagesID, idx), co.sorces, sourceId)

    while flag == 0 and idx < len(co.SequenceTags)-1:
        if id == len(colPDSS):
            flag=1
        else:
            id = 0
            found = 0
        predicateTag = co.SequenceTags[idx]
        predicateToken = co.SequenceTokens[idx]
        dependencyTag = co.SequenceTags[idx+1]
        dependencyToken = co.SequenceTokens[idx+1]

        while id < len(colPDSS) and found==0:
              pd=colPDSS[id]
              j, res = isFitPredicate(predicateTag, predicateToken, pd, id)
              if res:
                     if dependencyTag in colPDSS[j].dependencies :

                             if (dependencyTag == "ADJ" and isIncolFeatures(pd.featureADJ + "=yes", dependencyToken))or \
                                     (dependencyTag != "ADJ" ):

                                         fillInData(ps, dependencyToken,dependencyTag,isEmptyList(co.SequenceTagsWithSagesID, idx+1), co.sorces, sourceId)
                                         idx = idx + 1
                                         found=1

                             else:

                                 #idx = idx - 1
                                 flag = 1
                                 found = 1

                     else:
                        # idx = idx - 1
                         flag = 1
                         found = 1
              else:
                      id=id+1


             # idx = idx + 1



    if i == idx:  # its not work with dependencies
        return 1, idx
    if (idx >= len(co.SequenceTags) - 1):  # end of co.SequenceTags
        return 2, idx - 1
    else:
        tag = co.SequenceTags[idx]
        if tag == "SVO":
            fillInData(ps, co.SequenceTokens[idx], co.SequenceTags[idx], isEmptyList(co.SequenceTagsWithSagesID, idx),
                       co.sorces, sourceId)
            return 3, idx
        # if tag == "VERB":  #only imp=yes
        #     return 5, idx
        else:
            return 4, idx


# ===========================================================
def addDependencies2(co, idx, ps,sourceId):
     i=idx
     found = 0
     fillInData(ps, co.SequenceTokens[idx], co.SequenceTags[idx], isEmptyList(co.SequenceTagsWithSagesID, idx),co.sorces,sourceId)
     colDependenciesOfSubsequenceTags = []
     predicateTag = co.SequenceTags[idx]
     predicateToken = co.SequenceTokens[idx]
     for id, pd in enumerate(colPDSS):
         flag = 0
         if found==0:
             idx=i

             j,res= isFitPredicate(predicateTag,predicateToken,pd,id)

             if res:
                 idx = idx + 1
                 while flag == 0 and idx < len(co.SequenceTags):



                     dependencyTag=co.SequenceTags[idx]
                     dependencyToken = co.SequenceTokens[idx]

                     if dependencyTag in colPDSS[j].dependencies and isFitDependencies(predicateTag,
                                                                                       predicateToken,
                                                                                       dependencyTag,
                                                                                       dependencyToken):
                         if dependencyTag=="ADJ"  and isIncolFeatures("preffix=yes", dependencyToken)and\
                             dependencyTag in colDependenciesOfSubsequenceTags:
                                 idx = idx - 2  # -1
                                 flag = 1
                         else:
                                 colDependenciesOfSubsequenceTags.append(dependencyTag)

                                 fillInData(ps, co.SequenceTokens[idx], co.SequenceTags[idx], isEmptyList(co.SequenceTagsWithSagesID,idx),co.sorces,sourceId)
                                 found=1
                     else:
                         idx=idx-2  #-1
                         flag=1

                     idx = idx + 1



     if i == idx:  # its not work with dependencies
         return 1, idx
     if (idx >= len(co.SequenceTags) - 1) :  # end of co.SequenceTags
         return 2, idx - 1
     else:
         tag = co.SequenceTags[idx]
         if tag == "SVO":
             fillInData(ps, co.SequenceTokens[idx], co.SequenceTags[idx], isEmptyList(co.SequenceTagsWithSagesID,idx),co.sorces,sourceId)
             return 3, idx
        # if tag == "VERB":  #only imp=yes
        #     return 5, idx
         else:
             return 4, idx


#===========================================================
def isFitDependencies(predicateTag, predicateToken, dependencyTag, dependencyToken):
    for id, pd in enumerate(colPDSS):
        if pd.predicateName == predicateTag and isFitPredicate(predicateTag, predicateToken,pd,id):

            if dependencyTag == "ADJ":
                if pd.featureADJ == "":
                    return True
                if isIncolFeatures(pd.featureADJ + "=yes", dependencyToken):
                    return True

            else:
                return True
    return False
#===========================================================
def isFitPredicate(predicateTag,predicateToken,pd,idx):

     if pd.predicateName == predicateTag:
         if predicateTag=="ADJ":
             if pd.featureADJ=="":
                 return idx, True
             if isIncolFeatures(pd.featureADJ+"=yes", predicateToken):
                 return idx, True
         else:
             return idx, True
     return 0, False
#===================================================================

def findDependenciesOFcolPDSL(predicateTag,dependencyTag):
    for pd in colPDSL:
        if pd.predicateName == predicateTag and dependencyTag in pd.dependencies:
            return pd.dependencies
#=================================================================== doSequenceLabeling
def isFitLabeling(predicateTag,dependencyTag,ps):

    if predicateTag in ps.subSequenceTags:
        idx = ps.subSequenceTags.index(predicateTag)
        dependencies=findDependenciesOFcolPDSL(predicateTag,dependencyTag)
        while idx < len(ps.subSequenceTags) - 1:
           dTag = ps.subSequenceTags[idx + 1]
           if dTag in dependencies:

                  if dTag == dependencyTag:
                      return True
                  else:
                      idx = idx + 1
           else:
              return False



#==================================================================
def doSequenceLabeling(colParser):
    # subSequenceType keys:
    # 1= tanaKama         (disAgree)
    # 2= case/accepted/story
    # 3= tana omer        disAgree/agree
    # 4= omer tana       (disAgree)
    # 44= amar lo tana   (disAgree)
    # 5= divrei tana     (disAgree)
    # 6=CC               (cited)
    #66= PROPN Accompanied אם CC
    # 7= propn and propn (agree)
    # 8= CC but disagree with tanaKama

    colsubParser=[]
    sorcesId=1
    for idx,ps in enumerate(colParser):
        if "Ber" in ps.sorces and "2:2" in ps.sorces:
            print("100")

        if isFitLabeling("PROPN", "CC", ps):
            ps.subSequenceType = 6
        elif isFitLabeling("NNT", "PROPN", ps):
            ps.subSequenceType = 5
        elif isFitLabeling("PROPN", "STORY", ps) or isFitLabeling("VERB", "STORY", ps):
            ps.subSequenceType = 2

        elif isFitLabeling("PROPN", "CCONJ", ps) and ps.subSequenceTags.index("CCONJ")== len(ps.subSequenceTags)-1:
            ps.subSequenceType = 7
        elif isFitLabeling("PROPN", "VERB", ps):
            ps.subSequenceType = 3
        elif isFitLabeling("VERB","PROPN",  ps):
            ps.subSequenceType = 4

        elif "SVO" in ps.subSequenceTags :
            ps.subSequenceType =1

        elif 'ADV' in ps.subSequenceTags and 'VP' in ps.subSequenceTags:#question & answer
            i = ps.subSequenceTags.index('ADV')
            if isIncolFeatures("int=yes", ps.subSequenceTokens[i]):
                ps.subSequenceType = 1

        elif 'ADV' in ps.subSequenceTags: #question only
            i=ps.subSequenceTags.index('ADV')
            if isIncolFeatures("int=yes",ps.subSequenceTokens[i]):
                ps.subSequenceType = 2

        elif "VERB" in ps.subSequenceTags and isIncolFeatures("imp=yes", ps.subSequenceTokens[ps.subSequenceTags.index("VERB")]):
            ps.subSequenceType = 1


        if ps.sorcesId==sorcesId:
            colsubParser.append(ps)
        else:
            #chk with 2 Related Sequence
            LabelRelatedSequence(colsubParser)

            colsubParser=[]
            colsubParser.append(ps)
            sorcesId = ps.sorcesId

#=================================================================== LabelSequenceType

def LabelRelatedSequence(col):

  for idx, co in enumerate(col):
     print("Labelsorces=" +co.sorces)
     flag = 0
     if len(col)==1 and ("STORY" in  co.subSequenceTags):
         co.subSequenceType = 2
         flag=1
     if flag == 0 and idx > 0:

         if col[idx - 1].subSequenceType == 6 :
             if  "PROPN" in co.subSequenceTags:
                 co.subSequenceType = 66
                 flag = 1
             else:
                 token=col[idx-1].subSequenceTokens[col[idx-1].subSequenceTags.index("CC")]
                 if isIncolFeatures("tk=yes", token):
                     col[idx - 1].subSequenceType =8
                     co.subSequenceType = 2
                     flag = 1
                 else:

                     if isFitLabeling("PROPN", "VERB", col[idx - 1]):
                         col[idx - 1].subSequenceType = 3
                     elif isFitLabeling("VERB", "PROPN", col[idx - 1]):
                         col[idx - 1].subSequenceType = 4
                     co.subSequenceType = 2
                     flag = 1

     if flag == 0 and idx == len(col) - 1:
         if co.subSequenceType == 6 :
             if isFitLabeling("PROPN", "VERB", co):
                 co.subSequenceType = 3
             elif isFitLabeling("VERB", "PROPN", co):
                 co.subSequenceType = 4
             flag = 1

     #if there is one sage disagree in mishna, the rest sequences that came before, are tana kama
     if co.subSequenceType == 0 and flag == 0 and idx==0 and  len(col)>1:
        #======================
        if chkIfSameSageInCol(col):
           lableSequenceAsTK(col)
        #======================
        else:
            if idx < len(col) - 1:
               if col[idx + 1].subSequenceType in [3,4] and  len(col)==2:
                   co.subSequenceType=1
                   flag = 1
            if len(col)>2 and flag == 0:
               if col[idx + 1].subSequenceType in [3,6] and  col[idx + 2].subSequenceType!=3:
                   co.subSequenceType=1
                   flag = 1

     # compare between 2 sequence
     if co.subSequenceType==0 and flag==0:
        if flag==0 and idx < len(col)-1:
            if ("VP" in co.subSequenceTags and "VP" in  col[idx+1].subSequenceTags):
               t1= co.subSequenceTokens[co.subSequenceTags.index("VP")]
               t2= col[idx+1].subSequenceTokens[col[idx+1].subSequenceTags.index("VP")]
               if isIncolLemma(t1)==isIncolLemma(t2):
                   co.subSequenceType = 1
                   flag = 1


     if flag == 0 and idx < len(col) - 1:
        for i,tag in enumerate(co.subSequenceTags):
            if tag=="VERB" and isIncolFeatures("tk=yes", co.subSequenceTokens[0]) and co.subSequenceType ==0:
                co.subSequenceType = 1
                flag = 1


            elif tag=="VERB" and isIncolFeatures("imp=yes", co.subSequenceTokens[i]) and co.subSequenceType ==0:
                co.subSequenceType = 1
                flag = 1

     if flag == 0 and co.subSequenceType == 0:
         co.subSequenceType = 2
#=====================================================================lableSequenceAsTK(col)
def lableSequenceAsTK(col):
    for idx, pss in enumerate(col):
        if pss.subSequenceType==0 and idx < len(col)-1:
            pss.subSequenceType=1
        elif  pss.subSequenceType==0:
            pss.subSequenceType = 2

#====================================================================chkIfSameSageInCol
def chkIfSameSageInCol(col):
    """
      try:
      except Exception as e:
        print(e)
    """
    isSameSage = True
    idSage = "0"
    for idx, pss in enumerate(col):
        if isSameSage == True:
           if "PROPN" in pss.subSequenceTags:
              iSage = pss.subSequenceTags.index("PROPN")
              id = getNum(pss.SequenceTagsWithSagesID[iSage])
              if idSage == "0":
                idSage = id
              elif id != idSage:
                isSameSage = False
    return isSameSage
#====================================================================isIncolFeatures

def isIncolFeatures(s,token):
    if token in colToken:
        col=colFeatures[colToken.index(token)]
        for feature in s.split("|"):
            if  str(col).find(feature)== -1:      #feature not in col:
                return False
        return True
    else:
        return False
#===========================================================================
def extractNumFromStr(str):
    return [int(s) for s in str.split() if s.isdigit()]
#============================================================
def convert_first_to_generator(int_arr):
    return (str(w) for w in int_arr)
#====================================================================doPairCouples
def getNum(str):
    num=""
    if "PROPN" in str:
        return "1000"
    for s in str:
        if s.isdigit():
            num=num + s
    if num.isdigit():
        return num

    return "0"
#====================================================================
def tagginSourceOfMishna(co, i, word):
    if i == 0:
        co.SequenceTags.append("Masechet")
        co.sorces = co.sorces + word
        co.SorcesMasechet = word
    elif i == 1:
        co.mishnaTags.append("Chapter-MishnaUnit")
        co.sorces = co.sorces + word
        co.SorcesChapter = word

def getSource(co):
    i_masechet=co.SequenceTags.index("Masechet")
    i_chapter=co.SequenceTags.index("Chapter-MishnaUnit")
    return co.SequenceTokens[i_masechet],co.SequenceTokens[i_chapter]


#====================================================================
def doCouples(colParser):
    colCouple = []
    colsubParser = []
    colSequenceType=[]
    couple = Couple()
    sorcesId = 1
    nPROPN=0
    colUsedSages=[]
    for idx, ps in enumerate(colParser):
        if "Kil" in ps.sorces and "1:12" in ps.sorces:
            print("")
        if ps.sorcesId==sorcesId:
            colsubParser.append(ps)
            colSequenceType, nPROPN = chkHazalCouple(colSequenceType, ps, nPROPN)

        elif len(colSequenceType)==1 and nPROPN==1:
           # find couple of hazal and sage
           couple =createCoupleWithHazal(colsubParser)
           if couple!=[]:
              colCouple.append(couple)
           sorcesId = ps.sorcesId
           colsubParser = []
           colSequenceType = []
           nPROPN = 0
           colsubParser.append(ps)
           colSequenceType, nPROPN = chkHazalCouple(colSequenceType, ps, nPROPN)
        else:

            for i,pss in enumerate(colsubParser):

                if i < len(colsubParser)-1:
                    st= str(pss.subSequenceType) + "-" + str(colsubParser[i+1].subSequenceType)
                    if st in tr.pairOFSequences:
                        couple=createCouple(i,1, st, pss, colsubParser)

                        if couple.id1!= couple.id2 and couple.id1!="9999" and couple.id2!="9999":
                          if  couple.id2 not in colUsedSages:
                               colCouple.append(couple)
                               colUsedSages.append(couple.id1)

                        if chkIfAnotherCouple(i,colsubParser):
                           st = str(pss.subSequenceType) + "-" + str(colsubParser[i + 2].subSequenceType)
                           couple=createCouple(i,2, st, pss, colsubParser)
                           if couple.id1!= couple.id2 and couple.id1!="9999" and couple.id2!="9999":
                               if couple.id2 not in colUsedSages:
                                   colCouple.append(couple)
                                   colUsedSages.append(couple.id1)

            sorcesId=ps.sorcesId
            colsubParser = []
            colSequenceType=[]
            colUsedSages=[]
            nPROPN=0
            colsubParser.append(ps)
            colSequenceType, nPROPN=chkHazalCouple(colSequenceType,ps,nPROPN)
    return colCouple


def chkHazalCouple(colSequenceType,ps,nPROPN):

    if ps.subSequenceType in [1, 3, 4, 44, 5, 6, 66, 7]:
        colSequenceType.append(ps.subSequenceType)

    if "PROPN" in ps.subSequenceTags:
        nPROPN =nPROPN+ 1

    return colSequenceType,nPROPN

def createCoupleWithHazal(colsubParser):
    couple = Couple()

    for pss in colsubParser:
        if "PROPN" in pss.subSequenceTags:
            ind = pss.subSequenceTags.index("PROPN")
            if not (isIncolFeatures("Number=Plur", pss.subSequenceTokens[ind])):
               iSage1 = pss.subSequenceTags.index("PROPN")
               couple.id1 = getNum(pss.SequenceTagsWithSagesID[iSage1])
               couple.name1 = getNameOfSage(couple.id1)
               couple.relationType = "1"
               couple.id2 = "1000"
               couple.name2 = getNameOfSage(couple.id2)
               couple.sorces = pss.sorces
               couple.masechet = pss.masechet
               couple.chapter = pss.chapter
               return couple

        return []


#===================================================================chkIfAnotherCouple
def chkIfAnotherCouple(i,colsubParser):

    if i < len(colsubParser) - 2:
        if colsubParser[i].subSequenceType in [3,4,5]:
           st = str(colsubParser[i].subSequenceType) + "-" + str(colsubParser[i + 2].subSequenceType)
           if st in tr.pairOFSequences:
               return True
    return False
#===================================================================
def createCoupleNEW(i,j,st,pss,colsubParser):
    couple = Couple()
    couple.masechet = pss.masechet
    couple.chapter = pss.chapter
    iType = tr.pairOFSequences.index(st)

    if tr.pairOFSequencesType[iType] == "9":
        if isIncolLemma(pss.subSequenceTokens[pss.subSequenceTags.index("VERB")]) == isIncolLemma(
                colsubParser[i + j].subSequenceTokens[colsubParser[i + j].subSequenceTags.index("VERB")]) \
                and isIncolLemma(pss.subSequenceTokens[pss.subSequenceTags.index("VERB")]) != "":
            couple.relationType = "3"
        else:
            couple.relationType = "1"

    else:
        couple.relationType = tr.pairOFSequencesType[iType]


    if  pss.subSequenceType==1:
        couple.id1 = "1001"  #tanaKama
        iSage2 = colsubParser[i + j].subSequenceTags.index("PROPN")
        couple.id2 = getNum(colsubParser[i + j].SequenceTagsWithSagesID[iSage2]) if colsubParser[
                                                                                          i + j].subSequenceType > 1 else "1001"

    elif tr.pairOFSequencesType[iType] == "4":
        couple.id2 = "1001"  #tanaKama
        iSage1 = pss.subSequenceTags.index("PROPN")
        couple.id1 = getNum(pss.SequenceTagsWithSagesID[iSage1]) if pss.subSequenceType > 1 else "0"

    else:
        try:
            iSage1 = pss.subSequenceTags.index("PROPN")
            couple.id1 = getNum(pss.SequenceTagsWithSagesID[iSage1]) if pss.subSequenceType > 1 else "1001"
        except Exception as e:
            print(e)

        try:
            iSage2 = colsubParser[i + j].subSequenceTags.index("PROPN")
            couple.id2 = getNum(colsubParser[i + j].SequenceTagsWithSagesID[iSage2]) if colsubParser[i + j].subSequenceType > 1 else "1001"
        except Exception as e:
           print(e)



    couple.name1 = getNameOfSage(couple.id1)
    couple.name2 = getNameOfSage(couple.id2)
    couple.sorces = pss.sorces

    return couple





#====================================================================
def createCouple(i,j,st,pss,colsubParser):
    couple = Couple()
    couple.masechet = pss.masechet
    couple.chapter = pss.chapter
    iType = tr.pairOFSequences.index(st)

    if tr.pairOFSequencesType[iType] == "9":
        try:
            if isIncolLemma(pss.subSequenceTokens[pss.subSequenceTags.index("VERB")]) == isIncolLemma(
                    colsubParser[i + j].subSequenceTokens[colsubParser[i + j].subSequenceTags.index("VERB")]) \
                    and isIncolLemma(pss.subSequenceTokens[pss.subSequenceTags.index("VERB")]) != "":
                couple.relationType = "3"
            else:
                couple.relationType = "1"
        except Exception as e:
            print(e)


    else:
        couple.relationType = tr.pairOFSequencesType[iType]


    if  pss.subSequenceType==1:
        couple.id1 = "1001"
        iSage2 = colsubParser[i + j].subSequenceTags.index("PROPN")
        couple.id2 = getNum(colsubParser[i + j].SequenceTagsWithSagesID[iSage2]) if colsubParser[
                                                                                          i + j].subSequenceType > 1 else "1001"

    elif tr.pairOFSequencesType[iType] == "4":
        couple.id2 = "1001"
        iSage1 = pss.subSequenceTags.index("PROPN")
        couple.id1 = getNum(pss.SequenceTagsWithSagesID[iSage1]) if pss.subSequenceType > 1 else "0"

    else:
        try:
            iSage1 = pss.subSequenceTags.index("PROPN")
            couple.id1 = getNum(pss.SequenceTagsWithSagesID[iSage1]) if pss.subSequenceType > 1 else "1001"
        except Exception as e:
            print(e)

        try:
            iSage2 = colsubParser[i + j].subSequenceTags.index("PROPN")
            couple.id2 = getNum(colsubParser[i + j].SequenceTagsWithSagesID[iSage2]) if colsubParser[i + j].subSequenceType > 1 else "1001"
        except Exception as e:
           print(e)



    couple.name1 = getNameOfSage(couple.id1)
    couple.name2 = getNameOfSage(couple.id2)
    couple.sorces = pss.sorces

    return couple


#=================================================================== writeParserFile
def writeParserFile(fileName,colParser):

    with io.open(pathfindings + fileName, 'w', encoding='utf8') as fHandle:

        fHandle.write(
            "sorces" + ";" +
            "sorcesID" + ";" +
            "subSequenceTokens" + ";" +
            "subSequenceTags" + ";" +
            "subSequenceType" + ";" +
            "subSequenceTagsWithSagesID"
           )
        fHandle.write("\n")
        for ps in colParser:
            fHandle.write(
                " ".join(ps.sorces) + ";" +
                str(ps.sorcesId) + ";" +
                " ".join(ps.subSequenceTokens) + ";" +
                " ".join(ps.subSequenceTags) + ";" +
                str(ps.subSequenceType) + ";" +
                " ".join(""))
            fHandle.write("\n")
    fHandle.close()

#=========================================================getNameOfSage
def getNameOfSage(id):
    if id=="1001":
        return "תנא קמא"
    for sa in colTanaimList:
        if int(sa.id)==int(id):
            return " ".join(sa.firstName + sa.lastName + sa.nickname)
    return 0
#========================================================
def writeCouplesFile(lCoupleM,  fileName):
    with io.open(pathfindings + fileName, 'w', encoding='utf8') as fHandle:
        fHandle.write(
            "chapter" + ";" +
            "seder" + ";" +
            "masechet" + ";" +
            "id1" + ";" +
            "id2" + ";" +
            "name1" + ";" +
            "name2" + ";" +
            "isMishna" + ";" +
            "relationType")
        fHandle.write("\n")

        #col = [1, 0]

       # for i in col:
          #  if i == 1:
             #   lCouple = lCoupleM
           # elif i == 0:
        lCouple = lCoupleM

        for co in lCouple:

                try:
                    fHandle.write(
                        co.chapter + ";" +
                        getSederHeb(co.masechet) + ";" +
                        getMasechetHeb(co.masechet) + ";" +
                        str(co.id1) + ";" +
                        str(co.id2) + ";" +
                        co.name1 + ";" +
                        co.name2 + ";" +
                        str("1") + ";" +
                        str(co.relationType))
                    fHandle.write("\n")
                except Exception as e:
                    print(e)
    fHandle.close()
#============================================================

def getSederHeb(SorcesMasechet):
    s1 = ''.join([i for i in SorcesMasechet if i.isalpha()])
    for se in colSorces:
        s2 = ''.join([i for i in se .masechetEng if i.isalpha()])
        if s1 == s2:
            return str(se.sederHeb)
    return '33'
#=================================================================================

def getMasechetHeb(SorcesMasechet):
    s1 = ''.join([i for i in SorcesMasechet if i.isalpha()])
    for se in colSorces:
        s2 = ''.join([i for i in se.masechetEng if i.isalpha()])
        if s1 == s2:
            return str(se.masechetHeb)
    return '44'


#========================================================MAIN
colFeatures = []
colLemmas = []
colToken = []
colTags = []
colParserM=[]
colParserT=[]
colTanaimList=[]
colPDSL=[]   # # Predicate Dependencies Sequence Labeling
colPDSS= []  # Predicate Dependencies Sequence Segmantation
tr=TypeOFRelationship()

pathfindings = "C:\\P2\\findings\\"
pathReferenceFiles = "C:\\P2\\referenceFiles"


colCorpusT,colCorpusM,colFeatures,colLemmas,colToken,colTags,colPDSS,colPDSL,tr,colTanaimList,colSorces=reader()


colParserM=doSequenceSegmantation(colParserM,colCorpusM)
doSequenceLabeling(colParserM)
lCoupleM=doCouples(colParserM)
writeParserFile("subSequenceM1.txt",colParserM)
#writeCouplesFile(lCoupleM, lCoupleT, "Couples.txt")
writeCouplesFile(lCoupleM, "CouplesM1.txt")

#==========================================================

colParserT=doSequenceSegmantation(colParserT,colCorpusT)
doSequenceLabeling(colParserT)
lCoupleT=doCouples(colParserT)
writeParserFile("subSequenceT.txt",colParserT)
writeCouplesFile(lCoupleT, "CouplesT.txt")


#=====================================================================

print("END")

