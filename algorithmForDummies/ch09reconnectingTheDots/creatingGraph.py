graph = {
    'A': ['B', 'C']
    , 'B': ['A', 'C', 'D']
    , 'C': ['A', 'B', 'D', 'E']
    , 'D': ['B', 'C', 'E', 'F']
    , 'E': ['C', 'D', 'F']
    , 'F': ['D', 'E']
}

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# %

Graph = nx.Graph()
for node in graph:
    Graph.add_nodes_from(node)
    for edge in graph[node]:
        Graph.add_edge(node, edge)

pos = {
    'A': [0.00, 0.50], 'B': [0.25, 0.75]    , 'C': [0.25, 0.25], 'D': [0.75, 0.75], 'E': [0.75, 0.25], 'F': [1.00, 0.50]
}

# nx.draw(Graph, pos, with_labels=True)
plt.show()
nx.draw_networkx(Graph, pos)

plt.show()
