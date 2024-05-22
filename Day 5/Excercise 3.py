#Exercise: Count punctuation:

import string

string.punctuation

counts = {}
for one_character in string.punctuation:
    counts[one_character] = 0

s = input('Enter text: ').strip()

for one_character in s:
    if one_character in counts:     # is the character a key in the dict?
        counts[one_character] += 1  # add 1 to its count



for key, value in counts.items():
    if value > 0:
        print(f'{key}: {value}')
