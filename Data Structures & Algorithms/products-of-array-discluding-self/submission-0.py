class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * (len(nums))
        sufix = [0] * (len(nums)+1)

        for i in range(len(nums)):
            if (i==0):
                prefix[i]=nums[i]
            else:
                prefix[i] = prefix[i-1]*nums[i]
        
        for i in reversed(range(len(nums))):
            if (i==len(nums)-1):
                sufix[i]=nums[i]
            else:
                sufix[i] = sufix[i+1]*nums[i]
        
        result = [0]*len(nums)

        for i in range(len(nums)):
            if (i==0):
                result[i]=sufix[i+1]
            elif (i==(len(nums)-1)):
                result[i]=prefix[i-1]
            else:
                result[i]=prefix[i-1]*sufix[i+1]
            
        return result
        

