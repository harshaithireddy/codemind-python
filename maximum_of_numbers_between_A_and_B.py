n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

max_arr = []
for i in arr:
    if a <= i <= b:
        max_arr.append(i)

if len(max_arr) == 0:
    print("-1")
else:
    max_num = max(max_arr)
    print(max_num)