import csv
import math

def calculate_x(input_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        equation = next(reader)[0]  # Read the first row as the equation

    # Extract coefficients of x^2, y^2, x, y, and constant term
    a, b, c, d, e = [float(coef) for coef in equation.split(',')]

    # Calculate discriminant
    discriminant = (c * c) - (4 * a * e)

    if discriminant > 0:
        # Two real solutions
        x1 = (-c + math.sqrt(discriminant)) / (2 * a)
        x2 = (-c - math.sqrt(discriminant)) / (2 * a)
        print("x-coordinates where y=0:")
        print(x1)
        print(x2)
    elif discriminant == 0:
        # One real solution
        x = -c / (2 * a)
        print("x-coordinate where y=0:")
        print(x)
    else:
        # No real solutions
        print("No solutions found.")

# Example usage:
input_file = 'outputfile GA1A.csv'  # Replace with the path to your input CSV file

calculate_x(input_file)