"""Euler22


Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

import string

alph = list(string.ascii_uppercase)

with open("p022_names.txt", 'rb') as f:
    lines = [x.replace("\"", "") for x in f.read().split(",") if len(x) > 0]

lines.sort()

print lines

name_score = 0
for (i, name) in enumerate(lines, 1):
    position_score = i

    letter_score = 0
    for letter in name:
        letter_score += alph.index(letter) + 1

    name_score += letter_score * position_score

print name_score
