from itertools import permutations
import time

starttime = time.time()
computes = list()
solutions = list()
n = 9
xlist = list(range(n))
for yperm in permutations(range(0, n)):
    computes.append(0)
    ulist = [0] * len(xlist)
    vlist = [0] * len(xlist)
    for x in xlist:
        ulist[x] = xlist[x] - yperm[x]
        vlist[x] = yperm[x] + xlist[x]
    if len(set(ulist)) == len(ulist) \
            and len(set(vlist)) == len(vlist):
        print('Find a solution')
        solutions.append((xlist, yperm))
        print(xlist)
        print(yperm)

print('use time: %s with %i solutions'
      % ((time.time() - starttime), len(solutions)))
print('computes: %s' % len(computes))
