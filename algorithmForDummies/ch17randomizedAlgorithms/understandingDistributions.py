import numpy as np
from numpy.random import normal, uniform
import matplotlib.pyplot as plt

normal_distribution = normal(size=10000) * 25 + 100
weights = np.ones_like(normal_distribution
                       ) / len(normal_distribution)
plt.hist(normal_distribution, bins=20, weights=weights)
plt.xlabel("Value")
plt.ylabel("Probability")
plt.show()

uniform_distribution = uniform(size=10000) * 100
weights = np.ones_like(uniform_distribution
                       ) / len(uniform_distribution)
plt.hist(uniform_distribution, bins=20, weights=weights)
plt.xlabel("Value")
plt.ylabel("Probability")
plt.show()

# 这里使用随机算法，后面又一个例子是讲quick sort因为这个算法可能最坏的情况
# 但是使用随机的时候，就可以避免这种情况
# 我记得好像是merge sort，应该是记错了。quick sort是随机选取一个中作为中间值
# 然后把比这个值要大的值和比这个值要小的值放到两边，然后切成两百，然后继续随机选取

# TODO 这张要不先skip 321 但是这张是在说分布式 distributions
# 第19章和20章是线性规划，好像之前同学说到的是什么来着。启发式听起来像是粒子群算法
