col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))
                  
for i in range(col):
    for j in range(row):
        if matrix[i][j] == '.':
            matrix[i][j] = 0
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if k < 0 or k >= col or l < 0 or l >= row:
                        continue
                    elif matrix[k][l] == '*':
                        matrix[i][j] += 1
        print(matrix[i][j], end='')    
    print()
