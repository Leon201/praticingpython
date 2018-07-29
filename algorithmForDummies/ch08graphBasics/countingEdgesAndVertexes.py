import networkx as nx
import matplotlib.pyplot as plt

AGraph = nx.Graph()


Nodes = range(1, 5)
Edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5)]

AGraph.add_nodes_from(Nodes)
AGraph.add_edges_from(Edges)

AGraph.add_node(6)
sorted(nx.connected_components(AGraph))

nx.draw(AGraph, with_labels=True)
plt.show()

AGraph.add_edge(1, 6)
sorted(nx.connected_components(AGraph))

print(nx.degree(AGraph))
    # .values()
# has no attribute 'values'
# print(AGraph.values())

# 这里的clustering不是很明白
# 包括degree的概念，好像这个意思是重要性
#   或者是趋势。clustering是一个度量程度
#   是高还是低
nx.clustering(AGraph)


nx.draw(AGraph, with_labels=True)
plt.show()

# dict_values([4, 2, 3, 2, 2, 1])
