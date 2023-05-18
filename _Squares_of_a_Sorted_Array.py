n = int(input())
a = list(map(int, input().split()))

sq = []
for i in a:
    sq.append(i * i)

res = sorted(sq)
print(*res)