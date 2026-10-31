class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        for coin in coins:
            dp[coin] = 1
                        
        def dfs(i):
            if i in dp:
                return dp[i]
            
            ans = []
            for c in coins:
                if c<=i:
                    t = dfs(i-c)
                    if (t!=-1):
                        ans.append(dfs(i-c)+1)
            
            dp[i] = min(ans) if ans else -1
            return dp[i]
        
        dfs(amount)
        print(dp)
        return dfs(amount)
            