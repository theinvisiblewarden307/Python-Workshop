#Exercise: Calc with user input

def calc(s):
    
    num1, op, num2 = s.split()
    num1 = int(num1)
    num2 = int(num2)

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    else:
        result = '(Who knows?)'

    print(f'{num1} {op} {num2} = {result}')

calc('2 + 3')