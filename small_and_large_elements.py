def min_max(s):
    words = s.split()
    first_word = words[0]
    last_word = words[-1] 

    min_element = min(first_word)
    max_element = max(last_word)

    return min_element + " " + max_element


s = input()

res = min_max(s)
print(res)
