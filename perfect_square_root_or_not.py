import math

def is_perfect_square(n):
    sqrt = math.sqrt(n)
    return sqrt == int(sqrt)


n = int(input())
print(is_perfect_square(n))
