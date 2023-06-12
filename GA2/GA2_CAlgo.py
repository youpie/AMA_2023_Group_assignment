import numpy as np
import math

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
        CurrentPoint = 0
        TotalDistance = 0
        Path = [[0],[0],[0]]
        for i in range(len(self.PointX)-1):
            Row = DistanceArray[CurrentPoint]
            sav = 99999999
            for Num in Row:
                if Num < sav and Num != 0:
                    sav = Num
            location = Row.index(sav)           
            for j in range(len(self.PointX)):
                DistanceArray[j][CurrentPoint] = 0
            CurrentPoint = location
            TotalDistance += sav
            Path[0].append(location)
            Path[1].append(self.PointX[location])
            Path[2].append(self.PointY[location])
        Path[0].append(0)
        Path[1].append(0)
        Path[2].append(0)
        TotalDistance += (self.PointX[CurrentPoint] + self.PointY[CurrentPoint])
        Time = TotalDistance/17.4
        Time += len(self.PointX)*1.1*2
        Prev = [0,0]
        for i in range(len(self.PointX)):
            DifX = self.PointX[Path[0][i]]-self.PointX[Path[0][i+1]]
            DifY = self.PointY[Path[0][i]]-self.PointY[Path[0][i+1]]
            if DifX == 0 or DifY == 0:
                pass
            else:
                Time += 1.4
            Prev = [DifX,DifY]
        return Path, TotalDistance, Time
