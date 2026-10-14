class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        map = {}

        i = 0
        j = 0

        while j < len(s):
            if s[j] in map and map[s[j]]>=i:
                i = map[s[j]]+1
                map[s[j]] = j
            
            map[s[j]] = j
            longest = max(longest, j-i+1)
            j+=1
            
        
        return longest