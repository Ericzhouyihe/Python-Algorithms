from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if targetSum == 0:
            return True

        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.left, targetSum)
        return left or right

    def haspath(self, node: TreeNode, targetSum: int):
        if not node:
            return 0
        left = self.haspath(node.left, targetSum)
        right = self.haspath(node.right, targetSum)

        return left + node.val == targetSum or right + node.val == targetSum


# 测试
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    s = Solution()
    print(s.hasPathSum(root, 22))
