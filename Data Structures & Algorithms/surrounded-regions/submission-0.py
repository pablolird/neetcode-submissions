class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        infected = set()

        def dfs(i,j):
            if (not 0<=i<rows or not 0<=j<cols or (i,j) in infected
                or board[i][j]=="X"):
                return
            
            infected.add((i,j))
            for i1,j1 in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                dfs(i1,j1)

        for i in range(rows):
            if board[i][0]=="O":
                dfs(i,0)

        for j in range(cols):
            if board[0][j]=="O":
                dfs(0,j)

        for i in range(rows):
            if board[i][cols-1]=="O":
                dfs(i,cols-1)

        for j in range(cols):
            if board[rows-1][j]=="O":
                dfs(rows-1,j)

        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if board[i][j]=="O" and (i,j) not in infected:
                    board[i][j]="X"