class Solution:
    def selectionSort(self, nums: list[int]) -> list[int]:
        """
        选择排序算法实现
        每次在未排序的序列里找到最小值放到最前面, 或者找到最大值放到最后, 然后缩小未排序序列
        """
        n = len(nums)
        for i in range(n - 1):
            min_i = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_i]:
                    min_i = j
            # 交换元素
            if i != min_i:
                nums[i], nums[min_i] = nums[min_i], nums[i]

        return nums

arr = [1, 9, 7, 5, 3, 6, 4]
s = Solution()
s.selectionSort(arr)
print(arr)