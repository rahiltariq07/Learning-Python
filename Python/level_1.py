# 1. Python is a programmin language used to tell the computer what to do.
# It is popular because:
# - It looks like simple English
# - Easy for beginners
# - Used everywhere (websites, apps, AI, data science, automation)

# eg:
print("Hello, Rahil!")

# 2. Python Rules
# Python runs line by line.
# Python cares about spaces (indentation).
# No need to declare variable types.

# eg:
x = 10
name = "Rahil"
# Python automatically understands the type.

# 3. Variables
# A variable is a container used to store some data.

# eg:
age = 23
city = "Srinagar"
# You can use them later
print(age, city)

# 4. Data Types
# | Type  | Example             | Meaning                     |
# | ----- | ------------------- | --------------------------- |
# | int   |  10                 | Whole number                |
# | float |  10.5               | Decimal number              |
# | str   |  "Hello"            | Text                        |
# | bool  |  True / False       | Yes/No values               |
# | list  |  [1, 2, 3]          | A collection                |
# | tuple |  (1, 2)             | Like list but cannot change |
# | dict  |  {"name": "Rahil"}  | Key–value pairs             |

# eg:
marks = [90, 85, 88]
students = {"name": "Rahil", "Age": 23}

# 5. Print Statement
# To show output:

# eg:
print("Python is easy!")
# Print multipe things
print("My age is", 23)

# 6. Taking Input

# name = input("Enter your name: ")
# print("Hello", name)

# 7. Basic Operators

# 7.1 Math
print(10 + 5) # 15
print(10 - 5) # 5
print(10 * 5) # 50
print(10 / 3) # 3.33
print(10 // 3) # 3 (floor division)
print(10 % 3) # 1 (remainder)
print(2 ** 3) # 8 (power)

# 7.2 Comaprison
print(10 > 5)  # True
print(10 == 10)  # True
print(10 != 3)  # True

# Practice Question
# Q.no. 1:
name = input("Enter your name: ")
color = input("Enter your favourite color: ")

print(f"Hello {name}, your favourite color is {color}")

# Q.no. 2:
product_name = "Roti"
price = 7
quantity = 8

total = price * quantity

print(f"You bought {product_name}. Total cost is {total}")