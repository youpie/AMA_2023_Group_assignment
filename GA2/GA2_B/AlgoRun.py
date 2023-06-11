from NearestNeigAlgo import NearestNeighbour
import random
from RandomPoints import RandomPoints
from matplotlib import pyplot
import time

def TestAlgo(Algo):
    Ftime = time.time()
    TotalDistance = 0
    for i in range(100):
        NR, Xs, Ys = RandomPoints(25)
        NBAlgo = Algo(NR, Xs, Ys)
        Path, Distance = NBAlgo.RunAlgo()
        TotalDistance += Distance
    TotalTime = time.time() - Ftime
    return TotalDistance/100, TotalTime

Distance, Time = TestAlgo(NearestNeighbour)
print(Distance)
print(Time)


#pyplot.scatter(Path[1],Path[2])
#pyplot.plot(Path[1],Path[2])
#pyplot.show()