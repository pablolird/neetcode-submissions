class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = {}

        for t in tasks:
            if t not in map:
                map[t]=0
            map[t]+=1
        
        h = []
        for k in map:
            h.append((-map[k], k))
        
        heapq.heapify(h)
        q = deque()

        t = 0
        while (h or q):
            t+=1
            if (q and q[0][0]==t):
                v = q.popleft()
                heapq.heappush(h,(v[1],v[2]))
            
            if h:
                task = heapq.heappop(h)
                if (task[0]<-1):
                    q.append((t+n+1,task[0]+1,task[1]))

        return t
        