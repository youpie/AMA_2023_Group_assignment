from NearestNeigAlgo import NearestNeighbour
import random
from RandomPoints import RandomPoints
from matplotlib import pyplot
    

def TestAlgo(Algo):
    TotalDistance = 0
    for i in range(100):
        NR, Xs, Ys = RandomPoints(25)
        NBAlgo = Algo(NR, Xs, Ys)
        Path, Distance = NBAlgo.RunAlgo()
        TotalDistance += Distance
    return TotalDistance

Distance = TestAlgo(NearestNeighbour)
print(Distance)

#pyplot.scatter(Path[1],Path[2])
#pyplot.plot(Path[1],Path[2])
#pyplot.show()