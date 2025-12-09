# DICTIONARIES & SETS
# Used in real-world applications

# 1. What is a ***Dictionary***?
# A dictionary stores data in key–value pairs.
# Think of it like storing information in this format:
# word → meaning  
# name → age  
# roll_number → student_details

# eg:
student = {
    "name": "Rahil",
    "age": 23,
    "city": "Srinagar"
}

print(student)

# Here:
# | Key    | Value    |
# | ------ | -------- |
# | "name" | "Rahil"  |
# | "age"  | 25       |
# | "city" | "Mumbai" |

# 2. Accessing Dictionary Values
print(student["name"])   # Rahil
print(student["age"])    # 23

# 3. Adding New Key-Value Pair
student["course"] = "Python"

# 4. Changing Existing Value
student["age"] = 24 # in feb-2026

# 5. Removing a Key
student.pop("age")

# 6. Loop Through Dictionary
# Loop only Keys
for key in student:
    print(key)

# Loop keys + values
for key, value in student.items():
    print(f"{key}: {value}")

# 7. Useful Dictionary Functions
# | Function   | Meaning      |
# | ---------- | ------------ |
# |  keys()    | all keys     |
# |  values()  | all values   |
# |  items()   | key + value  |
# |  pop(key)  | remove a key |

print(student.keys())
print(student.values())
print(student.items())

# 8. ***SETS***
# A set is a collection of unique values (no duplicates).
# eg:
nums = {1, 2, 3, 4, 4}
print(nums) # 1, 2, 3, 4

# 9. Set Properties
# ✔ No duplicate values
# ✔ Order is not guaranteed
# ✔ Very fast for checking existence

# 10. Adding to a Set
nums.add(5)

# 11. Removing from a Set
nums.remove(4) # elements, not an index
print(nums)

# 12. Set Operations (Important)
# Union (combine both)
a = {1, 2}
b = {2, 3}

print(a | b) # {1, 2, 3}

# Intersection (common)
print(a & b)


## Practice Questions
# Q.no.: 1
student = {
    "name": "Rahil",
    "age": 23,
    "grade": 'A'
}

print(student["name"])

# Q.no.: 2
products = {
    "Roti": 7,
    "Jam": 2,
    "Milk": 17
}

products["Butter"] = 10
products["Jam"] = 3
products.pop("Milk")

print(products)

# Q.no.: 3
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print(set1 | set2)
print(set1 & set2)

print(set1 - set2)