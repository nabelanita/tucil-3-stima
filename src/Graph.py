from Algoritma import *
import networkx as nx
import matplotlib.pyplot as plt

def makeGraph(adjDict,listOfDistance):
    G = nx.Graph()

    # Masukin semua simpul ke graph
    for key in listOfDistance:
        G.add_node(key)
    
    # Hubungin semua node pake edge
    for key in adjDict:
        for tup in adjDict[key]:
            G.add_edge(key,tup[0],color="red")
    
    return G

def modifyGraph(graph,listReturn):
    tempGraph = nx.Graph(graph)
    for i in range(len(listReturn)-2):
        tempGraph.add_edge(listReturn[i],listReturn[i+1],color="red")
    return tempGraph

r1 = inputToAdj("../test/test3.txt")
r2 = inputToCoor("../test/test3.txt")
result = AStar("BundaranHI", "Gambir", r1, r2)
g1 = makeGraph(r1,r2)
g2 = modifyGraph(g1,result)

# Draw the graph
nx.draw(g2, with_labels=True)
plt.show()