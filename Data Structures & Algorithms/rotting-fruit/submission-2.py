class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rows, cols = len(grid), len(grid[0])
        rotten = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh.add((i,j))
        
        time = 0
        while (rotten):
            (x,y,t) = rotten.popleft()
            time = t
            for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if (0<=x1<rows and 0<=y1<cols and grid[x1][y1]==1):
                    grid[x1][y1] = 2
                    fresh.remove((x1,y1))
                    rotten.append((x1,y1,t+1))
            
        if bool(fresh):
            return -1
        return time