def isPal(a):
    str_a = str(a)
    rev = str_a[::-1]
    if a == int(rev):
        return True
    return False

n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    if isPal(i):
        cnt += 1
print(cnt)