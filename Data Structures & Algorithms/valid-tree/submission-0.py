class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map = {m: [] for m in range(n)}
        for a,b in edges:
            map[a].append(b)
            map[b].append(a)
    
        visited = set()
        done = set()
        isTree = [True]

        def dfs(prev,node):
            if node in visited:
                isTree[0] = False
                return
            if node in done:
                return
            visited.add(node)
            for neigh in map[node]:
                if neigh!=prev:
                    dfs(node, neigh)
            visited.remove(node)
            done.add(node)
        
        dfs(None,0)
        return len(done)==n and isTree[0]