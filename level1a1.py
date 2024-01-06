from itertools import permutations
import json

def calculate_total_distance(order, distances):
    total_distance = 0
    current_location = 'r0'  # Starting from the restaurant
    remaining_capacity = distances['vehicles']['v0']['capacity']

    for next_location in order:
        distance_to_next = distances[current_location]["neighbourhood_distance"][next_location]
        remaining_capacity -= distances["neighbourhoods"][next_location]["order_quantity"]

        # Check if remaining capacity is sufficient
        if remaining_capacity < 0:
            return float('inf')  # Return infinite distance if capacity constraint is violated

        total_distance += distance_to_next
        current_location = next_location

    # Return to the starting point (restaurant)
    total_distance += distances[current_location]["neighbourhood_distance"]['r0']
    return total_distance

def brute_force_cvrp(distances):
    locations = []
    for i in distances["neighbourhoods"]:
         locations.append('n' + str(i))
    print(locations)
    permutations_list = permutations(locations[1:])  # Exclude the starting point (restaurant)
    print(permutations_list)

    best_order = None
    min_distance = float('inf')

    for order in permutations_list:
        order = ('r0',) + order + ('r0',)  # Add starting and ending points
        distance = calculate_total_distance(order, distances)

        if distance < min_distance:
            min_distance = distance
            best_order = order

    return best_order, min_distance

if __name__ == "__main__":
    with open("level1a.json") as f:
        input_data = json.load(f)

    distances = input_data['neighbourhoods']
    best_order, min_distance = brute_force_cvrp(distances)

    print("Best order:", best_order)
    print("Min distance:", min_distance)
