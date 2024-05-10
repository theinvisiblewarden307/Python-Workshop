#Exercise: Word lengths:

words = {}   # empty dict

while True:
    s = input('Enter word: ').strip()

    if s == '':
        break
    
    words[s] = len(s)

print(words)