class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}

        for n in nums:
           if m.get(n, 0):
               return True

           m[n] = 1

        return False
 
