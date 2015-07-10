"""euler question 2"""

def fib(n):
    """fibonachi"""
    even = 0
    a, b = 1, 1
    for i in range(1000):
        a, b = b, a+b

        if a % 2 == 0:
            even += a

        if a > n:
            break
    return even

print fib(4000000)
