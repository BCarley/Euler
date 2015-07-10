"""euler9"""

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

            except MemoryError:
                print "Run out of memory, range is too long for c long!!"
                break


def nth_prime(n):
    """n is the number prime you want, due to the way the 'primes sieve'
    is constructed, n must be less than 100000000"""

    for (index, i) in enumerate(generate_primes()):
        if index + 1 == n:
            print "Found Prime %i! %i" % (index+1, i)
            return i
    print "Unable to find %ith prime" % n

print nth_prime(10001)
