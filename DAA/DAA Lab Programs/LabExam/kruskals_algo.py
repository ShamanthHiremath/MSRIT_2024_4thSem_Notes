
def find_parent(node, parent_root):
    if parent_root[node] != node:
        parent_root[node] = find_parent(parent_root[node], parent_root)  # Path compression
    return parent_root[node]

def union_set(u, v, parent_root, rank):
    # Fetch parent roots of u and v
    root_u = find_parent(u, parent_root)
    root_v = find_parent(v, parent_root)

    # Union by rank
    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent_root[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent_root[root_v] = root_u
        else:
            parent_root[root_v] = root_u
            rank[root_u] += 1

def minimum_spanning_tree(edges, n):
    # Sort the edges based on weights (in ascending order)
    edges.sort(key=lambda x: x[2])
    rank = [0] * n
    path = []

    # Create the disjoint sets
    # Initializes parent roots as themselves, assuming disconnected nodes
    parent_root = [i for i in range(n)]

    minimum_weight = 0
    
    # Kruskal's Algorithm
    for edge in edges:
        u, v, wt = edge
        u -= 1  # Adjusting for 0-based index
        v -= 1  # Adjusting for 0-based index
        
        u_parent = find_parent(u, parent_root)
        v_parent = find_parent(v, parent_root)

        # If u and v don't have the same parent, merge their sets
        if u_parent != v_parent:
            union_set(u_parent, v_parent, parent_root, rank)
            path.append([u, v, wt])
            minimum_weight += wt

    print(f"Printing the path set: {path}")
    return minimum_weight

def inputEdges():
    edges = []
    e = int(input("Enter the no. of edges: "))
    print("Enter edge pair as u -> v")
    for i in range(e):
        u = int(input(f"Pair {i}: "))
        v = int(input("->"))
        dir = int(input("Directed?: "))
        wt = int(input("Enter weight: "))
        
        edges.append([u, v, wt])

        if (not dir):
            edges.append([v, u, wt])
        
    return edges

# # Example usage:
# # Sample input
# edges = [
#     [1, 2, 2],
#     [1, 4, 6],
#     [2, 1, 2],
#     [2, 3, 3],
#     [2, 4, 8],
#     [2, 5, 5],
#     [3, 2, 3],
#     [3, 5, 7],
#     [4, 1, 6],
#     [4, 2, 8],
#     [4, 5, 9],
#     [5, 2, 5],
#     [5, 3, 7],
#     [5, 4, 9]
# ]


vertices = int(input("\nEnter number of vertices: "))    
edges = inputEdges()

# Sample output
print(minimum_spanning_tree(edges, vertices))  # Expected output: 16