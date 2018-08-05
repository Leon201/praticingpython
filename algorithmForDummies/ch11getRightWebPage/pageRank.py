import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

Graph_A = nx.DiGraph()
Graph_B = nx.DiGraph()
Graph_C = nx.DiGraph()

Nodes = range(1, 6)
Edges_OK = [
    (1, 2), (1, 3), (2, 3), (3, 1), (3, 2), (3, 4), (4, 5)
    , (4, 6), (5, 4), (5, 6), (6, 1)
]
Edges_dead_end = [
    (1, 2), (1, 3), (3, 1), (3, 2), (3, 4), (4, 5)
    , (4, 6), (5, 4), (5, 6), (6, 5), (6, 1)
]
Edges_trap = [
    (1, 2), (1, 3), (3, 1), (3, 2), (3, 4), (4, 5)
    , (4, 6), (5, 4), (5, 6), (6, 5)
]

Graph_A.add_nodes_from(Nodes)
Graph_A.add_edges_from(Edges_OK)
Graph_B.add_nodes_from(Nodes)
Graph_B.add_edges_from(Edges_dead_end)
Graph_C.add_nodes_from(Nodes)
Graph_C.add_edges_from(Edges_trap)

np.random.seed(2)
pos = nx.shell_layout(Graph_A)
# nx.draw(Graph_A, pos, with_labels=True)
nx.draw(Graph_B, pos, with_labels=True)
# nx.draw(Graph_C, pos, with_labels=True)
# arrows=True
plt.show()


# 就是5和6变成一个有向，一个无向
# 然后C图是6和1之间是没有连接的

# implementing naive

def initialize_PageRank(graph):
    nodes = len(graph)
    M = nx.to_numpy_matrix(graph)
    # print (M) # 这里的这个举证代表的是这里面所有的点之间的连接关系，而且是有方向的
    # print (M.T) # 这里应该是转置
    # squeeze的意思是把原来的举证压缩成一列，好像不是
    # 压缩到第一列，然后squeeze是变成一个一维的数据，有一种flat的感觉，flatMap
    # print(np.sum(M, axis=1))
    # print(np.asarray(np.sum(M, axis=1)))
    outbound = np.squeeze(np.asarray(np.sum(M, axis=1)))
    # print (outbound)
    prob_outbound = np.array(
        [1.0 / count
         if count > 0 else 0.0 for count in outbound]
    )
    G = np.asarray(np.multiply(M.T, prob_outbound))
    p = np.ones(nodes) / float(nodes)
    if np.min(np.sum(G, axis=0)) < 1.0:
        print ('Warning: G is substochastic')
    return G, p

G, p = initialize_PageRank(Graph_A)
print (G)
print (p)

from scipy import sparse
sG = sparse.csr_matrix(G)
print (sG)
print (np.dot(G, p))

def PageRank_naive(graph, iters = 50):
    G, p = initialize_PageRank(graph)
    for i in range(iters):
        p = np.dot(G, p)
    return np.round(p, 3)

# 没看懂，书中说B图的剩下的网络很不幸的把概率什么来着
# 然后把top排名变成了不重要
print('PageRank_naive(Graph_A)')
print(PageRank_naive(Graph_A))
print(PageRank_naive(Graph_B))
print(PageRank_naive(Graph_C))

# TODO page 220 introducing boredom and teleporting