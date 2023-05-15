s = input()
a = input()

cnt = 0
for i in s:
    if i == a:
        cnt += 1
if cnt == 0:
    print(-1)
else:
    print(cnt)