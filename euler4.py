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


def get_quadratic_residues(num, no_primes):
    """returns a list of the first num primes"""
    factor_base = []
    for prime in generate_primes():
        if (num ** ((prime - 1)/2)) % prime == 1:
            factor_base.append(prime)
        if len(factor_base) > no_primes:
            break
    return factor_base


def sieve_values(num, values, factor_base):
    """performs a sieve on the values to return a list of numbers,
    numbers that are returned as 1 are smooth numbers"""
    for prime in factor_base:
        cnt = 0
        for (index, i) in enumerate(values):
            if ((index + int(math.ceil(num ** 0.5))) ** 2 - num) % prime == 0:
                cnt += 1
                #print "divided by %i" % (prime), values
                values[index::prime] = [int(value/prime) for value in values[index::prime]]
                #print "Divided by %i at index %i, count is %i:" % (prime, index, cnt), values, "\n"

                if prime == 2 or cnt == 2:
                    break

    return values


def construct_matrix(num, values, factor_base):
    """returns a dictionary of factor vectors"""
    smooth_x = []
    for (index, value) in enumerate(values):
        if value == 1:
            smooth_x.append(index)

    smooth_y = [((x + math.ceil(num ** 0.5))**2 - num) for x in smooth_x]

    matrish = []
    for y in smooth_y:
        matrish.append([div_into(y, prime) % 2 for prime in factor_base])

    m = matrish
    return m


def div_into(x, y):
    """ """
    cnt = 0
    while True:
        if x % y == 0:
            x /= y
            cnt += 1
        else:
            break
    return cnt



def factorise(num):
    """perform a quadratic sieve to find the largest factors of num"""
    values = [(i + math.ceil(num ** 0.5)) ** 2 - num for i in xrange(-100, 100)]

    factor_base = get_quadratic_residues(num, no_primes=100)
    print "Factor Base:", factor_base
    sieved_values = sieve_values(num, values, factor_base)

    return construct_matrix(num, sieved_values, factor_base)

x = factorise(977779)

print "Sieved Values:", x
