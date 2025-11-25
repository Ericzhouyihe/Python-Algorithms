# 删除有序数组中的重复项 II
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        # 快慢指针
        slow, fast = 2, 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
