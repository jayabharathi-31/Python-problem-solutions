def count_divisors_divisible_by_3(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 3 == 0:   # i is a divisor AND divisible by 3
            count += 1
    return count

# Driver code
n = int(input("Enter n: "))
print(count_divisors_divisible_by_3(n))
