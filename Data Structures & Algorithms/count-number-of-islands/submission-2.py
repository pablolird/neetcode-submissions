class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def dfs(i, j):
            if (not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j]=="0"):
                return

            grid[i][j]="0"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j]=="1"):
                    ans+=1
                    dfs(i, j)
        
        return ans
