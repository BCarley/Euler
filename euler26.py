"""Euler 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""
from decimal import *
import sys

getcontext().prec = 750

#     print Decimal(1) / Decimal(x)

def find_pattern(num):
    """find the repeating pattern in a text

    >>> find_pattern(0.01001100110011001)
    '1001'

    >>> find_pattern(0.12354345345345)
    '345'
    """


    num = str(num)[2:].strip(' ')
    # print "Num:", num
    return get_index(num)


def get_index(num):
    """generator function for finding longer patterns
    """
    _list = []
    if len(num) < 10:
        return 0

    for x in xrange(len(num)):
        for y in xrange(1, len(num)):
            index = num.find(num[x:x+y], x+y, len(num))
            print "Start: %s, Stop: %s, Index: %s" % (x, x+y, index)
            print num[x:x+y]

            if index == -1:
                break

            if index <= x + y:
                break

        _list.append(num[x:x+y])

    return list(x for x in _list if len(x) == max(len(x) for x in _list))[0]


def main():
    """
    """

    print find_pattern(Decimal(1)/Decimal(379))

    sys.exit(0)
    _list = list(int(find_pattern(Decimal(1)/Decimal(x))) for x in xrange(1, 1000))
    print _list
    max_val = max(_list)
    max_idx = _list.index(max_val) + 1

    print "Largest repeating pattern was found to be %s for number %s" % (max_val, max_idx)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()