n = int(input())
a = list(map(int, input().split()))
total = 0
for i in a:
    num_str = str(i)
    for digit in num_str:
        total += int(digit)
        
print(total)