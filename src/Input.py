def inputToAdj(filename):
    # Format text input
    # 0 1 0 2
    # 1 0 3 4
    # 0 3 0 5
    # 2 4 5 0

    # Hasilnya dictionary dengan array isinya tuple
    # nama simpul tetangg dan jaraknya (for now)
    # ie. {A: [(B, 10), (C, 17))]}

    file = open(filename, "r")
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
            if (int(row[j]) > 0):
                result[curr].append((nodes[j], int(row[j])))
    
    return result
        
                



def inputToCoor(filename):
    # Format text input
    # A (x, y)
    # B (x, y)
    # etc

    # Hasil output: dictionary simpul dengan koordinatnya
    # ie. {'A': (x, y), 'B': (x, y)}

    file = open(filename, "r")
    N = int(file.readline())
    result = {}

    for i in range(N):
        line = file.readline().replace('(', ' ').replace(',', ' ').replace(')', ' ').split()
        print(line)
        result.update({line[0]: (int(line[1]), int(line[2]))})
    

    return result
    

r1 = inputToAdj('../test/test1.txt')
r2 = inputToCoor('../test/test1.txt')

print(r1)
print(r2)