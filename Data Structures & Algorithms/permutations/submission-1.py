class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        used = [False]*len(nums)


        def dfs():
            if len(curr)==len(nums):
                ans.append(curr.copy())
                return

            for i in range(len(nums)):
                if (used[i]):
                    continue
                used[i] = True
                curr.append(nums[i])
                dfs()
                curr.pop()
                used[i] = False

            
        
        dfs()
        return ans