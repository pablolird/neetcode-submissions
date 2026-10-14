from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        max = []

        for r in range(len(nums)):
            if (r-k>=0 and nums[r-k]==d[0]):
                d.popleft()

            if r==0:
                d.append(nums[r])
            else:
                while (d and d[-1]<nums[r]):
                    d.pop()
                d.append(nums[r])
            
            if (r-k+1>=0):
                max.append(d[0])
        
        return max

            

            

        
        