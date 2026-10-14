class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}

        for c in s:
            if c not in map_s:
                map_s[c] = 1
            else:
                map_s[c] = map_s[c]+1

        for c in t:
            if c not in map_s:
                return False
            else:
                map_s[c] = map_s[c]-1

                if map_s[c]==0:
                    del map_s[c]

        if not map_s:
            return True

        return False
                    