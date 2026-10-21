class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific_visited = set()
        atlantic_visited = set()

        def dfs(i, j, s):            
            for i1, j1 in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                if (not 0<=i1<rows or not 0<=j1<cols
                    or (i1,j1) in s):
                    continue
                
                if (heights[i1][j1] >= heights[i][j]):
                    s.add((i1,j1))
                    dfs(i1,j1,s)
                

        for j in range(cols):
            pacific_visited.add((0,j))
            dfs(0,j,pacific_visited)
        
        for i in range(rows):
            pacific_visited.add((i,0))
            dfs(i,0,pacific_visited)
        
        for j in range(cols):
            atlantic_visited.add((rows-1,j))
            dfs(rows-1,j,atlantic_visited)
        
        for i in range(rows):
            atlantic_visited.add((i,cols-1))
            dfs(i,cols-1,atlantic_visited)

        print(atlantic_visited)
        print(pacific_visited)
        return list(atlantic_visited.intersection(pacific_visited))