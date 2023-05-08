n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

filtered_arr = []
for i in arr:
    if a <= i <= b:
        filtered_arr.append(i)

if len(filtered_arr) == 0:
    print("-1")
else:
    print(*filtered_arr)