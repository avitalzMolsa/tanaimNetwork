import io
import csv
import editdistance


class ParserMishna():

    def __init__(self):
        self.sorces = ""
        self.SorcesMasechet = ""
        self.SorcesChapter = ""
        self.mishnaTokens = []
        self.mishnaTags = []
        self.mishnaWithSages = []




class RelationPattern():
    def __init__(self):
        self.ID = 0
        self.relationPatternPOS = ""
        self.relationTypeID = 0
        self.relationTypeDec = ""


class Sorces():
    def __init__(self):
        self.sederID = 0
        self.sederHeb = ""
        self.sederEng = ""
        self.masechetID = 0
        self.masechetHeb = ""
        self.masechetEng = ""


class Sage():
    def __init__(self):
        self.ID = 0
        self.preffix = ""
        self.firstName = ""
        self.lastName = []
        self.lastNameTags = []
        self.isStam = 0
        self.nickname = ""
        self.References = []
        self.varietyOfFirstNames = []
        self.varietyOfLastNames = []
        self.varietyOfLastNamesTags = []
        self.varietyOfSageID = []
        self.strongNum = 0


class Couple():
    def __init__(self):
        self.TextSorces = ""
        self.SorcesMasechet = ""
        self.SorcesChapter = ""
        self.textTokens = ""
        self.textTags = ""
        self.textWithSages = ""
        self.strongNum1 = 0
        self.strongNum2 = 0
        self.sage1 = ""
        self.sage2 = ""
        self.relationPatternPOS = ""
        self.RelID = 0  # for differ between rel 4 or 20


class OneOfCouple():
    def __init__(self):
        self.sageID = ""
        self.partOfRel = []
        self.lemma = ""


class StrongSageNum():
    def __init__(self):
        self.isMishna = 1
        self.strongNum = 0
        self.identicalStrongNum = 0
        self.weakNumM = 0
        self.weakNumT = 0
        self.preffix = ""
        self.firstName = ""
        self.lastName = ""
        self.lastNameTags = ""
        self.nickname = ""
        self.References = []


class SageIsStam():
    def __init__(self):
        self.nameToCompare=""
        self.preffix=""
        self.firstName = ""
        self.lastName = ""
        self.nickname = ""


class IdenticalSages():
    def __init__(self):
        self.stNum = 0
        self.preffix = ""
        self.firstName = ""
        self.lastName = ""
        self.lastNameTags = ""
        self.nickname = ""
        self.isMishna = ""

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

def reader():
    colFeatures = []
    colLemmas = []
    colToken = []
    colTags = []


    pathCorpus = "C:\\P2\\courpus"

    # read Tanaim Lexicon
    f_lex = pReferenceFiles + "\\TanaimLex.csv"
    with open(f_lex,encoding="utf-8-sig", newline='') as csvfile:
        Lex = csv.DictReader(csvfile)
        for row in Lex:
            colToken.append(row['token'])
            colTags.append(row['pos'])
            colFeatures.append(row['features'])
            colLemmas.append(row['lemma'])

    # read Corpus Mishna
    f_corpusM = pathCorpus + "\\corpusMisnaKoufman.txt"
    corpusM = io.open(f_corpusM, mode="r", encoding="utf-8")
    CorpusM = corpusM.readlines()

    # read Corpus Tosefta
    f_corpusT = pathCorpus + "\\corpusToseftaVINA.txt"
    corpusT = io.open(f_corpusT, mode="r", encoding="utf-8")
    CorpusT = corpusT.readlines()

    # read Relation that base from pos pattern
    f_relPattern = pReferenceFiles + "\\RelPattern.csv"
    colPatterns = []
    with open(f_relPattern, newline='') as csvfile:
        RelPatterns = csv.DictReader(csvfile)

        for row in RelPatterns:
            re = RelationPattern()
            re.ID = row['ID']
            re.relationPatternPOS = row['relationPatternPOS']
            re.relationTypeID = row['relationType']
            re.relationTypeDec = row['relationTypeDec']
            colPatterns.append(re)

    f_SederMasechetTab = pReferenceFiles + "\\SederMasechetTab.csv"
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

    f_SageIsStam = pReferenceFiles + "\\stam.csv"
    colStam = []
    with open(f_SageIsStam, newline='') as csvfile:
        stam = csv.DictReader(csvfile)

        for row in stam:
            re = SageIsStam()
            re.nameToCompare=row['nameToCompare']
            re.preffix=row['preffix']
            re.firstName = row['firstName']
            re.lastName = row['lastName']
            re.nickname = row['nickName']
            colStam.append(re)


    f_IdenticalSages = pReferenceFiles + "\\IdenticalSagesNames.csv"
    colIdenticalSages = []
    with open(f_IdenticalSages, newline='') as csvfile:
        IdenticalSa = csv.DictReader(csvfile)

        for row in IdenticalSa:
            re = IdenticalSages()
            re.stNum = row['strongNum']
            re.preffix = row['preffix']
            re.firstName = row['firstName']
            re.lastName = row['lastName']
            re.lastNameTags = row['lastNameTags']
            re.nickname = row['nickname']
            re.isMishna = row['isMishna']
            colIdenticalSages.append(re)

    f_TanaimList = pReferenceFiles + "\\TanaimList.csv"
    colTanaimList = []
    with open(f_TanaimList,encoding="utf-8-sig", newline='') as csvfile:
        TanaimListSa = csv.DictReader(csvfile)

        for row in TanaimListSa:
            ro = clsTanaim()
            if int(row['id'])>0:
                ro.id = row['id']
                ro.preffix = row['preffix']
                ro.firstName = row['firstName']
                ro.lastName = row['lastName']
                ro.nickname = row['nickname']
                ro.isTana = row['isTana']
                ro.genaration = row['genaration']

                colTanaimList.append(ro)


    return colToken, colTags, colLemmas, colFeatures, CorpusM, CorpusT, colPatterns, colSorces, colStam, colIdenticalSages, colTanaimList


