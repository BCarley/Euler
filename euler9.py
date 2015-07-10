"""euler9"""
for b in xrange(0, 1000):
    print "b: ", b
    for a in xrange(0, b):
        print "a: ", a
        if (a**2) + (b**2) + a*(a**2+b**2)**0.5 + b*(a**2+a**2)**0.5 + a*b == (1000**2)/2:
            print "Success!", a, b
