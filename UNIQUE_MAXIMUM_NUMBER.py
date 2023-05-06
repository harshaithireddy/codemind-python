n = int(input())
a = list(map(int, input().split()))
unique = []
for i in a:
    if a.count(i) == 1:
        unique.append(i)
  
if len(unique) == 0:
    print("-1")
else:
    print(max(unique))