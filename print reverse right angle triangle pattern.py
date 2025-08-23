

def print_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print_pattern(n)
