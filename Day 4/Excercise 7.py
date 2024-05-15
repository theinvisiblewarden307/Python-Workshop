#Excercise: "Hilo"

def hilo(numbers):
    highest = numbers[0]
    lowest = numbers[0]

    for one_number in numbers:
        if one_number > highest:
            highest = one_number
        if one_number < lowest:
            lowest = one_number

    return [highest, lowest]