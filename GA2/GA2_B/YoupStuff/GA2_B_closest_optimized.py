import numpy as np
import csv
import time
import matplotlib as mpl
mpl.use('GTK3Agg')
import matplotlib.pyplot as plt
import random
from os import environ
environ['OPENBLAS_NUM_THREADS'] = '4'

#calculate shortest path using Closest node heuristic

start_point = 0                #what point to start at
attempts = 1                   #how often to run the program to get average execution time
add_points = 0                 #how many points to add when the program is run
add_point_every_loop = False

def write_points(ammount,currlength):           #fill the input file with more random points
    if(ammount != 0):
        new_points = [[0],[0]]
        randomX = 0
        randomY = 0
        with open('/home/youpie/OneDrive/School!/AMA4/Projecten/Groep project/AMA_2023_Group_assignment/GA2/inputGAS2B.csv', mode='w') as output_file:
            current_length = currlength
            output_writer = csv.writer(output_file, delimiter=",")
            output_writer.writerow(["Point number","x","y"])
            # for i in range(1,current_length):
            #     output_writer.writerow([i,point_array[i].x,point_array[i].y])
            for i in range(ammount):
                while(randomX in new_points[0]):
                    randomX = random.randrange(1,100)
                while(randomY in new_points[1]):
                    randomY = random.randrange(1,100)
                new_points[0].append(randomX)
                new_points[1].append(randomY)
                output_writer.writerow([current_length,randomX,randomY])
                current_length+=1
        LOAD_csv()


def LOAD_csv():
    class point:                        #create class with position data and array of distance to all points
        x = 0.0
        y = 0.0
        distanceNearestPoint = 0
        nearestPoint = 0
    temp_point_array = list([[0,0]])
    with open("/home/youpie/OneDrive/School!/AMA4/Projecten/Groep project/AMA_2023_Group_assignment/GA2/inputGAS2B.csv") as csv_file:
        next(csv_file)
        csv_read=csv.reader(csv_file, delimiter=',')
        p = point()         #create point 0,0
        p.x = 0
        p.y = 0
        points.append(p)
        for i,row in enumerate(csv_read):
            p = point()
            p.x = int(row[1])                           #we create both an array filled with coordinates as well as object for each point as the approach to reading coordinates was changed to optimize speed
            p.y = int(row[2])
            temp_point_array.extend([[]])
            temp_point_array[i+1].append(p.x)
            temp_point_array[i+1].append(p.y)
            points.append(p)
    return np.asarray(temp_point_array)

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
        # plt.text(temp_point_array[0][i],temp_point_array[1][i],str(i))
        plt.plot([points_objects[route[i]].x,points_objects[route[i+1]].x],[points_objects[route[i]].y,points_objects[route[i]].y],color='tab:blue')         #create the 1x1 square movement requirements
        plt.plot([points_objects[route[i+1]].x,points_objects[route[i+1]].x],[points_objects[route[i]].y,points_objects[route[i+1]].y],color='tab:blue')
    plt.show()

def closest_point(points_array ,point):
    own_coords = np.copy(points_array[point])                            #create an array with all point locations. all already tested points have the position NaN so the process doesn't calculate them as thats not needed
    temp_point_array = points_array
    temp_point_array_norm = np.subtract(temp_point_array,own_coords)        #normalize the array by subtracting the location of the point we are currently looking from (like setting that point as 0,0)
    np.nan_to_num(temp_point_array_norm,0)
    distance_array = np.linalg.norm(temp_point_array_norm,axis=1)           #use linear algebra to calculate the normalised vector values of the point from the origin
    try:
        closest_distance = np.min(distance_array[np.nonzero(distance_array)])   #find the smallest value that isnt zero and find the index of that value in the array
        closest_point       = np.where(distance_array == closest_distance)
    except:
        closest_distance = 0                                                    #there is a very small chance that finding the minimal value goes wrong, this is to account for when that happens
        closest_point = [[0]]
        print("This result is not accurate, please change input data")
    return int(closest_point[0][0])

def inverse_pythagoran(points_array,route):                                 #find horizontal and vertical distance from point to nearest point 
    point_coords_start = np.zeros((len(route),2))
    for i in range(len(points)):
        point_coords_start[i] = points_array[route[i]]
    distances = np.subtract(np.roll(point_coords_start,(1,1)),point_coords_start)       #np.roll rolls the array forward by 1 so we can subtract the destination from the beginning point

    return np.sum(np.abs(distances))
    
points = list()             #create an array of objects of all points
execution_times = list()
point_coordinates = LOAD_csv()
write_points(add_points,len(points))
for repeat in range(attempts):
    start_time = time.time()                #start timer to time the time to execute code
    route = list()              #create array with the final route
    total_distance = 0   
    current_point = start_point
    route.append(start_point)
    shrinking_point_array = point_coordinates.astype(float)
    while(len(point_coordinates)!=len(route)):                                         #find the shortest distance from all points on route starting from starting point and following
        closest_next_point = closest_point(shrinking_point_array,current_point)
        shrinking_point_array[route[-1]] = [np.nan,np.nan]                              #set the point last added to the route to NaN,NaN
        current_point = closest_next_point
        route.append(closest_next_point)                                            #add the just found point to the route
    else:
        route.append(start_point)
        total_distance = inverse_pythagoran(point_coordinates,route)                #calculate the total distance

    execution_time = (time.time() - start_time)
    execution_times.append(execution_time)                                    
write_csv(total_distance,route)
np_execution_times = np.asarray(execution_times)
print("average time: " + str(np.average(np_execution_times)))                       #count exectution time
print("total time for %s attempts: " %(attempts) + str(np.sum(np_execution_times)))
plot(points,route)