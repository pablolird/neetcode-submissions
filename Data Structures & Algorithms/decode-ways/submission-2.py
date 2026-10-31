class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i] = 0
            if s[i] != '0':
                dp[i] = dfs(i+1)
            if (i<len(s)-1 and 10<=int(s[i:i+2])<=26):
                dp[i]+= dfs(i+2)
            
            return dp[i]
        
        return dfs(0)