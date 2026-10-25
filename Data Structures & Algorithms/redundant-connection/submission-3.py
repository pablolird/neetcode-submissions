# Union Find Solution
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [x for x in range(1,n+1)]
        rank = [1]*n

        def union(i,j):
            par_i, par_j = find(i), find(j)

            if (par_i == par_j):
                return [i,j]
            elif (rank[i-1]>rank[j-1]):
                par[par_j-1] = par_i
                rank[par_i-1]+=rank[par_j-1]
            else:
                par[par_i-1] = par_j
                rank[par_i-1]+=rank[par_j-1]
            return None

        def find(i):
            res = par[i-1]
            while (res!=i):
                i = par[i-1]
                res = par[res-1]
            return res
    
        for i,j in edges:
            if (union(i,j)):
                return [i,j]