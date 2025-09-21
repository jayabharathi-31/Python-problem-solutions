def move_negatives_to_end(arr):
    n = len(arr)
    negatives = []

    # First pass: move positives to front
    j = 0
    for i in range(n):
        if arr[i] >= 0:
            arr[j] = arr[i]
            j += 1
        else:
            negatives.append(arr[i])  # store negatives temporarily

    # Place negatives at the end
    for neg in negatives:
        arr[j] = neg
        j += 1

# Example usage
arr = [-5, 7, -3, -4, 9, 10, -1, 11]
move_negatives_to_end(arr)
print(arr)
