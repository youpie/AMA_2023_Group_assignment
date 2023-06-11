import numpy as np
import math
from collections import defaultdict

#imports 25 points and their x and y
#exports route and total length

class NearestNeighbour:
    def __init__(self, Pointnr, X, Y):
        self.Pointnr = Pointnr
        self.PointX = X
        self.PointY = Y

    def Distancearray(self):
        Array = []
        for Xs in self.X:
            Column = []
            for Ys in self.Y:
                
        return Array
    
    def RunAlgo(self):
        