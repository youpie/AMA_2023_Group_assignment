import numpy as np
import math
import random
import copy

#imports 25 points and their x and y
#exports route and total length

class RandomTries:#this algorithm is very simple, generate a random path, how long is this path?
    def __init__(self, Pointnr, X, Y):#is it shorter than the shortest found path? yes then save the path and the distance
        self.Pointnr = Pointnr #and do this for x amount of times
        self.PointX = X
        self.PointY = Y
        self.PointX.insert(0,0)
        self.PointY.insert(0,0)
        self.Pointnr.insert(0,0)
    
    def RunAlgo(self):
        MinDistance = 999999999
        PathSav = []
        Path = [[0],[0],[0]]
        for i in range(500):
            Points = copy.deepcopy(self.Pointnr)
            RandoPath=[]
            TotalDistance = 0
            for j in range(len(self.Pointnr)):
                NewPoint = random.choice(Points)
                RandoPath.append(NewPoint)
                Points.pop(Points.index(NewPoint))
            RandoPath.append(0)
            for j in range(len(RandoPath)-1):
                Current = RandoPath[j]
                Next = RandoPath[j+1]
                TotalDistance += (abs(self.PointX[Current]-self.PointX[Next])+abs(self.PointY[Current]-self.PointY[Next]))
            if TotalDistance < MinDistance:
                MinDistance = TotalDistance
                PathSav = copy.deepcopy(RandoPath)
        PathSav.pop(0)
        for Point in PathSav:
            Path[0].append(self.Pointnr[Point])
            Path[1].append(self.PointX[Point])
            Path[2].append(self.PointY[Point])
        return Path, MinDistance