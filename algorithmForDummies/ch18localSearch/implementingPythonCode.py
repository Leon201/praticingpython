import numpy as np
import random

from math import log2

import matplotlib.pyplot as plt

# % matplotlib inline
plt.show()


def signed(v):
    return v if np.random.random() < 0.5 else -v


def create_clauses(i, seed=1):
    np.random.seed(seed)
    return [(signed(np.random.randint(i)), signed(
        np.random.randint(i))) for j in range(i)]


def check_solution(solution, clauses):
    violations = list()
    for k, (a, b) in enumerate(clauses):
        if not ((
                (solution[abs(a)] == (a > 0))
                |
                (solution[abs(b)] == (b > 0))
        )):
            violations.append(k)
        return violations
