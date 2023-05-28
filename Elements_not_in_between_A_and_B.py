n = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())

new_lst = [x for x in lst if x < a or x > b]
if len(new_lst) == 0:
    print("-1")
else:
    print(*new_lst)