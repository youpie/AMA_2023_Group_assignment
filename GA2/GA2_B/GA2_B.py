from NearestNeigAlgo import NearestNeighbour
from AntPheremone import Pher
from RandoTry import RandomTries
import random
from RandomPoints import RandomPoints
from matplotlib import pyplot
import time

def TestAlgo(Algo):
    Ftime = time.time()
    TotalDistance = 0
    for i in range(100):#for the average run amount
        NR, Xs, Ys = RandomPoints(90)
        NBAlgo = Algo(NR, Xs, Ys)
        Path, Distance = NBAlgo.RunAlgo()
        TotalDistance += Distance
        #print(Path[0])
    TotalTime = time.time() - Ftime
    pyplot.scatter(Path[1],Path[2])
    pyplot.plot(Path[1],Path[2])
    pyplot.show()
    return TotalDistance/100, TotalTime

Distance, Time = TestAlgo(Pher)#current algorithms are Pher, NearestNeighbour and RandomTries, they are the import files
#this will give you the average distance the algorithm gives and how long it takes to do so
#this allows you to test algorithms by importing them as classes and running them a lot with random points
print(Distance)
print(Time)