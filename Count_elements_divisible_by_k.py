n, k = map(int, input().split())
a = list(map(int, input().split()))
lst = []
for i in a:
    if i % k == 0:
        lst.append(i)
print(len(lst))