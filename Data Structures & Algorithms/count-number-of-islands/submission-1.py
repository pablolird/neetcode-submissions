class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = [0]

        def dfs(i, j, flag=False):
            if (not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j]=="0"):
                return
            
            if not flag:
                ans[0]+=1

            grid[i][j]="0"
            dfs(i+1, j, True)
            dfs(i-1, j, True)
            dfs(i, j+1, True)
            dfs(i, j-1, True)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                dfs(i, j)
        
        return ans[0]
