n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in a:
    if i % 2 == 0 or i == 0:
        cnt += 1
print(cnt == len(a))