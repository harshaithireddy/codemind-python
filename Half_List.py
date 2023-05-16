n = int(input())
lst = list(map(int, input().split()))

res1 = lst[:(n//2) - 1:-1]
res2 = lst[:n//2:]
print(*(res1 + res2))