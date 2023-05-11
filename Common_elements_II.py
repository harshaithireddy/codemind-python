n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

uncommon = []
for i in A:
    if i not in B:
        uncommon.append(i)
for j in B:
    if j not in A:
        uncommon.append(j)
print(*uncommon)
