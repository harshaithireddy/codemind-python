import math

def isPerfectSquare(num):
    sqrt = math.isqrt(num)
    return sqrt * sqrt == num

n = int(input())
l = list(map(int, input().split()))

res = 0
for i in l:
    if isPerfectSquare(i):
        res += i
        
print(res)