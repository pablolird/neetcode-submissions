# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        p1 = dummy
        c = 1
        p2 = head

        while (c!=n):
            p2 = p2.next
            c+=1
        
        while (p2.next):
            p2 = p2.next
            p1 = p1.next

        p1.next = p1.next.next

        return dummy.next
        
