# 手写二叉堆实现
class Heapq:
    # 堆调整方法：将以 index 为根的子树调整为大顶堆
    def heapAdjust(self, nums: list, index: int, end: int):
        """
        nums: 堆数组
        index: 当前需要调整的根节点下标
        end: 堆的最后一个元素下标
        """
        left = index * 2 + 1  # 左子节点下标
        right = left + 1  # 右子节点下标
        while left <= end:
            max_index = index  # 假设当前根节点最大
            # 比较左子节点
            if nums[left] > nums[max_index]:
                max_index = left
            # 比较右子节点（注意要先判断是否越界）
            if right <= end and nums[right] > nums[max_index]:
                max_index = right
            if index == max_index:
                # 如果根节点就是最大值，调整结束
                break
            # 交换根节点与最大子节点
            nums[index], nums[max_index] = nums[max_index], nums[index]
            # 继续调整被交换下去的子树
            index = max_index
            left = index * 2 + 1
            right = left + 1

    # 建堆：将数组整体调整为大顶堆
    def heapify(self, nums: list):
        size = len(nums)
        # 从最后一个非叶子节点开始，依次向前调整
        for i in range((size - 2) // 2, -1, -1):
            self.heapAdjust(nums, i, size - 1)

    # 入队操作：插入新元素到堆中
    def heappush(self, nums: list, value):
        """
        nums: 堆数组
        value: 待插入的新元素
        """
        nums.append(value)  # 先将新元素加到末尾
        i = len(nums) - 1  # 新元素下标
        # 自下向上调整，恢复堆结构
        while i > 0:
            parent = (i - 1) // 2  # 父节点下标
            if nums[parent] >= value:
                # 父节点比新元素大，插入到当前位置
                break
            # 父节点下移
            nums[i] = nums[parent]
            i = parent
        nums[i] = value  # 插入到最终位置

    # 出队操作：弹出堆顶元素（最大值）
    def heappop(self, nums: list) -> int:
        """
        nums: 堆数组
        return: 堆顶元素
        """
        size = len(nums)
        if size == 0:
            raise IndexError("heappop from empty heap")
        # 交换堆顶和末尾元素
        nums[0], nums[-1] = nums[-1], nums[0]
        top = nums.pop()  # 弹出最大值
        if size > 1:
            # 重新调整堆
            self.heapAdjust(nums, 0, size - 2)
        return top

    # 堆排序：原地将数组升序排序
    def heapSort(self, nums: list):
        """
        nums: 待排序数组
        return: 升序排序后的数组
        """
        self.heapify(nums)  # 先建堆
        size = len(nums)
        # 依次将堆顶元素（最大值）交换到末尾，缩小堆范围
        for i in range(size - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]  # 堆顶与末尾交换
            self.heapAdjust(nums, 0, i - 1)  # 调整剩余部分为大顶堆
        return nums
