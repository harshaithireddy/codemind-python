def reverseInteger(x):

    is_negative = False
    if x < 0:
        is_negative = True
        x = abs(x)

    reverse = 0
    while x > 0:
        reverse = reverse * 10 + x % 10
        x //= 10

    if reverse > 2**31 - 1:
        return 0

    return -reverse if is_negative else reverse


x = int(input())

reversed_int = reverseInteger(x)
print(reversed_int)
