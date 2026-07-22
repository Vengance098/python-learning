# --- Tests for equality and inequality with strings ---
car = 'audi'
print("car == 'audi':", car == 'audi')       # True
print("car == 'bmw':", car == 'bmw')         # False
print("car != 'bmw':", car != 'bmw')         # True
print("car != 'audi':", car != 'audi')       # False

# --- Tests using the lower() method ---
name = 'Eric'
print("name.lower() == 'eric':", name.lower() == 'eric')   # True
print("name.lower() == 'john':", name.lower() == 'john')   # False

# --- Numerical tests: equality, inequality, >, <, >=, <= ---
age = 18

print("age == 18:", age == 18)     # True
print("age == 21:", age == 21)     # False

print("age != 21:", age != 21)     # True
print("age != 18:", age != 18)     # False

print("age > 15:", age > 15)       # True
print("age > 20:", age > 20)       # False

print("age < 15:", age < 15)       # False
print("age < 20:", age < 20)       # True

print("age >= 18:", age >= 18)     # True
print("age >= 19:", age >= 19)     # False

print("age <= 18:", age <= 18)     # True
print("age <= 17:", age <= 17)     # False

# --- Tests using the 'and' keyword ---
age_0 = 22
age_1 = 18
print("age_0 >= 21 and age_1 >= 21:", age_0 >= 21 and age_1 >= 21)  # False
age_1 = 22
print("age_0 >= 21 and age_1 >= 21:", age_0 >= 21 and age_1 >= 21)  # True

# --- Tests using the 'or' keyword ---
age_0 = 22
age_1 = 18
print("age_0 >= 21 or age_1 >= 21:", age_0 >= 21 or age_1 >= 21)  # True
age_0 = 18
print("age_0 >= 21 or age_1 >= 21:", age_0 >= 21 or age_1 >= 21)  # False

# --- Test whether an item is in a list ---
fruits = ['apple', 'banana', 'cherry']
print("'apple' in fruits:", 'apple' in fruits)     # True
print("'mango' in fruits:", 'mango' in fruits)     # False

# --- Test whether an item is not in a list ---
print("'mango' not in fruits:", 'mango' not in fruits)   # True
print("'apple' not in fruits:", 'apple' not in fruits)   # False