def cleanWord(word):
    lWord = []
    for w in word:
        if w not in ("<", ">", "[", "]", "?", "}", "{", "⟧", "⟦", ")", "(", "\n", "⌜", "⌝", "◦"):
            lWord.append(w)
    return "".join(lWord)


def getTypeOfRelFromPattern(idPattern):
    try:
        return " ".join(colPatterns[int(idPattern) - 1].relationTypeDec)
    except Exception as e:
        print(e)


def getSederHeb(SorcesMasechet):
    s1 = ''.join([i for i in SorcesMasechet if i.isalpha()])
    for se in colSorces:
        s2 = ''.join([i for i in se.masechetEng if i.isalpha()])
        if s1 == s2:
            return str(se.sederHeb)
    return '33'


def getMasechetHeb(SorcesMasechet):
    s1 = ''.join([i for i in SorcesMasechet if i.isalpha()])
    for se in colSorces:
        s2 = ''.join([i for i in se.masechetEng if i.isalpha()])
        if s1 == s2:
            return str(se.masechetHeb)
    return '44'


def isIncolFeatures(s, token):
    if token in colToken:
        col = colFeatures[colToken.index(token)]
        for feature in s.split("|"):
            if str(col).find(feature) == -1:  # feature not in col:
                return 0
        return 1
    else:
        return 0


def doSegmentation(Corpus):
    lParser = []
    for idx, line in enumerate(Corpus):
        pm = ParserMishna()
        prevWord = ""
        for i, word in enumerate(line.split(" ")):
            word = cleanWord(word)

            if word in colToken:
                i = colToken.index(word)

            elif word[0:1] in ["ו", "ב", "מ","ש"] :

                if word[1:] in colToken:
                    i = colToken.index(word[1:])
                    if colTags[i] == "PROPN" or colTags[i] == "VERB" or (colTags[i] == "ADJ" and isIncolFeatures("preffix=yes", word[1:])):
                        pm.mishnaTokens.append(word[0:1])
                        word = word[1:]
                elif prevWord in colToken and word[0:1] == "ו":
                    pm.mishnaTokens.append(word[0:1])
                    word = word[1:]
            pm.mishnaTokens.append(word)
            prevWord = word
        lParser.append(pm)
    return lParser


def tagginSourceOfMishna(pm, i, word):
    if i == 0:
        pm.mishnaTags.append("Masechet")
        pm.sorces = pm.sorces + word
        pm.SorcesMasechet = word
    elif i == 1:
        pm.mishnaTags.append("Chapter-MishnaUnit")
        pm.sorces = pm.sorces + word
        pm.SorcesChapter = word


