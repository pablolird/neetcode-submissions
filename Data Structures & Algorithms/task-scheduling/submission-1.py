class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = Counter(tasks)
        q = deque()
        h = [(-map[x],x) for x in map]
        heapq.heapify(h)
        t=0

        while (h or q):
            t+=1
            while (q and q[0][2]<=t):
                [letter, freq, _] = q.popleft()
                heapq.heappush(h, (freq, letter))
            if h:
                (freq, letter) = heapq.heappop(h)
                if (map.get(letter, 0)>1):
                    map[letter]-=1
                    q.append([letter, freq+1, t+n+1])
                else:
                    map.pop(letter, None)
                    
        return t