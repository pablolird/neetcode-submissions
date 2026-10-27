class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0]*n

        for i in range(n):
            if i==0:
                arr[i] = 1
            elif i==1:
                arr[i] = 2
            else:
                arr[i] = arr[i-1]+arr[i-2]
        
        return arr[-1]