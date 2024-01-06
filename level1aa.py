import json


def traveling_salesman_nearest_neighbor(distances, max_capacity):
    current_capacity = 0
    num_locations = len(distances)
    locations = list(range(num_locations))

    # Start with the first location as the current location
    current_location = locations[0]
    unvisited_locations = set(locations[1:])
    order = [current_location]
# Inside traveling_salesman_nearest_neighbor function
    while unvisited_locations:
        nearest_neighbor = min(unvisited_locations, key=lambda x: distances[f'n{current_location}']["distances"][x]['distance'])

        # Check if adding the nearest neighbor exceeds the maximum capacity
        if current_capacity + distances[f'n{current_location}']['order_quantity'] <= max_capacity:
            order.append(nearest_neighbor)
            unvisited_locations.remove(nearest_neighbor)
            current_location = nearest_neighbor
            current_capacity += distances[f'n{current_location}']['order_quantity']
            print(current_capacity)
        else:
            # If adding the nearest neighbor exceeds the capacity, return to the starting point
            if distances[f'n{current_location}']['order_quantity'] > max_capacity:
                print(f"Path{len(order)} cost: {calculate_total_distance(order, distances)}")
                print("Validation failed. Vehicle delivered more than its capacity.")
                break
            else:
                order.append(order[0])
                current_location = order[0]
                current_capacity = 0
    return order



def format_output(order):
    print(order)

    formatted_output = {"v0": {}}

    paths = []
    current_path = ["r0"]
    k=1
    
    for i in order:
        print("i",i)
        if i != 0 or k==1:
            current_path.append(f'n{i}')
            k=2
        else:
            paths.append(current_path)
            current_path=[]
            current_path = ["r0"]
            current_path.append(f'n{i}')
    paths.append(current_path)

    print(paths[0])
    print(paths[1])
    print(paths[2])
            
    for i in range(0,len(paths)):
            formatted_output["v0"][f"path{i}"] = paths[i]

    return formatted_output


if __name__ == "__main__":
    with open("level1a.json") as f:
        input_data = json.load(f)

    distances = input_data['neighbourhoods']
    max_capacity = input_data['vehicles']['v0']['capacity']

    best_order = traveling_salesman_nearest_neighbor(distances, max_capacity)
   # total_distance = calculate_total_distance(best_order, distances)

    output = format_output(best_order)
    print(output)
 
    #print("Total Distance:", total_distance)
   # Write the output to a new JSON file
    #with open("level1a_output.json", "w") as output_file:
       # json.dump(output, output_file, indent=2)
