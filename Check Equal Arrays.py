def are_arrays_equal(a, b):
    return sorted(a) == sorted(b)

# Example usage
print(are_arrays_equal([1, 2, 5, 4, 0], [2, 4, 5, 0, 1]))  # True
print(are_arrays_equal([1, 2, 5], [2, 4, 15]))  # False
