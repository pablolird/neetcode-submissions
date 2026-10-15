class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(s):
            if not s: 
                return True
            i, j = 0, len(s)-1
            while (i<j):
                if (s[i]!=s[j]):
                    return False
                i+=1
                j-=1
            
            return True

        def dfs(l, curr, prev):
            if (curr==len(s)):
                if l and curr==prev:
                    ans.append(l.copy())
                return
            
            if isPalindrome(s[prev:curr+1]):
                l.append(s[prev:curr+1])
                dfs(l, curr+1, curr+1)
                l.pop()
            
            dfs(l,curr+1,prev)

        dfs([], 0, 0)
        return ans