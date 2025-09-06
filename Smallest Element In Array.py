def firstAndSecondSmallest(arr):
    arr = sorted(set(arr))   # remove duplicates and sort
    return [arr[0], arr[1]] if len(arr) > 1 else [-1]

# 🔹 Take input from user
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

print(firstAndSecondSmallest(arr))
