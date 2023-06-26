from GA2_CAlgo import Exhange
from matplotlib import pyplot
import matplotlib
import numpy as np
import os
import csv

def LoadPoints(): #loads the points from the csv file
    pointarray = []
    with open(os.path.dirname(__file__) + "\inputGAS2C.csv", "r") as input:
        locations = csv.DictReader(input)
        for pointentry in locations:
            point = [int(pointentry["Point number"]),float(pointentry["x"]), float(pointentry["y"])]
            pointarray.append(point)
    return pointarray

PointArray = LoadPoints()
Nr, Xs, Ys = zip(*PointArray)
NBAlgo = Exhange(list(Nr), list(Xs), list(Ys))
Path, Distance = NBAlgo.RunAlgo() #runs the algorithm

pyplot.plot(Path[1],Path[2])
pyplot.scatter(Path[1],Path[2])
pyplot.show() #plots the points

Time = 0 #here we add up the time per part
Time += Distance/17.4 #where it would definatly take this amount of time to travel this distance
Time += (len(Path[0])-1)*1.1*2 #it needs to start and stop for each point, but only once for point 0 so thats why -1

TurnNumber = 0 #we find the number of 90 degree turns it needs to take
for i in range(len(Path[0])-1): #to check for all points
    if (Path[1][i]%1>0 and Path[1][i+1]%1>0) or (Path[2][i]%1>0 and Path[2][i+1]%1>0): #if 2 points have an uneven x or 2 uneven y's it would need to take 2 turns
        TurnNumber += 2
    elif Path[1][i]-Path[1][i+1] != 0 and Path[2][i]-Path[2][i+1] != 0: #if it is not in a straight line it would need to take 1 turn
        TurnNumber += 1
    elif Path[1][i]-Path[1][i+1] == 0 or Path[2][i]-Path[2][i+1] == 0: # if it is in a straight line it would not need to do anything
        pass
Time += TurnNumber * 1.4 #finding the amound of time needed for all of the 90 degree turns

Outputlist = [0]
Outputlist[0] = ("Total time: "+ str(Time))
Outputlist.append("Route: " + str(Path[0]))

np.savetxt(os.path.dirname(__file__) + '\OutputGAS2C.csv', Outputlist, delimiter =", ", fmt ='% s') #outputting the time and path to the csv file