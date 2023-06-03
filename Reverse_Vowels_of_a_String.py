def reverse_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowels:
            right -= 1
        elif s[right] in vowels:
            left += 1
        else:
            left += 1
            right -= 1

    return ''.join(s)


input_str = input().strip()
reversed_vowels_str = reverse_vowels(input_str)
print(reversed_vowels_str)