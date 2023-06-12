import numpy as np
import csv
import time

#calculate shortest path using Closest node heuristic

start_point = 0                 #what point to start at
attempts = 1                  #how often to run the program to get average execution time

def LOAD_csv():
    class point:                        #create class with position data and array of distance to all points
        x = 0.0
        y = 0.0
        DistanceToPoints = np.array([])
        nearestPoint = 0
    
    with open('AMA_2023_Group_assignment/GA2/inputGAS2B.csv') as csv_file:
        has_header = csv.Sniffer().has_header(csv_file.read(1024))      #ignore header
        csv_file.seek(0)  # Rewind.
        if has_header:
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
    with open('AMA_2023_Group_assignment/GA2/OutputGAS2B.csv', mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=",")

        distance_row = list()
        distance_row.append('total distance')
        distance_row.append(str(distance))

        route_row = list()
        route_row.append('route')
        route_row.append(str(route))

        output_writer.writerow(distance_row)
        output_writer.writerow(route_row)


def dist_all_points(points_array ,point):
    own_coords = np.array([points_array[point].x,points_array[point].y])
    temp_dist_list = list()
    for i in range(len(points_array)):                                          #calculate distance to all points around point using pythagoran theorem
        other_coord = np.array([points_array[i].x,points_array[i].y])
        distance_to = np.sqrt((own_coords[0]-other_coord[0])**2+(own_coords[1]-other_coord[1])**2)
        temp_dist_list.append(distance_to)
    points[point].DistanceToPoints = np.asarray(temp_dist_list)

def Set_seen_zero(points_array,point,already_seen):
    seen_list = points_array[point].DistanceToPoints.tolist()               #loops through all distances from points and sets ones already on route to 0
    for i in range(len(seen_list)):
        if(i in already_seen):
            seen_list[i] = 0;
    return np.asarray(seen_list)

def shortest_distance(points_array,point,already_seen):
    points_array_adjusted = Set_seen_zero(points_array,point,already_seen)          #set seen points to zero
    min_dist = np.min(points_array_adjusted[np.nonzero(points_array_adjusted)])     #find smalles number that isn't 0
    nearest_unseen_point = np.where(points_array_adjusted == min_dist)[0]           #find index of closest distance
    return(nearest_unseen_point[0])

def inverse_pythagoran(points_array,point1,point2):                                 #find horizontal and vertical distance from point to nearest point 
    horizontal  = np.abs(points_array[point1].x - points_array[point2].x)
    vertical    = np.abs(points_array[point1].y - points_array[point2].y)
    return np.array([horizontal,vertical])
    

execution_times = list()

for repeat in range(attempts):
    start_time = time.time()                #start timer to time the time to execute code

    points = list()             #create an array of objects of all points
    route = list()              #create array with the final route
    total_distance = 0

    LOAD_csv()

    for i in range(len(points)):    #calculate the distance to all points from all points
        dist_all_points(points,i)

    current_point = start_point
    route.append(start_point)
    while(len(points)!=len(route)):                                         #find the shortest distance from all points on route starting from starting point and following
        shortest_distance_found = shortest_distance(points,current_point,route)
        current_point = shortest_distance_found
        route.append(shortest_distance_found)
    else:
        route.append(start_point)

    last_point = start_point
    for point in route:                                             #calculate the distance from point to nearest point on route and adds to total distance
        distance = inverse_pythagoran(points, point, last_point)
        total_distance += distance[0]+distance[1]
        last_point = point

    write_csv(total_distance,route)
    execution_time = (time.time() - start_time)
    #print("--- %s seconds ---" % execution_time)
    execution_times.append(execution_time)
np_execution_times = np.asarray(execution_times)
print("average time: " + str(np.average(np_execution_times)))
print("total time for %s attempts: " %(attempts) + str(np.sum(np_execution_times)))