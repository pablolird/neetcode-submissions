class Solution:
    def numDecodings(self, s: str) -> int:
        map = {}
        map[len(s)-1] = 0 if s[-1]=="0" else 1
        map[len(s)] = 1

        def dfs(i):
            if i in map:
                return map[i]
            
            # X1 represents [i][i+1,...]
            x1 = 0
            # X2 represents [i,i+1][i+2,...]
            x2 = 0

            # X1 can only be possible if
            if (s[i]!='0'):
                x1 = dfs(i+1)
            # X2 can only be possible if            
            if (10<=int(s[i:i+2])<=26):
                x2 = dfs(i+2)

            map[i] = x1+x2
            return x1+x2
        
        dfs(0)
        return map[0]

