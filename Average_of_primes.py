def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
n = int(input())
a = map(int, input().split())
lst = []
for i in a:
    if isPrime(i):
        lst.append(i)
avg = sum(lst) / len(lst)
print("%.2f"%avg)