class Solution:
    def returnHours(self, piles, k):
        ans = 0
        for v in piles:
            ans+=(v+k-1)//k
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while (l<r):
            mid = (l+r)//2

            if (self.returnHours(piles, mid)<=h):
                r = mid
            else:
                l = mid+1
        return int(l)

            