class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []


        def dfs(curr, rem):
            if not rem:
                ans.append(curr)
                return

            for i, _ in enumerate(rem):
                rem_c = rem.copy()
                curr_c = curr.copy()
                x = rem_c.pop(i)
                curr_c.append(x)
                dfs(curr_c, rem_c)
            
        
        dfs([], nums)
        return ans