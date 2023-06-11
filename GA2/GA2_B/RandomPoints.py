import random

def RandomPoints(N): #n cannot be larger then 99, just use like 10 to 30 points
    if (N > 99):
        print("Input is too big")
        return 0, 0, 0
    RandomlistX = []
    RandomlistY = []
    Nrlist = []
    for i in range(N):
        Good = False
        while(Good == False):
            RandX = random.randint(1, 100)
            try:
                RandomlistX.index(RandX)
            except:
                Good = True

        Good = False
        while(Good == False):
            RandY = random.randint(1, 100)
            try:
                RandomlistY.index(RandY)
            except:
                Good = True
        RandomlistX.append(RandX)
        RandomlistY.append(RandY)
        Nrlist.append(i+1)
    return Nrlist, RandomlistX, RandomlistY