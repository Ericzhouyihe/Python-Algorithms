from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def createTree(preorder, inorder, n):
            """递归构建二叉树

            Args:
                preorder (_type_): 当前子树的前序遍历序列
                inorder (_type_): 当前子树的中序遍历序列
                n (_type_): 当前子树的节点数

            Returns:
                _type_: 当前子树的根节点
            """
            if n == 0:
                return None  # 递归终止条件：子树节点数为 0
            # 在中序遍历中查找根节点位置
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            # 创建根节点
            node = TreeNode(inorder[k])
            # 递归构建左子树 左子树有 k 个节点, 不包含根节点，所以截取 preorder[1:k+1]
            node.left = createTree(preorder[1 : k + 1], inorder[0:k], k)
            # 递归构建右子树
            node.right = createTree(preorder[k + 1 :], inorder[k + 1 :], n - k - 1)
            return node

        # 从整棵树的前序和中序序列开始递归构建
        return createTree(preorder, inorder, len(inorder))

    # 会快很多
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_dict = {}
        for index, value in enumerate(inorder):
            inorder_dict[value] = index

        def createTree(root_index, left, right):
            if left > right:
                return None
            value = preorder[root_index]
            node = TreeNode(value)
            inorder_index = inorder_dict[value]
            node.left = createTree(root_index + 1, left, inorder_index - 1)
            node.right = createTree(root_index + 1 + inorder_index - left, inorder_index + 1, right)

            return node

        # 从整棵树的前序和中序序列开始递归构建
        return createTree(0, 0, len(inorder) - 1)
