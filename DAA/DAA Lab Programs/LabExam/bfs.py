def bfs(graph):
    src = int(input("Enter Source Node: "))

    visited = [0 for _ in range(len(graph)+1)]
    queue = []
    queue.append(src)  
    visited[src] = 1
    
    print("BFS of the graph: ", end=" ")

    while queue:
        node = queue.pop(0)  # Dequeue a node from the queue 
        print(node, end=" ")  

        # Explore neighbors of the current node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = 1
                
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

bfs(graph)