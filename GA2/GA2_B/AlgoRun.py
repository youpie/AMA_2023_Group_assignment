from NearestNeigAlgo import NearestNeighbour
from AntPheremone import Pher
import random
from RandomPoints import RandomPoints
from matplotlib import pyplot
import time

def TestAlgo(Algo):
    Ftime = time.time()
    TotalDistance = 0
    for i in range(100):#for the average run amount
        NR, Xs, Ys = RandomPoints(25)
        NBAlgo = Algo(NR, Xs, Ys)
        Path, Distance = NBAlgo.RunAlgo()
        TotalDistance += Distance
        #print(Path[0])
    TotalTime = time.time() - Ftime
    pyplot.scatter(Path[1],Path[2])
    pyplot.plot(Path[1],Path[2])
    pyplot.show()
    return TotalDistance/100, TotalTime

Distance, Time = TestAlgo(NearestNeighbour)#current algorithms are Pher and NearestNeighbour, they are the import files
print(Distance)
print(Time)


#pyplot.scatter(Path[1],Path[2])
#pyplot.plot(Path[1],Path[2])
#pyplot.show()