#Excercise: Pig Latin

english = input("Please enter an english word, all lowercase, no punctuation and spaces:  ")

if english[0]in 'aeiou':
    print(english + "way")
else:
    print(english[1:] + english[0] + "ay")
    