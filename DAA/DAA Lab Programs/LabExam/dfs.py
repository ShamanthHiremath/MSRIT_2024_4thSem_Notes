def dfs(adj, visited, component, node):
    component.append(node)
    visited[node] = True
    # Recursively explore all adjacent nodes
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(adj, visited, component, neighbor)

def dfs_all(adj):
    print("DFS of the graph: ", end=" ")
    ans = []
    visited = [False] * (len(adj))

    for i in range(len(adj)):
        if not visited[i]:
            component = []
            dfs(adj, visited, component, i)
            ans.append(component)

    print(ans)
                
def dispGraph(graph):
    print("\nAdjacency list: ")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
                
def inputEdges():
    graph = {}
    n = int(input("Enter the no. of edges: "))

    print("Enter edge pair as u -> v")
    for i in range(n):
        u = int(input(f"Pair {i+1}: "))
        v = int(input("->"))
        dir = int(input("Directed?: "))
        
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        if (not dir):
            if v not in graph:
                graph[v] = []
            graph[v].append(u)
            
    return graph

graph = inputEdges()

dispGraph(graph)

dfs_all(graph)