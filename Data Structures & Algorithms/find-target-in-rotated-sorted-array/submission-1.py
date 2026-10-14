class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while (l<r):
            mid = (l+r)//2

            if (nums[mid]==target):
                return mid
            if (nums[mid]<nums[r]):
                if (nums[mid]<target and target<=nums[r]):
                    l = mid+1
                else:
                    r = mid
            else:
                if (nums[l]<= target and nums[mid]>target):
                    r = mid
                else:
                    l = mid+1
        
        if (nums[l]==target):
            return l
        return -1

        