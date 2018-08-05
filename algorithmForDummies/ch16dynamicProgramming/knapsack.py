import numpy as np

# 这里是讲轮船的体量是20吨，然后每吨的利润如下6种，体积的单位重量
# 计算出最好的组合，以及最后的总重量
# 这个问题一开始就没有理解，也没有思路，先看一下代码吧

values = np.array([3, 4, 3, 5, 8, 10])
weights = np.array([2, 3, 4, 4, 5, 9])
# 总共有6种货物
items = len(weights)
# 体量是20k立方吧
capacity = 20

# 增加字典，在每个字典里面都加上一个对象的字典
# 对象第一位是-1，后面是size，存的也是一个数组加一个数字
memo = dict()
for size in range(0, capacity + 1, 1):
    memo[(-1, size)] = ([], 0)

# 然后用货物编号开始遍历
for item in range(items):
    # 然后根据体量20，从最小的0开始遍历
    for size in range(0, capacity + 1, 1):
        # 如果货物编号的重量大于体积
        # 那一开始是不可能大于体积的，然后一个个货物试过去
        # 都不行然后增加size，同时不断的更新memo中的数据数字编号因为从0开始的
        # memo的初始化数值是-1，就是说这20个体量里面没有一个货物
        if weights[item] > size:
            # 这里对所有的memo的这个size都设置成空数组和0
            memo[item, size] = memo[item - 1, size]
        else:
            # 这里终于是有货物可以装下了，获得前一个货物的数据
            # 一开始是没有前一个货物的，所以这里的数据就是空数组和0
            previous_row, previous_row_value = memo[item - 1, size - weights[item]]
            # 如果上一个货物和当前size的这个体量的第二个值，不知道什么意思，反正这里肯定是0
            # 大于这个货物的利润加上上一个获取的利润，这里也是0，这里一开始是不可能，先看下一个分支
            if memo[item - 1, size][1] > values[item] + previous_row_value:
                memo[item, size] = memo[item - 1, size]
                # 就对当前的size和当前货物的值，通过上一个数组，拼接当前的货物对象，然后在把之前的值增加上当前货物的利润
                # 一开始的时候，自然就是第一个对象，然后加上这个对象的利润值
            else:
                memo[item, size] = (previous_row + [item], previous_row_value + values[item])
                # 然后回到第一个分支，如果当前的利润比之前的要大，现在的货物直接就等于货物名称减去1然后和现在的体量的值
                # 看错了，是上一个货物编号的利润比现在这个货物的利润值要大，然后就把这个数据拷贝过来
                # 然后相反，如果理论没有现在的这个利润大，就更新当前的这个货物和这个体量的值
                # 等于是对所有的可能和所有的体量组合进行了遍历

                # 而且如果没有更好的组合，就会把数据拷贝过来，也就是最后一个组合和体量也就保存了最优的组合了
                # 说是话，有点绕，但是感觉就是遍历所有的可能，不是去做替换，而是保留最好的组合，然后再根据不同的重量减去现在的仲康，
                # 去找上一个memo，因为是对这个size或在所有的item中去拷贝，所以也不怕找不到，直接找编号item-1就能找到
                # 然后一开始就初始化了item=-1的数据是空的

best_set, score = memo[items - 1, capacity]

print('The best set %s weights %i and values %i'
      % (best_set, np.sum(weights[best_set]), score))
# The best set [0, 3, 4, 5] weights 20 and values 26
# jupyter notebook 跑出来也是这个结果
# 这里结果的意思是1， 4， 5， 6这些结果，最后的总重量是20，和体积没有关系，然后利润是26
# 不是应该是直接找一个利润率最大的不就好了，是不是因为重量不可分割导致需要去做组合，然后总重量正好是20

print(len(memo))
# 打印出来memo的数据量有147， 7 * 21 -1到5 0到20

print(memo[2, 10])

from scipy.misc import comb

objects = 6
# 这个方法是组合的意思，因为range是从0开始的所以要加上1
# 然后就是在6个项目中，选出2个作为组合，有几种组合的方法
cooob = [comb(objects, k + 1) for k in range(objects)]
print(cooob)
print(
    np.sum(cooob)
)

# 这一章说的是动态算法，好像不是说代码是动态的，或者说就是因为不同的情况，所以每次执行的代码走的分支是不一样的
# 也就是多了一些分支，具体在执行的时候，可能会有不一样的结果