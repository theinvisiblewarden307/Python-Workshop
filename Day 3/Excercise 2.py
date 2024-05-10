#Exercise: Vowels, digits, and others (dict edition):

counts = {'vowels':0, 'digits':0, 'others':0}

s = input('Enter text: ').strip()

for one_character in s:   # iterate over the string, one character at a time
    if one_character in 'aeiou':
        counts['vowels'] += 1    # update the vowel count
    elif one_character.isdigit():    # if the charater is a digit
        counts['digits'] += 1     # add 1 to the digit count
    else:
        counts['others'] += 1     # add 1 to the others count

print(counts)


