"""
Euler 15

Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner

How many such routes are there through a 20x20 grid?

This works, but it is incredibly slow, maybe removing the join?

"""

import itertools
import time

start = time.time()

def gen(n):
    n = n * 2
    x = list(''.join(i) for i in itertools.product("01", repeat=n-1) if i.count("1") == n/2-1)

    x = len(x) * 2
    print "%s paths found in %s seconds!(for a %s^2 square)" % (x, time.time() - start, n/2)
    return

gen(20)

