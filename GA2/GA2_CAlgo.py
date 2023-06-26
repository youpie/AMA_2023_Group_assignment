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
    
    def Switch(self, A, B, Path):
        Inbet0 = Path[0][A+1]
        Path[0][A+1] = Path[0][B]
        Path[0][B] = Inbet0

        Inbet1 = Path[1][A+1]
        Path[1][A+1] = Path[1][B]
        Path[1][B] = Inbet1

        Inbet2 = Path[2][A+1]
        Path[2][A+1] = Path[2][B]
        Path[2][B] = Inbet2

        if B > (A + 3):
            Replace0 = Path[0][A+2:B]
            Replace1 = Path[1][A+2:B]
            Replace2 = Path[2][A+2:B]
            Replace0.reverse()
            Replace1.reverse()
            Replace2.reverse()
            for i in range(len(Replace0)):
                Path[0][A+i+2] = Replace0[i]
                Path[1][A+i+2] = Replace1[i]
                Path[2][A+i+2] = Replace2[i]
        return Path
    
    def Distance(self, A, B, Path):
        Distance = abs(Path[1][A]-Path[1][B])+abs(Path[2][A]-Path[2][B])
        return Distance

    def PairExchange(self, Path, Totaldistance):
        sav = len(Path[0])-3
        for i in range(sav):
            for j in range(sav - i):
                Index2 = j + i + 2
                SwitchLength = self.Distance(i,Index2,Path) + self.Distance(i+1,Index2+1,Path)
                CurrentLength = self.Distance(i,i+1,Path) + self.Distance(Index2,Index2+1,Path)
                if SwitchLength < CurrentLength:
                    self.Switch(i,Index2,Path)
                    Totaldistance = (Totaldistance - CurrentLength) + SwitchLength
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
        Path, TotalDistance = self.PairExchange(Path, TotalDistance)
        Path, TotalDistance = self.PairExchange(Path, TotalDistance)
        Path, TotalDistance = self.PairExchange(Path, TotalDistance)
        Path, TotalDistance = self.PairExchange(Path, TotalDistance)
        Path, TotalDistance = self.PairExchange(Path, TotalDistance)
        return Path, TotalDistance
    
