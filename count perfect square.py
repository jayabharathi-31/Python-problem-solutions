import math

def countSquares(n):
    # largest integer whose square is < n
    return int(math.isqrt(n - 1))

# Driver code
n = int(input("Enter n: "))
print(countSquares(n))
