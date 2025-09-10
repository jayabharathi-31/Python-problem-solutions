def divisors(n, i=1):
    if i > n:
        return
    if n % i == 0:
        print(i, end=" ")
    divisors(n, i + 1)

n = int(input())
divisors(n)
