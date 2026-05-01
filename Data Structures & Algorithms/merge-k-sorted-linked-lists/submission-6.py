# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        if len(lists) > 2:
            mid = len(lists) // 2
            left = self.mergeKLists(lists[:mid])
            right = self.mergeKLists(lists[mid:])
            return self.mergeKLists([left, right])
        
        dummy = ListNode()
        curr = dummy
        left = lists[0]
        right = lists[1]
        
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left
        else:
            curr.next = right
        
        return dummy.next
