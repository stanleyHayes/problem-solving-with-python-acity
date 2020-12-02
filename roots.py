# ax ** 2 + bx + c
# Take co-efficient of x2
a = float(input("Enter co-efficient of x2: "))
# Take co-efficient of x
b = float(input("Enter co-efficient of x: "))
# Take constant
c = float(input("Enter constant: "))

# calculate b**2 - 4 * a * c
d = (b ** 2) - (4 * a * c)

# Calculate value of x1
x1 = (-b + (d ** 0.5)) / (2 * a)

# Calculate value of x2
x2 = (-b - (d ** 0.5)) / (2 * a)

print(f"The roots of an equation with co-efficients a = {a}, b = {b} and c = {c} is\nx1 = {x1} and x2 = {x2}")