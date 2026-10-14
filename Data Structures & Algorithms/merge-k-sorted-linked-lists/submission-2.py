# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while (len(lists)>1):
            for i in range((len(lists)+1)//2):
                if (i+1<len(lists)):
                    lists[i+1] = self.merge2Lists(lists[i], lists[i+1])
                    lists.pop(i)
        
        return lists[0] if lists else None
    
    def merge2Lists(self, head1, head2):
        h1, h2 = head1, head2

        dummy = ListNode(0)
        h = dummy

        while (h1 and h2):
            if (h1.val < h2.val):
                h.next = h1
                h1 = h1.next
            else:
                h.next = h2
                h2 = h2.next
            h = h.next
        
        if (h2):
            h.next = h2
        else:
            h.next = h1
        
        return dummy.next