# File Handling (Reading & Writing Files)
# It allows your program to save data, read data, and create files

# 1. What is File Handling?
#Your Python program can:
# ✔ Create a file
# ✔ Write data into a file
# ✔ Read data from a file
# ✔ Update the file

# Common file types:
# .txt (text)
# .csv
# .json

# 2.Opening a File
# Python uses open() function.
# open("filename", "mode")

# Modes:
# | Mode  | Meaning                                       |
# | ----- | --------------------------------------------- |
# | `"r"` | read (file must exist)                        |
# | `"w"` | write (creates new OR clears existing)        |
# | `"a"` | append (add to end without deleting old data) |

# 3. Writing to a File
file = open("data.txt", "w")
file.write("Hello, this is a test file!")
file.close()
# This will create a file named data.txt and write the text.

# 4. Appending to a file
file = open("data.txt", "a")
file.write("\nThis line is added later")
file.close()
# "a" will NOT delete old content.

# 5. Reading a File
# Method 1: read entire file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Method 2: read line by line
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()

# 6. Best Practice: Using **with open()**
# This automatically closes the file.
with open("nachan.txt", "w") as file:
    file.write("Kyasa")

with open("nachan.txt", "a") as file:
    file.write("\nbas ha yaare")

with open("nachan.txt", "r") as file:
    content = file.read()
    print(content)

with open("nachan.txt", "r") as file:
    for line in file:
        print(line)

# 7. Writing multiple lines
lines  = ["\nRahil\n", "Ali\n", "Aisha\n"]

with open("nachan.txt", "a") as file:
    file.writelines(lines)

# 8. Check if file exists (optional knowledge)
import os

if os.path.exists("nachan.txt"):
    print("file exists")
else:
    print("file not found")


## Practice Questions:
# Q.no.: 1
with open("info.txt", "w") as file:
    file.write("Hello, I am learning Python")

# Q.no.: 2
with open("info.txt", "a") as file:
    file.write("\nPython file handling is easy.")

with open("info.txt", "r") as file:
    print(file.read())

with open("info.txt", "r") as file:
    for line in file:
        print(line)

# Q.no.: 3
students = ["Rahil\n", "Ali\n", "Aisha\n"]
with open("students.txt", "w") as file:
    file.writelines(students)

with open("students.txt", "r") as file:
    print(file.readlines())

with open("students.txt", "r") as file:
    for name in file:
        print(name.strip().upper())