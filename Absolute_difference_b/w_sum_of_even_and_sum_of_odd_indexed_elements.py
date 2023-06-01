def even_sum(n, a):
    e_sum = 0
    for i in range(0, n, 2):
        e_sum += a[i]
    return(e_sum)
    
def odd_sum(n, a):
    o_sum = 0
    for i in range(1, n, 2):
        o_sum += a[i]
    return(o_sum)
    
n = int(input())
a = list(map(int, input().split()))
print(abs(even_sum(n, a) - odd_sum(n, a)))