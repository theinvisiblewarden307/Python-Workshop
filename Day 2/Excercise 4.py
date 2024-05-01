#Excercise: Summing digits

total = 0

while True:
    numbers = input("enter a number: ").strip()
    if numbers == '':
            break
    for i in numbers:
          if i.isdigit():
                total += int(i)
          else:
                print(f"Hey {i} is not a digit!")

print(f"{total} is total.")
        