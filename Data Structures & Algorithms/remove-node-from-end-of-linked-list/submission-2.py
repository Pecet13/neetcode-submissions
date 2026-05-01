# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        # reverse
        curr_node = head
        prev_node = None
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        # remove n-th from the beginning
        head = prev_node
        curr_node = head
        prev_node = None
        next_node = curr_node.next
        for _ in range(1, n):
            prev_node = curr_node
            curr_node = next_node
            next_node = curr_node.next
        if prev_node:
            prev_node.next = next_node
        else:
            head = next_node
        
        # reverse back
        curr_node = head
        prev_node = None
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node