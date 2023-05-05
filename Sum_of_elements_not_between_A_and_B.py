n = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())

new_lst = [x for x in lst if x < a or x > b]
print(sum(new_lst))