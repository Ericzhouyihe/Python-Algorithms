# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


# 前序+后序 还原二叉树
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        left_val = preorder[1]
        idx = postorder.index(left_val)
        root.left = self.constructFromPrePost(preorder[1 : idx + 2], postorder[: idx + 1])
        root.right = self.constructFromPrePost(preorder[idx + 2 :], postorder[idx + 1 : -1])

        return root


# 索引的解法
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        pset = {v: i for i, v in enumerate(postorder)}
        w = preorder[0]
        p0 = TreeNode(w)
        if len(preorder) == 1:
            return p0
        ls = pset[preorder[1]] + 1
        p0.left = self.constructFromPrePost(preorder[1 : ls + 1], postorder[:ls])
        p0.right = self.constructFromPrePost(preorder[ls + 1 :], postorder[ls:-1])
        return p0
