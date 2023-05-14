s = input().lower()
vowels = "aeiou"
count = 0

for i in s:
    if i in vowels:
        count += 1
        
print(count)