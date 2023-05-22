n = int(input())
str_n = str(n)

lst = []
for i in range(len(str_n)):
    lst.append(int(str_n[i]))
    
print(max(lst))