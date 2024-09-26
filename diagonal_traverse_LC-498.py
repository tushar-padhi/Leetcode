
def diagonaltraverse(matrix):
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    columns = len(matrix[0])
    diagonals = [[] for _ in range(rows + columns - 1)]
    
    res = diagonals[0]
    for i in range(rows):
        for j in range(columns):
            diagonals[i+j].append(matrix[i][j])
    
    for i in range(1, len(diagonals)):
        if i % 2 == 1:
            res.extend(diagonals[i])
        else:
            res.extend(diagonals[i][::-1])
    
    return res
            


matrix = [[1]]
print(diagonaltraverse(matrix))