def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
n = int(input())
lst = []
for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)
non_primes = lst.copy()
for j in lst:
    if isPrime(j):
        non_primes.remove(j)
print(len(non_primes))
