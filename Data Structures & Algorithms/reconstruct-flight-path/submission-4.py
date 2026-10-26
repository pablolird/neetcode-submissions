class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}

        for from_i, to_i in tickets:
            if from_i not in adj:
                adj[from_i] = []
            if to_i not in adj:
                adj[to_i] = []
            adj[from_i].append(to_i)
        
        for k in adj:
            adj[k].sort(reverse=True)
        
        path = []
        def dfs(node):
            while adj[node]:
                v = adj[node].pop()
                dfs(v)
            path.append(node)
        
        dfs("JFK")
        return list(reversed(path))
