from Input import *

def AStar(simpulAwal, simpulTujuan, adjDict, listOfDistance):
    # adjDict adalah dictionary hasil return fungsi inputToAdj
    # listOfDistance adalah return fungsi inputToCoor
    tampunganSimpulTetangga = [{simpulAwal: []}]
    # print(tampunganSimpulTetangga)
    listSimpulTetangga = []
    # for tup in adjDict[simpulAwal]:
    #     listSimpulTetangga.append(tup[0])
    # print(listSimpulTetangga)
    visited = {}
    for key in listOfDistance:
        visited[key] = False
    # print(visited)
    result = evaluateSimpul(simpulAwal,simpulAwal,listSimpulTetangga,simpulTujuan,tampunganSimpulTetangga,visited,adjDict,listOfDistance)
    print(result)
    return result

def evaluateSimpul(simpulAwal, simpulSekarang, listSimpulTetangga, simpulTujuan, tampunganSimpulTetangga, visited, adjDict, listOfDistance):
    tempListSimpulTetangga = list(listSimpulTetangga)
    tempVisited = visited
    tempTampunganSimpulTetangga = list(tampunganSimpulTetangga)
    if (simpulSekarang == simpulTujuan):
        listReturn = list(listSimpulTetangga)
        listReturn.append(simpulSekarang)
        cost = getJarakSimpulXKeSimpulAwal(listReturn,adjDict)
        # print(cost)
        listReturn.append(cost)
        return listReturn
    else:
        # print(simpulSekarang)
        listTampungan = list(tempListSimpulTetangga)
        listTampungan.append(simpulSekarang)
        print(listTampungan)
        # for dictionary in tampunganSimpulTetangga:
        #     if simpulSekarang in dictionary:
        #         listTampungan = list(dictionary[simpulSekarang])
        #         listTampungan.append(simpulSekarang)

        for key in adjDict:
            if (key == simpulSekarang):
                for tup in adjDict[key]:
                    if not (tempVisited[tup[0]]):
                        calonKey = tup[0]
                        calonDict = {calonKey: listTampungan}
                        tempTampunganSimpulTetangga.append(calonDict)
        print("Ini tampunganSimpulTetangga yang udah ditambah sama tetangga baru")
        print(tempTampunganSimpulTetangga)
        
        for dictionary in tempTampunganSimpulTetangga:
            if (simpulSekarang in dictionary):
                if (isTwoListsEqual(tempListSimpulTetangga,dictionary[simpulSekarang])):
                    tempVisited[simpulSekarang] = True
                    tempTampunganSimpulTetangga.remove(dictionary)
                    break
        # if not(visited[simpulAwal]):
        #     visited[simpulAwal] = True
        print("visited yang baru:")
        print(tempVisited)
        print("tampunganSimpulTetangga hasil udah remove simpul sekarang")
        print(tempTampunganSimpulTetangga)

        nilaiTerkecil = 0.0
        simpulWithNilaiTerkecil = "X"
        for dictionary in tempTampunganSimpulTetangga:
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
        print("Simpul yang bakal dikunjungin selanjutnya: ")
        print(simpulWithNilaiTerkecil) 

        for dictionary in tampunganSimpulTetangga:
            if simpulWithNilaiTerkecil in dictionary:
                listTampungan = list(dictionary[simpulWithNilaiTerkecil])
                # listTampungan.append(simpulSekarang)
        print("listTampungan baru:")
        print(listTampungan)
        return evaluateSimpul(simpulAwal,simpulWithNilaiTerkecil,listTampungan,simpulTujuan,tempTampunganSimpulTetangga,tempVisited,adjDict,listOfDistance)

def getJarakSimpulXKeSimpulAwal(listUrutanJalan, adjDict):
    jarak = 0.0
    for i in range(len(listUrutanJalan)-1):
        for key in adjDict:
            if (key == listUrutanJalan[i]):
                for tup in adjDict[key]:
                    if (tup[0] == listUrutanJalan[i+1]):
                        jarak += tup[1]
                        # print(jarak)
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