def doTaggingWords(lParser):
    for pm in lParser:
        for idx, word in enumerate(pm.mishnaTokens):
            if idx < 2:
                tagginSourceOfMishna(pm, idx, word)
            else:
                if "8:5" in pm.sorces and "Arak." in pm.sorces:
                    print(idx)
                try:

                    prevTag = pm.mishnaTags[idx - 1] if idx > 0 else "NONE"
                    prevToken = pm.mishnaTokens[idx - 1] if idx > 0 else ""
                    prevprevTag = pm.mishnaTags[idx - 2] if idx > 1 else "NONE"
                    prevprevToken = pm.mishnaTokens[idx - 2] if idx > 1 else ""
                    nextToken = pm.mishnaTokens[idx + 1] if idx < len(pm.mishnaTokens) - 1 else "NONE"
                    nextTag = colTags[colToken.index(nextToken)] if nextToken in colToken else "NONE"
                    nextnextToken = pm.mishnaTokens[idx + 2] if idx < len(pm.mishnaTokens) - 2 else "NONE"
                    nextnextTag = colTags[colToken.index(nextnextToken)] if nextToken in colToken else "NONE"
                except Exception as e:
                    print(e)

                if word in colToken:
                    i = colToken.index(word)
                    if colTags[i] == "NN" and (nextTag=="PROPN" and  isIncolFeatures("abbreviation=yes", nextToken)) and nextnextTag=="VERB":
                        pm.mishnaTags.append("NONE")  #ben azaii omer

                    elif doFindPlace(colTags[i], word, prevTag, prevToken) > 0:
                        pm.mishnaTags.append("NP")
                    elif colTags[i] == "PROPN" and isIncolLemma(word) != "":

                        if (prevTag == "NN" or prevprevTag == "NN"):
                            pm.mishnaTags.append("NP")
                        else:
                            pm.mishnaTags.append(colTags[i])
                    else:
                        pm.mishnaTags.append(colTags[i])
                else:

                    # ========== Rules base of PROPN  or  NP

                    if (prevTag == "NN"):  # and nextTag != "DET"

                        if prevprevTag == "VERB":  # amar ben zoma   OR   Yebam. 8:7 amar ben Azaii
                            pm.mishnaTags.append("PROPN")

                        elif prevprevTag == "NP" or prevprevTag == "PROPN":
                            flag = 0
                            i = idx
                            while prevTag not in ['Masechet', 'Chapter-MishnaUnit', 'NONE']:
                                prevTag = pm.mishnaTags[i - 1] if i > 0 else "NONE"
                                prevprevTag = pm.mishnaTags[i - 2] if i > 0 else "NONE"
                                i -= 1
                                if prevTag == 'PRON' and prevprevTag == 'VERB':
                                    flag = 1
                            if flag == 1:
                                pm.mishnaTags.append("PROPN")
                            else:
                                pm.mishnaTags.append("NP")
                        else:
                            pm.mishnaTags[idx - 1] = "NONE"  # push instead NN
                            pm.mishnaTags.append("NONE")
                    # s1
                    elif (nextTag == "ADJ" and isIncolFeatures("suffix=yes", nextToken)) and (
                            nextnextTag == "VERB"):  # colFeatures[colTags.index(prevTag)])):
                        pm.mishnaTags.append("PROPN")

                    # s2
                    elif (prevTag == "ADJ" and prevprevTag == "CC"):
                        pm.mishnaTags.append("PROPN")

                    # s3
                    elif (prevTag == "ADJ" and prevprevTag == "NN" and isIncolFeatures("preffix=yes | Number=Sing",
                                                                                       prevToken)):
                        pm.mishnaTags.append("NP")

                    # s4
                    elif (prevTag == "ADJ" and isIncolFeatures("preffix=yes | Number=Plur",
                                                               prevToken) and nextTag == "VERB"):
                        pm.mishnaTags.append("PROPN")  # bet Hilel   bet Shamaii

                    # s5
                    elif nextTag in ("CCONJ", "PREPOSITION") and ((prevTag == "NNT") or (
                            prevTag == "ADJ" and isIncolFeatures("preffix=yes | Number=Sing", prevToken))):
                        pm.mishnaTags.append("PROPN")

                    # s6
                    elif nextTag == "VERB" and prevTag == "ADJ" and isIncolFeatures("preffix=yes | Number=Sing",
                                                                                    prevToken):
                        pm.mishnaTags.append("PROPN")

                    # s7
                    elif (nextTag == "ADJ") and (prevTag == "ADJ" and isIncolFeatures("preffix=yes | Number=Sing",
                                                                                      prevToken)):
                        pm.mishnaTags.append("PROPN")

                    # s8
                    elif (nextTag == "NN") and (
                            prevTag == "ADJ" and isIncolFeatures("preffix=yes | Number=Sing", prevToken)):
                        pm.mishnaTags.append("PROPN")

                    # s9
                    elif prevprevTag == "VERB" and prevTag == "ADJ" and isIncolFeatures("preffix=yes | Number=Sing",
                                                                                        prevToken):
                        pm.mishnaTags.append("PROPN")

                    # s10
                    elif prevprevTag == "NNT" and prevTag == "ADJ" and isIncolFeatures("preffix=yes | Number=Sing",
                                                                                       prevToken):
                        pm.mishnaTags.append("PROPN")

                    # s11
                    elif prevprevTag == "PRON" and prevTag == "ADJ" and isIncolFeatures("preffix=yes | Number=Sing",
                                                                                        prevToken):
                        pm.mishnaTags.append("PROPN")

                    # s12
                    elif prevprevTag == "CCONJ" and prevTag == "ADJ" and isIncolFeatures("preffix=yes | Number=Sing",
                                                                                         prevToken):
                        pm.mishnaTags.append("PROPN")

                    else:
                        pm.mishnaTags.append("NONE")


def RemoveStoryFromLParser(lParser):
    lParserFiltered = []
    for pm in lParser:
        if " ".join(pm.mishnaTags).find('STORY') == -1:
            lParserFiltered.append(pm)
    return lParserFiltered


def writeParserFile(lParser, fileName):
    pReferenceFiles = "C:\\P2\\findings\\"
    with io.open(pReferenceFiles + fileName, 'w', encoding='utf8') as fHandle:

        fHandle.write(
            "sorces" + ";" +
            "SequenceTokens" + ";" +
            "SequenceTags" + ";" +
            "SequenceTagsWithSagesID"
           )
        fHandle.write("\n")
        for pm in lParser:
            fHandle.write(
                " ".join(pm.sorces) + ";" +
                " ".join(pm.mishnaTokens) + ";" +
                " ".join(pm.mishnaTags) + ";" +
                " ".join(str(pm.mishnaWithSages)))
            fHandle.write("\n")
    fHandle.close()



def writeSagesFile(lSages, fileName):

    with io.open(pathfindingsFiles + fileName, 'w', encoding='utf8') as fHandle:
        try:
            for sa in lSages:
                for ref in sa.References:
                    fHandle.write(
                        str(sa.id) + ";" +
                        str(sa.firstName) + ";" +
                        str(" ".join(sa.lastName)) + ";" +
                        str(sa.nickname) + ";" +
                        str(sa.preffix) + ";" +
                        str(ref))
                       # str(" ".join(sa.References)))
                    fHandle.write("\n")
        except Exception as e:
            print(e)

    fHandle.close()



