def common_words(s1, s2):
    s1 = s1.lower().split()
    s2 = s2.lower().split()

    common_words = []
    for word in s2:
        if word in s1 and word not in common_words:
            common_words.append(word)

    return common_words


s1 = input()
s2 = input()

res = common_words(s1, s2)
print(*res)
