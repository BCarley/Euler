"""Euler 20

sum of the digits in the number 100!
"""

print sum(int(x) for x in str(reduce(lambda x, y: x*y, xrange(1,101))))