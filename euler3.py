"""euler question 3"""
import math

def is_prime(num):
    """logic test to find a prime number"""
    if num <= 3:
        return num >= 2

    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in xrange(5, int(math.ceil(math.sqrt(num))), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True

def largest_prime(num):
    """finds the largest prime number"""
    if int(math.ceil(math.sqrt(num))) % 2 == 0:
        end = int(math.ceil(math.sqrt(num))) + 1
    else:
        end = int(math.ceil(math.sqrt(num)))
        print end
    for i in reversed(xrange(3, end, 2)):
        if num % i == 0:
            if is_prime(i):
                return i

print largest_prime(600851475143)
