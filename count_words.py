def count_words(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    
    count = 0
    words = s.split()

    for i in words:
        if i[0].lower() in vowels and i[-1].lower() in consonants:
            count += 1

    return count
    
    
s = input()

result = count_words(s)
print(result)
