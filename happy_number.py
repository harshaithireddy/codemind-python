def is_happy_number(n):
    while n != 1 and n != 4:
        digit_sum = 0
        while n > 0:
            digit = n % 10
            digit_sum += digit * digit
            n //= 10
        n = digit_sum
    return n == 1 or n == 7

n = int(input())
print(is_happy_number(n))