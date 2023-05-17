def find_min_max(s):
    words = s.split()
    min_max_pairs = []

    for word in words:
        min_char = min(word)
        max_char = max(word)
        min_max_pairs.append(min_char + " " + max_char)

    return " ".join(min_max_pairs)

s = input()

res = find_min_max(s)
print(res)
