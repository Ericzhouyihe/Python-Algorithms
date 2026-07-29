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

    def preorderTraversal01(self, root: TreeNode) -> List[int]:
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

    def preorderTraversal02(self, root: TreeNode) -> List[int]:
        """
        二叉树前序遍历(非迭代实现)
        :param root: 根节点
        :return: 按前序遍历顺序的数组
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

    def inorderTraversal01(self, root: TreeNode) -> List[int]:
        """
        二叉树中序遍历(递归实现)
        :param root: 根节点
        :return: 中序遍历结果
        """
        res = []  # 用于存储遍历结果

        def inorder(node):
            if not node:
                return  # 递归终止条件：节点为空
            inorder(node.left)  # 递归遍历左子树
            res.append(node.val)  # 访问当前节点
            inorder(node.right)  # 递归遍历右子树

        inorder(root)  # 从根节点开始递归
        return res  # 返回中序遍历结果

    def inorderTraversal02(self, root:TreeNode) -> List[int]:
        """
        二叉树中序遍历(非递归)
        :param root: 根节点
        :return: 中序遍历结果
        """

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

        resturn = res

    def postorderTraversal01(self, root:TreeNode) -> List[int]:
        """
        二叉树后序遍历(递归)
        :param root: 根节点
        :return: 后序遍历结果
        """
        res = []

        def postorder(node: TreeNode):
            if not node:
                return
            if node.right:
                postorder(node.right)
            if node.left:
                postorder(node.left)
            res.append(node.val)

        postorder(root)
        return res

    def postorderTraversal02(self, root: TreeNode) -> List[int]:
        """
        二叉树后序遍历(非递归)
        :param root: 根节点
        :return: 后序遍历结果
        """
        res = []
        stack = []
        prev = None

        while root or stack:  # 只要当前节点不为空或栈不为空就继续遍历
            # 一直向左走，将所有左子节点入栈
            while root:
                stack.append(root)      # 当前节点入栈
                root = root.left        # 继续遍历左子树

            node = stack.pop()          # 弹出栈顶节点，准备访问或遍历其右子树

            # 判断是否可以访问当前节点
            # 1. 没有右子树
            # 2. 右子树已经访问过（即上一次访问的节点是当前节点的右子节点）
            if not node.right or node.right == prev:
                res.append(node.val)    # 访问当前节点
                prev = node             # 更新上一次访问的节点
                root = None             # 当前节点已访问，重置root，防止重复入栈
            else:
                # 右子树还未访问，当前节点重新入栈，转而遍历右子树
                stack.append(node)
                root = node.right

        return res

    def levelOrder(self, root:TreeNode) -> List[List[int]]:
        """
        二叉树层序遍历（广度优先搜索，BFS）
        :param root: 根节点
        :return: 二叉树层序遍历（广度优先搜索，BFS）
        """
        if not root:
            return []

        from collections import deque
        queue = deque([root])
        order = []

        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level:
                order.append(level)
        return order
