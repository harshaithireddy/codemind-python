def self_dividing(n):
    str_n = str(n)
    flag = True
    if n % 10 == 0:
        flag = False
        return
    for i in str_n:
        if n % int(i) != 0:
            flag = False
    return flag
    
a = int(input())
b = int(input())
for i in range(a, b+1):
    if self_dividing(i):
        print(i, end = " ")