"""
Euler 14

n > n/2 (n is even)
n > 3n + 1 (n is odd)

for which number, n, can we produce the longest chain?



"""
import itertools
import time

start = time.time()
cache = [0] * 1000001
cache[1] = 1

def generate_chain(num, cache):
    """find the chain length for each number"""
    init = num
    for i in itertools.count():
        if num < 1:
            break

        if num <= 1000000:
            if cache[num] != 0:
                i += cache[num]
                break

        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1

    return (init, i)

for x in xrange(1000000):
    if x % 100000 == 0:
        print "Up to %d!" % x

    tup = generate_chain(x, cache)
    cache[tup[0]] = tup[1]


elapsed = (time.time() - start)
print "Found %d at %d in %d seconds" % (max(cache), cache.index(max(cache)), elapsed)
print cache[837799]
