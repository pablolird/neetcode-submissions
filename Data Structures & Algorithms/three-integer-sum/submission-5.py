class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = set()

        for i, n in enumerate(nums):
            target = -n
            map = {}

            for j in range(i+1, len(nums)):
                if nums[j] not in map:
                    map[target - nums[j]] = j
                    continue
                
                triplets.add(tuple(sorted([n, target-nums[j], nums[j]])))

            
        return [list(item) for item in triplets]
            

                
