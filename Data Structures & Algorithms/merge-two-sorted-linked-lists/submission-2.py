# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        curr1 = list1
        curr2 = list2
        if curr1.val <= curr2.val:
            head = curr1
        else:
            head = curr2
        curr = head
        
        while curr1 is not None or curr2 is not None:
            if curr1 is not None and (curr2 is None or curr1.val <= curr2.val):
                next1 = curr1.next
                curr.next = curr1
                curr = curr.next
                curr1 = next1
            else:
                next2 = curr2.next
                curr.next = curr2
                curr = curr.next
                curr2 = next2

        return head