#Exercise: Guessing game:

import random
number = random.randint(0,100)
while True:
    guess = input("Guess the Number! Its between 0 and 100.  ").strip()
    if guess.isdigit():
        guess_converted = int(guess)
        if guess_converted == number:
            print("Great Job! You guessed accurately!")
            break
        elif guess_converted > number:
            print("That's too high! Try again.")
            break
        else:
            print("That's way too low, give it another go!")
            break
    else:
        print("Hey!, That's not a number!")
        break