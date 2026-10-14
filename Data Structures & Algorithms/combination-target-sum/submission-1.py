class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(curr, sum, index):
            if index==len(nums) or sum>target:
                return
            
            curr.append(nums[index])
            sum+=nums[index]

            if (sum==target):
                ans.append(curr.copy())
            
            dfs(curr, sum, index)
            curr.pop()
            sum-=nums[index]

            dfs(curr, sum, index+1)
        
        dfs([], 0, 0)

        return ans
            