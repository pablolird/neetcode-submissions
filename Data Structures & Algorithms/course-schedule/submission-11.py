class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        canFinish = [True]
        map = {}
        visited = set()
        done = set()

        for n in range(numCourses):
            map[n] = []
        
        for pair in prerequisites:
            map[pair[1]].append(pair[0])
        
        def dfs(n):
            visited.add(n)
            for neigh in map[n]:
                if neigh in done:
                    continue
                elif neigh in visited:
                    canFinish[0] = False
                    return
                else:
                    dfs(neigh)
            done.add(n)
            visited.remove(n)
        
        for n in range(numCourses):
            if n not in done:
                dfs(n)
        
        return canFinish[0]
