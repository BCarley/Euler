"""euler 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

"""
import collections
words = collections.OrderedDict()

words["1single_digit"] = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

words["2two_digit"] = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

words["3hundred"] = [''] + [i + "hundred" for i in words["1single_digit"] if len(i) > 0]

words["4thousand"] = [''] + [i + "thousand" for i in words["1single_digit"] if len(i) > 0]

teens = {11:'eleven', 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
         16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}

def number_builder(num):

    length = 'and'
    # i.e. "one hundred and one" vs "one hundred"
    if num % 100 == 0 or num <= 100:
        length = ''

    if num % 100 in teens:
        length += teens[num % 100]
        num -= num % 100

    for item in words:
        length += words[item][num % 10]
        num = (num - (num % 10)) / 10
    return length

y = [number_builder(i) for i in xrange(1,1001)]
print len(y)
print sum(len(i) for i in y)

print number_builder(342)