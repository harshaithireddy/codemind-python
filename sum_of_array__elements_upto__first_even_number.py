n = int(input())
a = list(map(int, input().split()))
lst = []
for i in a:
    if i % 2 == 1:
        lst.append(i)
    if i % 2 == 0:
        break
print(sum(lst))