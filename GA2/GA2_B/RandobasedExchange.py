import numpy as np
import math
import random
import copy

#imports 25 points and their x and y
#exports route and total length

class RandomExchange:#this algorithm is very simple, generate a random path, how long is this path?
    def __init__(self, Pointnr, X, Y):#is it shorter than the shortest found path? yes then save the path and the distance
        self.Pointnr = Pointnr #and do this for x amount of times
        self.PointX = X
        self.PointY = Y
        self.PointX.insert(0,0)
        self.PointY.insert(0,0)
        self.Pointnr.insert(0,0)

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
    
    def RunAlgo(self):
        MinDistance = 999999999
        PathSav = []
        Path = [[0],[0],[0]]
        for i in range(1):
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
                PathSav = RandoPath
        PathSav.pop(0)
        for Point in PathSav:
            Path[0].append(self.Pointnr[Point])
            Path[1].append(self.PointX[Point])
            Path[2].append(self.PointY[Point])
        Path, MinDistance = self.PairExchange(Path, MinDistance)
        Path, MinDistance = self.PairExchange(Path, MinDistance)
        Path, MinDistance = self.PairExchange(Path, MinDistance)
        Path, MinDistance = self.PairExchange(Path, MinDistance)
        return Path, MinDistance