def fillSageNode(pm, i, itsRabi):
    sa = Sage()
    sa.References.append(pm.mishnaTokens[0])
    
    if pm.mishnaTags[i] == "PROPN":
        sa.firstName = pm.mishnaTokens[i]

        if i > 0:
            if (pm.mishnaTags[i - 1] == 'ADJ' \
                    and isIncolFeatures("preffix=yes", pm.mishnaTokens[i - 1]) or pm.mishnaTags[
                        i - 1] == 'NN'):  # colFeatures[colTags.index(pm.mishnaTags[i - 1])])) \
                sa.preffix = pm.mishnaTokens[i - 1]

        if i < (len(pm.mishnaTokens) - 2):
            if pm.mishnaTags[i + 1] == 'NN':
                try:

                    while (pm.mishnaTags[i + 1] == 'NP') or \
                            (pm.mishnaTags[i + 1] == 'NN' and pm.mishnaTags[i + 2] == "NP") or \
                            (pm.mishnaTags[i + 1] == 'NN' and pm.mishnaTags[i + 2] == "ADJ" and isIncolFeatures(
                                "preffix=yes", pm.mishnaTokens[i + 2]) and not isIncolFeatures("Number=Plur",
                                                                                               pm.mishnaTokens[
                                                                                                   i + 2])) or \
                            (pm.mishnaTags[i + 1] == 'ADJ' and isIncolFeatures("preffix=yes", pm.mishnaTokens[
                                i + 1]) and not isIncolFeatures("Number=Plur", pm.mishnaTokens[i + 1]) and
                             pm.mishnaTags[i + 2] not in ['PROPN']):
                        sa.lastName.append(pm.mishnaTokens[i + 1])
                        sa.lastNameTags.append(pm.mishnaTags[i + 1])
                        i += 1
                except Exception as e:
                    print(e)
        if sa.lastNameTags!=[]:
            if sa.lastNameTags[len(sa.lastNameTags)-1]=="ADJ" and isIncolFeatures("preffix=yes", sa.lastName[len(sa.lastName)-1]):
                sa.lastNameTags.pop(len(sa.lastNameTags) - 1)
                sa.lastName.pop(len(sa.lastName)-1)

        if i < (len(pm.mishnaTokens) - 2):
            if (pm.mishnaTags[i + 1] == 'ADJ' \
                    and not isIncolFeatures("preffix=yes", pm.mishnaTokens[i + 1])
                    and not isIncolFeatures("part=yes", pm.mishnaTokens[i + 1])):
                sa.nickname = pm.mishnaTokens[i + 1]
            else:
                try:
                    j = 1
                    while (pm.mishnaTags[i + j] in ('ADJ', 'NP') \
                           and isIncolFeatures("part=yes", pm.mishnaTokens[i + j])):
                        sa.nickname = sa.nickname + pm.mishnaTokens[i + j] + " "
                        j += 1
                    if j < 3:
                        sa.nickname = ""
                except Exception as e:
                    print(e)

        if sa.nickname == "" and sa.lastName == [] and sa.preffix != "בית":
            found = 0
            for st in colStam:
                if chkFirstNameSimilarity(st.nameToCompare, sa.firstName) == 1 and found == 0:
                    sa.preffix=st.preffix
                    sa.firstName=st.firstName
                    if st.lastName != "":
                        s = st.lastName.split(" ")
                        sa.lastName.append(s[0])
                        sa.lastName.append(s[1])
                        sa.lastNameTags.append("NN")
                        sa.lastNameTags.append("NP")
                    if st.nickname != "":
                        sa.nickname = st.nickname.strip()

                    sa.isStam = 1
                    found = 1
        elif sa.nickname == "" and sa.preffix != "בית":
            found = 0
            for st in colStam:
                if chkFirstNameSimilarity(st.nameToCompare, sa.firstName) == 1 and \
                   chkLastNameSimilarity(st.lastName," ".join(sa.lastName))== 1 and found == 0:
                       sa.nickname = st.nickname.strip(" ")


    elif itsRabi == i:
        sa.preffix = "רבי"
        sa.firstName = "יהודה"
        sa.nickname = "הנשיא"

    return sa


def chkSimilarityByLemma(s1, s2):
    sName1 = ""
    sName2 = ""
    # s1 = cleanApostrophes(s1)
    # s2 = cleanApostrophes(s2)

    for s in s1.split(" "):
        lemma = isIncolLemma(s)
        sName1 = sName1 + " " + lemma if lemma != "" else sName1 + " " + s

    for s in s2.split(" "):
        lemma = isIncolLemma(s)
        sName2 = sName2 + " " + lemma if lemma != "" else sName2 + " " + s

    if editdistance.eval(sName1, sName2) == 0:
        return 1
    return 0


def cleanApostrophes(s):
    lstApostrophes = ["׳", "'"]
    try:
        for apost in lstApostrophes:
            if s.find(apost) != -1:
                s = remove(s, s.index(apost))
    except Exception as e:
        print("cleanApostrophes")
        print(e)
    return s


