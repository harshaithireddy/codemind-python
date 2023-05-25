n = int(input())
str_n = str(n)

sum1 = 0
pro = 1
for i in str_n:
    sum1 += int(i)
    pro *= int(i)
print(abs(sum1 - pro))