# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = float("-inf")
        self.dfs(root)
        return int(self.m)
    def dfs(self, root):
        if not root:
            return 0
        if root.left:
            l = max(0, self.dfs(root.left))
        else:
            l = 0
        if root.right:
            r = max(0, self.dfs(root.right))
        else:
            r = 0
        self.m = max(self.m, l+r+root.val)
        return root.val + max(l, r)
