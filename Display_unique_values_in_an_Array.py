n = int(input())
a = list(map(int, input().split()))
lst = []
for i in a:
    if a.count(i) == 1:
        lst.append(i)
        
if len(lst) == 0:
    print("-1")
else:
    for i in lst:
        print(i, end = " ")
    