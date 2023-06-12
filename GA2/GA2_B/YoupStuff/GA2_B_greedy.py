import numpy as np
import csv
import time
import matplotlib as mpl
mpl.use('GTK3Agg')
import matplotlib.pyplot as plt
import random
from os import environ
environ['OMP_NUM_THREADS'] = '4'
import ast

#calculate shortest path using Closest node heuristic

start_point = 0                 #what point to start at
attempts = 1                   #how often to run the program to get average execution time
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
    with open("/home/youpie/OneDrive/School!/AMA4/Projecten/Groep project/AMA_2023_Group_assignment/GA2/inputGAS2B.csv") as csv_file:
        next(csv_file)
        csv_read=csv.reader(csv_file, delimiter=',')
        for i,row in enumerate(csv_read):
            points.extend([[]])
            points[i].append(int(row[1]))
            points[i].append(int(row[2]))
    print(points)
    print(len(points))


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
    temp_point_array = points_objects  
    for i in range(len(points_objects)):
        plt.text(temp_point_array[i][0],temp_point_array[i][1],str(i))
        plt.plot([points_objects[route[i]][0],points_objects[route[i+1]][0]],[points_objects[route[i]][1],points_objects[route[i]][1]])         #create the 1x1 square movement requirements
        plt.plot([points_objects[route[i+1]][0],points_objects[route[i+1]][0]],[points_objects[route[i]][1],points_objects[route[i+1]][1]])
    plt.show()

def calculate_distances(points_array ,point,where):
    short_points_array = np.asarray(points_array[where+1:len(points_array)])
    if(len(short_points_array) <= 0): return 0
    temp_point_array_norm = np.subtract(short_points_array,point)
    distance_array = np.linalg.norm(temp_point_array_norm,axis=1)           #use linear algebra to calculate the normalised vector values of the point from the origin
    for i,distance_to_point in enumerate(distance_array):
            key = str([i,i+where+1])  
            distance_dict[key] = distance_to_point

def inverse_pythagoran(points_array,point1,point2):                                 #find horizontal and vertical distance from point to nearest point 
    horizontal  = np.abs(points_array[point1][0] - points_array[point2][0])
    vertical    = np.abs(points_array[point1][1] - points_array[point2][1])
    return np.array([horizontal,vertical])

def check_cycle(start_point, connections,route):
    route = []
    next_point = start_point
    connections_temp = connections.copy()
    for i in range(len(connections)):
        next_point_location = np.where(np.asarray(connections_temp)[:,(0,1)] == next_point)
        # print(np.asarray(np.asarray(connections_temp)[:,0] == next_point) or np.asarray(np.asarray(connections_temp)[:,1] == next_point))
        if(np.size(next_point_location) == 0 ): return [False,route]
        route.append(connections_temp[next_point_location[0][0]][next_point_location[1][0]])
        next_point = connections_temp[next_point_location[0][0]][not next_point_location[1][0]]
        if(next_point in route and len(route) < len(points)): return [True,route]
        connections_temp.pop(next_point_location[0][0])
    route.append(start_point)
    return [False,route];

points = list()   
execution_times = list()
LOAD_csv()
for repeat in range(attempts):
    start_time = time.time()                #start timer to time the time to execute code
    distance_dict = {} 
    node_connections = np.zeros((len(points)))
    print(node_connections)
    route = []
    connections = list()
    total_distance = 0
    max_connections = len(points)*2
    for i, current_point in enumerate(points):
        calculate_distances(points,current_point,i)
    print(distance_dict)
    print(len(distance_dict))
    
    while np.sum(node_connections) < max_connections:
        if(not distance_dict):
            print("This problem can not be solved by greedy")
            break
        min_dist = min(distance_dict)
        connecting_points = ast.literal_eval(min_dist)
        if((node_connections[connecting_points[0]] < 2 and node_connections[connecting_points[1]] < 2)):
            print(min_dist)
            total_distance += distance_dict[min_dist]
            connections.append(connecting_points)
            if(check_cycle(start_point,connections,route)[0]):
                connections.pop()
                print("cycle at " + str(connecting_points))
            else:
                node_connections[connecting_points[0]] += 1
                node_connections[connecting_points[1]] += 1
        distance_dict.pop(min_dist)
    print("penis")
    route = check_cycle(start_point,connections,route)[1]
    

    print(connections)
    print(route)
    print(total_distance)


    execution_times.append(time.time() - start_time)

np_execution_times = np.asarray(execution_times)
print("average time: " + str(np.average(np_execution_times)))                       #count exectution time
print("total time for %s attempts: " %(attempts) + str(np.sum(np_execution_times)))
write_csv(total_distance,route)
plot(points,route)