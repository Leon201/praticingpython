import networkx as nx
import matplotlib.pyplot as plt

AGraph = nx.Graph()

Nodes = range(1, 6)
Edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5), (1, 6)]

AGraph.add_nodes_from(Nodes)
AGraph.add_edges_from(Edges)

print(nx.degree_centrality(AGraph))

nx.draw(AGraph)

plt.show()

AGraph.add_node(7)

print(
    nx.closeness_centrality(AGraph))

print(
    nx.betweenness_centrality(AGraph)
)