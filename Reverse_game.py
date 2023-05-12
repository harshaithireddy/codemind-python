def rev(a):
    str_a = str(a)
    res = str_a[::-1]
    return int(res)

n = int(input())
a = list(map(int, input().split()))
for i in a:
    print(rev(i), end = " ")
    