def is_fibonacci(n):
    a = 0
    b = 1

    while b <= n:
        if b == n:
            return True
        a, b = b, a + b

    return False


n = int(input())
print(is_fibonacci(n))
