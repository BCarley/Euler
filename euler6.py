"""euler 6"""
#sum of squares
def sum_of_squares(num):
    """sum of squares"""
    return (num * (num + 1) * (num * 2 + 1))/6

def square_of_sum(num):
    """square of sum"""
    print range(1, num + 1 )
    return (sum(range(1, num + 1))) ** 2

print square_of_sum(100) - sum_of_squares(100)
