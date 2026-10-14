# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge2Lists(list1, list2)
        

    def merge2Lists(self, head1, head2):
        h1, h2 = head1, head2

        dummy = ListNode(0)
        h = dummy

        while (h1 and h2):
            if (h1.val < h2.val):
                h.next = ListNode(h1.val)
                h1 = h1.next
            else:
                h.next = ListNode(h2.val)
                h2 = h2.next
            h = h.next
        
        if (h2):
            h.next = h2
        else:
            h.next = h1
        
        return dummy.next