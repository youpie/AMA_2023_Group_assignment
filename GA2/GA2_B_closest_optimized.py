import numpy as np
import csv
import time
import matplotlib as mpl
mpl.use('GTK3Agg')
import matplotlib.pyplot as plt
import random
from os import environ
environ['OMP_NUM_THREADS'] = '4'

#calculate shortest path using Closest node heuristic

start_point = 0                 #what point to start at
attempts = 10000                    #how often to run the program to get average execution time
add_points = 0                     #how many points to add when the program is run
add_point_every_loop = False

def write_points(ammount,currlength,point_array):           #fill the input file with more random points
    if(ammount != 0):
        with open('/home/youpie/OneDrive/School!/AMA4/Projecten/Groep project/AMA_2023_Group_assignment/GA2/inputGAS2B.csv', mode='w') as output_file:
            current_length = currlength
            output_writer = csv.writer(output_file, delimiter=",")
            output_writer.writerow(["Point number","x","y"])
            for i in range(1,current_length):
                output_writer.writerow([i,point_array[i].x,point_array[i].y])
            for i in range(ammount):
                output_writer.writerow([current_length,random.randrange(1,100),random.randrange(1,100)])
                current_length+=1
        LOAD_csv()


def LOAD_csv():
    class point:                        #create class with position data and array of distance to all points
        x = 0.0
        y = 0.0
        distanceNearestPoint = 0
        nearestPoint = 0
    
    with open("/home/youpie/OneDrive/School!/AMA4/Projecten/Groep project/AMA_2023_Group_assignment/GA2/inputGAS2B.csv") as csv_file:
        next(csv_file)
        csv_read=csv.reader(csv_file, delimiter=',')
        p = point()         #create point 0,0
        p.x = 0
        p.y = 0
        points.append(p)
        for row in csv_read:
            p = point()
            p.x = int(row[1])
            p.y = int(row[2])
            points.append(p)

def write_csv(distance, route):                                     #write total distance and route to csv file
    with open('/home/youpie/OneDrive/School!/AMA4/Projecten/Groep project/AMA_2023_Group_assignment/GA2/OutputGAS2B.csv', mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=",")

        distance_row = list()
        distance_row.append('total distance')
        distance_row.append(str(distance))

        route_row = list()
        route_row.append('route')
        route_row.append(str(route))

        output_writer.writerow(distance_row)
        output_writer.writerow(route_row)



def plot(points_objects,route):             #plot the points
    temp_point_array = list([[],[]])
    for i in range(len(points_objects)):
        temp_point_array[0].append(points_objects[i].x)
        temp_point_array[1].append(points_objects[i].y)
    plt.scatter(temp_point_array[0],temp_point_array[1])
    for i in range(len(points_objects)):
        plt.text(temp_point_array[0][i],temp_point_array[1][i],str(i))
        plt.plot([points_objects[route[i]].x,points_objects[route[i+1]].x],[points_objects[route[i]].y,points_objects[route[i]].y])         #create the 1x1 square movement requirements
        plt.plot([points_objects[route[i+1]].x,points_objects[route[i+1]].x],[points_objects[route[i]].y,points_objects[route[i+1]].y])
    plt.show()

def closest_point(points_array ,point):
    own_coords = np.array([points_array[point].x,points_array[point].y])
    temp_point_array = np.full((len(points),2),own_coords)
    for i in range(len(points_array)):                          #fill a 2D array with coordinates, instead of 2 arrays with x column and y column but just a bunch of xy arrays
        if points_array[i].distanceNearestPoint == 0:
            temp_point_array[i][0] = points_array[i].x
            temp_point_array[i][1] = points_array[i].y
    temp_point_array_norm = np.subtract(temp_point_array,own_coords)
    distance_array = np.linalg.norm(temp_point_array_norm,axis=1)           #use linear algebra to calculate the normalised vector values of the point from the origin
    try:
        closest_distance = np.min(distance_array[np.nonzero(distance_array)])
        closest_point = np.where(distance_array == closest_distance)
    except:
        closest_distance = 0                                                    #there is a very small chance that finding the minimal value goes wrong, this is to account for when that happens
        closest_point = [[0]]
    points[point].distanceNearestPoint = closest_distance
    points[point].nearestPoint = closest_point
    return int(closest_point[0][0])

def inverse_pythagoran(points_array,point1,point2):                                 #find horizontal and vertical distance from point to nearest point 
    horizontal  = np.abs(points_array[point1].x - points_array[point2].x)
    vertical    = np.abs(points_array[point1].y - points_array[point2].y)
    return np.array([horizontal,vertical])
    
points = list()             #create an array of objects of all points
execution_times = list()
LOAD_csv()
write_points(add_points,len(points),points)
for repeat in range(attempts):
    start_time = time.time()                #start timer to time the time to execute code
    route = list()              #create array with the final route
    total_distance = 0

    if(add_point_every_loop):
        write_points(add_points,len(points),points)    

    current_point = start_point
    route.append(start_point)
    while(len(points)!=len(route)):                                         #find the shortest distance from all points on route starting from starting point and following
        closest_next_point = closest_point(points,current_point)
        current_point = closest_next_point
        route.append(closest_next_point)
    else:
        route.append(start_point)
        last_point = start_point
        for i,current_point in enumerate(route):                                #calculate the total distance that has been traveled
            distance = inverse_pythagoran(points, last_point, current_point)
            last_point = current_point
            total_distance += distance[0]+distance[1]   

    execution_time = (time.time() - start_time)
    execution_times.append(execution_time)

    for i in range(len(points)):
        points[i].distanceNearestPoint = 0
write_csv(total_distance,route)
np_execution_times = np.asarray(execution_times)
print("average time: " + str(np.average(np_execution_times)))                       #count exectution time
print("total time for %s attempts: " %(attempts) + str(np.sum(np_execution_times)))
plot(points,route)