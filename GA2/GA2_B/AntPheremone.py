import numpy as np
import math
import random
import copy

#imports 25 points and their x and y
#exports route and total length

class Pher:
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
        ChanceArraySav = []
        for i in range(len(self.PointX)):
            Column = []
            for j in range(len(self.PointY)):
                if i == j:
                    Column.append(0)
                else:
                    Column.append(1)
            ChanceArraySav.append(Column)
        for i in range(len(ChanceArraySav)):
            ChanceArraySav[i][0] = 0

        for i in range(1):
            for i in range(100):#amount of ants to send out
                CurrentPoint = 0
                TotalDistance = 0
                ChanceArray = copy.deepcopy(ChanceArraySav)
                Path = [[0],[0],[0]]
                for i in range(len(self.PointX)-1):
                    Row = DistanceArray[CurrentPoint]
                    RowSav = Row
                    RowChance = ChanceArray[CurrentPoint]
                    sav = random.choices(Row, RowChance)
                    location = 0
                    for i in range(len(RowSav)):
                        if sav[0] == RowSav[i]:
                            location = i
                #location = np.where(RowSav)
                    CurrentPoint = location
                    for j in range(len(self.PointX)):
                        ChanceArray[j][CurrentPoint] = 0
                    TotalDistance += sav[0]
                    Path[0].append(location)
                    Path[1].append(self.PointX[location])
                    Path[2].append(self.PointY[location])
                EndCap = self.PointX[CurrentPoint] + self.PointY[CurrentPoint]
                Addition = ((100/(EndCap+TotalDistance))*5)**2
                Path[0].append(0)
                Path[1].append(0)
                Path[2].append(0)
                for i in range(len(Path[0])-1): # use to increase pheremone count on good path
                    ChanceArraySav[Path[0][i]][Path[0][i+1]] = ChanceArraySav[Path[0][i]][Path[0][i+1]]+Addition
                    ChanceArraySav[Path[0][i+1]][Path[0][i]] = ChanceArraySav[Path[0][i+1]][Path[0][i]]+Addition
        TotalDistance += (self.PointX[CurrentPoint] + self.PointY[CurrentPoint])
        return Path, TotalDistance
