#Exercise: Digits, vowels, and others:

digits = 0
vowels = 0
others = 0

s = input('Enter text: ').strip()

for one_character in s:
    if one_character in 'aeiou':
        # print(f'{one_character} is a vowel')
        vowels += 1
    elif one_character.isdigit():
        # print(f'{one_character} is a digit')
        digits += 1
    else:
        # print(f'{one_character} is other')       
        others += 1

print(f'digits = {digits}')
print(f'vowels = {vowels}')
print(f'others = {others}')

