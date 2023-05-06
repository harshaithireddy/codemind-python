def isPrime(num):
    if num < 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def product(lst):
    pro = 1
    for i in lst:
        pro *= i
    return pro

n = int(input())
a = list(map(int, input().split()))
prime_list = []
non_prime = []
for i in a:
    if isPrime(i):
        prime_list.append(i)
    else:
        non_prime.append(i)

print(abs(product(prime_list) - product(non_prime)))
