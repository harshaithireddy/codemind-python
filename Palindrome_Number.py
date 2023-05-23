def isPal(n):
    str_n = str(n)
    rev = str_n[::-1]
    
    return n == int(rev)

t = int(input())
for _ in range(t):
    n = int(input())
    print(isPal(n))
    