def findDuplicates(arr):
    count = {}
    result = []
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num in count:
        if count[num] == 2:
            result.append(num)
    return result

# Example usage:
print(findDuplicates([2, 3, 1, 2, 3]))  # Output: [2, 3]
print(findDuplicates([3, 1, 2]))        # Output: []
