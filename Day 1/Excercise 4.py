#Excercise 4: Which word comes first?

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if word1 < word2:
    print(f"{word1} comes before the {word2}")
else:
    print(f"{word2} comes before the {word1}")