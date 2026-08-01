from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node:TreeNode):
            if not node:
                return

            if node.left:
                inorder(node.left)
            res.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)
        return res

# 非递归
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack.pop()
            res.append(node.val)
            cur = node.right

        return res
