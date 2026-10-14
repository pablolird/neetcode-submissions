class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        maxLength = 0

        for n in nums:
            length = 0
            if n-1 not in numSet:
                x = n
                while x in numSet:
                    length+=1
                    x+=1
            
            if length>maxLength:
                maxLength = length
        
        return maxLength