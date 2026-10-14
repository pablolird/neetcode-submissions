class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       map = {}

       for i, n in enumerate(nums):
            # target = n + m
            # m = target - n    
           if (target-n) in map:
               return [map[target-n], i]

           map[n] = i       
