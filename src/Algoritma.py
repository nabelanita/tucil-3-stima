from Input import *

def AStar(simpulAwal, simpulTujuan, adjDict, listOfDistance):
    # adjDict adalah dictionary hasil return fungsi inputToAdj
    # listOfDistance adalah return fungsi inputToCoor
    result = []
    tampunganSimpulTetangga = []
    listSimpulTetangga = adjDict[simpulAwal]
    print(listSimpulTetangga)
    visited = {}
    for key in listOfDistance:
        visited[key] = False
    evaluateSimpul(simpulAwal,simpulAwal,listSimpulTetangga,simpulTujuan,tampunganSimpulTetangga,result,visited,adjDict,listOfDistance)

def evaluateSimpul(simpulAwal, simpulSekarang, listSimpulTetangga, simpulTujuan, tampunganSimpulTetangga, result, visited, adjDict, listOfDistance):
    if (simpulSekarang == simpulTujuan):
        listReturn = list(listSimpulTetangga)
        listReturn.append(simpulSekarang)
        return listReturn
    else:
        print(simpulSekarang)
        listTampungan = list(listSimpulTetangga)
        listTampungan.append(simpulSekarang)
        # for dictionary in tampunganSimpulTetangga:
        #     if simpulSekarang in dictionary:
        #         listTampungan = list(dictionary[simpulSekarang])
        #         listTampungan.append(simpulSekarang)

        for key in adjDict:
            if (key == simpulSekarang):
                for tup in adjDict[key]:
                    if not (visited[tup[0]]):
                        calonKey = tup[0]
                        calonDict = {calonKey: listTampungan}
                        tampunganSimpulTetangga.append(calonDict)
        
        for dictionary in tampunganSimpulTetangga:
            if (simpulSekarang in dictionary):
                if (isTwoListsEqual(listSimpulTetangga,dictionary[simpulSekarang])):
                    visited[simpulSekarang] = True
                    tampunganSimpulTetangga.remove(dictionary)
                    break

        nilaiTerkecil = 0.0
        simpulWithNilaiTerkecil = "X"
        for dictionary in tampunganSimpulTetangga:
            for key in dictionary:
                listSementara = list(dictionary[key])
                listSementara.append(key)
                jarakSementara = getJarakSimpulXKeSimpulAwal(listSementara,adjDict) + getJarakLurusSimpulXKeSimpulTujuan(listOfDistance,simpulSekarang,simpulTujuan)
                if (nilaiTerkecil == 0.0):
                    nilaiTerkecil = jarakSementara
                    simpulWithNilaiTerkecil = key
                else:
                    if (jarakSementara < nilaiTerkecil):
                        nilaiTerkecil = jarakSementara
                        simpulWithNilaiTerkecil = key    

        for dictionary in tampunganSimpulTetangga:
            if simpulWithNilaiTerkecil in dictionary:
                listTampungan = list(dictionary[simpulWithNilaiTerkecil])
                # listTampungan.append(simpulSekarang)
        evaluateSimpul(simpulAwal,simpulWithNilaiTerkecil,listTampungan,simpulTujuan,tampunganSimpulTetangga,result,visited,adjDict,listOfDistance)

def getJarakSimpulXKeSimpulAwal(listUrutanJalan, adjDict):
    jarak = 0.0
    for i in range(len(listUrutanJalan)-1):
        for key in adjDict:
            if (key == i):
                for tup in adjDict[key]:
                    if (tup[0] == i+1):
                        jarak += tup[1]
    return jarak

def getJarakLurusSimpulXKeSimpulTujuan(listOfDistance, X, simpulTujuan):
    # X adalah simpul saat ini
    # listOfDistance adalah return dari fungsi inputToCoor
    dictJarakLurus = findDistanceTo(listOfDistance,simpulTujuan)
    jarakLurus = 0.0
    for key in dictJarakLurus:
        if (key == X):
            jarakLurus = dictJarakLurus[key]
    return jarakLurus

def isTwoListsEqual(list1, list2):
    equal = True
    for element1 in list1:
        if not (element1 in list2):
            equal = False
            break
    if not (equal):
        return equal
    else:
        for element2 in list2:
            if not (element2 in list1):
                equal = False
                break
        return equal