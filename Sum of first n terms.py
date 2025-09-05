def sum_of_cubes(n):
    # Using formula: (n*(n+1)//2) ** 2
    return (n * (n + 1) // 2) ** 2

# Driver code
n = int(input("Enter n: "))
print(sum_of_cubes(n))
