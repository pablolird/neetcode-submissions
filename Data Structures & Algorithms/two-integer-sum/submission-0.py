class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
           if m.get(target-n, -1) != -1:
               return [ m[target-n], i ]
           else:
               m[n] = i
        
        return []