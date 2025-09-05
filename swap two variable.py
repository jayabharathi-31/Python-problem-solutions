# Swapping two variables using a temporary variable

# Take input from user
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("Before swapping: a =", a, "b =", b)

# Step 1: store a in temp
temp = a

# Step 2: copy b into a
a = b

# Step 3: copy temp into b
b = temp

print("After swapping:  a =", a, "b =", b)
