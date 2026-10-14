
def topIndex(l):
    max = 0

    for i,x in enumerate(l):
        if x>l[max]:
            max=i
    return max



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26

        longest = 0
        p1 = 0
        p2 = 0

        while (p2<len(s)):
            letterIndex = ord(s[p2])-ord("A")
            freq[letterIndex]+=1

            while ((p2-p1+1)>freq[topIndex(freq)]+k):
                freq[ord(s[p1])-ord("A")]-=1
                p1+=1

            longest = max(longest, p2-p1+1)
            p2+=1
        
        return longest
                

            