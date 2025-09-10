def alternate_elements(arr):
    # Take every second element starting from index 0
    return arr[::2]

# Example usage:
arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 3, 4, 5]

print(alternate_elements(arr1))  # Output: [1, 3]
print(alternate_elements(arr2))  # Output: [1, 3, 5]
