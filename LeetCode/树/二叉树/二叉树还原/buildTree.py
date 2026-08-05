# 二叉树的还原：指通过已知的二叉树遍历序列，重建出原始的二叉树结构
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        二叉树节点定义（链式存储结构）

        属性:
            val: 节点存储的值
            left: 指向左子节点的指针（无左子节点时为 None）
            right: 指向右子节点的指针（无右子节点时为 None）
        """
        self.val = val  # 节点的值
        self.left = left  # 左子节点指针
        self.right = right  # 右子节点指针


# 利用前序与中序遍历序列重建二叉树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def createTree(preorder, inorder, n):
            """
            递归构建二叉树

            参数:
                preorder: 当前子树的前序遍历序列
                inorder: 当前子树的中序遍历序列
                n: 当前子树的节点数
            返回:
                TreeNode，当前子树的根节点
            """
            if n == 0:
                return None  # 递归终止条件：子树节点数为 0
            # 在中序遍历中查找根节点位置
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            # 创建根节点
            node = TreeNode(inorder[k])
            # 递归构建左子树
            node.left = createTree(preorder[1 : k + 1], inorder[0:k], k)
            # 递归构建右子树
            node.right = createTree(preorder[k + 1 :], inorder[k + 1 :], n - k - 1)
            return node

        # 从整棵树的前序和中序序列开始递归构建
        return createTree(preorder, inorder, len(inorder))
