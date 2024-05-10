#Excercise: Guessing game:

secret=47
guess=input("Guess the secret number: ")

if int(guess) == secret:
    print("Congratulations! You guessed the number right on!")
elif int(guess) < secret:
    print("Too low!")
else:
    print("Too high!")

print("Game Over!")