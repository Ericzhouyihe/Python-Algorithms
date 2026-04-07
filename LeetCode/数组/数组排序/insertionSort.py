class Solution:
    def insertionSort(self, nums: list[int]) -> list[int]:
        """
        插入排序算法实现
        初始已排序部分只有一个数字, 判断未排序的空间中第一个应该插入到已排序中的前面还是后面
        后面每次都判断未排序空间中的数字应该插入的位置, 并进行插入
        """
        for i in range(1, len(nums)):
            num = nums[i]
            j = i
            while j > 0 and nums[j - 1] > num:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = num

        return nums

arr = [1, 9, 7, 5, 3, 6, 4]
s = Solution()
s.insertionSort(arr)
print(arr)