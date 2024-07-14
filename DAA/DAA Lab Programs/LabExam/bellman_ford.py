def bellmanFord(n, m, src, edges):
    # Initialize distances to infinity
    dist = [float('inf')] * n
    dist[src] = 0  # Distance to source vertex is 0

    # Relax edges for n-1 iterations
    for i in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight

    # Check for negative cycles
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + weight:
            print("Negative cycle detected")
            exit(0)

    return dist


def main():
    n = 5  # Number of vertices
    m = 7  # Number of edges

    # Example edges list
    edges = [
        [0, 1, -1],  # Edge from vertex 0 to vertex 1 with weight -1
        [0, 2, 4],   # Edge from vertex 0 to vertex 2 with weight 4
        [1, 2, 3],   # Edge from vertex 1 to vertex 2 with weight 3
        [1, 3, 2],   # Edge from vertex 1 to vertex 3 with weight 2
        [1, 4, 2],   # Edge from vertex 1 to vertex 4 with weight 2
        [3, 2, 5],   # Edge from vertex 3 to vertex 2 with weight 5
        [3, 1, 1]    # Edge from vertex 3 to vertex 1 with weight 1
    ]

    src = 0  # Source vertex for Bellman-Ford algorithm

    shortest_distances = bellmanFord(n, m, src, edges)

    # Output the shortest distances from the source vertex
    for i in range(n):
        print(f"Distance to vertex {i} from source: ", end="")
        if shortest_distances[i] == float('inf'):
            print("INF")
        else:
            print(shortest_distances[i])


if __name__ == "__main__":
    main()
