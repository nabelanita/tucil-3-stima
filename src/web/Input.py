from Utility import *
import os

def inputToAdjWeb(inputFile):
    file = inputFile.splitlines()
    N = int(file[0])
    result = {}
    nodes = []

    for i in range(1, N+1):
        line = file[i].split(' ')
        result.update({line[0]: []})
        nodes.append(line[0])
    
    for i in range(N+1, 2*N+1):
        curr = nodes[i-(N+1)]
        row = file[i].split(' ')
        for j in range(len(row)):
            if (float(row[j]) > 0):
                result[curr].append((nodes[j], float(row[j])))
    
    return result

# file1 = inputToAdjWeb("../test/test1.txt")
# file2 = inputToAdj("../test/test1.txt")
# print(file1)
# print(file2)

def inputToCoorWeb(inputFile):
    file = inputFile.splitlines()
    N = int(file[0])
    result = {}
    for i in range(1,N+1):
        line = file[i].replace('(', ' ').replace(',', ' ').replace(')', ' ').split()
        result.update({line[0]: (float(line[1]), float(line[2]))})
    
    return result
    


def inputToAdj(filename):
    # Format text input
    # 0 1 0 2 -> dalam km, float
    # 1 0 3 4
    # 0 3 0 5
    # 2 4 5 0

    # Hasilnya dictionary dengan array isinya tuple
    # nama simpul tetangg dan jaraknya (for now)
    # ie. {A: [(B, 10), (C, 17))]}

    # file = open(filename, "r")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    lines = os.path.join(dir_path, "../test/" + filename)
    file = open(lines)
    N = int(file.readline())
    result = {}
    nodes = []

    for i in range(N):
        line = file.readline().split(' ')
        result.update({line[0]: []})
        nodes.append(line[0])
    
    for i in range(N):
        curr = nodes[i]
        row = file.readline().split(' ')
        for j in range(N):
            if (float(row[j]) > 0):
                result[curr].append((nodes[j], float(row[j])))
    
    file.close

    return result
        
                



def inputToCoor(filename):
    # Format text input
    # A (x, y)
    # B (x, y)
    # etc

    # Hasil output: dictionary simpul dengan koordinatnya
    # ie. {'A': (latitude, longitude), 'B': (latitude, longitude)} -> ln lt dalam degree

    dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.name == "nt" :
        lines = os.path.join(dir_path, "..\\test\\" + filename)
    else:
        lines = os.path.join(dir_path, "../test/" + filename)
    file = open(lines)
    N = int(file.readline())
    result = {}

    for i in range(N):
        line = file.readline().replace('(', ' ').replace(',', ' ').replace(')', ' ').split()
        result.update({line[0]: (float(line[1]), float(line[2]))})
    
    file.close()

    return result