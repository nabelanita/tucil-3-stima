from math import radians, cos, sin, asin, sqrt

def findDistanceTo(coorNode, target):
    targetCoor = coorNode[target]
    result = {}

    for key in coorNode:
        if (key != target):
            result.update({key: findDistanceTwoNodes(coorNode, key, target)})
    
    return result


def findDistanceTwoNodes(coorNode, source, target):
    srcCoor = coorNode[source]
    trgCoor = coorNode[target]
    return haversine(srcCoor[0], srcCoor[1], trgCoor[0], trgCoor[1])

def haversine(ltA, lnA, ltB, lnB):
    lnA, ltA, lnB, ltB = map(radians, [lnA, ltA, lnB, ltB])

    # rumus haversine
    # 6317 = jari2 bumi dlm km
    return 6371.0088 * 2.0 * asin(sqrt(sin((ltB - ltA)/2.0)**2.0 + cos(ltA) * cos(ltB) * sin((lnB - lnA)/2.0)**2.0))

def convertToLatLng(source, listCoor):
    result = []
    for i in range(len(source)-1):
        result.append((listCoor[source[i]][0],listCoor[source[i]][1]))

    return result