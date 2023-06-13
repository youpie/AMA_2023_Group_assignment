import csv
import math
import numpy as np

def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        points = []
        next(reader)  # Ignore the first row
        for row in reader:
            values = row[1:]  # Ignore the first column
            points.append([float(value) for value in values])
        return np.array(points)

def calculate_conic_section(points):
    x = points[:, 0]
    y = points[:, 1]
    A = np.vstack([x**2, x*y, y**2, x, y]).T
    b = -np.ones(len(points))
    conic_coefficients = np.linalg.lstsq(A, b, rcond=None)[0]
    return conic_coefficients

def calculate_determinant_and_solutions(conic_coefficients):
    a, b, c, d, e = conic_coefficients
    #use discriminant of abc formula since al coefficients with y are 0
    discriminant = d**2 - 4 * a * 1
    if discriminant < 0:
        return []  # No real solutions
    
    #use abc formula to calculate zeroes
    x1 = (-d + math.sqrt(discriminant) )/(2*a)
    x2 = (-d - math.sqrt(discriminant) )/(2*a)
    return [x1, x2]

def landing_location(array):
    xtotal = []
    #add the input points to an array if they are bigger than 0
    for x in array:
        if x > 0:
            xtotal.append(x)   

    print("Predicted landing location is:")
    if len(xtotal) > 1:
        #prints furthest distance if the are multiple zeroes bigger than 0
        if xtotal[0] < xtotal[1]:
            print(xtotal[1])
        else:
            print(xtotal[0])
        #otherwise just print the zero that was found
    else:
        if len(xtotal) == 1:
            print(xtotal[0])
        else:
            print("No zeroes were found.")
#inputfile is defined here
file_path = 'inputGA1B.csv'

#print all the info
points = parse_input_file(file_path)
#print all points (mostly for testing purposes)
for i in points:
    print(i)
#calculate conic section coefficients
conic_coefficients = calculate_conic_section(points)
#calculate zeroes
points_y_equals_zero = calculate_determinant_and_solutions(conic_coefficients)
#print all coefficients
print("Conic section coefficients:", conic_coefficients)
#print all zeroes
print("Points where y = 0:", points_y_equals_zero)
#print all positive zeroes (possible landing locations)
landing_location(points_y_equals_zero)
