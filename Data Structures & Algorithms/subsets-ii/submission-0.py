class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(curr, index):
            if (index==len(nums)):
                ans.append(curr.copy())
                return
            
            curr.append(nums[index])
            dfs(curr, index+1)
            curr.pop()

            while (index+1 < len(nums) and nums[index]==nums[index+1]):
                index+=1
            dfs(curr, index+1)

        
        dfs([], 0)
        return ans



            
