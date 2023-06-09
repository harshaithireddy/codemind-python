def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
arr = map(int, input().split())
a = int(input())
cnt = 0
for i in arr:
    if isPrime(i):
        if i <= a:
            cnt += 1
print(cnt)