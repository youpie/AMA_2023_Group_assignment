import numpy as np
import csv
import math

points = list()
route = list([0])
total_distance = 0

def LOAD_csv():
    class point:
        x = 0.0
        y = 0.0
        DistanceToPoints = np.array([])
        nearestPoint = 0
    
    with open('AMA_2023_Group_assignment/GA2/inputGAS2B.csv') as csv_file:
        has_header = csv.Sniffer().has_header(csv_file.read(1024))
        csv_file.seek(0)  # Rewind.
        if has_header:
            next(csv_file)
        csv_read=csv.reader(csv_file, delimiter=',')
        p = point()
        p.x = 0
        p.y = 0
        points.append(p)
        for row in csv_read:
                p = point()
                p.x = int(row[1])
                p.y = int(row[2])
                points.append(p)


def dist_all_points(points_array ,point):
    own_coords = np.array([points_array[point].x,points_array[point].y])
    temp_dist_list = list()
    for i in range(len(points_array)):
        other_coord = np.array([points_array[i].x,points_array[i].y])
        distance_to = np.sqrt((own_coords[0]-other_coord[0])**2+(own_coords[1]-other_coord[1])**2)
        temp_dist_list.append(distance_to)
    points[point].DistanceToPoints = np.asarray(temp_dist_list)

def Set_seen_zero(points_array,point,already_seen):
    seen_list = points_array[point].DistanceToPoints.tolist()
    for i in range(len(seen_list)):
        if(i in already_seen):
            seen_list[i] = 0;
    return np.asarray(seen_list)

def shortest_distance(points_array,point,already_seen):
    points_array_adjusted = Set_seen_zero(points_array,point,already_seen)
    min_dist = np.min(points_array_adjusted[np.nonzero(points_array_adjusted)])
    nearest_unseen_point = np.where(points_array_adjusted == min_dist)[0]
    return(nearest_unseen_point[0])
    
        
          
LOAD_csv()
for i in range(len(points)):
    dist_all_points(points,i)

current_point = 0
while(len(points)!=len(route)):
    shortest_distance_found = shortest_distance(points,current_point,route)
    total_distance += points[current_point].DistanceToPoints[shortest_distance_found]
    current_point = shortest_distance_found
    route.append(shortest_distance_found)
else:
    route.append(0)
    total_distance += points[route[len(route)-2]].DistanceToPoints[route[len(route)-1]]
    print(route)
    print(total_distance)