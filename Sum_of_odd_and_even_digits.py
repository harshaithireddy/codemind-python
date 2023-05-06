n = int(input())
a = list(map(int, input().split()))
osum, esum = 0, 0
for i in range(n):
    if i % 2 == 1:
        osum += a[i]
    else:
        esum += a[i]

if osum - esum == 0:
    print("YES")
else:
    print("NO")