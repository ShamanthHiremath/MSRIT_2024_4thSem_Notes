from collections import defaultdict

def calculate_prims_mst(n, m, g):
    # Create adjacency list
    adj = defaultdict(list)
    for edge in g:
        u, v, w = edge
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Initialize arrays
    weights = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)

    # Main algorithm
    src = 1
    weights[src] = 0
    for _ in range(1, n + 1):
        mini = float('inf')
        for j in range(1, n + 1):
            if not visited[j] and weights[j] < mini:
                mini = weights[j]
                u = j

        visited[u] = True
        for neighbor, weight in adj[u]:
            v = neighbor
            w = weight
            if not visited[v] and w < weights[v]:
                weights[v] = w
                parent[v] = u

    # Form MST
    ans_mst = []
    for i in range(src + 1, n + 1):
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
    graph = []
    n = int(input("Enter the no. of edges: "))

    print("Enter edge pair as u -> v")
    for i in range(n):
        u = int(input(f"Pair {i}: "))
        v = int(input("->"))
        # dir = int(input("Directed?: "))
        wt = int(input("Enter weight: "))
        
        # if u not in graph:
            # graph[u] = []
        graph.append([u, v, wt])

        # if (not dir):
        # if v not in graph:
            # graph[v] = []
        graph.append([v, u, wt])

# Sample output
print(calculate_prims_mst(5, 14, g))