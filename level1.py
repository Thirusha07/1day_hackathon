import json

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    return total_distance

def greedy_solution(remaining_neighbourhoods, current_location, capacity, distances):
    current_capacity = 0
    current_route = [current_location]

    while remaining_neighbourhoods:
        nearest_neighbour = min(remaining_neighbourhoods, key=lambda x: distances[current_location][x])
        
        if current_capacity + remaining_neighbourhoods[nearest_neighbour]['order_quantity'] <= capacity:
            current_route.append(nearest_neighbour)
            current_capacity += remaining_neighbourhoods[nearest_neighbour]['order_quantity']
            current_location = nearest_neighbour
            remaining_neighbourhoods.pop(nearest_neighbour)
        else:
            current_route.append(current_route[0])  # Return to the starting point
            return current_route, current_capacity

    current_route.append(current_route[0])  # Return to the starting point
    return current_route, current_capacity

def solve_cvrp(input_data):
    neighbourhoods = input_data['neighbourhoods']
    capacity = input_data['vehicles']['v0']['capacity']
    remaining_neighbourhoods = {k: v for k, v in neighbourhoods.items()}

    routes = []

    while remaining_neighbourhoods:
        current_location = 'r0' if not routes else routes[-1][-2]
        route, route_capacity = greedy_solution(remaining_neighbourhoods, current_location, capacity, input_data['distances'])
        routes.append(route)

    return routes

if __name__ == "__main__":
    with open("level1a.json") as f:
        input_data = json.load(f)

    solution = solve_cvrp(input_data)

    print("Solution:")
    for idx, route in enumerate(solution):
        print(f"Route {idx + 1}: {route} - Distance: {calculate_distance(route, input_data['distances'])}")
