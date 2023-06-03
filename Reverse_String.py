def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


input_str = list(input())
reverse_string(input_str)
reversed_str = ''.join(input_str)

print(reversed_str)