# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> Optional[bool]:
        if not root:
            return
        if root.left:
            if root.left.val >= root.val:
                return False
            self.isValidBST(root.left)
        if root.right:
            if root.right.val <= root.val:
                return False
            self.isValidBST(root.right)

        return True

    def isValidBST1(self, root: Optional[TreeNode]) -> Optional[bool]:

        def helper(node, lower=float("-inf"), upper=float("inf")) -> bool:
            if not node:
                return False

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
