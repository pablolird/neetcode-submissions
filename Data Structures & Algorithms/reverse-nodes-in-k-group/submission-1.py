# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p2 = dummy

        while (True):
            p1 = p2
            for _ in range(k):
                p2 = p2.next
                if (not p2):
                    return dummy.next
            
            finish = p2.next
            start = p1
            first_node = p1.next

            p0 = None
            p1 = p1.next
            while (p1!=finish):
                x = p1.next
                p1.next = p0
                p0 = p1
                p1 = x
            
            first_node.next = finish
            start.next = p2
            p2 = first_node


