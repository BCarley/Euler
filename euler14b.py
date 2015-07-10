"""
Euler 14

n > n/2 (n is even)
n > 3n + 1 (n is odd)

for which number, n, can we produce the longest chain?

in this I have attempted to use a more complete cache, involving all the numbers that are generated by the generate_list
function but the process of creating the list open ended list is slowing everything down...

stupid append....

"""
import itertools
import time

start = time.time()
cache = [0] * 1000001
cache[1] = 1

def generate_list(num, cache):
    plus = 0
    _list = [num]
    while True:
        if num <= 1:
            break

        if num < 1000000 and cache[num] != 0:
            plus = cache[num]
            break


        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1

        _list.append(num)

    numbered_list = [(x, y) for (x, y) in itertools.izip(_list, (i + plus for i in reversed(xrange(len(_list))))) if x < 1000000]

    return numbered_list


for num in xrange(1000000):
    if cache[num] != 0:
        continue

    for (x, y) in generate_list(num, cache):
        cache[x] = y



elapsed = (time.time() - start)
print "Found %d at %d in %s seconds" % (max(cache), cache.index(max(cache)), elapsed)
print cache[837799]
