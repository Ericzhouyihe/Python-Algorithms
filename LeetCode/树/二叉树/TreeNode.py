from typing import List

class TreeNode:
    """
    二叉树节点定义（链式存储结构）

    属性:
        val: 节点存储的值
        left: 指向左子节点的指针（无左子节点时为 None）
        right: 指向右子节点的指针（无右子节点时为 None）
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 节点的值
        self.left = left  # 左子节点指针
        self.right = right  # 右子节点指针

class Solution:

    def precedenceTraversalRecursion(self, root: TreeNode) -> List[int]:
        """
        二叉树的前序遍历（递归实现）
        参数: root: TreeNode，二叉树的根节点
        返回: List[int]，前序遍历的节点值列表
        """
        res = []  # 用于存储遍历结果

        def preorder(node):
            if not node:
                return  # 递归终止条件：节点为空
            res.append(node.val)  # 1. 访问根节点
            preorder(node.left)  # 2. 递归遍历左子树
            preorder(node.right)  # 3. 递归遍历右子树

        preorder(root)  # 从根节点开始递归
        return res

    def precedenceTraversalNotRecursive(self, root: TreeNode) -> List[int]:
        """
        """
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res