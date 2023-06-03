def slice_string(string, start, end):
    return string[start:end]


string = input()
start = int(input())
end = int(input())

slice_str = slice_string(string, start, end+1)
print(slice_str)