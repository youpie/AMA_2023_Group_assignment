import numpy as np
import csv
import os
import math
from collections import defaultdict
import time
import matplotlib.pyplot as plt

starttime = time.time_ns()

def Distance(Xa, Ya, Xb, Yb):
    D = (math.sqrt((Xa-Xb)**2+(Ya-Yb)**2))
    return D

pointarray = []
with open(os.path.dirname(__file__) + "\inputGAS2A.csv", "r") as input:
    locations = csv.DictReader(input)
    for pointentry in locations:
        point = [int(pointentry["Point number"]),float(pointentry["x"]), float(pointentry["y"])]
        pointarray.append(point)

DistanceArray = []
for i in pointarray:
    Columbs = []
    for j in pointarray:
        Columbs.append(Distance(i[1],i[2],j[1],j[2]))
    DistanceArray.append(Columbs)

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        number,X,Y = zip(*pointarray)
        for u, v, weight in result:
            Outputlist[u+1][v+1] = round(weight,3)
            Outputlist[v+1][u+1] = round(weight,3)
            plt.plot([X[u],X[v]],[Y[u],Y[v]])

Outputlist=[]
for i in range(len(DistanceArray[0])+1):
    columb = []
    for j in range(len(DistanceArray[0])+1):
        columb.append('-')
    Outputlist.append(columb)

Tree = Graph(len(DistanceArray[0]))
for j in range(len(DistanceArray[0])):
    for i in range(len(DistanceArray[0])):
        if DistanceArray[j][i] != 0:
            Tree.add_edge(j,i,DistanceArray[j][i])
Tree.kruskal()

Outputlist[0][0] = "x"
for i in range(len(Outputlist[0])-1):
    Outputlist[i+1][0] = i+1
    Outputlist[0][i+1] = i+1

np.savetxt(os.path.dirname(__file__) + '\OutputGAS2A2.csv', Outputlist, delimiter =", ", fmt ='% s')

print("--- total runtime is: " + str((time.time_ns() - starttime)/1000000) + "ms ---")

number,X,Y = zip(*pointarray)
plt.scatter(X,Y)
plt.show()