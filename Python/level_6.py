# Strings & Important String Functions
# Strings are one of the most important parts of Python.
# A string simply means text.

# eg:
name = "Rahil"
message = "Python is easy!"

# 1. String Basics
# Strings are written in quotes
# Strings can contain letters, numbers, spaces, symbols

# 2. Accessing Characters (Indexing)
# Just like lists, strings have indexes.

name = "Rahil"
print(name[0])  # R
print(name[1])  # a
print(name[-1]) # l (negative index -> from end)

# 3. String Slicing
# You can get parts of a string:
text = "Python"

print(text[0:3])  # Pyt
print(text[:4])   # Pyth
print(text[2:])   # thon

# 4. Important String Functions
# upper() -> uppercase
print("Nachan".upper())
name = "Rahil"
name = name.upper()
print(name)

# lower() -> lowercase
print("NACHAN".lower())
name = "RAHIL"
name = name.lower()
print(name)

# title() -> first letter capital of every word
print("kyasa tuhi chuv thk".title())
name = "rahil"
name = name.title()
print(name)

# strip() -> removes spaces
print("  hello  ".strip()) # removes initial and last spaces of the string, works as a trim function of js

# replace(old, new)
print("Hello Rahil".replace("Rahil", "Ali"))

greet = "Hello Ahmad"
greet = greet.replace("Ahmad", "Rahil")
print(greet)

# split() -> convert string to list
fruits = "apple,banana,grapes"
list_fruits = fruits.split(",")

print(list_fruits)

# join -> converts list to string
print(", ".join(["a", "b", "c"]))

new_fruits = ", ".join(list_fruits)
print(new_fruits)

# 5. Checking Things in String
# Check if a word exists
print("python" in "I love python")

# Length of string
print(len("Rahil")) # starts from 1

# 6. String Formatting
# Used to build messages.

# Using f-strings
name = "Rahil"
age = 25
print(f"My name is {name} and I am {age} years old")

# 7. Looping Through a String
for n in name:
    print (n)


## Practice Questions
# Q.no.: 1
string = "python programming"
upperd_string = string.upper()
print(upperd_string)

# Q.no.: 2
str1 = " hello world  "
new_str1 = str1.strip()
print(new_str1)
print(new_str1.replace("world", "Rahil"))

# Q.no.: 3
sentence = input("Enter a sentence: ")
words = sentence.split(" ")
print(words)
print(len(words))

for word in words:
    print(word)