def plus_one(a):
    n = len(a)
    carry = 1

    for i in range(n-1, -1, -1):
        sum = a[i] + carry
        a[i] = sum % 10
        carry = sum // 10
        
    if carry == 1:
        a.insert(0, 1)
        
    return a

n = int(input())
a = list(map(int, input().split()))

print(*plus_one(a))