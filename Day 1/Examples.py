#This is a Python comment!

    #The following function will print strings:
print("Hello?")

    #Integers can be printed as well and we dont need to use quotes:
print(5)

    #We can also print the result of an operation:
print(8+2)

    #We can also consider integers as strings:
print("1"+"2")

    #Getting input from the user:
name1 = input("What is your name: ")

        #Now we can type that name along with hello and the input variable:
print("Hello, " + name1 + "!")

#We can also use operators to compare values:
if 5>3:
    print("5 is greater than 3")

    #We can use the f string to print the value of a variable in a string;
print(f"Hello, {name1}! Hope you are having a great day!")
    #We can use integers in the f string as well:
print(f"Hello, {name1}! Hope you are having a great day! Your lucky number is {5}")
    #We can also use variables in the f string:
Lucky_Number= 7
print(f"Hello, {name1}! Hope you are having a great day! Your lucky number is {Lucky_Number}")

    #VERY IMPORTANT: We can use the compare operators to compare alphabetical  order of the strings as well:
word1 = input("Enter first word: ") 
word2 = input("Enter second word: ")
if word1 < word2:
    print(f"{word1} comes first!")
else:
    print(f"{word2} comes first!")

#more complex conditionals(nesting condtions and introducing elif):
name2 = input("Enter name: ")

if name2 == 'Ramanuj':
    print("Hi Boss!")
elif name2 == "Someone":
    print("thats not really a good name.")
else:
    print(f'Hello {name2}')

#We can also use combining conditions:
x=10
y=20
if x==10 and y==20:
    print("That's right!")

#We can also convert strings to integers:
s=5
print(int(s)+2)

#We can use methods such as .strip to remove extra spaces from start and end of string:
M= "            n    "   
print(M.strip())


#To compare case sensitive strings using .lower():

o = "abcd"
p= "AbCd"

if o == p:
    print("True")
else:
    print("False")

    #now:
if o == p.lower():
    print("True")
else:
    print("False")
