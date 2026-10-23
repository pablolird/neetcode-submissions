class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = []
        map = {n: [] for n in range(numCourses)}
        visited = set()
        done = set()
        canFinish = [True]

        for curr, prev in prerequisites:
            map[curr].append(prev)
        
        def dfs(n):
            visited.add(n)
            for neigh in map[n]:
                if neigh in done:
                    continue
                elif neigh in visited:
                    canFinish[0] = False
                else:
                    dfs(neigh)
            stack.append(n)
            done.add(n)
            visited.remove(n)
        
        for n in range(numCourses):
            if n not in done:
                dfs(n)
        
        if canFinish[0]:
            return stack
        return []
        

