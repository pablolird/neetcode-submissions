class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}

        for c in s:
            if not m.get(c, 0):
                m[c] = 1
            else:
                m[c] = m[c] + 1

        for c in t:
            if m.get(c):
                if m[c]==1:
                    m.pop(c)
                else:
                    m[c] = m[c] - 1
            else:
                return False

        if m:
           return False

        return True 
                
