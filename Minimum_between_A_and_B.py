n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

min_arr = []
for i in arr:
    if a <= i <= b:
        min_arr.append(i)

if len(min_arr) == 0:
    print("-1")
else:
    min_num = min(min_arr)
    print(min_num)