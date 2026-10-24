class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map = {node:[] for node in range(n)}
        for a,b in edges:
            map[a].append(b)
            map[b].append(a)
        
        done = set()
        count = 0

        def dfs(n):
            done.add(n)
            for neigh in map[n]:
                if neigh not in done:
                    dfs(neigh)

        for node in range(n):
            if node not in done:
                count+=1
                dfs(node)
        
        return count