n = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(0, n, 2):
    x = arr[i]
    y = arr[i+1]
    for j in range(y):
        result.append(x)

print(*result)