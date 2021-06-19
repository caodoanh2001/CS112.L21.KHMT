def check(pos, puted_rows, col):
    for i in range(puted_rows):
        if pos[i] == col or \
            pos[i] - i == col - puted_rows or \
            pos[i] + i == col + puted_rows:
            return False
    return True

def put(pos, row, n):
    global result
    if row == n:
        result += 1
    else:
        for col in range(n):
            if check(pos, row, col):
                pos[row] = col
                put(pos, row + 1, n)

def get_result(n):
    if n == 0:
        return 0
    pos = [-1] * n
    put(pos, 0, n)
    return result
    
result = 0
n = int(input())
print(get_result(n))