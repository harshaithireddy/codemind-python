def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    for i in alphabet:
        if i not in s:
            return False
    return True

s = input()

res = is_pangram(s)
print(res)
