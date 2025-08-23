def number_pattern(n):
    for i in range(n, 0, -1):   
        for j in range(i, 0, -1):  
            print(j, end="")
        print()  


if __name__ == "__main__":
    n = int(input("Enter n: "))
    number_pattern(n)
