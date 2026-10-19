"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Maps node.val to node

        if not node:
            return None

        q = deque()
        node_c = Node(node.val)
        q.append((node, node_c))
        map = {}
        map[node_c.val] = node_c

        while (q):
            (n, n_c) = q.pop()

            for neigh in n.neighbors:
                if (neigh.val in map):
                    n_c.neighbors.append(map[neigh.val])
                else:
                    neigh_c = Node(neigh.val)
                    q.append((neigh, neigh_c))
                    map[neigh_c.val] = neigh_c
                    n_c.neighbors.append(neigh_c)
        
        return node_c
        

