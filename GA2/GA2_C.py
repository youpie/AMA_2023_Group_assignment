from GA2_CAlgo import Exhange
from matplotlib import pyplot
import matplotlib
import numpy as np
import os
import csv

def LoadPoints():
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
Path, Distance = NBAlgo.RunAlgo()

pyplot.plot(Path[1],Path[2])
pyplot.scatter(Path[1],Path[2])
pyplot.show()
Time = 0
Outputlist = [0]
Outputlist[0] = ("Total time: "+ str(Time))
Outputlist.append("Route: " + str(Path[0]))

np.savetxt(os.path.dirname(__file__) + '\OutputGAS2C.csv', Outputlist, delimiter =", ", fmt ='% s')