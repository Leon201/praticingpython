import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

graph = {
    'A': {'B': 2, 'C': 3}
    , 'B': {'C': 2, 'D': 2}
    , 'C': {'D': 3, 'E': 2}
    , 'D': {'F': 3}
    , 'E': {'D': 1, 'F': 1}
    , 'F': {}
}

Graph = nx.DiGraph()
# 这里终于有有方向的图了，拿之前的图，难道没有方向这个权重会被替换掉
for node in graph:
    Graph.add_nodes_from(node)
    for edge, weight in graph[node].items():
        Graph.add_edge(node, edge, weight=weight)

pos = {
    'A': [0.00, 0.50], 'B': [0.25, 0.75]
    , 'C': [0.25, 0.25], 'D': [0.75, 0.75]
    , 'E': [0.75, 0.25], 'F': [1.00, 0.50]
}

labels = nx.get_edge_attributes(Graph, 'weight')
nx.draw(Graph, pos, with_labels=True)
nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels)
nx.draw_networkx(Graph, pos)

plt.show()


from algorithmForDummies.Ch09reconnectingTheDots.introducingPriorityQueues \
    import priority_queue


def dijkstra(graph, start, end):
    inf = float('inf')
    known = set()
    priority = priority_queue()
    path = {start: start}

    for vertex in graph:
        if vertex == start:
            priority.push(0, vertex)
        else:
            priority.push(inf, vertex)
    last = start

    while last != end:
        (weight, actual_node) = priority.pop()
        if actual_node not in known:
            for next_node in graph[actual_node]:
                # 下一个顶点的权重和出发点的权重
                # 然后把下一个的数值是这个顶点的权重加上图中的距离权重
                upto_actual = priority.index[actual_node]
                upto_next = priority.index[next_node]
                to_next = upto_actual + \
                    graph[actual_node][next_node]
                # 如果在优先队列里面的数值比这个值大，那就更新优先队列
                # 出发点的初始值是0，其他都是无限大
                # 然后把这个出发点连接的所有的顶点的权重都更新一遍
                if to_next < upto_next:
                    priority.push(to_next, next_node)
                    print("Found shortcut from %s to %s"
                          % (actual_node, next_node))
                    print ("\tTotal length up so far: %i"
                           % to_next)
                    # 如果发现了更短的路径，从下一个顶点到这个顶点的路径会被替换成成这个顶点
                    path[next_node] = actual_node

            # 可以说这里就是通过连接的点的顺序去修改这个path中的数据，然后一直到连接到end就结束
            last = actual_node
            # 然后这个顶点也就被放到node中，这个actualnode其实是已经在prio里面的
            known.add(actual_node)

    return priority.index, path

dist, path = dijkstra(graph, "A", "F")
print(path)

# 这边要倒过来找是因为，存放的时候，就是把next作为key存放的
# TODO 这里不理解的地方是，权重在不断的更新，但是路径存放却是倒过来的
# 是因为出发点会有很多连接点，但是这些连接的点所对应的数据永远都是一条，也就是一对多变成多对一，或者说是一对一
# 然后反过来找，不会出现多条路径，然后这个next的顶点的path一直会被跟新，只要发现更小的权重
def reverse_path(path, start, end):
    progression = [end]
    # 如果过程的最后一个不是start
    while progression[-1] != start:
        # 就在过程的最后增加这个值
        # 这个值是通过过程的最后一个值去path里面找到的下一个值
        progression.append(path[progression[-1]])
    print (progression)
    # 然后把这个过程倒过来
    # print (progression[:-1])
    # print (progression[::-2])
    # print (progression[-1::])
    # print (progression[::-3])
    # 懂吗
    # 【start: end : step]
    return progression[::-1]
#

print (reverse_path(path, 'A', 'F'))