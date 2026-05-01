# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        over = 0

        while l1 and l2:
            curr.next = l1
            curr = l1
            if l1.val + l2.val + over >= 10:
                curr.val = (l1.val + l2.val + over) % 10
                over = 1
            else:
                curr.val = l1.val + l2.val + over
                over = 0
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            curr.next = l1
            while over and l1:
                l1.val += 1
                if l1.val < 10:
                    over = 0
                l1.val = l1.val % 10
                curr = l1
                l1 = l1.next
        elif l2:
            curr.next = l2
            while over and l2:
                l2.val += 1
                if l2.val < 10:
                    over = 0
                l2.val = l2.val % 10
                curr = l2
                l2 = l2.next
        
        if over:
            curr.next = ListNode(val=1)

        return dummy.next
