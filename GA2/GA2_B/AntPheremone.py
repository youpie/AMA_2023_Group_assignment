import numpy as np
import math
import random

#imports 25 points and their x and y
#exports route and total length

class NearestNeighbour:
    def __init__(self, Pointnr, X, Y):
        self.Pointnr = Pointnr
        self.PointX = X
        self.PointY = Y
        self.PointX.insert(0,0)
        self.PointY.insert(0,0)
        self.Pointnr.insert(0,0)

    def Distancearray(self):
        Array = []
        for i in range(len(self.PointX)):
            Column = []
            for j in range(len(self.PointY)):
                Column.append(abs(self.PointX[i]-self.PointX[j])+abs(self.PointY[i]-self.PointY[j]))
            Array.append(Column)
        return Array
    
    def RunAlgo(self):
        DistanceArray = self.Distancearray()
        ChanceArray = []
        for i in range(len(self.PointX)):
            Column = []
            for j in range(len(self.PointY)):
                Column.append(1)
            ChanceArray.append(Column)
        CurrentPoint = 0
        TotalDistance = 0
        Path = [[0],[0],[0]]
        for i in range(len(self.PointX)-1):
            Row = DistanceArray[CurrentPoint]
            RowChance = ChanceArray[CurrentPoint]
            sav = random.choices(Row, RowChance)
            location = Row.index(sav)
        Path[0].append(0)
        Path[1].append(0)
        Path[2].append(0)
        TotalDistance += (self.PointX[CurrentPoint] + self.PointY[CurrentPoint])
        return Path, TotalDistance
