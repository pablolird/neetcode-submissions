class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j,0))
        while q:
            (x,y,d) = q.popleft()
            for (x1,y1) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if (0<=x1<rows and 0<=y1<cols and grid[x1][y1]!=-1 and grid[x1][y1]>d+1):
                    grid[x1][y1] = d+1
                    q.append((x1,y1,d+1))

