import numpy as np
import csv
import os
import math
import time
import matplotlib.pyplot as plt

starttime = time.time_ns()

def Distance(Xa, Ya, Xb, Yb):#calculates the distance between 2 points with pythagoras
    D = (math.sqrt((Xa-Xb)**2+(Ya-Yb)**2))
    return D

pointarray = []
with open(os.path.dirname(__file__) + "\inputGAS2A.csv", "r") as input:#reads all of the points from the file
    locations = csv.DictReader(input)
    for pointentry in locations:
        point = [int(pointentry["Point number"]),float(pointentry["x"]), float(pointentry["y"])]
        pointarray.append(point)
number,X,Y = zip(*pointarray)

DistanceArray = []#calculates the distance from every point to ever other points
for i in pointarray:
    Columbs = []
    for j in pointarray:
        Columbs.append(Distance(i[1],i[2],j[1],j[2]))
    DistanceArray.append(Columbs)
DistanceArray = np.asarray(DistanceArray)           

Outputlist=[]#creates an empty output list
for i in range(len(DistanceArray[0])+1):
    columb = []
    for j in range(len(DistanceArray[0])+1):
        columb.append('-')
    Outputlist.append(columb)

Connected = [0]
for i in range(len(DistanceArray[0])-1):#as prim algorithm goes, it adds point 1, then goes trough all connected points and finds the lowest distance
    sav = 999999999999999               #connection and adds that point, then makes all of the connections of that point to the other connected ones 0
    for j in Connected:                 #and then keep repeating this until all points are added
        Row = DistanceArray[j]
        if np.min(Row[np.nonzero(Row)])<sav:
            sav = np.min(Row[np.nonzero(Row)])
    location = np.asarray(np.where(DistanceArray == sav))
    for Num in location[0]:
        if Num not in Connected:
            Connected.append(Num)
            break
    sav = [9999999999, 1, 1]
    for j in Connected:
        for d in Connected:
            if DistanceArray[j][d]<sav[0] and DistanceArray[j][d] != 0:
                sav = [DistanceArray[j][d], j, d]
            DistanceArray[j][d] = 0
    plt.plot([X[sav[1]],X[sav[2]]],[Y[sav[1]],Y[sav[2]]])
    Outputlist[sav[1]+1][sav[2]+1] = str(round(sav[0], 3))
    Outputlist[sav[2]+1][sav[1]+1] = str(round(sav[0], 3))

Outputlist[0][0] = "x" #just used for formatting of the outputlist, adds the 1...n to the top and left
for i in range(len(Outputlist[0])-1):
    Outputlist[i+1][0] = i+1
    Outputlist[0][i+1] = i+1

np.savetxt(os.path.dirname(__file__) + '\OutputGAS2A1.csv', Outputlist, delimiter =", ", fmt ='% s')#writes out the list

print("--- total runtime is: " + str((time.time_ns() - starttime)/1000000) + "ms ---")#prints the total time taken


plt.scatter(X,Y)
plt.show()#plots all of the points and opens a graph to show the minimum spanning tree