from Algoritma import *

r1 = inputToAdj("test1.txt")
r2 = inputToCoor("test1.txt")


print(r2)

distToRome = findDistanceTo(r2, 'Rome')
# print(distToRome)

AStar('Rome', 'Madrid', r1, r2)
