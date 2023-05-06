length = int(input())
a = list(map(int, input().split()))
n = int(input())

lst = []
max_a = max(a)
for i in range(length):
    if a[i] + n >= max_a:
        lst.append(True)
    else:
        lst.append(False)
        
for i in lst:
    print(i, end = " ")