# 最大堆
class MaxHeap:
    def __init__(self):
        self.max_heap = []

    def __buildMaxHeap(self, nums):
        # 将数组元素复制到堆中
        self.max_heap = nums.copy()
        size = len(nums)

        # 从最后一个非叶子节点开始，自底向上构建堆
        for i in range((size - 2) // 2, -1, -1):
            self.__shift_down(i, size)

    def maxHeapSort(self, nums):
        # 第一阶段：构建初始大顶堆
        self.__buildMaxHeap(nums)

        size = len(self.max_heap)
        # 第二阶段：重复提取最大值
        for i in range(size - 1, -1, -1):
            # 交换堆顶元素与当前末尾元素
            self.max_heap[0], self.max_heap[i] = self.max_heap[i], self.max_heap[0]
            # 对新的堆顶元素进行下移调整，堆的大小为 i
            self.__shift_down(0, i)

        # 返回排序后的数组
        return self.max_heap

    def __shift_down(self, i: int, n: int):
        # 下移调整：将节点与其较大的子节点比较并交换
        while 2 * i + 1 < n:
            left, right = 2 * i + 1, 2 * i + 2

            # 找出较大的子节点
            larger = left
            if right < n and self.max_heap[right] > self.max_heap[left]:
                larger = right

            # 如果当前节点小于较大子节点，则交换
            if self.max_heap[i] < self.max_heap[larger]:
                self.max_heap[i], self.max_heap[larger] = (
                    self.max_heap[larger],
                    self.max_heap[i],
                )
                i = larger
            else:
                break


class Solution:
    def heapSort(self, nums):
        return MaxHeap().maxHeapSort(nums)


arr = [1, 9, 7, 5, 3, 6, 4]
s = Solution()
s.heapSort(arr)
print(arr)
