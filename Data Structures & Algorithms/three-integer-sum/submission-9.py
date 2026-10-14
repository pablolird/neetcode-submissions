class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        triplets = []

        for i, n in enumerate(nums):
            if (i!=0 and nums[i]==nums[i-1]):
                continue
            p1 = i+1
            p2 = len(nums)-1

            target = -n

            while (p1<p2):
                if (p1!=i+1 and nums[p1]==nums[p1-1]):
                    p1+=1
                    continue

                if (p2!=(len(nums)-1) and nums[p2]==nums[p2+1]):
                    p2-=1
                    continue           

                sum = nums[p1]+nums[p2]

                if (sum==target):
                    triplets.append([nums[p1], nums[p2], n])
                
                if (sum<target):
                    p1 +=1
                    continue
                
                p2-=1
            
        
        return triplets

                
