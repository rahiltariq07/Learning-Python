# 1. IF-ELSE (Decision Making)
# if-else helps Python make decisions

#  eg:
age = 23
# int(input("Enter your age: "))

if (age > 18):
    print("Your are an adult")
elif (age < 18):
    print("You are a minor")
else:
    print("You are exactly 18 years old")

# 2. Comparison Operator
# | Operator | Meaning          |
# | -------- | ---------------- |
# | ==       | equal            |
# | !=       | not equal        |
# | >        | greater          |
# | <        | smaller          |
# | >=       | greater or equal |
# | <=       | smaller or equal |

# 3. Logical Operators
# | Operator | Meaning                      |
# | -------- | ---------------------------- |
# | and      | both conditions must be true |
# | or       | any one condition true       |
# | not      | reverses the value           |
age = 61

if age >= 18 and age <= 60:
    print("Working age")
else:
    print("Retired")

# 4. FOR LOOP
# Repeat something fixed number of times
for i in range(5, 0, -2):
    print(i)

# Looping through a list
names = ["Rahil", "Amaan", "Aisha"]
for n in names:
    print(n)

# 5. WHILE LOOP
count = 1

while count <=5:
    print(count)
    count += 1

# 6. Break & Continue
# Break
for i in range(10):
    if(i == 7):
        break
    print(i)

# Continue
for i in range(6):
    if i == 3:
        continue
    print(i)

# Practice Questions
# Q.no. 1:
for i in range(50):
    if(i % 5 == 0):
        continue
    elif(i == 37):
        break
    print(i)

