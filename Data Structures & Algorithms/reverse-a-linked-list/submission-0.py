# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(node):
    n = node
    if (node and node.next!=None):
        n = reverse(node.next)
        node.next.next = node
        node.next = None
    
    return n


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        k = reverse(h)
        return k

