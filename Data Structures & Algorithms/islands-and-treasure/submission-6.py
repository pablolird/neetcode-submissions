class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q = deque()
                    q.append((i,j,0))
                    visited = set()
                    while q:
                        (x,y,d) = q.popleft()
                        visited.add((x,y))
                        for (x1,y1) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                            if ((x1,y1) in visited or not 0<=x1<rows 
                            or not 0<=y1<cols or grid[x1][y1]==-1):
                                continue
                            
                            if (grid[x1][y1]>d+1):
                                grid[x1][y1] = d+1
                                q.append((x1,y1,d+1))

