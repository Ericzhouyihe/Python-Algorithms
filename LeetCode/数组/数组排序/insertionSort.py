class Solution:
    def insertionSort(self, nums: list[int]) -> list[int]:
        """插入排序算法实现"""
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