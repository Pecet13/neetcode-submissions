# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = {root: 1}
        visited = set()
        queue = [root]
        while queue:
            u = queue.pop(0)
            if u:
                for v in (u.left, u.right):
                    if v and v not in visited:
                        depth[v] = depth[u] + 1
                        queue.append(v)
                visited.add(u)
        return max(depth.values())
