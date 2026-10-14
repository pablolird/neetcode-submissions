
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_l = {}
        
        for s in strs:
            m = [0] * 26
            for c in s:
                m[ord(c)-97] = m[ord(c)-97] + 1;                

            if map_l.get(tuple(m), -1) == -1:
                map_l[tuple(m)] = [ s ]
            else:
                map_l[tuple(m)].append(s)

        return list(map_l.values())