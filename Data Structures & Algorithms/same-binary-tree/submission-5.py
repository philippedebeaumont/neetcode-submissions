# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            nodep, nodeq = stack.pop()
            
            if not nodep and not nodeq:
                continue
            if not nodep or not nodeq or nodep.val != nodeq.val:
                return False

            stack.append((nodep.right, nodeq.right))
            stack.append((nodep.left, nodeq.left))

        return True