import numpy as np
import math

#imports 25 points and their x and y
#exports route and total length

class Exhange:
    def __init__(self, Pointnr, X, Y):#adds all points as input
        self.Pointnr = Pointnr
        self.PointX = X
        self.PointY = Y
        self.PointX.insert(0,0)
        self.PointY.insert(0,0)
        self.Pointnr.insert(0,0)

    def Distancearray(self):#calculates a distance array list prim and kruskal
        Array = []
        for i in range(len(self.PointX)):
            Column = []
            for j in range(len(self.PointY)):
                Column.append(abs(self.PointX[i]-self.PointX[j])+abs(self.PointY[i]-self.PointY[j]))
            Array.append(Column)
        return Array
    
    def PairExchange(self, Path, Totaldistance):
        
        return Path, Totaldistance
    
    def RunAlgo(self):#this algorithm is a lot alike prim, except it finds the smallest connection on the current point
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
        Path, TotalDistance = self.PairExchange(Path, TotalDistance)
        return Path, TotalDistance
    
