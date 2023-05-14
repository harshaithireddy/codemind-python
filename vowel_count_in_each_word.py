s = input().split()
vowels = 'aeiou'

lst = []
for i in s:
    cnt = 0
    for j in i:
        if j in vowels:
            cnt += 1
    lst.append(cnt)
    
print(*lst)
        