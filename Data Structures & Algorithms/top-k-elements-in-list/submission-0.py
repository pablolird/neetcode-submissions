class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        k_list = [[] * (len(nums)+1) for _ in range(len(nums)+1)]

        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] = map[n] + 1

        for i in map:
            k_list[map[i]].append(i)
        
        ans = []

        for i in reversed(k_list):
            for n in i:
                ans.append(n)
                if (len(ans)==k):
                    return ans
        