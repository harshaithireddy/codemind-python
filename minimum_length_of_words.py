n = input().split()
lst = []
for i in n:
    lst.append(len(i))
print(min(lst))