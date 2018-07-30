import networkx as nx

graph = {
    'A': {
        # 'B': 2, 'C': 3
    }
    , 'B': {
        # 'A': 2,
        # 'C': 2,
        'D': 2}
    , 'C': {
        # 'A': 3,
        'B': 2, 'D': 3, 'E': 2}
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

# -----------------

from algorithmForDummies.Ch09reconnectingTheDots.introducingPriorityQueues \
    import priority_queue


def kruskal(graph):
    priority = priority_queue()
    print("Pushing all edges into the priority queue")
    treepath = list()
    connected = dict()
    for node in graph:
        # connected[node] = [node]
        # 这里是直接使用数组
        for dest, weight in graph[node].items():
            # 增加了这两行
            if not connected.__contains__(dest):
                connected[dest] = [dest]
            priority.push(weight, (node, dest))
            # 这里的这个堆，也是前面是key，后面的这个是对象吗
    print("Totally %i edges" % len(priority))
    print("Connected componets: %s"
          % connected.values())

    total = 0
    # 这里也就是是不是treepath的长度是不是和图是一样的
    # 这里后面也要增加一个条件，不然这个heap没东西弹出了，因为A这个顶点是不连接的
    while len(treepath) < (len(graph) - 1) and len(priority) > 0:
        # 会从最小值开始，最小值也就是用边的权重来排序的
        # 而且这样所有的边都会有
        # TODO 如果有没有连接的顶点怎么办，上面的这个while应该是使用connected吧
        # 这里只要又一个顶点没有被连接过就挂了
        (weight, (start, end)) = priority.pop()
        # 这里的赋值是可以根据数据的形式来赋值的，感觉和前面数组里面的两个值交换一样
        # 这里的所谓的连接过的顶点不一定是直接连接的顶点，还有他的end所连接的所有的顶点
        # 而end所连接的顶点，也可能这end的end的所有连接过的顶点
        # 这里增加了前面的这个条件, 但是这个条件是不是会用上呢
        if \
                connected.__contains__(start) and \
                end not in connected[start]:
            # 这样treepath才会被放进来，否则这个path或者说这个边是会被忽略的
            # 所以说这里不是每个顶点来遍历的，这要是曾经被连接过的顶点，就会通知这个被连接过的顶点
            # 然后不断的传递和通知
            # 而且priority什么都pop不出来的时候，函数就结束了吧。会怎么样
            treepath.append((start, end))
            print("Summing %s and %s components:"
                  % (connected[start], connected[end]))
            print("\tadded edge from %s " \
                  "to %s weighting %i"
                  % (start, end, weight))
            total += weight
            connected[start] += connected[end][:]
            # 这里叫做字典，这里增加end这里是什么意思
            for element in connected[end]:
                connected[element] = connected[start]
    print("Total spaning tree length: %i" % total)
    # test
    print("test connected: ", connected)
    print("test treepath: ", treepath)
    return sorted(treepath, key=lambda x: x[0])


print('\nMinimum spanning tree: %s' % kruskal(graph))

# (,) 这种应该就是对象的意思

# TODO 怎么办，后面的不想看了，什么连接的顶点，然后才往treepath里面增加，而且增加的时候，增加的是start的所有的顶点
# 应该就是这个算法的原理，再看看

# Minimum spanning tree: [('B', 'C'), ('B', 'D'), ('D', 'E'), ('E', 'F')]

# 变成了有方向，C到B，但是没有B到C
# Minimum spanning tree: [('B', 'D'), ('C', 'B'), ('D', 'E'), ('E', 'F')]
# 其实也就是把连接的信息全部传递到那个顶点，然后，也不需要替换，因为已经用priority_queue来排序过了
# 然后判断的关键就是，这个顶点是不是是已经连接过了，这个顶点的信息就会不断的增加，每次连接都把这个顶点连接的信息和现在新连接的信息合并到一起
# TODO 还是想不通，不会漏信息吗，也就是说无关的顶点是不会有信息合并的，模模糊糊一点都想不通，基本上所有的顶点都有，然后和数据中存储的信息的顺序可能也有关系
# skip， kruskal. 怎么办，不想看，直接看下面的最小路径把