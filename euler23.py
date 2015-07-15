"""Euler 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,

the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""
from itertools import chain, product
import time


def divisor_sum(num):
    """find the sum of the proper divisors for a number
    """
    return sum(set(chain.from_iterable((x, num/x) for x in xrange(1, int(num**0.5)+1) if num % x == 0))) - num


abundant_nums = [x for x in xrange(28123) if divisor_sum(x) > x]

print "Started calculating now"

start = time.time()

products = [0] * 28125

for num_1 in abundant_nums:
    for num_2 in (num_2 for num_2 in abundant_nums if num_2 >= num_1 and num_1 + num_2 <= 28124 and products[num_2+num_1] == 0):
        products[num_1 + num_2] = 1

print "Product Calculated in %s" % (time.time() - start)
# print [(index, i) for (index, i) in enumerate(products) if i < 1000]
print sum(index for (index, i) in enumerate(products) if i == 0)