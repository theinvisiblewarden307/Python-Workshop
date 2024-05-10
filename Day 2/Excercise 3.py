#Excercise: Sum to 100

#I just changed the for loop to a while loop and added a condition to check if the total is less than 100

total = 0

while total < 100:
    numbers = input("enter a number: ").strip()
    if numbers.isdigit():
        total += int(numbers)
    else:
         print(f"Hey you cannot use {numbers} as a integer!")

print(f"Total is {total}")