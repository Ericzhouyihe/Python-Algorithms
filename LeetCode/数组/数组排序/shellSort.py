class Solution:
    def shellSort(self, nums: list[int]) -> list[int]:
        gap = len(nums) // 2

        while gap > 0:
            # 根据间隔值判断每一组数据和前一组的关系, 并判断是否和前面数据进行交换
            for i in range(gap, len(nums)):
                # 通过插入排序进行
                num = nums[i]
                j = i
                while j - gap >= 0 and nums[j - gap] > num:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = num
            gap //= 2


arr = [7, 2, 6, 8, 0, 4, 1, 5, 9, 3, 13]
s = Solution()
s.shellSort(arr)
print(arr)
