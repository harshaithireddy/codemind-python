from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

counter = Counter(arr)
super_elements = []
for i, count in counter.items():
    if i == count:
        super_elements.append(i)

if not super_elements:
    print(-1)
else:
    average = sum(super_elements) / len(super_elements)
    print("%.2f"%average)