a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in set(A):
    if i in set(B):
        cnt += 1
print(cnt)