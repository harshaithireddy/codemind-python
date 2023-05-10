a, b = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

lst = []
for i in arr1:
    for j in arr2:
        if i == j:
            lst.append(i)
new_list = []
for i in lst:
    if i not in new_list:
        new_list.append(i)
print(*new_list)