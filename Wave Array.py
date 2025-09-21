def wave_sort(arr):
    n = len(arr)
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Examples
arr1 = [1, 2, 3, 4, 5]
wave_sort(arr1)
print(arr1)  # Output: [2, 1, 4, 3, 5]

arr2 = [2, 4, 7, 8, 9, 10]
wave_sort(arr2)
print(arr2)  # Output: [4, 2, 8, 7, 10, 9]

arr3 = [1]
wave_sort(arr3)
print(arr3)  # Output: [1]
