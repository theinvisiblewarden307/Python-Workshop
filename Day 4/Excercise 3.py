#Exercise: Even better calculator

def calc(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    else:
        result = '(Who knows?)'

    print(f'{num1} {op} {num2} = {result}')

calc(1,'+',2)