def find_missing_number(arr):
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)

# Example usage
print(find_missing_number([1, 2, 3, 5]))        # 4
print(find_missing_number([8, 2, 4, 5, 3, 7, 1]))  # 6
print(find_missing_number([1]))                # 2
