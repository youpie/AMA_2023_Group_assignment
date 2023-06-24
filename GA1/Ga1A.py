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

        # Extract the first and second point from the second row
        second_row = rows[1]
        t = float(second_row[0])
        x = float(second_row[1])
        #use the first point to calculate the speed needed to reach that point. This speed will be used to calculate the time to reach the landing point
        speed = x * (1/t)
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
        print(f"t = {t}")
