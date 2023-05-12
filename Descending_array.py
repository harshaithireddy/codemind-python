n = int(input())
a = list(map(int, input().split()))
des = True
for i in range(len(a) - 1):
    if a[i] < a[i+1]:
        des = False
        break
if des:
    print("yes")
else:
    print("no")