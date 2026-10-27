class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        arr = [0]*n

        for i in reversed(range(n)):
            if i==n-1 or i==n-2:
                arr[i] = cost[i]
                continue
            
            arr[i] = cost[i]+min(arr[i+1],arr[i+2])
        
        return min(arr[0],arr[1])