def isIncolLemma(token):
    col = ""
    if token in colToken:
        col = colLemmas[colToken.index(token)]
    else:
        token = cleanApostrophes(token)
        if token in colToken:
            col = colLemmas[colToken.index(token)]
    return col




def chkSimilarityByAlternatingLetters(s1, s2):
    if len(s1) == len(s2):
        alternatingLetters = ['יב', 'בי', 'אה', 'הא', 'בפ', 'פב', 'יה', 'הי', 'יא', 'אי', 'יו', 'וי', 'לא', 'אל', 'לי',
                              'יל', 'ני', 'ינ', 'רד', 'דר', 'הף', 'ףה', 'יף', 'ףי']
        lst = []
        try:
            lst.append([c1 + c2 for c1, c2 in zip(s1, s2) if c1 != c2])
            for ch in list(lst[0]):
                if editdistance.eval(ch[1], ch[0]) != 0:
                    if ch not in alternatingLetters:
                        return 0
            return 1
        except Exception as e:
            print(e)





def remove(s, indx):
    return ''.join(x for x in s if s.index(x) != indx)


def chkSimilarityByMissingLetters(s1, s2):
    lstApostrophes = ["׳", "'"]
    try:

        for apost in lstApostrophes:
            if s1.find(apost) != -1:
                s1 = remove(s1, s1.index(apost))
            if s2.find(apost) != -1:
                s2 = remove(s2, s2.index(apost))

        maxLenS = s1 if len(s1) > len(s2) else s2
        minLenS = s1 if len(s1) < len(s2) else s2
        if editdistance.eval(s1, s2) == 0:
            return 1
        if (len(maxLenS) - len(minLenS) == 1):
            flag = 0
            j = 0
            for i in range(0, len(minLenS)):
                if maxLenS[j] != minLenS[i] and flag == 0:
                    flag = 1
                    if maxLenS[j] in ['ה', 'י', 'ו', 'ע', 'ם', 'ת', 'נ', 'א', 'ל']:
                        j = j + 1
                    else:
                        return 0
                if maxLenS[j] == minLenS[i]:
                    j = j + 1
                else:
                    return 0
            return 1
        else:
            return 0

    except Exception as e:
        print(e)


def chkFirstNameSimilarity(saFirstName, sageFirstName):
    if editdistance.eval(sageFirstName, saFirstName) == 0:
        return 1

    if (chkSimilarityByAlternatingLetters(saFirstName, sageFirstName) == 1):
        return 1

    if (isIncolFeatures("MissingLetters=no", saFirstName) == 0) and (
            isIncolFeatures("MissingLetters=no", sageFirstName) == 0):
        if (chkSimilarityByMissingLetters(saFirstName, sageFirstName) == 1):
            return 1

    if chkSimilarityByLemma(saFirstName, sageFirstName) == 1:
        return 1

    return 0

def chkLastNameSimilarity(saLastName, sageLastName):
    found=0
    if editdistance.eval(saLastName, sageLastName) == 0:
        return 1

    if saLastName != "" and sageLastName != "":
        saList = []
        sageList = []
        #remove rabi
        if len(saLastName.split(" ")) != len(sageLastName.split(" ")):
            for i,token in enumerate(saLastName.split(" ")):
                tag=""
                if token in colToken:
                    tag = colTags[colToken.index(token)]
                if tag!="ADJ":
                    saList.append(token)

            for i,token in enumerate(sageLastName.split(" ")):
                tag = ""
                if token in colToken:
                    tag = colTags[colToken.index(token)]
                if tag!="ADJ":
                    sageList.append(token)
        else:
            saList = saLastName.split(" ")
            sageList = sageLastName.split(" ")

        if len(saList) == len(sageList):
           for i in range(len(saList)):

                if (chkSimilarityByAlternatingLetters(saList[i], sageList[i]) == 1):
                    found += 1

                elif (chkSimilarityByMissingLetters(saList[i], sageList[i]) == 1):
                    found += 1

                elif chkSimilarityByLemma(saList[i], sageList[i]) == 1:
                    found += 1
           if found==len(sageList):
               return 1
    return 0



def chkLastNameSimilarity1(saLastName, sageLastName, saLastNameTags, sageLastNameTags):
    if editdistance.eval(saLastName, sageLastName) == 0:  # and sage.lastName != [] :
        return 1

    if saLastName != "" and sageLastName != "":
        saListTags = saLastNameTags.split(" ")
        sageListTags = sageLastNameTags.split(" ")
        saList = saLastName.split(" ")
        sageList = sageLastName.split(" ")

        saInd = []
        sageInd = []
        if saLastNameTags.find("NP") != -1 and sageLastNameTags.find("NP") != -1:
            saInd.append(saListTags.index("NP"))
            sageInd.append(sageListTags.index("NP"))
            saLastName = saList[saInd[0]]
            sageLastName = sageList[sageInd[0]]
        elif (saLastNameTags.find("ADJ") != -1 and sageLastNameTags.find("ADJ") != -1) and not \
                (saLastNameTags.find("NP") != -1 or sageLastNameTags.find("NP") != -1):
            saInd.append(saListTags.index("ADJ"))
            sageInd.append(sageListTags.index("ADJ"))
            saLastName = saList[saInd[0]]
            sageLastName = sageList[sageInd[0]]

        if (chkSimilarityByAlternatingLetters(saLastName, sageLastName) == 1):
            return 1

        if (chkSimilarityByMissingLetters(saLastName, sageLastName) == 1):
            return 1

        if chkSimilarityByLemma(saLastName, sageLastName) == 1:
            return 1

    return 0


