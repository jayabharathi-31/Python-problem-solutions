def reverse_digits(n):
    rev = 0
    while n > 0:
        digit = n % 10       # get last digit
        rev = rev * 10 + digit  # build reversed number
        n //= 10             # remove last digit
    return rev

# Driver code
n = int(input("Enter n: "))
print(reverse_digits(n))
