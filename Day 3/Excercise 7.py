#Exercise: Dict to config:

small={}
for key,value in small.items():
    with open('small.txt','a') as f:
        f.write(f'{key}: {value}\n')
with open('small.txt') as f:
    print(f.read())