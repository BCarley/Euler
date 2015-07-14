"""Euler 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import collections
from itertools import chain

def divisor_sum(num):
    """find the sum of the divisors for a number
    """
    return sum(chain.from_iterable((x, num/x) for x in xrange(1, int(num**0.5)+1) if num % x == 0)) - num



def get_amicable_nums(num):
    """return a list of amicable numbers from 1 to num
    """

    divisor_sums = [divisor_sum(num) for num in xrange(1, num+1)]


    # print list(enumerate(divisor_sums, 1))

    amicable_nums = []

    # at index = 220, x = 284
    for (index, x) in enumerate(divisor_sums, 1):
        print "d(%s) = %s" % (index, x)

        if x <= num and x != 1 and index != 1 and x != index:
            if x == divisor_sums[x-1] and index == divisor_sums[index]:
                amicable_nums.append(index)

    return amicable_nums


# sum_amicable = sum(index for (index, num) in enumerate(divisor_sums, 1) if num in amicable_sums)
print divisor_sum(284)


print 50 in get_amicable_nums(285)
# print
print get_amicable_nums(285)
# print sum(get_amicable_nums(10000))
# print (10000 in get_amicable_nums(10000))
# print max(get_amicable_nums(10000))
# # print sum(amicable_nums)

