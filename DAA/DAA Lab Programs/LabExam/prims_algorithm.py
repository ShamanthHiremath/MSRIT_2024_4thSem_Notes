# from collections import defaultdict

def calculate_prims_mst(n, src, adj):
    # # Create adjacency list
    # adj = defaultdict(list)
    # for edge in graph:
    #     u, v, w = edge
    #     adj[u].append((v, w))
    #     adj[v].append((u, w))

    # Initialize arrays
    weights = [float('inf')] * (n)
    visited = [False] * (n)
    parent = [-1] * (n)

    # Main algorithm
    weights[src] = 0
    
    for _ in range(n):
        min_wt = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and weights[i] < min_wt:
                min_wt = weights[i]
                u = i

        visited[u] = True
        for neighbor, weight in adj[u]:
            v = neighbor
            w = weight
            if not visited[v] and weights[v] > w:
                weights[v] = w
                parent[v] = u

    # Form MST
    ans_mst = []
    for i in range(src + 1, n):
        ans_mst.append(((parent[i], i), weights[i]))

    return ans_mst

# Sample input
g = [
    (1, 2, 2),
    (1, 4, 6),
    (2, 1, 2),
    (2, 3, 3),
    (2, 4, 8),
    (2, 5, 5),
    (3, 2, 3),
    (3, 5, 7),
    (4, 1, 6),
    (4, 2, 8),
    (4, 5, 9),
    (5, 2, 5),
    (5, 3, 7),
    (5, 4, 9)
]

def inputEdges():
    graph = {}
    
    n = int(input("Enter the no. of edges: "))

    print("Enter edge pair as u -> v")
    for i in range(n):
        u = int(input(f"Pair {i+1}: "))
        v = int(input("->"))
        dir = int(input("Directed? (1 for yes, 0 for no): "))
        wt = int(input("Enter weight: "))
        
        if u not in graph:
            graph[u] = []
        graph[u].append((v, wt))

        if not dir:
            if v not in graph:
                graph[v] = []
            graph[v].append((u, wt))
        
    return graph

graph = inputEdges()
# Sample output
src = int(input("Enter the source vertex: "))
print(calculate_prims_mst(len(graph), src, graph))