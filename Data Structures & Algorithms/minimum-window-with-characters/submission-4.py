class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (t==""):
            return ""

        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0)+1

        need = len(t_map.values())
        s_map = {}
        have = 0
        l = 0
        best = ""
        for r in range(len(s)):
            if s[r] in t_map:
                if t_map[s[r]] - s_map.get(s[r], 0) == 1:
                    have+=1
                s_map[s[r]] = s_map.get(s[r],0)+1
            
            while (have>=need):
                if (best=="") or r-l+1<len(best):
                    best=s[l:r+1]

                if s[l] in t_map:
                    if t_map[s[l]] - s_map.get(s[l], 0) == 0:
                        have-=1
                    s_map[s[l]] = s_map.get(s[l],0)-1
                    if s_map[s[l]]==0:
                        s_map.pop(s[l])
                l+=1
        
        return best
        
        