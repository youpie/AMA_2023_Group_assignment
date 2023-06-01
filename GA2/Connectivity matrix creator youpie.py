import numpy as np
import csv

def fetchcsv(filename):
    # Load CSV file into numpy array
    r = np.genfromtxt(filename,delimiter=',',dtype=int, names=True)
    
 
    # Read CSV file using csv.reader
    reader = csv.reader(open(filename, "r"), delimiter=",")
    x = list(reader)
    result = np.array(x).astype("str")

     
    Labels = []
    #Extract column labels from the first row of the CSV
    for i  in range (len(result[0])):
        Labels.append(result[0][i])
    del Labels[0]


    
    dictionary ={}
    
    keys=[]
    values = []
    
    #Create keys list from Labels
    for i in range (len(r[0])-1):
        keys.append(Labels[i])

    
    temp_dic ={}
    
    sub_keys = []
    
    sub_values =[]
    
    # Create a dictionary of dictionaries from the numpy array
    for j in range (len(r[0])-1):
        for i in range (len(r[0])-1):
            if  r[j][i+1]!=-1:
                sub_keys.append(Labels[i])
                print(Labels[i])
                sub_values.append(r[j][i+1])
        for key, value in zip(sub_keys, sub_values): # type: ignore
            temp_dic[key] = value
            
        values.append(temp_dic)
        sub_keys = []
        sub_values=[]
    
        temp_dic={}
    
    keydict = []
    #Create the final dictionary using keys and values lists
    for key, value in zip(keys,values): # type: ignore
            dictionary[key] = value
    keydict.append(Labels)
    keydict.append(dictionary)
    return keydict

def fetchcsv2(filename):
    # Load CSV file into numpy array
    r = np.genfromtxt(filename,delimiter=',',dtype=int, names=True)
    
 
    # Read CSV file using csv.reader
    reader = csv.reader(open(filename, "r"), delimiter=",")
    x = list(reader)
    result = np.array(x).astype("str")

     
    Labels = []
    #Extract column labels from the first row of the CSV
    for i  in range (len(result)):
        Labels.append(result[i][0])
    del Labels[0]

    dictionary ={}

    values = []
    
    temp_dic ={}
    
    sub_keys = []
    
    sub_values =[]
    
    # Create a dictionary of dictionaries from the numpy array
    for j in range (len(result)-1):
        for i in range (len(r[0])-1):
            if  r[j][i+1]!=-1:
                sub_keys.append(result[0][i+1])
                sub_values.append(r[j][i+1])
        for key, value in zip(sub_keys, sub_values): # type: ignore
            temp_dic[key] = value
            
        values.append(temp_dic)
        
        sub_values=[]
        sub_keys =[]
        temp_dic={}

    #Create the final dictionary using keys and values lists
    for key, value in zip(Labels,values): # type: ignore
            dictionary[key] = value
    return dictionary

connectivity = fetchcsv('Connection_matrix.csv')
points = fetchcsv2('points.csv')
print(connectivity)
print(points)

possible_routes = {}
connectivity_matrix = [[]]
connectivity_matrix_temp = []

connectivity_matrix[0].append('-')
for i in range (len(connectivity[1])):
    connectivity_matrix_temp = []
    connectivity_matrix[0].append(connectivity[0][i])
    connectivity_matrix_temp.append(connectivity[0][i])
    connectivity_matrix.append(connectivity_matrix_temp)

print(connectivity_matrix)

for i in range (len(connectivity[1])):
     main_node = connectivity[0][i]
     for sub_node in (connectivity[1][main_node]):
        if(main_node!=sub_node):
            X_difference = abs(points[main_node]['x']-points[sub_node]['x'])
            Y_difference = abs(points[main_node]['y']-points[sub_node]['y'])
            distance = np.sqrt(X_difference**2 + Y_difference**2)
            print(main_node+"-"+sub_node + ": " + str(distance))
            possible_routes[main_node+sub_node] = round(distance,2)

for row in range (len(connectivity[1])):
    for column in range (len(connectivity[1])):
            connectivity_matrix[row+1].append('-') 

print(connectivity_matrix)

for i in range (len(connectivity[1])):
     main_node = connectivity[0][i]
     for sub_node in (connectivity[1][main_node]):
        if(main_node!=sub_node):
            print(main_node+sub_node)
            for row in range (len(connectivity[1])):
                for column in range (len(connectivity[1])):
                    if(connectivity_matrix[0][column+1]+connectivity_matrix[row+1][0] == (main_node+sub_node or sub_node+main_node)):
                        try:
                            connectivity_matrix[row+1][column+1]=possible_routes[main_node+sub_node]
                        except:
                            connectivity_matrix[row+1][column+1]=possible_routes[sub_node+main_node]
            

print(connectivity_matrix)

f = open('outputfile.csv', 'w')
writer = csv.writer(f)
for i in range(len(connectivity_matrix)):
    writer.writerow(connectivity_matrix[i])