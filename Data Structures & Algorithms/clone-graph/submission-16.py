"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# DFS recursive
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        def dfs(n):
            n_c = Node(n.val)
            clones[n] = n_c
            for neigh in n.neighbors:
                if neigh not in clones:
                    clones[n].neighbors.append(dfs(neigh))
                else:
                    clones[n].neighbors.append(clones[neigh])
            return clones[n]
        return dfs(node) if node else None