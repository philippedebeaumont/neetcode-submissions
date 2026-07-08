# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root, float("-inf"), float("inf"))

    def isBST(self, root, low, high):
        if not root:
            return True
        if root.left and (root.left.val <= low or root.left.val >= root.val):
            return False
        elif root.right and (root.right.val >= high or root.right.val <= root.val):
            return False
        else:
            return self.isBST(root.left, low, root.val) and self.isBST(root.right, root.val, high)
            