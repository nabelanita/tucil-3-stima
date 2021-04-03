from Input import *
from Utility import *

def AStar(simpulAwal, simpulTujuan, adjDict, listOfDistance):
    # adjDict adalah dictionary hasil return fungsi inputToAdj
    # listOfDistance adalah return fungsi inputToCoor
    result = [simpulAwal]
    tampunganSimpulTetangga = {}

def updateTampunganSimpulTetangga(simpulAwal, simpulSaatIni, tampunganSimpulTetangga, adjDict):
    if (len(tampunganSimpulTetangga) == 0):
        for value in adjDict[simpulAwal]:
            tampunganSimpulTetangga[value[0]] = list((simpulAwal))
    else:
        for value in adjDict[simpulSaatIni]:
            tampunganSimpulTetangga[value[0]] = 

def evaluateElements(simpulAwal, simpulSaatIni, simpulTujuan, adjDict, listOfDistance, tampunganSimpulTetangga):
    # Assign tampunganSimpulTetangga dulu
    
    nilaiTerkecil = 0.0
    simpulSelanjutnya = "placeholder"
    for key in tampunganSimpulTetangga:
        if (nilaiTerkecil == 0.0):
            nilaiTerkecil = getJarakSimpulXKeSimpulAwal(tampunganSimpulTetangga,key,adjDict,simpulAwal) + getJarakLurusSimpulXKeSimpulTujuan(listOfDistance,key,simpulTujuan)
            simpulSelanjutnya = key
        else:
            nilaiSaatIni = getJarakSimpulXKeSimpulAwal(tampunganSimpulTetangga,key,adjDict,simpulAwal) + getJarakLurusSimpulXKeSimpulTujuan(listOfDistance,key,simpulTujuan)
            if (nilaiSaatIni < nilaiTerkecil):
                nilaiTerkecil = nilaiSaatIni
                simpulSelanjutnya = key
    evaluateElements(simpulAwal,simpulSelanjutnya,simpulTujuan,adjDict,listOfDistance,tampunganSimpulTetangga)
    
def getJarakSimpulXKeSimpulAwal(tampunganSimpulTetangga, X, adjDict, simpulAwal):
    # X adalah simpul yang ingin dicari jaraknya dari simpul awal
    jarak = 0.0 # simpen nilai jarak
    if (len(tampunganSimpulTetangga[X]) == 1): # cek kalo value tampunganSimpulTetangga (list) cuma punya satu elemen
        listJarakDariSimpulAwal = adjDict[simpulAwal] # simpen list jarak semua simpul tetangga dari simpul awal
        for value in listJarakDariSimpulAwal: # value bertipe tuple
            if (value[0] == X): # kalo value index ke-0 dari tuple sama dengan X
                jarak += value[1] # tambahin value[1] ke jarak
    else: # value tampunganSimpulTetangga (list) punya lebih dari satu elemen
        listPathSampaiX = tampunganSimpulTetangga[X] # simpen value dari tampunganSimpulTetangga[X] (list)
        for i in range(len(listPathSampaiX)):
            listJarak = adjDict[listPathSampaiX[i]] # tampung list jarak semua simpul tetangga dari listPathSampaiX[i]
            if (i != len(listPathSampaiX)-1): # cek kalo i bukan index terakhir dari listPathSampaiX
                for value in listJarak: # value bertipe tuple
                    if (value[0] == listPathSampaiX[i+1]): # cek kalo value[0] sama dengan listPathSampaiX[i+1] 
                        jarak += value[1]
            else: # kalo i adalah index terakhir dari listPathSampaiX
                for value in listJarak: # value bertipe tuple
                    if (value[0] == X): # cek kalo value[0] sama dengan X
                        jarak += value[1] 
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