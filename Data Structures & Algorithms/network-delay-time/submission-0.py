class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {x: [] for x in range(1,n+1)}
        for a,b,t in times:
            if a not in adj:
                adj[a] = []
            adj[a].append((b,t))
        
        times = [float('inf')]*n
        times[k-1] = 0
        h = [(k,0)]

        while h:
            n,t = heapq.heappop(h)

            if t>times[n-1]:
                continue
            
            for neigh,neigh_t in adj[n]:
                if (neigh_t+t<times[neigh-1]):
                    heapq.heappush(h,(neigh,neigh_t+t))
                    times[neigh-1] = neigh_t+t
        
        res = max(times)
        return res if res!=float('inf') else -1