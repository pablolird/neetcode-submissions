class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        map = {}
        for word in wordList:
            map[word] = []

        patternmap = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                if pattern not in patternmap:
                    patternmap[pattern] = []
                patternmap[pattern].append(word)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                l = patternmap[pattern]
                for w in l:
                    if (w==word):
                        continue
                    map[word].append(w)
        
        visited = set(beginWord)
        def bfs(word):
            q = deque()
            q.append((1,word))
            while q:
                t,w = q.popleft()
                if w==endWord:
                    return t
                
                for neigh in map[w]:
                    if neigh in visited:
                        continue
                    q.append((t+1,neigh))
                    visited.add(neigh)
            
            return 0
        
        return bfs(beginWord)