from heapq import heappush, heappop, heapify
from collections import defaultdict, Counter
from random import shuffle, seed

generator = ["A"] * 6 + ["C"] * 4 + ["G"] * 2 + ["T"] * 2
text = ""
seed(4)
for i in range(1000):
    shuffle(generator)
    text += generator[0]

print(text)
frequencies = Counter(list(text))
print(frequencies)

heap = ([[freq, [char, ""]] for char, freq in frequencies.items()])

heapify(heap)
print(heap)

iteration = 0
while len(heap) > 1:
    iteration += 1
    lo = heappop(heap)
    hi = heappop(heap)
    print('Step %i 1st: %s 2nd: %s' % (iteration, lo, hi))
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

# 这里什么意思啊，感觉像是对字母进行重新编码

# 假设这个heap最后是一个数组，然后数组里面还有数组，从第二个开始
# len肯定是1了
# print(heap)
# 所以要先pop出来，变成了一个一维数组，只是一个heap的话，说明只能pop出一个东西来
tree = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
print("Symbol\tWeight\tCode")
for e in tree:
    print("%s\t%s\t%s" % (e[0], frequencies[e[0]], e[1]))

# Counter({'A': 405, 'C': 292, 'T': 158, 'G': 145})
# [[145, ['G', '']], [158, ['T', '']], [292, ['C', '']], [405, ['A', '']]]
# Step 1 1st: [145, ['G', '']] 2nd: [158, ['T', '']]
# Step 2 1st: [292, ['C', '']] 2nd: [303, ['G', '0'], ['T', '1']]
# Step 3 1st: [405, ['A', '']] 2nd: [595, ['C', '0'], ['G', '10'], ['T', '11']]
# [[1000, ['A', '0'], ['C', '10'], ['G', '110'], ['T', '111']]]
# Symbol	Weight	Code
# A	405	0
# C	292	10
# G	145	110
# T	158	111

# 所以说看到的第三步还没有结束，会把里面低位的统一加0，高位统一加1重新编码

