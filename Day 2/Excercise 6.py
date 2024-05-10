#Exercise: Sum numbers

total = 0


while True:
    numbers = input("Enter a number string:  ").strip()
    if numbers == '':
        break
        
    list_of_numbers = numbers.split()
    
    for i in list_of_numbers:
        if i.isdigit():
            n = int(i)
            total += n

        else:
            print(f"Hey!, {i} is not a numerical value!")


print(f"{total} is total.")