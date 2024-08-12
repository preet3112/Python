# Adding and multiplication
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
print(a*4)

# Nesting lists
c = [1, 2, 3]
d = [1, 2, [3, 4, 5, [30, 40, 50]], 6, 7, 8, [9, 10]]

print(d[2][3][1])

# Mutability - Modify the content of the list
c[1] = 100
c[2] = 300
c[0:4] = [10, 20, 30]
print(c)
