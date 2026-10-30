class Solution:
    def longestPalindrome(self, s: str) -> str:
        sol = ""

        for i,c in enumerate(s):
            l = i
            r = i
            while (l>=0 and r<len(s) and s[l]==s[r]):
                if len(sol)<r-l+1:
                    sol = s[l:r+1]
                l -=1
                r +=1
        
        for i,c in enumerate(s):
            l = i
            r = i+1
            while (l>=0 and r<len(s) and s[l]==s[r]):
                if len(sol)<r-l+1:
                    sol = s[l:r+1]
                l -=1
                r +=1
        
        return sol