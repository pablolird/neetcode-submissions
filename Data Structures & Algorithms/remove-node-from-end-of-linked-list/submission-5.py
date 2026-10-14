# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = ListNode()
        p1.next = head

        c = 1
        p2 = head

        while (c!=n):
            p2 = p2.next
            c+=1
        
        while (p2 and p2.next):
            p2 = p2.next
            p1 = p1.next
        
        if (p1.next==head):
            return head.next

        p1.next = p1.next.next

        return head
        
