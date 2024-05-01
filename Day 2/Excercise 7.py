#Exercise: Pig Latin sentence
output = ''
sentence = input('Enter a sentence: ').strip()

for word in sentence.split():
    if word[0] in 'aeiou':
        output += word + 'way '
    else:
        output += word[1:] + word[0] + 'ay '

print(output)