def is_possible(arr, k, mid):
    painters = 1
    time = 0
    for board in arr:
        if board > mid:
            return False
        if time + board > mid:
            painters += 1
            time = board
        else:
            time += board
    return painters <= k

def min_time_to_paint(arr, k):
    low = max(arr)
    high = sum(arr)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(arr, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

# Example usage:
arr = [5,10,30,20,15]
k = 3
print(min_time_to_paint(arr, k))  # Output: 35
