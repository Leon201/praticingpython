import random
import networkx as nx
random.seed(0)

data = {
    'A': ['B', 'H']
    , 'B': ['A', 'C']
    , 'C': ['B', 'D']
    , 'D': ['C', 'E']
    , 'E': ['D', 'F', 'G']
    , 'F': ['E', 'A']
    , 'G': ['E', 'H']
    , 'H': ['G', 'A']
}

graph = nx.DiGraph(data)


pos = nx.spring_layout(graph)

paths = nx.all_simple_paths(graph, 'A', 'H')

path_list = []
for path in paths:
    path_list.append(path)
    print ('Path Candidate: ', path)

sel_path = random.randint(0, len(path_list) - 1)

print ("The seleted path is: ", path_list[sel_path])


import matplotlib.pyplot as plt
nx.draw_networkx_labels(graph, pos)
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos)
plt.show()
