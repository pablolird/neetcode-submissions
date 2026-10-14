# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier = 1
        num1 = 0

        while (l1):
            num1 += l1.val*multiplier
            multiplier *=10
            l1 = l1.next

        multiplier = 1
        num2 = 0

        while (l2):
            num2 += l2.val*multiplier
            multiplier *=10
            l2 = l2.next
        
        ans = num1+num2
        length = len(str(ans))

        divider = 1
        dummy = ListNode(0)
        n = dummy
        for _ in range(length):
            x = ans//divider
            digit = x%10
            n.next = ListNode(digit)
            divider *=10
            n = n.next
        
        return dummy.next
