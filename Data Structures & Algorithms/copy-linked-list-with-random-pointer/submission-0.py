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
        new_h = Node(0)
        x = new_h
        while (h):
            aux = Node(h.val)
            map[h] = aux
            x.next = aux
            x = aux
            h = h.next
        
        map[None] = None

        h = head
        x = new_h.next
        while (h):
            x.random = map[h.random]
            h = h.next
            x = x.next
        
        return new_h.next

        

