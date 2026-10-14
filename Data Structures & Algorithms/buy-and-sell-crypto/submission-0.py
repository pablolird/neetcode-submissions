class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buy = prices[0]

        for p in prices:
            if (maxProfit < p-buy):
                maxProfit = p-buy

            if (p<buy):
                buy = p
        
        return maxProfit

            
            
