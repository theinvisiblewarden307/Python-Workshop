#Excercise: Odds and Evens:

from random import randint

odds = []
evens = []

s = input('How many numbers: ').strip()

if s.isdigit():
    n = int(s)

    for counter in range(n):
        number = randint(0, 100)
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    print(f'odds = {odds}')
    print(f'evens = {evens}')
else:
    print(f'{s} is not numeric; exiting')
