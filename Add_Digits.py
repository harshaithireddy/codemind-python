def add_digits(n):
    while n > 9:
        sum1 = 0
        while n > 0:
            sum1 += n % 10
            n //= 10
        n = sum1
    return n

n = int(input())
res = add_digits(n)
print(res)