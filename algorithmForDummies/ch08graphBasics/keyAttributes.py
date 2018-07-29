import networkx as nx
import matplotlib.pyplot as plt
# %matplotlib inline

# matplotlib inline

AGraph = nx.Graph()

Nodes = range(1, 5)
Edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5)]

AGraph.add_nodes_from(Nodes)
AGraph.add_edges_from(Edges)

nx.draw(AGraph, with_labels=True)

plt.show()

# %是内嵌函数，可以直接执行plt.show()
