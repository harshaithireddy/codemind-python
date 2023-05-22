n = int(input())
str_n = str(n)

res = 0
for i in range(len(str_n)):
    res += int(str_n[i]) ** (i + 1)

print(n == res)