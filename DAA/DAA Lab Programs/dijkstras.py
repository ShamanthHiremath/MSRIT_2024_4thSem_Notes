import heapq

def dijkstra(vertices, edges, source):
    # Create adjacency list with vertices and their weights/distances
    adj = {i: [] for i in range(vertices)}
    for edge in edges:
        u, v, d = edge
        adj[u].append((v, d))
        adj[v].append((u, d))
    
    dist = [float('inf')] * vertices
    dist[source] = 0
    # Priority queue to store pairs as (distance, node)
    pq = [(0, source)]
    while pq:
        # Fetch minimum most record
        distnode, topnode = heapq.heappop(pq)

        # Traverse neighbors/adjacent nodes
        for neighbor, distance in adj[topnode]:
            if dist[neighbor] > distnode + distance:
                # Update distance
                dist[neighbor] = distnode + distance
                heapq.heappush(pq, (dist[neighbor], neighbor))

    print("Printing the distance of all nodes from the source node: ")
    for i in range(0, vertices):
        print(f"{i}", end= " ")
    print("\n", dist)
    
    return dist

# Example usage
vertices = 4
edges = [
    [0, 1, 5],
    [0, 2, 8],
    [1, 2, 9],
    [1, 3, 2],
    [2, 3, 6]
]
source = 0
print(dijkstra(vertices,edges,source))