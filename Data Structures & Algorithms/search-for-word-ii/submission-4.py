class TrieNode:
    def __init__(self):
        self.map = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        ans = set()
        used = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for w in words:
            ptr = root
            for c in w:
                if c not in ptr.map:
                    ptr.map[c] = TrieNode()
                ptr = ptr.map[c]
            ptr.end = True

        def dfs(node, curr, i, j):
            used[i][j] = True
            if node.end==True:
                ans.add(curr)

            if (j+1<len(board[0]) and not used[i][j+1] and board[i][j+1] in node.map):
                dfs(node.map[board[i][j+1]], curr+board[i][j+1], i, j+1)
            if (j-1>=0 and not used[i][j-1] and board[i][j-1] in node.map):
                dfs(node.map[board[i][j-1]], curr+board[i][j-1], i, j-1)
            if (i+1<len(board) and not used[i+1][j] and board[i+1][j] in node.map):
                dfs(node.map[board[i+1][j]], curr+board[i+1][j], i+1, j)
            if (i-1>=0 and not used[i-1][j] and board[i-1][j] in node.map):
                dfs(node.map[board[i-1][j]], curr+board[i-1][j], i-1, j)
            used[i][j] = False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in root.map:
                    dfs(root.map[board[i][j]], board[i][j], i, j)
        
        return list(ans)

                