def chkNicknameSimilarity(sa, sage):
    if editdistance.eval(sa.nickname.strip(" "), sage.nickname.strip(" ")) == 0:  # and sage.nickname != "":
        return 1
    if (chkSimilarityByAlternatingLetters(sa.nickname, sage.nickname) == 1):
        return 1
    if chkSimilarityByLemma(sa.nickname, sage.nickname) == 1:
        return 1

    return 0


def chkpreffix(sa, sage):
    if editdistance.eval(sa.preffix, sage.preffix) == 0:  # and sage.nickname != "":
        return 1
    if ((isIncolFeatures("Number=Sing", sa.preffix) and sage.preffix == "") or (
            isIncolFeatures("Number=Sing", sage.preffix) and sa.preffix == "")):
        return 1

    if (chkSimilarityByAlternatingLetters(sa.preffix, sage.preffix) == 1):
        return 1

    if chkSimilarityByLemma(sa.preffix, sage.preffix) == 1:
        return 1
    return 0


def areYouRecognizeThisSage(sa, lSages):
    if len(lSages) == 0:
        return 0
    for i, sage in enumerate(lSages):
        if sage.id =="47" :
            print("")
        res0 = chkpreffix(sa, sage)
        res1 = chkFirstNameSimilarity(sa.firstName, sage.firstName)
        res2 = chkLastNameSimilarity(" ".join(sa.lastName),sage.lastName)
        res3 = chkNicknameSimilarity(sa, sage)
        if res0 and res1 and res2 and res3:
            sage.References.append(sa.References[0])
            return lSages[i].id

    return 0


def doFindPlace(tag, token, prevTag, prevToken):
    if (tag == "PROPN" and isIncolFeatures("place=yes", token) and isIncolFeatures("part=yes", prevToken)) or \
            tag == "PROPN" and isIncolFeatures("place=yes", token) and prevTag == "NN":
        return 1
    return 0



def doFindRabi(pm):
    itsRabi = 0
    if (" ".join(pm.mishnaTags).find('ADJ VERB') != -1) or \
            " ".join(pm.mishnaTags).find('NNT ADJ') != -1:
        for idx, tag in enumerate(pm.mishnaTags):
            if idx < len(pm.mishnaTags) - 1:
                nextTag = pm.mishnaTags[idx + 1]
            if idx>0:
                prevTag=pm.mishnaTags[idx-1]
            if (tag == 'ADJ' and isIncolFeatures("preffix=yes", pm.mishnaTokens[idx]) and nextTag == 'VERB' and prevTag !="ADJ")or \
                    (tag == 'ADJ' and isIncolFeatures("preffix=yes",
                                                      pm.mishnaTokens[idx]) and nextTag != 'PROPN' and prevTag == "NNT")   :
                itsRabi = idx
                pm.mishnaTags[idx]="PROPN"
    return itsRabi


def doSagesIdentification(lParser):
    lSages = []

    for i, pm in enumerate(lParser):
        print(pm.sorces)
        if "Maas" in pm.sorces and "2:5" in pm.sorces:
            print("")
        itsRabi = doFindRabi(pm)
        nSages = "".join(pm.mishnaTags).count('PROPN')
        nSages += 1 if itsRabi != 0 else 0

        if nSages > 0:
            for idx, tag in enumerate(pm.mishnaTags):

                if (tag == 'PROPN' and not isIncolFeatures("Number=Plur", pm.mishnaTokens[idx])):
                      #  or (tag == 'ADJ' and itsRabi == idx):

                    sa = fillSageNode(pm, idx, itsRabi)
                    res = areYouRecognizeThisSage(sa, colTanaimList)

                    if res == 0:
                        sa.ID = "9999"
                        pm.mishnaWithSages.append(sa.ID)
                        lSages.append(sa)
                    else:
                        pm.mishnaWithSages.append(res)
                elif (tag == 'PROPN' and  isIncolFeatures("Number=Plur", pm.mishnaTokens[idx])):
                    pm.mishnaWithSages.append("1000")
                else:
                    pm.mishnaWithSages.append(tag)

    return lSages


def doProcessPattern(pattern1, pattern2):
    return pattern1 + pattern2


def isNotDouplicateCouple(lCouplesInMishna, coCompare):
    for co in lCouplesInMishna:
        if (coCompare.sage1 == co.sage1 and coCompare.sage2 == co.sage2) or (
                coCompare.sage1 == co.sage2 and coCompare.sage2 == co.sage1):
            return 0
    return 1


def doFindDistanceBetweenSages(pm, sa1, sa2):
    found1 = 0;
    found2 = 0;
    ind1 = 0;
    ind2 = 0
    for i, s1 in enumerate(pm.mishnaWithSages):
        if sa1 == str(s1) and found1 == 0:
            ind1 = i
            found1 = 1

    for i, s2 in enumerate(pm.mishnaWithSages):
        if sa2 == str(s2) and found2 == 0:
            ind2 = i
            found2 = 1

    for i in range(ind1 + 1, ind2 - 1):
        if pm.mishnaTags[i] == "PROPN":
            return 1

    return 0


