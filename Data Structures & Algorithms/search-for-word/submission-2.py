class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = []
        used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs (i, j, index):
            if (not 0<=j<len(board[0]) or not 0<=i<len(board) or used[i][j]):
                return
            
            if (word[index]==board[i][j]):
                used[i][j] = True
                if (index==len(word)-1):
                    found.append("s")
                else:
                    dfs(i-1, j, index+1)
                    dfs(i+1, j, index+1)
                    dfs(i, j+1, index+1)
                    dfs(i, j-1, index+1)
                used[i][j] = False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i,j,0)

        if found:
            return True
        else:
            return False
