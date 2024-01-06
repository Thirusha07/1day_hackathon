

import numpy as np

def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def total_distance(route, distance_matrix):
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i + 1]]
    return total

def nearest_neighbor(current_city, unvisited, distance_matrix, vehicle_capacity):
    route = [current_city]
    current_capacity = 0

    while unvisited:
        nearest_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        if current_capacity + demands[nearest_city] <= vehicle_capacity:
            route.append(nearest_city)
            current_capacity += demands[nearest_city]
            unvisited.remove(nearest_city)
            current_city = nearest_city
        else:
            break

    return route

def solve_vrp(distance, demands, vehicle_capacity):
    num_cities = len(distance)
    unvisited = set(range(1, num_cities))  # Exclude the depot (city 0)
    routes = []

    while unvisited:
        current_city = 0  # Starting from the depot
        route = nearest_neighbor(current_city, unvisited, distance, vehicle_capacity)
        routes.append(route)

    return routes

# Example usage


from collections import deque
import json
with open("level1a.json") as f:
        data = json.load(f)
dist=[]
rest=data['restaurants']['r0']['neighbourhood_distance']
dist.append([0]+data['restaurants']['r0']['neighbourhood_distance'])
c=0
demands=[0]
for i in data['neighbourhoods']:
    dist.append([rest[c]]+data['neighbourhoods'][i]['distances'])
    demands.append(data['neighbourhoods'][i]['order_quantity'])
    c=c+1
dist=np.array(dist)
print(dist)
print(demands)

vehicle_capacity = 1120

result_routes = solve_vrp(dist, demands, vehicle_capacity)
dictOut={}
# Print the result
for i, route in enumerate(result_routes):
    rou=[]
    for j in route:
        if j==0:
            rou.append("r"+str(j))
        else:
            rou.append("n"+str(j-1))
    rou.append("r0")
    #print(rou)
    print(f"path{i + 1}: {rou}")
    dictOut[f"path{i + 1}"]= rou


dictFin={}
dictFin["v0"]=dictOut
print(dictFin)

import json


file_path = "level1a_output.json"

# Write the dictionary to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(dictFin, json_file, indent=2)

	
