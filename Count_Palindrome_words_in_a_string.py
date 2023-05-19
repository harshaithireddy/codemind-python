def is_pal(s):
    rev = s[::-1]
    return s == rev

s = input()
s = s.lower().split()

cnt = 0
for i in s:
    if is_pal(i):
        cnt += 1
print(cnt)