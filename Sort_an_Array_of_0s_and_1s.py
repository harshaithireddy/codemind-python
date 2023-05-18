def zeros_ones(n, arr):
    left = 0
    right = n - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
            
        while arr[right] == 1 and left < right:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    return arr

n = int(input())
arr = list(map(int, input().split()))

result = zeros_ones(n, arr)
print(*result)
