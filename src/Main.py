from Algoritma import *

r1 = inputToAdj("../test/test3.txt")
r2 = inputToCoor("../test/test3.txt")

print("============DARI MAIN NON WEB=============")
print(r1)
print(r2)
print(" ")

# distToRome = findDistanceTo(r2, 'Rome')
# print(distToRome)

result = AStar('BundaranHI', 'Gambir', r1, r2)
print(result)
conv = convertToLatLng(result, r2)
print(conv)