def doFindCouplesAndRel(lAllSagesInMishna, pm, sa, lCouples, isMishna):
    foundPat = 0
    lCouplesInMishna = []
    co = Couple()
    # if sa.sageID != "" and len(sa.partOfRel) > 1:
    if isSageInList(lAllSagesInMishna, sa) == 0:
        lAllSagesInMishna.append(sa)
    if len(lAllSagesInMishna) > 1:
        for ind1, sa1 in enumerate(lAllSagesInMishna):
            for ind2 in range(ind1 + 1, len(lAllSagesInMishna)):
                if sa1.sageID != lAllSagesInMishna[ind2].sageID:
                    currentPattern = doProcessPattern(sa1.partOfRel, lAllSagesInMishna[ind2].partOfRel)
                    for pat in colPatterns:
                        if foundPat == 0:
                            if editdistance.eval(" ".join(currentPattern), pat.relationPatternPOS.strip()) == 0:
                                foundPat = 1

                                if int(pat.ID) in (4, 21):
                                    res = doCompareLemma(sa1.lemma, lAllSagesInMishna[ind2].lemma)

                                    if res == 1:
                                        foundPat = 0
                                    elif res == 21:
                                        co.RelID = 21
                                    elif res == 4:
                                        co.RelID = 4
                                elif int(pat.ID) > 10:
                                    if doFindDistanceBetweenSages(pm, sa1.sageID, lAllSagesInMishna[ind2].sageID):
                                        foundPat = 0
                                else:
                                    co.RelID = pat.ID
                                if foundPat == 1:
                                    co.relationPatternPOS = pat.relationPatternPOS
                                    #co.RelID = pat.ID
                                    co.TextSorces = pm.sorces
                                    co.SorcesMasechet = pm.SorcesMasechet
                                    co.SorcesChapter = pm.SorcesChapter
                                    co.textTags = " ".join(pm.mishnaTags)
                                    co.textTokens = " ".join(pm.mishnaTokens)
                                    co.textWithSages = " ".join(str(pm.mishnaWithSages))
                                    co.sage1 = sa1.sageID
                                    co.sage2 = lAllSagesInMishna[ind2].sageID
                                    co.strongNum1 = co.sage1
                                    co.strongNum2 =co.sage2
                                    if isNotDouplicateCouple(lCouplesInMishna, co):
                                        lCouples.append(co)
                                    lCouplesInMishna.append(co)
                                    co = Couple()
                foundPat = 0





def getStrongNum(sageID, isMishna):
    lSagesAllStrongNum=[]
    for sa in lSagesAllStrongNum:
        if isMishna:
            if editdistance.eval(str(sa.weakNumM), sageID.strip()) == 0:
                return sa.strongNum
        else:
            if editdistance.eval(str(sa.weakNumT), sageID.strip()) == 0:
                return sa.strongNum
    return 1000



def getNameOfSage(id):
    for sa in colTanaimList:
        if sa.id==id:
            return " ".join(sa.firstName + sa.lastName + sa.nickname)
    return 0



def doCompareLemma(lemma1, lemma2):
    if lemma1 != "" and lemma2 == "":
        return 1
    if lemma1 == "" and lemma2 != "":
        return 1
    if lemma1 == lemma2 and lemma2 != "":
        return 21
    if lemma1 != lemma2 and lemma2 != "":
        return 4
    if lemma1 == "" and lemma2 == "":
        return 4


def isNotAlone(pm, i):
    if (i < len(pm.mishnaWithSages) - 1) and i > 0:
        if pm.mishnaWithSages[i] == "CCONJ":
            if pm.mishnaWithSages[i + 1] == "NONE":
                return 0
            else:
                return 1
        if pm.mishnaWithSages[i + 1] != "NONE" or pm.mishnaWithSages[i - 1] != "NONE":
            return 1
    return 0


def analysisTextForCouples(lParser, isMishna):
    RelWords = ["ADV", "PREPOSITION", "CCONJ", "CC"]
    NotRelWords = ["ADJ", "NP", "NN", "PRON", "Masechet", "Chapter-MishnaUnit"]
    lCouples = []

    for j, pm in enumerate(lParser):
        if (pm.SorcesMasechet.find("‎Shev.") != -1) and pm.SorcesChapter.find("3:3") != -1:
            print("‎Shev. 3:3")
        lAllSagesInMishna = []
        sa = OneOfCouple()
        for i, word in enumerate(pm.mishnaWithSages):
            prevTag = pm.mishnaWithSages[i - 1] if i > 0 else "NONE"
            nextTag = pm.mishnaWithSages[i + 1] if i < len(pm.mishnaWithSages) - 1 else "NONE"

            found = 0
            while found == 0:

                if word == "VERB" and nextTag == "PRON":
                    if isSageInList(lAllSagesInMishna, sa) == 0:
                        lAllSagesInMishna.append(sa)
                    sa = OneOfCouple()
                    sa.partOfRel.append(word)
                    sa.lemma = isIncolLemma(pm.mishnaTokens[i])
                    found = 1
                elif word == "VERB" and word not in sa.partOfRel and "NNT" not in sa.partOfRel and isNotAlone(pm, i):
                    sa.partOfRel.append(word)
                    sa.lemma = isIncolLemma(pm.mishnaTokens[i])
                    found = 1
                elif word == "NNT" and word not in sa.partOfRel and "VERB" not in sa.partOfRel:
                    sa.partOfRel.append(word)
                    found = 1
                elif word in RelWords and word not in sa.partOfRel and prevTag not in NotRelWords and isNotAlone(pm, i):
                    sa.partOfRel.append(word)
                    found = 1
                elif (str(word).isnumeric() or word == "PROPN") and (
                        sa.sageID == "" and "PROPN" not in sa.partOfRel and isNotAlone(pm, i)):
                    sa.sageID = str(word)
                    sa.partOfRel.append("PROPN")
                    found = 1
                elif word == "NONE" and sa.partOfRel == []:
                    found = 1
                elif word in NotRelWords:
                    found = 1
                elif sa.sageID == "":
                    found = 1
                else:
                    if isSageInList(lAllSagesInMishna, sa) == 0:
                        lAllSagesInMishna.append(sa)
                    sa = OneOfCouple()
        doFindCouplesAndRel(lAllSagesInMishna, pm, sa, lCouples, isMishna)
    return lCouples


