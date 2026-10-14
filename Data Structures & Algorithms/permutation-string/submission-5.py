class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h = [0]*26
        for c in s1:
            h[ord(c)-ord('a')]+=1
        
        l = 0
        r = 0
        h2 = [0]*26
        # setting sliding window initialization
        while (r-l+1<=len(s1) and r<len(s2)):
            i = ord(s2[r])-ord('a')
            h2[i]+=1
            r+=1
        
        while (r<len(s2)):
            if (h==h2):
                return True
            
            i1 = ord(s2[r])-ord('a')
            i2 = ord(s2[l])-ord('a')
            h2[i1]+=1
            h2[i2]-=1
            l+=1
            r+=1
        
        if (h==h2):
            return True
        
        return False



            
