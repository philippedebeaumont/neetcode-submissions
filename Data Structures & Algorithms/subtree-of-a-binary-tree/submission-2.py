# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"

        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

    def z_function(self, s: str) -> list:
        z = [0] * len(s)
        n = len(s)
        for i in range(1, n):
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)
        combined = serialized_subRoot + "|" + serialized_root

        z_values = self.z_function(combined)
        sub_len = len(serialized_subRoot)

        for i in range(sub_len + 1, len(combined)):
            if z_values[i] == sub_len:
                return True
        return False