class Solution:
    # note for future work
    # don't forget heaps in python are always MINHEAPS! ! ! 
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = list((Counter(tasks)).values())
        heap = [-x for x in heap]
        heapq.heapify(heap)
        
        t = 0
        q = deque()

        while (heap or q):
            t+=1

            if (q and q[0][0] <= t):
                _, v = q.popleft()
                heapq.heappush(heap, v)

            if heap:
                v = heapq.heappop(heap)
                v+=1
                if (v):
                    q.append((t+n+1, v))
        
        return t
