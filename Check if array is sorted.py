def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:  # if current element > next element
            return False
    return True


# Example usage
arr1 = [10, 20, 30, 40, 50]
arr2 = [90, 80, 100, 70, 40, 30]

print(is_sorted(arr1))  # True
print(is_sorted(arr2))  # False
