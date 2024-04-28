#Excercise: Which word comes first?(Remastered):

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if word1 < word2:
    print(f" Word 1: {word1} comes before the Word 2: {word2}")
elif word2 < word1:
    print(f" Word 1: {word2} comes before the  Word 2: {word1}")
elif word1 == word2:
    print(f'You entered {word1} twice!')