def factorial(n):
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    return fact
    
n = int(input())
str_n = str(n)
sum1 = 0
for i in str_n:
    sum1 += factorial(int(i))

if n == sum1:
    print(f'The number {n} is a strong number')
else:
    print(f'The number {n} is not a strong number')