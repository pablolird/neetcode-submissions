class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = [c for c in s.lower() if c.isalnum()]
        p1 = 0
        p2 = len(S)-1 

        while (p1<p2):
            if (S[p1]!=S[p2]):
                return False
            p1+=1
            p2-=1
        
        return True