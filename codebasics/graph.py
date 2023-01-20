# Day 11 - Binary Search Tree(BST) 2 --------------
# diff from graph and tree: 
# Tree has one path to a node.
# graph can have many paths to one node. (spacious path)

# Graphs and trees are recursive
# When using recursion, think about the simplist case.

class Graph:
  def __init__(self, edges):
    self.edges = edges
    self.graph_dict = {}
    # loop through the touples
    for start, end in self.edges:
      # if start('Mumbai') is in dict.
      if start in self.graph_dict:
        # after first key value is added. Append the end('Dubai') to start('Mumbai') in the dict already.
        self.graph_dict[start].append(end)
      else:
        # if dict is blank add start('Mumbai') as key and end('paris') as the value.
        self.graph_dict[start] = [end]
    print("graph dict: ", self.graph_dict)

  # Gets all paths
  def get_paths(self, start, end, path=[]):
    # The simplist cast is if your going to the same place your entered.
    path = path + [start]
    if start == end:
      return [path]
    # if start does not have any routes to end. Ex: your looking for routes with a start that has no edges.
    if start not in self.graph_dict:
      return []
    paths = []
    # loop through start[start] - which is the nested routes.
    for node in self.graph_dict[start]:
      # check if its already in the path first, if not then do ..
      if node not in path:
        # how many paths are there. 
        new_paths = self.get_paths(node, end, path)
        # add all the new paths to paths[]
        for p in new_paths:
          paths.append(p)
    return paths

  def get_shortest_path(self, start, end, path=[]):
    # If the start path is the same as the end path, return itself.
    path = path + [start]
    if start == end:
      return path
    # if start is not a key in the dict, return none.
    if start not in self.graph_dict:
      return None
    # We dont know at the beginning what the shortest path is.
    shortest_path = None
    # loop through the dict keys.
    for node in self.graph_dict[start]:
      # if the key is not in the path
      if node not in path:
        # sp will be recursively called to get the shortest path. ***
        sp = self.get_shortest_path(node, end, path)
        # in case 
        if sp:
          # if i dont have a shortest path then whatever shortest path i do get i want to keep it. or if the sp is shorter than the shortest_path i would want to keep it.
          if shortest_path is None or len(sp) < len(shortest_path):
            shortest_path = sp
    # return the path
    return shortest_path

if __name__ == '__main__':
  routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
  ]

  route_graph = Graph(routes)

  # start = "Mumbai"
  # end = "New York"
  # print(f"Paths between {start} and {end}: ", route_graph.get_paths(start, end))

  start = "Paris"
  end = "New York"
  print(f"Shortest paths between {start} and {end}: ", route_graph.get_shortest_path(start, end))