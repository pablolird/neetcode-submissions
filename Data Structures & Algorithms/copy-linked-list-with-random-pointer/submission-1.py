"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}

        h = head
        while (h):
            aux = Node(h.val)
            map[h] = aux
            h = h.next
        
        map[None] = None

        h = head
        x = map[head]
        while (h):
            x.random = map[h.random]
            x.next = map[h.next]
            h = h.next
            x = x.next
        
        return map[head]

        

