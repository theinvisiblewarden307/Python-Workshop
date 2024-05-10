#Excercise; Get a Character:

s = input("Enter a word: ")
i = input("Enter the numeric index: ")

if int(i) < 0:
    print("Error! Value is too low.")
elif int(i) >= len(s):
    print("Error: Too High!")
else:
    print(f"Character at index {i} is {s[int(i)]}")
