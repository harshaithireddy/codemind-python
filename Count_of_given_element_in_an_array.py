n = int(input())
a = list(map(int, input().split()))
key = int(input())

count = 0
for i in a:
    if i == key:
        count += 1
print(count)