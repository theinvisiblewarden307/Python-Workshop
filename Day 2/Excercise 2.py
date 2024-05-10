#Excercise: Total of Three

total = 0

for i in range(3):
    numbers = input("enter a number: ").strip()
    if numbers.isdigit():
        total += int(numbers)
    else:
         print(f"Hey you cannot use {numbers} as a integer!")

print(total)