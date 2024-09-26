
def solve(board):
    rows = len(board)
    col = len(board[0])
    for i in range(1, rows):
        for j in range(1, col):
            if board[i][j] == board[i][j-1]:
                board[i][j].replace("O","X")
    
    return board
    
board = [["O","X","X"],["O","O","X"],["X","O","X"]]
print(solve(board))