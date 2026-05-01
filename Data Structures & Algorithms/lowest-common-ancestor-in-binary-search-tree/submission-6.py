# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr_p, curr_q, anc = root, root, root
        while curr_p.val == curr_q.val:
            anc = curr_p
            if curr_p.val < p.val:
                curr_p = curr_p.right
            elif curr_p.val > p.val:
                curr_p = curr_p.left
            if curr_q.val < q.val:
                curr_q = curr_q.right
            elif curr_q.val > q.val:
                curr_q = curr_q.left
        return anc
