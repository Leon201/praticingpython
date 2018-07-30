import networkx as nx
graph = {
    'A': {'B': 2, 'C': 3}
    , 'B': {'A': 2, 'C': 2, 'D': 2}
    , 'C': {'A': 3, 'B': 2, 'D': 3, 'E': 2}
    , 'D': {'B': 2, 'C': 3, 'E': 1, 'F': 3}
    , 'E': {'C': 2, 'D': 1, 'F': 1}
    , 'F': {'D': 3, 'E': 1}
}

Graph = nx.Graph()
for node in graph:
    Graph.add_nodes_from(node)
    for edge, weight in graph[node].items():
        Graph.add_edge(node, edge, weight=weight)

pos = {
    'A': [0.00, 0.50], 'B': [0.25, 0.75]
    , 'C': [0.25, 0.25], 'D': [0.75, 0.75]
    , 'E': [0.75, 0.25], 'F': [1.00, 0.50]
}


from algorithmForDummies.Ch09reconnectingTheDots.introducingPriorityQueues \
    import priority_queue

def prim(graph, start):
    treepath = {}
    total = 0
    queue = priority_queue()
    queue .push(0, (start, start))
    while queue:
        weight, (node_start, node_end) = queue.pop()
        if node_end not in treepath:
            treepath[node_end] = node_start
            if weight:
                print ("Added edge from %s" \
                       " to %s weighting %i"
                       % (node_start, node_end, weight))
                total += weight
            for next_node, weight \
                in graph[node_end].items():
                queue.push(weight, (node_end, next_node))
    print ("Total spanning tree length: %i" % total)
    return treepath

treepath = prim(graph, 'A')

print('treepath: ', treepath)
def reprsent_tree(treepath):
    progressino = list()
    for node in treepath:
        if node != treepath[node]:
            progressino.append((treepath[node], node))
    return sorted(progressino, key=lambda x: x[0])

print (reprsent_tree(treepath))

# 括号逗号的这个到底是什么东西呢，好像是数组，好像和数组是一样的，但是又可以作为参数
# 然后map也是可以作为参数，用两个星号就可以成为函数特定的参数了，map的key作为函数的参数的名称

