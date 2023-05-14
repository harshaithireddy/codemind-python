s = input()
vowels = set('aeiou')
not_present = sorted(v for v in vowels if v not in s)
if not_present:
    print(*not_present)
else:
    print(0)
