def getMinMax(arr):
    return [min(arr), max(arr)] if arr else []

# take input from user
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

print(getMinMax(arr))
