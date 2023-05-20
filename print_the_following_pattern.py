n = int(input())

for i in range(n):
    for j in range(n):
        print(chr(ord('A') + i), end = " ")
    print()