n = int(input())
arr = list(map(int, input().split()))
k = int(input())

count_dict = {}
for num in arr:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

result = []
for num, count in count_dict.items():
    if count == k:
        result.append(num)

if not result:
    print("-1")
else:
    print(*result)