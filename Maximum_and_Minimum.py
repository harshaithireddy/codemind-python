from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

counter = Counter(arr)
super_elements = []
for num, count in counter.items():
    if num == count:
        super_elements.append(num)

if not super_elements:
    print(-1)
else:
    print(min(super_elements), max(super_elements))