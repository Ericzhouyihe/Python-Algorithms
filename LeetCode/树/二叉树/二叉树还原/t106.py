from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {}
        for index, value in enumerate(inorder):
            inorder_dict[value] = index

        def creatTree(root_index: int, left: int, right: int):
            if left > right:
                return
            value = postorder[root_index]
            inorder_index = inorder_dict[value]
            node = TreeNode(value)
            node.left = creatTree(root_index - 1 - right + inorder_index, left, inorder_index - 1)
            node.right = creatTree(root_index - 1, inorder_index + 1, right)
            return node

        return creatTree(len(postorder) - 1, 0, len(inorder) - 1)
