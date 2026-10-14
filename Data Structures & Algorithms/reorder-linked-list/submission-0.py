# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s_prev = None
        s, f = head, head

        # if list has 1 element (might not be necessary)
        if (head.next == None):
            return None

        # use slow and fast pointer to find middle
        while (f != None and f.next != None):
            s_prev = s
            s = s.next
            f = f.next.next
        
        # separate 2 halves of the list
        if (s_prev != None):
            s_prev.next = None

        # reverse 2nd half
        h2_prev = None
        h2 = s
        while (h2 != None):
            x = h2
            h2 = h2.next
            x.next = h2_prev
            h2_prev = x
        
        h2 = h2_prev
        h = head
        x = head
        # merge the 2 halves
        while (h != None and h2 != None):
            x = h
            h = h.next
            x.next = h2
            h2 = h2.next
            x.next.next = h
        
        if (h2 != None):
            x.next.next = h2

        return None
        




        





