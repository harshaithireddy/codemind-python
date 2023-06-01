n = int(input())
a = map(int, input().split())
even_sum, odd_sum = 0, 0
for i in a:
    if i % 2 == 0:
        even_sum += i
    elif i % 2 == 1:
        odd_sum += i
print(abs(even_sum - odd_sum))