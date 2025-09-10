arr = list(map(int, input().split()))

if len(arr) < 3:
    print(-1)
else:
    arr.sort(reverse=True)
    print(arr[2])
