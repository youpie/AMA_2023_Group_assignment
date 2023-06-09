import csv
import numpy as np

def fit_parabola(input_file):
    # Read data from the input CSV file
    with open(input_file, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        rows = list(reader)[1:]  # Skip the first row
        points = [tuple(map(float, row[1:])) for row in rows]  # Skip the first column

    # Extract x and y data from the points
    x_data = np.array([point[0] for point in points])
    y_data = np.array([point[1] for point in points])

    # Create the coefficient matrix A and the constant vector b
    A = np.vstack([x_data ** 2, x_data, np.ones(len(x_data))]).T
    b = y_data

    # Solve the linear system of equations to find the parabola equation coefficients
    coefficients = np.linalg.lstsq(A, b, rcond=None)[0]

    # Extract the coefficients for the parabola equation
    a, b, c = coefficients

    # Construct the parabola equation
    parabola_equation = f"{a}x^2 + {b}x + {c}"

    # Calculate x-coordinates where y = 0
    roots = np.roots([a, b, c])

    return parabola_equation, roots

def calc_speed(input_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        rows = list(reader)[1:]  # Skip the first row
        
        # Extract each point and put it in a separate array
        point = rows[0]
        point2 = rows[1]
        point3 = rows[2]
        point4 = rows[3]
        point5 = rows[4]

        xtotal = float(point[1])+float(point2[1])+float(point3[1])+float(point4[1])+float(point5[1])
        ttotal = float(point[0])+float(point2[0])+float(point3[0])+float(point4[0])+float(point5[0])
        xaverage = xtotal/5
        taverage = ttotal/5
            #use the first point to calculate the speed needed to reach that point. This speed will be used to calculate the time to reach the landing point
        speed = xaverage * (1/taverage)
        print("speed is:")
        print(speed)
    return speed

#Load point file
input_file = 'inputGA1A.csv'

#use the function above with the correct input file to do all calculations
equation, crossings = fit_parabola(input_file)
#print the found equation
print("Parabola Equation:")
print(equation)

#print each x that is bigger than 0
print("Crossing(s) where y = 0 and x > 0:")
for x in crossings:
    if x > 0:
        print(f"x = {x}")

speed = calc_speed(input_file)
#print the time taken to reach each positive x
print("Time to reach this point in seconds:")
for x in crossings:
    if x > 0:
        #time taken is calculated by distance/speed(m/s) (air resistance is not taken into account) (speed is calculates in the calc_speed function)
        t = x / speed
        if t < 0:
            t = t*-1
        print(f"t = {t}")
