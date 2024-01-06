import json

def calculate_total_distance(order, distances):
    total_distance = 0
    for i in range(len(order) - 1):
        source_key = f'n{order[i]}'
        target_key = f'n{order[i + 1]}'
        total_distance += distances[source_key]["distances"][order[i + 1]]
    
    # Return to the starting point
    total_distance += distances[f'n{order[-1]}']["distances"][order[0]]
    
    return total_distance

def traveling_salesman_nearest_neighbor(distances):
    num_locations = len(distances)
    locations = list(range(num_locations))

    # Start with the first location as the current location
    current_location = locations[0]
    unvisited_locations = set(locations[1:])
    order = [current_location]

    while unvisited_locations:
        nearest_neighbor = min(unvisited_locations, key=lambda x: distances[f'n{current_location}']["distances"][x])
        order.append(nearest_neighbor)
        unvisited_locations.remove(nearest_neighbor)
        current_location = nearest_neighbor

    return order

def format_output(order, distances):
    path = ["r0"] + [f'n{loc}' for loc in order] + ["r0"]
    return {"v0": {"path": path}}

if __name__ == "__main__":
    with open("level0.json") as f:
        input_data = json.load(f)

    distances = input_data['neighbourhoods']
    print("distances:",distances)

    best_order = traveling_salesman_nearest_neighbor(distances)
    min_distance = calculate_total_distance(best_order, distances)

    output = format_output(best_order, distances)

    print(json.dumps(output, indent=2))
