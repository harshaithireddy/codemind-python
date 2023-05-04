def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(2, n):
    if n % i == 0:
        j = n // i
        if is_prime(i) and is_prime(j) and i != j:
            print(i, j)
            break
else:
    print("-1")
