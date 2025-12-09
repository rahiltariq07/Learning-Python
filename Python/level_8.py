# Error Handling (Try-Except)
# Error Handling helps your program not crash when something goes wrong

# 1. What is Error Handling?
# Sometimes your program gets errors like:
# Dividing by zero
# File not found
# Wrong input
# List index out of range

# Instead of crashing, Python lets you handle these errors using:
# ✔ try
# ✔ except

# 2. Basic Try-Except Example
try:
    num = 10/0
except:
    print("Something went wrong")
# Instead of crashing, it prints a message.

# 3. Handling a Specific Error
# Example: ZeroDivisionError
try:
    num = 100/0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 4. Multiple Except Blocks
try:
    x = int("abc")
except ValueError:
    print("Invalid number")
except:
    print("Unknown error")

# 5. Try-Except-Else
# else runs only if no error happens.
try:
    num = 10 / 2
except:
    print("Error!")
else:
    print("No error, result is:", num)

# 6. Try-Except-Finally
# finally always runs (error or no error)
try:
    f = open("students.txt")
except:
    print("File not found")
finally:
    print("Done checking file")

# 7. Why We Use Error Handling?
# ✔ To avoid app crashing
# ✔ To show user-friendly messages
# ✔ To handle unexpected input
# ✔ To make program stable

# 8. Real-world Example
try:
    age = int(input("Enter age: "))
    print(f"Your age is: {age}")
except ValueError:
    print("Please enter a valid number!")


## Practice Questions
# Q.no.: 1
try:
    num = int(input("Enter a number: "))
    div = 10/num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please Enter a valid number")
else:
    print(div)

# Q.no.: 2
try:
    with open("students.txt", "r") as file:
        value = file.read()
except:
    print("File not found!")
else:
    print(value)

# Q.no.: 3
try:
    number = int(input("Enter a number bro: "))
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Program finished.")