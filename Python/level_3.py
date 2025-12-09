# Functions in Python:
# A function is a small block of code that does one specific task.
# Think of it like a machine:
# You give input to the machine,
# It does work inside,
# And sometimes gives you output.

# 1. Why do we use functions:
# ✔ To avoid repeating the same code again
# ✔ To organize code nicely
# ✔ To make code easy to read
# ✔ To reuse logic many times

# 2. How to create a function:
# We use the keyword **def**

def greet():
    print("Hello, World!")

# 3. Calling a function:
greet()

# 4. Function with Parameters (inputs)
# A parameter is a variable that receives input inside the function.
def hello(name):
    print(f"Hello, {name}")

hello("Rahil")

# 5. Function with Multiple Parameters
def add(a, b):
    print(a + b)

add(2, 4)

# 6. Function that Returns a Value
# Sometimes we want a function to give back a result.
# Use return.

def multiply(c, d):
    return c * d

result = multiply(5, 3)
print(result)

# 7. Default Parameter Values
# If you don't give a value, Python will use the default.

def shh(nachan = "Rahil"):
    print(f"Hello, {nachan}")

shh() # Hello, Rahil
shh("Ali") # Hello, Ali

# 8. Keywords Arguments
# You can mention the parameter name while calling.

def info(name, age):
    print(name, age)

info(age= 23, name = "Rahil") # Order doesn't matter when keywords are used.

# 9. Functions and Return vs Print
# Very important difference:
# print() → only shows result on screen
# return → gives value back so you can use it later

# eg: 
def add(a, b):
    return a + b

# You can use the output:
total = add(5, 10)
print(total)

# 10. Function Scope (Where a variable lives)
# Variables inside a function cannot be used outside.
def test():
    x = 10  # local variable

test()
# print(x)   # ❌ ERROR: x is not defined


# Practice Questions
# Q.no.: 1
def square(num):
    print(num * num)

square(5)

# Q.no.: 2
def calculate(price, quantity, discount):
    total = price * quantity

    return total - (total * discount / 100)

final_amount = calculate(100, 2, 10)
print(int(final_amount))