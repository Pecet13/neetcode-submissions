# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        visited = set()
        depth = {root: 0}
        queue = [root]
        while queue:
            u = queue.pop(0)
            if u:
                for v in (u.left, u.right):
                    if v and v not in visited:
                        depth[v] = depth[u] + 1
                        queue.append(v)
                visited.add(u)
        res = []
        for key in depth.keys():
            if depth[key] < len(res):
                res[depth[key]].append(key.val)
            else:
                res.append([key.val])
        return res
