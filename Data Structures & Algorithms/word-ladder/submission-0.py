class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        map = { beginWord: [] }
        for word in wordList:
            map[word] = []

        wordList.append(beginWord)

        for word in wordList:
            for word2 in wordList:
                if word==word2:
                    continue
                count=0
                for i in range(len(word)):
                    if word[i]!=word2[i]:
                        count+=1
                if count==1:
                    map[word].append(word2)
        
        visited = set()
        def bfs(word):
            q = deque()
            q.append((1,None,word))
            while q:
                t,prev,w = q.popleft()
                visited.add(w)
                if w==endWord:
                    return t
                
                for neigh in map[w]:
                    if prev==neigh or neigh in visited:
                        continue
                    q.append((t+1,w,neigh))
            
            return 0
        
        return bfs(beginWord)