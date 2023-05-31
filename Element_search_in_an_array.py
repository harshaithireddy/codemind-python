n = int(input())
a = map(int, input().split())
key = int(input())
flag = False
for i in a:
    if i == key:
        flag = True
        break
print(flag)