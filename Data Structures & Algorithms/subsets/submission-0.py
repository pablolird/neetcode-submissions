class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        if not nums:
            return []
        
        self.iter([], nums, 0)
        return self.ans
        


    def iter(self, curr, nums, i):
        c1 = curr.copy()
        c2 = curr.copy()
        c2.append(nums[i])

        if (i==len(nums)-1):
            self.ans.append(c1)
            self.ans.append(c2)
            return
        
        self.iter(c1, nums, i+1)
        self.iter(c2, nums, i+1)

