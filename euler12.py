"""euler question 12

Find the first pyrmidal number that has 500 factors

"""
import math
import itertools

def generate_triangular_numbers():
    """
    generate triangular number, will not break at any point.
    """
    num = 0
    for x in itertools.count():
        num += x
        yield num

def factorise_num(num):
    """
    return a list of factors
    """

    return [i for i in xrange(1, int(n**0.5) + 1) if not n % i] # returns the pairs of factors
    # --- old ---- [y for y in xrange(1, int(round(num/2)+1)) if num % y == 0]

for x in generate_triangular_numbers():
    if x == 0:
        continue

    facts = len(factorise_num(x)) * 2
    # print "Factors for %i: \n" % x, factorise_num(x)

    print "Factorising %i, %i factors!" % (x, facts)
    if facts >= 500:
        break