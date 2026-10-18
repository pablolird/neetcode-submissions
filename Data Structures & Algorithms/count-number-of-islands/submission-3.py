class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def bfs(i, j):
            q = deque()
            q.append((i,j))

            while q:
                (r, c) = q.popleft()
                if (0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]=="1"):
                    grid[r][c]="0"
                    q.append((r-1,c))
                    q.append((r+1,c))
                    q.append((r,c+1))
                    q.append((r,c-1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    ans+=1
                    bfs(i,j)
        
        return ans