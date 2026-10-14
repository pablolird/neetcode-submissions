# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        p = dummy

        for i, pointer in enumerate(lists):
            if pointer:
                heap.append((pointer.val, i, pointer))
        
        heapq.heapify(heap)

        while (heap):
            _, index, pointer = heapq.heappop(heap)
            p.next = pointer
            p = p.next
            if (pointer.next):
                heapq.heappush(heap, (pointer.next.val, index, pointer.next))
        
        return dummy.next

