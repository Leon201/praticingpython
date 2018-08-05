[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


from functools import lru_cache

#这里还有注解，加了注解之后，函数在运行的时候会有新的属性？
@lru_cache(maxsize=None)
def fib(n, tab=0):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print("lvl %i, Summing fib(%i) and fib(%i)" %
              (tab, n - 1, n - 2))
        return fib(n - 1, tab + 1) + fib(n - 2, tab + 1)


fib(7)

memo = dict()
print(fib.cache_info())
print("------")
def fib_mem(n, tab=0):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if (n - 1, n - 2) not in memo:
            print("lvl %i, Summing fib(%i) and fib(%i)" %
                  (tab, n - 1, n - 2))
            memo[(n - 1, n - 2)] = fib_mem(n - 1, tab + 1) + fib_mem(n - 2, tab + 1)
        return memo[(n - 1, n - 2)]

fib_mem(7)
print(memo)

# %timeit -n 1 -r 1 print(fib(36))

# TODO 这里和后面的memoization，还有8皇后问题的关系
# force delay这里是吗，force delay是函数编译运行的作用域不一样的实现过程吗，force delay定义的函数语法也是meta linguistic, 这块没有懂