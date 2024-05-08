#Exercise: Restaurant:

menu = {'sandwich':10, 'apple':5, 'tea':7, 'cake':12}

total = 0

while True:
    order = input('Order: ').strip()

    if order == '':
        break

    if order in menu:
        price = menu[order] 
        total += price
        print(f'{order} costs {price}, total is now {total}')
    else:
        print(f'We are out of {order} today!')

print(f'Total is {total}')