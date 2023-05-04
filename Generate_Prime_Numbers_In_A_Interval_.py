def isPrime(n):
    if n < 2:
        return False
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a = int(input())
b = int(input())
for i in range (a, b):
    if isPrime(i):
        print(i)