def find_rotation_count(arr):
    # The number of rotations is the index of the minimum element
    min_val = arr[0]
    min_idx = 0
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
    
    return min_idx


# Example usage
print(find_rotation_count([5, 1, 2, 3, 4]))  # Output: 1
print(find_rotation_count([1, 2, 3, 4, 5]))  # Output: 0
print(find_rotation_count([6, 9, 2, 4]))     # Output: 2
