class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []

        for n in nums:
            heapq.heappush(q, n)
            if (len(q)>k):
                heapq.heappop(q)
        
        return q[0]