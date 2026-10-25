class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        map = {}
        for a,b in edges:
            if a not in map:
                map[a] = []
            if b not in map:
                map[b] = []
            map[a].append(b)
            map[b].append(a)

        visited = set()
        cycle_edges = set()

        def dfs(prev,i):
            if i in visited:
                return i
            
            visited.add(i)
            
            for neigh in map[i]:
                if (prev==neigh):
                    continue
                v = dfs(i,neigh)
                if (v!=None):
                    cycle_edges.add((i,neigh))
                    cycle_edges.add((neigh,i))
                    if (v==i):
                        return None
                    return v

            
            return None
        
        dfs(-1,1)
        for edge in reversed(edges):
            if tuple(edge) in cycle_edges:
                return edge

        
