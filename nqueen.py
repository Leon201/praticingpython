# 首先理解一下题目，就是说在一个棋盘上放皇后，然后放上8个，皇后之间都不会和其他皇后发生冲突
# 棋盘是8*8， 皇后的运行路线是四面八方
# 然后可以是通过循环，或者是递归，其实都是一样的

# 假设一个思路，在棋盘上随机放上一个
# 然后可以随机放上第二个，看一下是不是冲突
# 然后不断的放第3个，一直到找不到任何的解，就要回退到上一步

# 这一步就是已经记录下了不可行的解，然后是个数，和解
# 下次再找新的时候，可以先看一下是不是在这个解里，然后这个解需要通过排列组合来比较

# 通过无穷算法，貌似是可以不停的计算然后找到所有的解的，但是这本书里面的算法是什么看一下

######

# 这里是local search算法的概念
# 其实也就是分布式计算的local算法
# 这里有点类似于粒子群算法，好像和maya三维动画里面的particle dynamics没有什么关系
# 书中描述的算法是先随机的在棋盘上放好
# 然后把皇后向上下左右移动，然后看看是不是能有更少的攻击，这样就至少可以分出8个分支
# 然后如果攻击变少了，那就往这个方向分配

# 粒子群算法，particle swarm optimization

# N皇后问题的位移解法
# https://www.jianshu.com/p/2ea643764174
# 虽然还没有看懂，但是给了一个思路就是，其实是占用了棋盘上的空间
# 比如说横竖斜，4个方向是不可以冲突的，就好像是在另外一个维度里面占用了空间
# 所以可以，所有的原来的坐标可以改成4维的坐标，然后

# 斜过来的坐标，然后怎么还有个遗传算法
# https://www.cnblogs.com/ktao/p/7721811.html

# 这里所有的坐标改成比如【3， 4】， 改成[3， 4， 3 + 8 - 4， 4 + 8 - 3]
# 也就是【3， 4， 7， 9】
# 修改的方法是x增加，u增加，v减小，然后搜索对比

# 看看遗传算法是怎么找到解的，能不能找到所有解
# 按道理讲，棋盘只有8个格子，只能放8个皇后
# 然后那个遗传算法也是最快找到一个解，或者是几个解，看看能找到多少个解
# 那个local search里面就是找到多少个解之后，就不找了

import time

solutions = list()
recursives = list()
starttime = time.time()
xlist = list(range(9))
ylist = list(range(len(xlist)))
ulist = [0] * len(xlist)
vlist = [0] * len(xlist)
for x in xlist:
    ulist[x] = xlist[x] - ylist[x]
    vlist[x] = ylist[x] + xlist[x]


def changeAndVerify(xlist, ylist, ulist, vlist, oy=0):
    recursives.append(0)
        # exit(1)
    if oy > len(xlist):
        return
    for ny in range(oy + 1, len(xlist)):
        ylist[oy], ylist[ny] = ylist[ny], ylist[oy]
        ulist[oy] = xlist[oy] - ylist[oy]
        vlist[ny] = ylist[ny] + xlist[ny]

        if len(set(ulist)) == len(ulist) \
                and len(set(vlist)) == len(vlist):
            print('Find a solution')
            solutions.append((xlist, ylist))
            print(xlist)
            print(ylist)
        changeAndVerify(xlist, ylist, ulist, vlist, oy + 1)

# 直接用combination, 然后验证
# TODO 这里的解个数不对
# use time: 0.0216372013092041 with 20 solutions
# recursive: 13700
changeAndVerify(xlist, ylist, ulist, vlist)
print('use time: %s with %i solutions'
      % ((time.time() - starttime), len(solutions)))
print('recursive: %s' % len(recursives))

# 这可以改成heap或者stack或者queue
# 然后是分布式和粒子群

# 和这个人的代码比较一下
# http://www.cnblogs.com/newflydd/p/5097473.html
# https://www.hexcode.cn/article/show/eight-queen
# 八皇后极限编程 15皇后，用时：4903毫秒，计算结果：2279184
