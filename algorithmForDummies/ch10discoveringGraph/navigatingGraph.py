import networkx as nx
import matplotlib.pyplot as plt

data = {
    'A': ['B', 'F', 'H']
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
nx.draw_networkx_labels(graph, pos)
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos)
plt.show()

print(
    nx.shortest_path_length(graph, 'A')
)

