

def print_pattern(n: int):
    for i in range(1, n + 1):
        print("*" * i)

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print_pattern(n)
