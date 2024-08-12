#           0      1       2
people = ['jas', 'veer', 'mann']
print(people)
# integer
numbers = [1, 2, 3, 4, 5]
print(numbers)
# Different type of data in single list
items = ['Computer', 10, 4.5, True, 'Mouse', 5.6]
print(items)
a = [1, 2]
b = [2, 1]
print(a == b)
# negative indexing
fruits = ['apple', 'mango', 'peach', 'orange', 'watermelon', 'grape']
# +ve        0        1         2       3           4            5
# -ve        -6       -5        -4      -3          -2            -1
print(fruits[-5])
# List Slicing
print(fruits[2:5])
print(fruits[3:])
print(fruits[-5:-1])
print(fruits[-5:])

# in and not in operators
print('peach' in fruits)

print('pineapple' not in fruits)

# List Functions
# Length
print(len(fruits))

# insert
fruits.insert(1,"pineapple")

# Append
fruits.append("Test")
fruits.append(["guava", "apricot"])
print(fruits)

# extend
fruits.extend(["guava", "apricot"])
print(fruits)

# Remove
fruits.remove("Test")
print(fruits)

# pop
fruits.pop()
print(fruits)

# Min and Max
scores = [1, 2, 3, 4, 5, 6, 50, 36]
print(max(scores))
print(min(scores))
