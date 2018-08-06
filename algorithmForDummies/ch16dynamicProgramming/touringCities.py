import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

D = np.array(
    [
        [0, 20, 16, 25, 24]
        , [20, 0, 12, 12, 27]
        , [16, 12, 0, 10, 14]
        , [25, 12, 10, 0, 20]
        , [24, 27, 14, 20, 0]
    ]
)

Graph = nx.Graph()
print('Dshape0', D.shape[0])
# 这里shape的意思是什么呢，应该就是数组的形状和维度
Graph.add_nodes_from(range(D.shape[0]))
for i in range(D.shape[0]):
    for j in range(D.shape[0]):
        Graph.add_edge(i, j, weight=D[i, j])
# 这里如果是映射的话，不是符号不需要空格

np.random.seed(2)
#
pos = nx.shell_layout(Graph)
nx.draw(Graph, pos, with_labels=True)
labels = nx.get_edge_attributes(Graph, 'weight')
nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels)
plt.show()

from itertools import permutations

best_solution = [None, np.sum(D)]
# 看出来了，shape是维度，然后0的话代表的就是1维的地方有几个参数
# 这样说起来其实也不是维度，可以一说是维度，比如说2维数组。
for solution in list(permutations(range(1, D.shape[0]))):
    start, distance = (0, 0)
    for next_one in solution:
        distance += D[start, next_one]
        start = next_one
    distance += D[start, 0]
    if distance <= best_solution[1]:
        best_solution = [[0] + list(solution) + [0], distance]
        print('Best solution so far: %s kms' %
              str(best_solution)[1:-1])

print(best_solution)

from scipy.special import perm

print(perm(13, 13) / 2)

from itertools import combinations

memo = {(frozenset([0, idx + 1]), idx + 1): (dist, [0, idx + 1])
        for idx, dist in enumerate(D[0][1:])}
cities = D.shape[0]
for subset_size in range(2, cities):
    new_memo = dict()
    for subset in [frozenset(comb) | {0} for comb in
                   combinations(range(1, cities)
                       , subset_size)]:
        for ending in subset - {0}:
            all_paths = list()
            for k in subset:
                if k != 0 and k != ending:
                    length = memo[(subset - {ending}, k)][0] \
                             + D[k][ending]
                    index = memo[(subset - {ending}, k)][1] \
                    + [ending]
                    all_paths.append((length, index))
            new_memo[(subset, ending)] = min(all_paths)

    memo = new_memo

tours = list()
for distance, path in memo.values():
    distance += D[path[-1], 0]
    tours.append((distance, path + [0]))

distance, path = min(tours)
print('Shortest dynamic programming tour is: %s, %s kms'
      % (path, distance))

# TODO 这里还没有看懂
