class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(m,n):
            rob1 = 0
            rob2 = 0

            for i in range(m,n+1):
                temp = max(rob1+nums[i], rob2)
                rob1 = rob2
                rob2 = temp
            
            return max(rob1,rob2)
        
        if len(nums)==1:
            return nums[0]
        return max(helper(0,len(nums)-2),helper(1, len(nums)-1))

