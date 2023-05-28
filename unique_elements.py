n = int(input())
arr = list(map(int, input().split()))

unique_elements = []

for i in arr:
    if i not in unique_elements:
        unique_elements.append(i)

for i in unique_elements:
    print(i, end=" ")