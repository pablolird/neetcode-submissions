# Union Find Solution
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n

        def find(i):
            res = i
            while (res != par[res]):
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(i,j):
            i, j = find(i), find(j)
            
            if (i==j):
                return 0
            
            if (rank[i]>rank[j]):
                par[j] = i
                rank[i]+=rank[j]
            else:
                par[i] = j
                rank[j]+=rank[i]
            return 1
        res = n
        for a,b in edges:
            res-=union(a,b)
        return res