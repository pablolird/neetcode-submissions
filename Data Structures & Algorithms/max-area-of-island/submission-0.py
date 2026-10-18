class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            grid[i][j] = 0
            count = 0

            while (q):
                (r, c) = q.popleft()
                count+=1
                for (a, b) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if (0<=a<rows and 0<=b<cols and grid[a][b]):
                        grid[a][b]=0
                        q.append((a,b))
            return count

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    ans = max(ans, bfs(i,j))
        
        return ans