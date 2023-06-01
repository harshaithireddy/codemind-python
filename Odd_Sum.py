t = int(input())
a = map(int, input().split())
sum = 0
for j in a:
    if j % 2 == 1:
        sum += j
print(sum)