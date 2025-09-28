def aggressive_cows(stalls, k):
    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0]
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        count, last_pos = 1, stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= mid:
                count += 1
                last_pos = stalls[i]

        if count >= k:  # can place cows
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


# Example usage
print(aggressive_cows([1, 2, 4, 8, 9], 3))  # Output: 3
print(aggressive_cows([10, 1, 2, 7, 5], 3)) # Output: 4
