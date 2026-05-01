# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower = -math.inf, upper = math.inf) -> bool:
        if not root:
            return True
        return root.val > lower and root.val < upper and \
            self.isValidBST(root.left, lower, root.val) and \
            self.isValidBST(root.right, root.val, upper)
    