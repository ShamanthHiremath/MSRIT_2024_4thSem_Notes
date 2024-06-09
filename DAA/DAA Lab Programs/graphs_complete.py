def bfs(graph):
    src = int(input("Enter Source Node: "))

    visited = [0 for _ in range(len(graph)+1)]
    queue = []
    queue.append(src)  
    visited[src] = 1

    while queue:
        node = queue.pop(0)  # Dequeue a node from the queue
        print(node)  

        # Explore neighbors of the current node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = 1


def dfs(adj, visited, component, node):
    component.append(node)
    visited[node] = True
    # Recursively explore all adjacent nodes
    for neighbor in adj.get(node, []):
        if not visited[neighbor]:
            dfs(adj, visited, component, neighbor)

def dfs_all(adj):
    print("DFS of the graph: ", end=" ")
    ans = []
    visited = [False] * (len(adj)+1)

    for i in range(len(adj)+1):
        if i==0:
            continue
        if not visited[i]:
            component = []
            dfs(adj, visited, component, i)
            ans.append(component)

    print(ans)

 
def dfs(v, graph):
    stack = []
    stack.append(v)
    visited = [0 for x in range(len(graph)+1)]
    result = []
    while stack:
        u = stack[-1]
        if u not in visited:
            visited.add(u)
            for neighbor in reversed(graph[u]):  # Reverse for consistent order
                if neighbor not in visited :
                    stack.append(neighbor)
        else:
            stack.pop()
            if u not in result:
                result.append(u)

def isBipartite(graph):
    colors = {x : [-1] for x in range(1, len(graph)+1)}  # Dictionary to store colors of nodes
    stack = [(1, 0)]  # Stack for DFS traversal with node and its color
    colors[1] = 0  # Assign color 0 to the source node
    print("(Node, Color) of all nodes: ", end=" ")
    while stack:
        node, color = stack.pop()
        colorname = "Red" if color else "Blue"
        print(f"({node}, {colorname})", end=" ")  # For now, just print the node

        # Explore neighbors of the current node
        for neighbor in graph[node]:
            # If neighbor is not colored, assign the opposite color to it
            # if colors[neighbor] == -1:
            if neighbor not in colors:
                colors[neighbor] = 1 - color
                stack.append((neighbor, 1 - color))
            # If neighbor has the same color as the current node, graph is not bipartite
            elif colors[neighbor] == color:
                print("\nThe given graph is NOT BIPPARTITE")
                return False
    print("\nThe given graph is BIPPARTITE")
    return True

def dispGraph(graph):
    for node in range(len(graph)+1):
        if node==0:
            continue
        print(node, end=": ")
        for neighbor in graph[node]:
            print(neighbor, end=" ")
        print()

def inputEdges(graph):
    n = int(input("Enter the no. of edges: "))

    print("Enter edge pair as u -> v")
    for i in range(n):
        u = int(input(f"Pair {i}: "))
        v = int(input("->"))
        dir = int(input("Directed?: "))
        
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        if (not dir):
            if v not in graph:
                graph[v] = []
            graph[v].append(u)



# graph as as dictionary of integer as keys and a appendable list
# graph = {x : [-1] for x in range(1, 9)}
graph = {}

print(graph)

inputEdges(graph)

dispGraph(graph)

bfs(graph)

dfs_all(graph)

isBipartite(graph)