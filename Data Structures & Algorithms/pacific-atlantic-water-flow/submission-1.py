class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(i, j, s):
            s.add((i,j))
            for i1, j1 in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                if (not 0<=i1<rows or not 0<=j1<cols
                    or (i1,j1) in s or heights[i1][j1] < heights[i][j]):
                    continue
                    
                dfs(i1,j1,s)
                

        for j in range(cols):
            dfs(0,j,pacific_visited)
        
        for i in range(rows):
            dfs(i,0,pacific_visited)
        
        for j in range(cols):
            dfs(rows-1,j,atlantic_visited)
        
        for i in range(rows):
            dfs(i,cols-1,atlantic_visited)

        return list(atlantic_visited.intersection(pacific_visited))