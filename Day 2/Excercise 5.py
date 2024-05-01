#Exercise: Odds and evens

odds = []
evens = []

while True:
   
    numbers = input("Enter any number: ").strip()

    if numbers == '':
        break
    elif numbers.isdigit():
        n = int(numbers)
        if n % 2 == 1:
           odds.append(n)
        elif n % 2 == 0:
            evens.append(n)

print(odds)
print(evens)