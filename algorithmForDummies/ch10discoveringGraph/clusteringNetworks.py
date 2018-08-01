import networkx as nx
import matplotlib.pyplot as plt

graph = nx.karate_club_graph()

pos = nx.spring_layout(graph)

nx.draw(graph, pos, with_labels=True)
plt.show()

# discovering communities

# Finding and printing all cliques of four

cliques = nx.find_cliques(graph)
print ('All cliques of four: %s'
       % {c for c in cliques if len(c) >= 4})

# Joinging cliques of four into communities
# communities = cliques.k_clique_communities(graph, k=4)

# 没有这个方法 ！！