"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# DFS solution
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        clones = {}
        stack = [node]
        n_c = Node(node.val)
        clones[node] = n_c

        while stack:
            n = stack.pop()
            for neigh in n.neighbors:
                if neigh not in clones:
                    neigh_c = Node(neigh.val)
                    clones[neigh] = neigh_c
                    clones[n].neighbors.append(neigh_c)
                    stack.append(neigh)
                else:
                    clones[n].neighbors.append(clones[neigh])
        
        return clones[node]
                