from Algoritma import *

r1 = inputToAdj("../test/test1.txt")
r2 = inputToCoor("../test/test1.txt")

# print(r1)
# print(r2)

distToRome = findDistanceTo(r2, 'Rome')
# print(distToRome)

AStar('Rome', 'Madrid', r1, r2)
