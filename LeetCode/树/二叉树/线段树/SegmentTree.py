# 线段树的节点类
class TreeNode:
    def __init__(self, val=0):
        self.left = -1  # 区间左边界
        self.right = -1  # 区间右边界
        self.val = val  # 节点值（区间值，如区间和、区间最大值等）
        self.lazy_tag = None  # 区间延迟更新标记（如区间加法、区间赋值等懒惰标记）


# 线段树类
class SegmentTree:
    def __init__(self, nums, function):
        """
        :param nums: 原始数据数组
        :param function: 区间聚合函数（如 sum, max, min 等）
        """
        self.size = len(nums)
        # 线段树最多需要 4 * n 个节点，使用数组存储
        self.tree = [TreeNode() for _ in range(4 * self.size)]
        self.nums = nums
        self.function = function
        if self.size > 0:
            self.__build(0, 0, self.size - 1)

    def __build(self, index, left, right):
        """
        递归构建线段树
        :param index: 当前节点在数组中的下标
        :param left: 当前节点管理的区间左端点
        :param right: 当前节点管理的区间右端点
        """
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:
            # 叶子节点，直接赋值为原数组对应元素
            self.tree[index].val = self.nums[left]
            return

        mid = left + (right - left) // 2
        left_index = index * 2 + 1  # 左子节点下标
        right_index = index * 2 + 2  # 右子节点下标
        self.__build(left_index, left, mid)  # 构建左子树
        self.__build(right_index, mid + 1, right)  # 构建右子树
        self.__pushup(index)  # 更新当前节点的区间值

    def __pushup(self, index):
        """
        向上更新当前节点的区间值
        :param index: 当前节点在数组中的下标
        """
        left_index = index * 2 + 1  # 左子节点下标
        right_index = index * 2 + 2  # 右子节点下标
        # 当前节点的区间值由左右子节点的区间值聚合得到
        self.tree[index].val = self.function(self.tree[left_index].val, self.tree[right_index].val)
