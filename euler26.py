"""Euler 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit
recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""
from decimal import *
import sys
import time
import math

#     print Decimal(1) / Decimal(x)

def find_pattern(num):
    """find the repeating pattern in a text

    >>> num = "0.12312341231234"
    >>> getcontext().prec = len(num)
    >>> find_pattern(num)
    '1231234'

    >>> num = "0.01001100110011001"
    >>> getcontext().prec = len(num)
    >>> find_pattern(num)
    '1001'

    >>> num = "0.12354345345345"
    >>> getcontext().prec = len(num)
    >>> find_pattern(num)
    '345'

    >>> num = "0.3333333333333"
    >>> getcontext().prec = len(num)
    >>> find_pattern(num)
    '3'

    >>>
    """
    num = str(num)[2:].strip(' ').lstrip("0")

    if len(num) < 5: # getcontext().prec - 2
        return 0

    nlen = len(num)

    # starting index of pattern, moving along string by one each time
    for x in xrange(nlen):

        # ending index of pattern, extending pattern by one each move
        for y in xrange(1, nlen):

            # start of pattern is found at this point
            index = num.find(num[x:x+y], x+y, nlen)

            # break if not found
            if index == -1:
                break

            # check if the current pattern is the largest in the string
            if is_found(num[x:], num[x:x+y]):
                return num[x:x+y]

        if x > 10:
            break

    return 0


def is_found(num, pattern):
    """checks to see if the current pattern is the repeating pattern, if it is, returns true

    >>> is_found("33333333", "3")
    True

    >>> is_found("333333333", "3")
    True

    >>> is_found("01231234512312345", "123")
    False

    >>> is_found("0123123412312345", "1231234")
    False

    >>> is_found("12341231234123", "1234123")
    True

    >>> is_found("45345345", "453")
    True

    >>> is_found("345345", "354")
    False
    """

    # find what the remainder is for the whole string
    if len(pattern) == 0:
        return False

    trim = len(num) % len(pattern)

    # if the current pattern can be extended exactly to the whole number
    if not trim and pattern * (len(num)/len(pattern)) == num:
        return True

    # if the current pattern cannot be extended completely, trim the string and check the remainder too
    elif trim and pattern * (len(num)/len(pattern)) == num[:-trim] and pattern[:trim] == num[-trim:]:
        return True

    else:
        return False

def is_prime(num):
    """logic test to find a prime number

    >>> is_prime(983)
    True
    """
    if num <= 3:
        return num >= 2

    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in xrange(5, int(math.ceil(math.sqrt(num))), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True


def main():
    """
    main method
    """
    start = time.time()

    getcontext().prec = 10000

    _list = list(int(find_pattern(str(Decimal(1)/Decimal(x)))) for x in xrange(1, 1000) if is_prime(x))

    max_val = max(_list)
    max_idx = _list.index(max_val) + 1

    print "Largest repeating pattern was found to be %s for number %s" % (max_val, max_idx)
    print "Answer found in %s seconds" % (time.time() - start)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()