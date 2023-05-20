n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(ord('A') + i-1), end = " ")
    print()