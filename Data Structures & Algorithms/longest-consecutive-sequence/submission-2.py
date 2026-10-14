class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = {}
        finish = {}

        for n in nums:
            if n in start or n in finish:
                continue

            if n-1 not in finish and n+1 not in start:
                start[n] = 1
                finish[n] = 1
                continue

            if n-1 in finish and n+1 in start:
                length1 = finish.pop(n-1)
                length2 = start.pop(n+1)

                start[n-length1] = length1+length2+1
                finish[n+length2] = length1+length2+1
                continue

            if n-1 in finish:
                length = finish.pop(n-1)
                finish[n] = length +1
                start[n-length] = length + 1

            if n+1 in start:
                length = start.pop(n+1)
                start[n] = length +1
                finish[n+length] = length + 1
        
        if not start:
            return 0
        
        return max(start.values())