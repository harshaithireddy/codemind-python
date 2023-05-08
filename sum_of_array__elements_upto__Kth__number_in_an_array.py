n = int(input())
a = list(map(int, input().split()))
num = int(input())
sum = 0
for i in range(0, num):
    sum += a[i]
print(sum)