import json

'''def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        source_key = f'n{order[i]}'
        target_key = f'n{order[i + 1]}'
        total_distance += distances[source_key]["distances"][target_key]
    
    # Return to the starting point
    total_distance += distances[f'n{order[-1]}']["distances"][order[0]]
    print("total distance", total_distance)
    
    return total_distance '''

def traveling_salesman_nearest_neighbor(distances):
    max_quantity=600
    capacity=0
    num_locations = len(distances)
  #  print("num_locations", num_locations)
    locations = list(range(num_locations))
  #  print("locations", locations)

    # Start with the first location as the current location
    current_location = locations[0]
    unvisited_locations = set(locations[1:])
    #print("unvisited_location", unvisited_locations)
    order = [current_location]
   # print("order", order)

    while unvisited_locations:
        nearest_neighbor = min(unvisited_locations, key=lambda x: distances[f'n{current_location}']["distances"][x])
        order.append(nearest_neighbor)
        unvisited_locations.remove(nearest_neighbor)
        current_location = nearest_neighbor

    return order

def format_output(order):
    path = ["r0"] + [f'n{loc}' for loc in order] + ["r0"]
    return {"v0": {"path": path}}

if __name__ == "__main__":
    with open("level1a.json") as f:
        input_data = json.load(f)

    distances = input_data['neighbourhoods']

    best_order = traveling_salesman_nearest_neighbor(distances)
   


    output = format_output(best_order)
    print(output)

   

