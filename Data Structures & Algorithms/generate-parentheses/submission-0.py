class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(curr, i, j):
            if ((not i and j) or i>n):
                return
            
            if (i==j==n):
                ans.append(curr)
            
            curr+="("
            dfs(curr, i+1, j)
            curr=curr[:-1]

            if (j<i):
                curr+=")"
                dfs(curr, i, j+1)

        dfs("", 0, 0)
        return ans