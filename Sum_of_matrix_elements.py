M = int(input())
N = int(input())

matrix = []
for i in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_of_elements = 0
for i in range(M):
    for j in range(N):
        sum_of_elements += matrix[i][j]

print(sum_of_elements)
