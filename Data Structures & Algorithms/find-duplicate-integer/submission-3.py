class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}

        for n in nums:
            if (n in map):
                return n
            
            map[n] = True
        