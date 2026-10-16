class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["."*n]*n
        ans = []
        
        def dfs(row):
            if (row==len(board)):
                ans.append(board.copy())
                return

            for i,_ in enumerate(board[row]):
                top = [row-1,i]
                topLeft = [row-1,i-1]
                topRight = [row-1,i+1]
                validCell = True

                while (top[0]>=0):
                    if board[top[0]][top[1]]=="Q":
                        validCell = False
                        break
                    top[0]-=1
                
                while (topLeft[0]>=0 and topLeft[1]>=0):
                    if board[topLeft[0]][topLeft[1]]=="Q":
                        validCell = False
                        break
                    topLeft[0]-=1
                    topLeft[1]-=1
                    
                while (topRight[0]>=0 and topRight[1]<len(board[row])):
                    if board[topRight[0]][topRight[1]]=="Q":
                        validCell = False
                        break
                    topRight[0]-=1
                    topRight[1]+=1
                
                if validCell:
                    board[row] = board[row][:i] + "Q" + board[row][i + 1:]
                    dfs(row+1)
                    board[row] = board[row][:i] + "." + board[row][i + 1:]
        
        dfs(0)
        return ans