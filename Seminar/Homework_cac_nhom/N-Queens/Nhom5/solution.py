result = []

 
def isSafe(board, row, col, n):
 
    for i in range(col):
        if (board[row][i]):
            return False
 
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return False
        i -= 1
        j -= 1
 
    i = row
    j = col
    while j >= 0 and i < n:
        if(board[i][j]):
            return False
        i = i + 1
        j = j - 1
 
    return True

 
def solveNQUtil(board, col, n):

    if (col == n):
        v = []
        for i in board:
            for j in range(len(i)):
                if i[j] == 1:
                    v.append(j+1)
        result.append(v)
        return True

    res = False
    for i in range(n):

        if (isSafe(board, i, col, n)):
 
            board[i][col] = 1
 
            res = solveNQUtil(board, col + 1, n) or res
 
            board[i][col] = 0 
 
    return res
 
 
 
def solveNQ(n):
    result.clear()
    board = [[0 for j in range(n)]
             for i in range(n)]
    solveNQUtil(board, 0, n)
    result.sort()
    return result
 

n = int(input())
res = solveNQ(n)
print(len(res))