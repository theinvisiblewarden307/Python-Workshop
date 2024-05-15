#Excercise: Returning values

def calc(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    else:
        result = '(Who knows?)'

    return f'{num1} {op} {num2} = {result}'

x = calc(2, '+', 3)