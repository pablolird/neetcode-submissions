class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (nums[slow]==nums[fast]):
                break
        
        slow2 = 0
        while (nums[slow]!=nums[slow2]):
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return nums[slow]