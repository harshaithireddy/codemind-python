n = int(input())

factors = 0
for i in range(1, n):
    if n % i == 0:
        factors += i

print(factors > n)