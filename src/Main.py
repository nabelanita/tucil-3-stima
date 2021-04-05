from Algoritma import *
from Graph import *

r1 = inputToAdj("../test/test3.txt")
r2 = inputToCoor("../test/test3.txt")

# print(r1)
# print(r2)

# distToRome = findDistanceTo(r2, 'Rome')
# print(distToRome)

# AStar('BundaranHI', 'Gambir', r1, r2)
newGraph = makeGraph(r1,r2)
print(type(newGraph))