def dijkstra(vertices, graph, source):
    
    dist = [float('inf')] * vertices
    dist[source] = 0
    visited = set()

    while len(visited) < vertices:
        # Find the unvisited node with the smallest distance
        min_distance = float('inf')
        min_node = -1
        for i in range(vertices):
            if i not in visited and dist[i] < min_distance:
                min_distance = dist[i]
                min_node = i
        
        # If no node is reachable, break out of the loop
        if min_node == -1:
            break
        
        visited.add(min_node)

        # Traverse neighbors/adjacent nodes
        for neighbor, distance in graph[min_node]:
            if neighbor not in visited:
                new_distance = dist[min_node] + distance
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance

    print("Printing the distance of all nodes from the source node: ")
    for i in range(vertices):
        print(f"{source} to {i}: {dist[i]}")
    
    return dist

def inputEdges(graph):
    
    n = int(input("Enter the no. of edges: "))

    print("Enter edge pair as u -> v")
    for i in range(n):
        u = int(input(f"Pair {i}: "))
        v = int(input("->"))
        dir = int(input("Directed?: "))
        wt = int(input("Enter weight: "))
        
        if u not in graph:
            graph[u] = []
        graph[u].append([v, wt])

        if (not dir):
            if v not in graph:
                graph[v] = []
            graph[v].append([u, wt])



vertices = int(input("\nEnter number of vertices: "))    
graph = [[] for i in range(vertices)]
inputEdges(graph)

print("\nAdjacency list: ")
for i in range(vertices):
    print(f"{i}: {graph[i]}")

src = int(input("\nEnter source vertex: "))
print(dijkstra(vertices, graph, src))

# Dijkstra's with paths to each neighbour

# def dijkstra(vertices, graph, source):
#     dist = [float('inf')] * vertices
#     dist[source] = 0
#     previous = [-1] * vertices
#     visited = set()

#     while len(visited) < vertices:
#         # Find the unvisited node with the smallest distance
#         min_distance = float('inf')
#         min_node = -1
#         for i in range(vertices):
#             if i not in visited and dist[i] < min_distance:
#                 min_distance = dist[i]
#                 min_node = i

#         # If no node is reachable, break out of the loop
#         if min_node == -1:
#             break

#         visited.add(min_node)

#         # Traverse neighbors/adjacent nodes
#         for neighbor, distance in graph[min_node]:
#             if neighbor not in visited:
#                 new_distance = dist[min_node] + distance
#                 if new_distance < dist[neighbor]:
#                     dist[neighbor] = new_distance
#                     previous[neighbor] = min_node

#     # Function to reconstruct the path from source to a given target
#     def reconstruct_path(target):
#         path = []
#         while target != -1:
#             path.append(target)
#             target = previous[target]
#         path.reverse()
#         return path

#     print("Printing the distance of all nodes from the source node and their paths: ")
#     for i in range(vertices):
#         if dist[i] == float('inf'):
#             print(f"{source} to {i}: No path")
#         else:
#             path = reconstruct_path(i)
#             print(f"{source} to {i}: Distance = {dist[i]}, Path = {' -> '.join(map(str, path))}")
    
#     return dist, previous

# def inputEdges(graph):
#     n = int(input("Enter the number of edges: "))
#     print("Enter edge pair as u -> v")
#     for i in range(n):
#         u = int(input(f"Pair {i}: "))
#         v = int(input("-> "))
#         dir = int(input("Directed? (1 for yes, 0 for no): "))
#         wt = int(input("Enter weight: "))
        
#         if u not in graph:
#             graph[u] = []
#         graph[u].append([v, wt])

#         if not dir:
#             if v not in graph:
#                 graph[v] = []
#             graph[v].append([u, wt])

# vertices = int(input("\nEnter number of vertices: "))    
# graph = [[] for _ in range(vertices)]
# inputEdges(graph)

# print("\nAdjacency list: ")
# for i in range(vertices):
#     print(f"{i}: {graph[i]}")

# src = int(input("\nEnter source vertex: "))
# dijkstra(vertices, graph, src)


# or

# import heapq

# def dijkstra(vertices, edges, source):
    
#     dist = [float('inf')] * vertices
#     dist[source] = 0
#     # Priority queue to store pairs as (distance, node)
#     pq = [(0, source)]
#     while pq:
#         # Fetch minimum most record
#         dist_node, min_node = heapq.heappop(pq)

#         # Traverse neighbors/adjacent nodes
#         for neighbor, distance in adj[min_node]:
#             if dist[neighbor] > dist_node + distance:
#                 # Update distance
#                 dist[neighbor] = dist_node + distance
#                 heapq.heappush(pq, (dist[neighbor], neighbor))

#     print("Printing the distance of all nodes from the source node: ")
#     for i in range(0, vertices):
#         print(f"{source} to {i}: {dist[i]}")
    
#     return dist

# def inputEdges(graph):
    
#     n = int(input("Enter the no. of edges: "))

#     print("Enter edge pair as u -> v")
#     for i in range(n):
#         u = int(input(f"Pair {i}: "))
#         v = int(input("->"))
#         dir = int(input("Directed?: "))
#         wt = int(input("Enter weight: "))
        
#         if u not in graph:
#             graph[u] = []
#         graph[u].append([v, wt])

#         if (not dir):
#             if v not in graph:
#                 graph[v] = []
#             graph[v].append([u, wt])



# vertices = int(input("\nEnter number of vertices: "))    
# graph = [[] for i in range(vertices)]
# inputEdges(graph)

# print("\nAdjacency list: ")
# for i in range(vertices):
#     print(f"{i}: {graph[i]}")

# src = int(input("\nEnter source vertex: "))
# print(dijkstra(vertices, graph, src))
