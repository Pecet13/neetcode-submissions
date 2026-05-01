# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        n = -1
        while dummy:
            dummy = dummy.next
            n += 1

        left, right = head, head
        left_next = ListNode()
        while n > 0:
            right = left
            for _ in range(n):
                right = right.next
            left_next = left.next
            left.next = right
            right.next = left_next
            print(left_next.val)
            left = left_next
            n -= 2
        left_next.next = None