def isSageInList(lAllSagesInMishna, sa):
    for s in (lAllSagesInMishna):
        if sa.sageID == s.sageID or sa.sageID == "":
            return 1
    return 0


def writeCouplesFile(lParserCoupleM, lParserCoupleT, fileName):
    with io.open(pathfindingsFiles + fileName, 'w', encoding='utf8') as fHandle:
        fHandle.write(
            "sederHeb" + ";" +
            "MasechetHeb" + ";" +
            "SorcesChapter" + ";" +
            "textTokens" + ";" +
            "textWithSages" + ";" +
            "sage1" + ";" +
            "sage2" + ";" +
            "strongNum1" + ";" +
            "strongNum2" + ";" +
            "IdRel" + ";" +
            "isMishna" + ";" +
            "relationPatternPOS")
        fHandle.write("\n")

        col = [1, 0]
        for i in col:
            if i == 1:
                lParserCouple = lParserCoupleM
            elif i == 0:
                lParserCouple = lParserCoupleT

            for co in lParserCouple:

                try:
                    fHandle.write(
                        getSederHeb(co.SorcesMasechet) + ";" +
                        getMasechetHeb(co.SorcesMasechet) + ";" +
                        co.SorcesChapter + ";" +
                        " ".join(co.textTokens) + ";" +
                        " ".join(co.textWithSages) + ";" +
                        getNameOfSage(co.sage1) + ";" +
                        getNameOfSage(co.sage2) + ";" +
                        str(int(co.strongNum1)) + ";" +
                        str(int(co.strongNum2)) + ";" +
                        getTypeOfRelFromPattern(co.RelID) + ";" +
                        str(i) + ";" +
                        co.relationPatternPOS)
                    fHandle.write("\n")
                except Exception as e:
                    print(e)
    fHandle.close()

def addIdenticalSagesToList(col):
    for sage in colIdenticalSages:
        for j in sage.isMishna.split(" "):
            flag = 0
            for i, sa in enumerate(col):

                if flag == 0 and sa.isMishna == int(j):
                    res0 = chkpreffix(sa, sage)
                    res1 = chkFirstNameSimilarity(sa.firstName, sage.firstName)

                    if sa.lastName != "" and res0 == 1 and res1 == 1:
                        res2 = chkLastNameSimilarity1(sa.lastName, sage.lastName, sa.lastNameTags, sage.lastNameTags)
                    res3 = 1 if sa.nickname == "" else 0

                    if res0 and res1 and res2 and res3:
                        st = StrongSageNum()
                        st.isMishna = j
                        st.strongNum = sage.stNum
                        st.weakNumT = sage.stNum
                        st.preffix = sage.preffix
                        st.firstName = sage.firstName
                        st.lastName = sage.lastName
                        st.nickname = sage.nickname
                        st.References = sa.References
                        st.identicalStrongNum = sa.strongNum
                        sa.nickname = "(א)"
                        col.append(st)
                        flag = 1

    return col









# ===========================MAIN===============================================================

pathfindingsFiles = "C:\\findings\\"
pReferenceFiles ="C:\\P2\\referenceFiles"
colToken, colTags, colLemmas, colFeatures, CorpusM, CorpusT, colPatterns, colSorces, colStam, colIdenticalSages,colTanaimList = reader()


# Mishna
lParserM = doSegmentation(CorpusM)
doTaggingWords(lParserM)
lSagesM = doSagesIdentification(lParserM)
writeParserFile(lParserM, "MishnaTokensTags.txt")
writeSagesFile(colTanaimList, "SagesRefMishna.txt")


# Tosefta
lParserT = doSegmentation(CorpusT)
doTaggingWords(lParserT)
lSagesT = doSagesIdentification(lParserT)
writeParserFile(lParserT, "ToseftaTokensTags.txt")
writeSagesFile(colTanaimList, "SagesRefTosefta.txt")

# ParserCouple
lParserCoupleM = analysisTextForCouples(lParserM, 1)
lParserCoupleT = analysisTextForCouples(lParserT, 0)
writeCouplesFile(lParserCoupleM, lParserCoupleT, "Couples.txt")

print("END")