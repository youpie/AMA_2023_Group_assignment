import csv
import os #added to be used to find the input and output files easier
import numpy as np
from typing import List

def modify_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        rows = [row[1:] for row in reader]  # Delete first column

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Modified CSV file created successfully.")

# Example usage:
input_file = 'inputGA1A.csv'      # Replace with the path to your input CSV file
output_file = 'inputGA1AYES.csv'    # Replace with the desired path for the modified CSV file

modify_csv(input_file, output_file)

#this is a class which allows you to save the x and y of a point
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        

#these 2 calculate the A B C D E for the matrix and the right side
    def ellipseEQ(self):
        return [self.y**2 ,self.x*self.y ,self.x, self.y, -1]

    def ellipseSQ(self):
        return self.x**2

inputarray = []

#reads the points from the file, taken from IA1 example with a change to the filepath to make it easier to use
with open(os.path.dirname(__file__) + "\inputGA1AYES.csv", "r") as input:
    locations = csv.DictReader(input)
    for pointentry in locations:
        point = Point(pointentry["x"], pointentry["y"])
        inputarray.append(point)

#finds the amount of points
calcarray = np.array(inputarray)
numOfRows = calcarray.shape[0]

if numOfRows == 5: #checks if the amount of points is the amount intended
    sol = []
    eq = []
    print("Given 5 points an ellipse equation will be calculated")
    for n in range(5): #finds each row for the matrix
        eq.append(inputarray[n].ellipseEQ())
        sol.append(inputarray[n].ellipseSQ())

    #makes a 5x5 array and a vector length 5 for np to solve
    eqarray = np.array(eq)
    solarray = np.array(sol)

    #checks to see if the detirminate is 0 to make sure if there is a solution
    if np.linalg.det(eqarray) != 0:
        #the solving and formatting of the solution, the *-1 is to negate the -1 which isent in ellipseSQ
        #i added a round because no sensor is precise enough to measure the absurd amount of decimal places it had first
        # also the value of 2.9999999999 hurts my eyes
        solution = np.round(np.linalg.solve(eqarray, solarray)*-1, 4)
        Equation = ["{0},{1},{2},{3},{4}".format(solution[0], solution[1], solution[2], solution[3], solution[4])]

        #opens the excel file and writes the equation into it to then close it again
        f = open(os.path.dirname(__file__) + '\outputfile GA1A.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(Equation)
        f.close()
    else: # both of these give feedback so when someone inputs bad points they will know
        print("this is not a valid set of points")
else:
    print("this is not a valid set of points")