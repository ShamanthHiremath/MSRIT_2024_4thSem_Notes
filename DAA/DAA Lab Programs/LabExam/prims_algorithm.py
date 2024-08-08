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
    
    mst_weight = 0
    
    for _ in range(n):
        min_wt = float('inf')
        min_node = -1
        for i in range(n):
            if not visited[i] and min_wt > weights[i]:
                min_wt = weights[i]
                min_node = i

        visited[min_node] = True
        mst_weight += min_wt
        
        for neighbor, weight in adj[min_node]:
            if not visited[neighbor] and weights[neighbor] > weight:
                weights[neighbor] = weight
                parent[neighbor] = min_node

    # Form MST
    ans_mst = []
    for i in range(n):
        if parent[i] != -1:
            ans_mst.append(((parent[i], i), weights[i]))
    
    print(f"Minimum Spanning Tree weight: {mst_weight}")

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

def inputGraph():
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

graph = inputGraph()
# Sample output
src = int(input("Enter the source vertex: "))
print(calculate_prims_mst(len(graph), src, graph))