class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["."*n]*n
        cols = set()
        posDiag = set()
        negDiag = set()
        ans = []
        
        def dfs(row):
            if (row==len(board)):
                ans.append(board.copy())
                return

            for col,_ in enumerate(board[row]):
                if (col not in cols and col-row not in negDiag and col+row not in posDiag):
                    cols.add(col)
                    negDiag.add(col-row)
                    posDiag.add(col+row)
                    board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                    
                    dfs(row+1)

                    cols.remove(col)
                    negDiag.remove(col-row)
                    posDiag.remove(col+row)
                    board[row] = board[row][:col] + "." + board[row][col + 1:]
                    
        
        dfs(0)
        return ans