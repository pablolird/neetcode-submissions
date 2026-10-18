class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def bfs(i, j):
            q = deque()
            q.append((i,j))

            while q:
                (r, c) = q.popleft()

                for (a, b) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if (0<=a<len(grid) and 0<=b<len(grid[0]) and grid[a][b]=="1"):
                        grid[a][b]="0"
                        q.append((a,b))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    ans+=1
                    bfs(i,j)
        
        return ans