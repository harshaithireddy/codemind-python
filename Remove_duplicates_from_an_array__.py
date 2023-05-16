n = int(input())
l = list(map(int, input().split()))

lst = []
for i in l:
    if i not in lst:
        lst.append(i)
        
print(*lst)