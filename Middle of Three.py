def middle_of_three(a, b, c):
    # If a is between b and c
    if (a > b and a < c) or (a > c and a < b):
        return a
    # If b is between a and c
    elif (b > a and b < c) or (b > c and b < a):
        return b
    else:
        return c

# Driver code
a, b, c = map(int, input("Enter three distinct numbers (a b c): ").split())
print(middle_of_three(a, b, c))
