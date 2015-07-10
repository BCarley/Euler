rng = range(1, 20)
num = 20
while True:
    div = [num % i for i in rng]
    if sum(div) == 0:
        print "found!", num
        break
    num += 20

