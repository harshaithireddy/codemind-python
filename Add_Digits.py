def add_digits(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9


num = int(input())
result = add_digits(num)
print(result)
