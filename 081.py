matrix = []
with open('p081_matrix.txt') as file:
    for l in file:
        matrix.append([int(n) for n in l.split(',')])


n = len(matrix)
for i in reversed(range(n-1)):
    matrix[i][-1] += matrix[i+1][-1]
    matrix[-1][i] += matrix[-1][i+1]

for r in reversed(range(n-1)):
    for c in reversed(range(n-1)):
        matrix[r][c] += min(matrix[r+1][c], matrix[r][c+1])

total = matrix[0][0]
