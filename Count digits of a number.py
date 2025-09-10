def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

# Example
n = int(input("Enter a number: "))
print(count_digits(n))
