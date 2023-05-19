def common_words(s1, s2):
    s1 = s1.lower().split()
    s2 = s2.lower().split()
    cnt = 0
    for i in s1:
        if i in s2:
            cnt += 1
    return cnt
    
s1 = input()
s2 = input()

res = common_words(s1, s2)
print(res)