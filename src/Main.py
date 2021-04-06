from Algoritma import *
# from Graph import *

r1 = inputToAdj("../test/test3.txt")
r2 = inputToCoor("../test/test3.txt")

result = AStar('TuguTani', 'Monas', r1, r2)
print(result)
conv = convertToLatLng(result, r2)
print(conv)
