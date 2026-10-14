class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)

        for i in range(len(nums)-1):
            result[i+1] = nums[i]*result[i]
        
        postfix=1
        for i in reversed(range(len(nums)-1)):
            postfix*=nums[i+1]
            result[i]*=postfix
        
        return result
            