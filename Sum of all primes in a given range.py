def prime_sum_in_range(L, R):
    primes = [True] * (R + 1)
    primes[0] = primes[1] = False

    # Simple Sieve
    for i in range(2, int(R ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, R + 1, i):
                primes[j] = False

    # Sum primes in range
    return sum(i for i in range(L, R + 1) if primes[i])


# Example
print(prime_sum_in_range(10, 20))  # 60
print(prime_sum_in_range(15, 25))  # 59
 
