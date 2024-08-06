def tsp_nearest_neighbor():
    num_cities = int(input("Enter the number of cities: "))
    
    # Initialize the graph as an adjacency list
    graph = {i: {} for i in range(num_cities)}
    
    # Input distances between cities
    for i in range(num_cities):
        num_neighbors = int(input(f"Enter the number of neighbors for city {i}: "))
        for _ in range(num_neighbors):
            neighbor = int(input(f"Enter a neighbor city for city {i}: "))
            distance = int(input(f"Enter the distance between city {i} and city {neighbor}: "))
            graph[i][neighbor] = distance
    
    start_city = int(input(f"Enter the starting city (0 to {num_cities-1}): "))
    
    path = [start_city]
    current_city = start_city
    total_distance = 0
    
    while len(path) < num_cities:
        next_city = None
        min_distance = float('inf')
        
        for neighbor, distance in graph[current_city].items():
            if neighbor not in path and min_distance > distance:
                min_distance = distance
                next_city = neighbor
        
        if next_city is None:
            break
        
        total_distance += min_distance
        path.append(next_city)
        current_city = next_city
    
    # Attempt to return to the starting city if possible
    if start_city in graph[current_city]:
        total_distance += graph[current_city][start_city]
        path.append(start_city)
    else:
        print("Warning: Cannot return to the starting city")
    
    print("The total distance is:", total_distance)
    return path

# Run the TSP algorithm
path = tsp_nearest_neighbor()
print("THE PATH IS:", path)