n = int(input())
a = list(map(int, input().split()))

even_count = 0
odd_count = 0

for i in a:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count, odd_count)