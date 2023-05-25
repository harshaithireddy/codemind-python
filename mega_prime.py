def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

def isMegaPrime(n):
    if not isPrime(n):
        return False
    for digit in str(n):
        if not isPrime(int(digit)):
            return False
    return True
    
    
n = int(input())
if isMegaPrime(n):
    print("Mega Prime")
else:
    print("Not Mega Prime")