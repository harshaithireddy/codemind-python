def isPrime(n):
    if n < 2:
        return False
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def megaPrime(n):
    strn = str(n)
    cnt = 0
    for i in range(len(strn)):
        if isPrime(int(strn[i])):
            cnt += 1
    if cnt == len(strn):
        return True
    return False


n = int(input())
if isPrime(n) and megaPrime(n):
    print("Mega Prime")
else:
    print("Not Mega Prime")