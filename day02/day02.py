## Advent of Code 2020: Day 2
## https://adventofcode.com/2020/day/2
## Jesse Williams | github.com/vblank182
## Answers: [Part 1]: 536, [Part 2]: 558

import re
from collections import Counter

passwordDB = []
validPasswords1 = 0
validPasswords2 = 0

# Create password database
with open('day02_input.txt') as f:
    for line in f.readlines():
        # DB List Structure: (char_min, char_max, required_char, password)
        passwordDB.append( re.search("(\d+)-(\d+)\s([a-z]):\s([a-z]+)", line).groups() )


##################
###|  Part 1  |###
##################

# Search for valid passwords
for (char_min, char_max, required_char, password) in passwordDB:
    charCounts = Counter(password)
    if int(char_min) <= charCounts[required_char] <= int(char_max):
        validPasswords1 += 1

print(f'[Part 1] {validPasswords1} valid passwords found.')


##################
###|  Part 2  |###
##################

# Search for valid passwords
for (index_lo, index_hi, required_char, password) in passwordDB:
    if ( (password[int(index_lo)-1] == required_char) ^ (password[int(index_hi)-1] == required_char) ):
        validPasswords2 += 1

print(f'[Part 2] {validPasswords2} valid passwords found.')
