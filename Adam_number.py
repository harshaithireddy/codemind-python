n = int(input())
sq = n * n
str_n = str(n)
rev_n = str_n[::-1]
sq_rev = str(int(rev_n) * int(rev_n))

print(sq == int(sq_rev[::-1]))