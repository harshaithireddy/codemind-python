n = int(input())
a = list(map(int, input().split()))
num = n // 2

if n % 2 == 0:
    sum1, sum2 = 0, 0
    for i in range(num):
        sum1 += a[i] 
    for i in range(num, n):
        sum2 += a[i]
else:
    sum1, sum2 = 0, 0
    for i in range(0, num + 1):
        sum1 += i
    for j in range(num, n):
        sum2 += a[j]
print(sum1)
print(sum2)