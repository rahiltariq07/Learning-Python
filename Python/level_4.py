# LISTS & TUPLES
# These two are very important because they store multiple values.

# 1. ***Lists***(Changeable Collection)
# A list is like a bag that can hold many items.
# You can add, remove, or change items

names = ["Rahil", "Ali", "Aisha"]
numbers = [1, 2, 3, 4, 5]
mixed = [23, "Rahil", True]

# 2. Accessing Items
# Lists use indexes (positions).
# Index starts from 0.

print(names[0]) # Rahil
print(names[1]) # Ali
print(names[2]) # Aisha

# 3. Changing List Items
numbers[1] = 20
print(numbers)

# 4. Adding Items to List
# append() -> adds at end
names.append("Raheek")
print(names)

# insert(index, value) -> add at specific position
names.insert(0, "Mohammad")
print(names)

# 5. Remove Items
# remove(value)
names.remove("Mohammad")
print(names)

# pop(index)
names.pop(1) # If no index -> removes last item.
print(names)

# 6. Looping Through a List
for n in names:
    print(n)

# 7. List Length
length = len(names)
print(length)

# 8. Slicing Lists
# Used to get parts of a list
nums = [10, 20, 30, 40, 50]

print(nums[1:4])
print(nums[:3])
print(nums[2:])

# 9. ***TUPLES*** (List but cannot change)
# A tuple is like a list, but you can't modify it.
# It is fixed

colors = ("red", "green", "black")
print(colors[1])
# Tuples are faster and safe because they cannot be changed

## ⭐ Differences Between List & Tuple
# | Feature  | List         | Tuple                 |
# | -------- | ------------ | --------------------- |
# | Editable | Yes          | No                    |
# | Syntax   | `[]`         | `()`                  |
# | Speed    | Slower       | Faster                |
# | Use when | Data changes | Data should stay same |


# Practice Questions
# Q.no.: 1
fruits = ["apple", "banana", "kiwi", "orange", "melon"]
print(fruits[0])
print(fruits[-1])

# Q.no.: 2
ints = [1, 2, 3, 4, 5]
ints.append(6)
ints.pop(3)

print(ints)

# Q.no.: 3
cities = ("Srinagar", "Delhi", "Mumbai", "Rajasthan", "Hyderabad")

for c in cities:
    print(f"City name: {c}")