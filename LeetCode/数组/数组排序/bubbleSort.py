class Solution:
    def bubbleSort(self, nums: list[int]) -> list[int]:
        """冒泡排序算法实现"""
        n = len(nums)
        # 外层循环控制趟数，每一趟将当前未排序区间的最大值「冒泡」到末尾
        for i in range(n - 1):
            swapped = False  # 记录本趟是否发生过交换
            # 内层循环负责相邻元素两两比较，将较大值后移
            for j in range(n - i - 1):
                # 如果前一个元素大于后一个元素，则交换
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True  # 发生了交换
            # 如果本趟没有发生任何交换，说明数组已经有序，可以提前结束
            if not swapped:
                break
        return nums  # 返回排序后的数组

arr = [1, 9, 7, 5, 3, 6, 4]
s = Solution()
s.bubbleSort(arr)
print(arr)