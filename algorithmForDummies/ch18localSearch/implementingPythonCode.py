import numpy as np
import random

from math import log2

import matplotlib.pyplot as plt

# % matplotlib inline
plt.show()


# 随机的加上正负符号
def signed(v):
    return v if np.random.random() < 0.5 else -v


def create_clauses(i, seed=1):
    np.random.seed(seed)
    return [(signed(np.random.randint(i)), signed(
        np.random.randint(i))) for j in range(i)]



# 给1加上符号，有一般的概率是否，也就是生成随机的true，false
# 然后前面的编号是排序排好的
# 第二个参数没有用上
def create_random_solution(i, *kwargs):
    return {j: signed(1) == 1 for j in range(i)}


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


def sat2(clauses, n, start=create_random_solution):
    for external_loop in range(round(log2(n))):
        solution = start(n, clauses)
        history = list()
        for internal_loop in range(2 * n ** 2):
            response = check_solution(solution, clauses)
            unsatisfied = len(response)
            history.append(unsatisfied)
            if unsatisfied == 0:
                print("Solution in %i external loops, " %
                      (external_loop + 1), end=" ")
                print("%i internal loops" %
                      (internal_loop + 1))
                break
            else:
                r1 = random.choice(response)
                r2 = np.random.randint(2)
                clause_to_fix = clauses[r1][r2]
                solution[abs(clause_to_fix)] = (
                        clause_to_fix > 0)
        else:
            continue
        break
    return history, solution


n = 1000
# Solvable seeds with n=1000 : 0,1,2,3,4,5,6,9,10
# Unsolvable seeds with n=1000 : 8
clauses = create_clauses(n, seed=0)
history, solution = sat2(clauses, n
                         , start=create_random_solution)

plt.plot(np.array(history), 'b-')
plt.xlabel("Random ajustments")
plt.ylabel("Unsatisfied clauses")
plt.grid(True)
plt.show()

