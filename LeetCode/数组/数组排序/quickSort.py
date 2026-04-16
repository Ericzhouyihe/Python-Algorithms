import random


class Solution:
    def quickSort(self, nums, l, r) -> list[int]:
        if l < r:
            i = self.randomPartition(nums, l, r)
            self.quickSort(nums, l, i)
            self.quickSort(nums, i, r)

        return nums

    def randomPartition(self, nums, low, high) -> int:
        # 随机选择基准值，避免最坏情况
        i = random.randint(low, high)
        # 将基准数与最低位互换
        nums[i], nums[low] = nums[low], nums[i]
        # 随机将基准数移到首位，后续进行分区操作
        return self.partition(nums, low, high)


    def partition(self, nums, low, high):
        pivot = nums[0]
        i, j = low, high
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1

        nums[i], nums[j] = nums[j], nums[i]
        return i


arr = [1, 9, 7, 5, 3, 6, 4]
s = Solution()
s.quickSort(arr, 0, len(arr))
print(arr)
