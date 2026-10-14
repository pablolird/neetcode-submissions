class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(curr, i, j):
            if (i==j==n):
                ans.append(curr)
            
            if (i<n):
                dfs(curr+"(", i+1, j)

            if (j<i):
                dfs(curr+")", i, j+1)

        dfs("", 0, 0)
        return ans