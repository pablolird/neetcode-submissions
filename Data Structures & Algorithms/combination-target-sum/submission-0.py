class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        ans = []

        def dfs(nums, index, curr, currSum, ans):
            if currSum>=target:
                if currSum==target:
                    ans.append(curr.copy())
                return

            
            curr.append(nums[index])
            dfs(nums, index, curr, currSum+nums[index], ans)
            curr.pop()
            if (index+1<len(nums)):
                dfs(nums, index+1, curr, currSum, ans)
        
        dfs(nums, 0, curr, 0, ans)

        return ans