class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0]*n

        for i in reversed(range(n)):
            if i==n-1:
                arr[i] = nums[i]
                continue
            if i==n-2:
                arr[i] = max(nums[i],nums[i+1])
                continue
            
            arr[i] = max(nums[i]+arr[i+2], arr[i+1])
        
        print(arr)
        return max(arr)