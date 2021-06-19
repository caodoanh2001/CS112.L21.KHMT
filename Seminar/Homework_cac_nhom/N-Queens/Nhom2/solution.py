def solveNQueens(n):
        puzzle = [["."*n] for i in range(n)]        
        cols, diagonals, anti_diagonals, result = set(), set(), set(), []
        
        def place_queen(row, puzzle):
            
            if(row == n):
                result.append(puzzle[:])
                return
                
            for col in range(n):
                if(col in cols or (row-col) in diagonals or (row + col) in anti_diagonals):
                    continue
                
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                puzzle[row] = "." * (col) + "Q" + "." * (n-col-1)

                place_queen( row + 1, puzzle )

                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

                puzzle[row] = "." * n
                
        place_queen( 0, puzzle )
        return len(result)
n = int(input())
print(solveNQueens(n))