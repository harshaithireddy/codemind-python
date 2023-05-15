s = input()

cnt = 0
for i in s:
    if i.isdigit():
        cnt += 1
        
if cnt == 0:
    print("Doesn't contain digit")
else:
    print(f'Contains {cnt} digit')