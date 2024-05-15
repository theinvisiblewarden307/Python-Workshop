def calc(num1, op, num2):
    ''' calc() can find the sum or difference of any 2 integers.

    Expects: 3 Arguments (int ,'string', int)
    Modifies: Nothing
    Returns: A string
    '''
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    else:
        result = '(Who knows?)'

    print(f'{num1} {op} {num2} = {result}')

help(calc)