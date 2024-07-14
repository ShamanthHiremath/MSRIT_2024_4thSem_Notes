#Travelling salesman
def tsp_nearest_neighbor():
  graph = {'a' : {"b" : 10 , "c" : 2} , "b" : {"c":5, "a":10} , "c": {"a" : 2 , "b" : 5}}
  num_vertices = int(input("Enter the number of vertices in the graph: "))

  '''for i in range(num_vertices):
    vertex = input(f"Enter the name of vertex {i+1}: ")
    graph[vertex] = {}
    num_edges = int(input(f"Enter the number of edges for vertex {vertex}: "))

  for j in range(num_edges):
    neighbor = input(f"Enter the name of neighbor {j+1} for vertex {vertex}: ")
    distance = int(input(f"Enter the distance between {vertex} and {neighbor}: "))
    graph[vertex][neighbor] = distance  '''

  start_vertex = input("Enter the starting vertex: ")

  path = [start_vertex]
  current_vertex = start_vertex
  total_distance = 0

  while len(path) < len(graph):
    next_vertex = None
    min_distance = float('inf')

    for vertex in graph[current_vertex]:
      if vertex not in path:
        distance = graph[current_vertex][vertex]
        if distance < min_distance:
          min_distance = distance
          next_vertex = vertex

    total_distance += min_distance
    path.append(next_vertex)
    current_vertex = next_vertex

  print("The minimum distance is:", total_distance)
  return path

path = tsp_nearest_neighbor()
print("THE PATH IS:",path)