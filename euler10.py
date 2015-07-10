"""euler question 4

Trying to find the largest palindromic product of 2 three digit numbers.
attempting to use the quadratic sieve method for this"""
import math
import numpy as np

def is_palindromic(num):
    """tests a number to see is palindromic, returns Bool"""
    if str(num)[::-1] == str(num):
        return True
    else:
        return False


def generate_primes(end=10000000):
    """generator function that yeilds primes that are, by default
    less than 10000000

    10000000 is about the limit the sieve will work to until we start running out of memory"""

    np1 = end + 1
    s = range(end + 1)
    s[1] = 0

    for i in xrange(2, np1):
        if s[i]:
            try:
                s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
                yield i

            except MemoryError, e :
                raise "Run out of memory, range is too long for c long!! \n Exception: %s" % e

prime_sum = 0
for i in generate_primes():
    if i < 2000000:
        prime_sum += i
    else:
        break
print prime_sum
