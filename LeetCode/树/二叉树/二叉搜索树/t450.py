# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif not root.left or not root.right:
            root = root.left if root.left else root.right
        else:
            success = root.right
            while success.left:
                success = success.left
            success.right = self.deleteNode(root.right, success.val)
            success.left = root.left
            return success

        return root
