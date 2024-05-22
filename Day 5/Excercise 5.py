#Exercise: Richify vowels

import rich

s = input('Enter text: ').strip()   # get a string from the user

# set up our output string (to be empty)
output = ''


# go through each character in the user's input, s
for one_character in s:

    # if we see a vowel, then put FORMAT_START + vowel + FORMAT_END on output
    if one_character in 'aeiou':
        output += f'[yellow italic on black]{one_character}[/yellow italic on black]'

    # Not a vowel? Just add the character to output
    else:
        output += one_character

# use rich.print to print, which handles the formatting
rich.print(output)