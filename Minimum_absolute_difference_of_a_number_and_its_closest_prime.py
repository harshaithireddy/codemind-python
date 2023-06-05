def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def closestprimediff(n):
    if isprime(n):
        return 0
    else:
        i = n + 1
        while True:
            if isprime(i):
                break
            i += 1
        j = n - 1
        while True:
            if isprime(j):
                break
            j -= 1
        return min(abs(n-i), abs(n-j))


n = int(input())
print(closestprimediff(n))